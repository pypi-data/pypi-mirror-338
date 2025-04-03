"""Functionality for working with the annotated pairs format.

This module provides tools for converting ICAI experiment results to the
annotated pairs format, a standardized JSON format for representing model
comparisons with annotations from both human evaluators and principles.
"""

import datetime
import hashlib
import json
from pathlib import Path
from typing import Dict, List, Mapping, Optional, Sequence

import pandas as pd
from loguru import logger

from inverse_cai.data.loader import icai

# Constants
HUMAN_ANNOTATOR_DESCRIPTION = "Human annotator from original dataset"
FORMAT_VERSION = "1.0"


def hash_string(s: str) -> str:
    """Create a shortened hash of a string."""
    return hashlib.md5(s.encode("utf-8")).hexdigest()[:8]


def hash_comparison(text_a: str, text_b: str, prompt: Optional[str]) -> str:
    """Create a hash ID for a comparison based on its content."""
    combined = f"{text_a}|{text_b}|"
    if prompt is not None:
        combined = f"{prompt}|{combined}"
    return hash_string(combined)


def votes_to_annotations(
    votes: Mapping[int, Optional[bool]],
    principle_index_to_text: Mapping[int, str],
    active_principles: Sequence[str],
    reference_preference: str,
) -> Dict[str, Dict[str, str]]:
    """Convert principle votes to annotations in the standardized format.

    Args:
        votes: Dictionary mapping principle IDs to their votes (True/False/None)
        principle_index_to_text: Dictionary mapping principle IDs to their text
        active_principles: List of active principles to include
        reference_preference: The reference preference (text_a or text_b)

    Returns:
        Dictionary mapping principle IDs (hashed) to dictionaries with preferences
    """
    annotations = {}

    for principle_idx, vote in votes.items():
        principle_text = principle_index_to_text[principle_idx]

        # Only include principles that are active
        if principle_text in active_principles:
            principle_id = hash_string(principle_text)

            # Convert vote to text_a, text_b or not_applicable
            if vote is None:
                annotations[principle_id] = {"pref": "not_applicable"}
            elif vote is True:
                # Principle agrees with reference preference
                annotations[principle_id] = {"pref": reference_preference}
            else:  # vote is False
                # Principle disagrees with reference preference
                annotations[principle_id] = {
                    "pref": "text_b" if reference_preference == "text_a" else "text_a"
                }

    return annotations


def add_annotators(
    output: Dict,
    principles: Mapping[int, str],
    filtered_principles: Sequence[str],
    filter_to_constitution: bool = True,
) -> None:
    """Add human and principle annotators to the output structure.

    This function modifies the output dictionary in-place by adding annotator
    information to output["annotators"] and setting the default annotator.

    Args:
        output: The output dataset dictionary to modify in-place
        principles: Dictionary of principles where keys are principle IDs
        filtered_principles: List of filtered principles
        filter_to_constitution: Only include principles that made it to the constitution
    """
    # Create human annotator
    human_annotator_id = hash_string(HUMAN_ANNOTATOR_DESCRIPTION)
    output["annotators"][human_annotator_id] = {
        "name": "Human",
        "description": HUMAN_ANNOTATOR_DESCRIPTION,
        "type": "human",
    }
    output["metadata"]["default_annotator"] = human_annotator_id

    # Determine active principles
    active_principles = (
        filtered_principles if filter_to_constitution else list(principles.values())
    )

    # Create principle annotators
    for principle in active_principles:
        annotator_id = hash_string(principle)
        output["annotators"][annotator_id] = {
            "description": principle,
            "type": "principle",
        }


def create_annotated_pairs(
    train_df: pd.DataFrame,
    principles: Mapping[int, str],
    filtered_principles: Sequence[str],
    comparison_votes: Mapping[int, Dict[int, Optional[bool]]],
    dataset_name: str,
    filter_to_constitution: bool = True,
) -> Dict:
    """Convert ICAI results to annotated pairs format using direct data inputs.

    Args:
        train_df: DataFrame with training data. Must have mandatory "text_a", "text_b", and "preferred_text" rows, and an optional "input" (prompt).
        principles: Dictionary of principles where keys are principle IDs
        filtered_principles: List of filtered principles (those that made it to the constitution)
        comparison_votes: Dictionary of comparison votes
        dataset_name: Name for the dataset
        filter_to_constitution: Only include principles that made it to the constitution

    Returns:
        The annotated pairs format as a dictionary
    """
    # Initialize the output structure
    output = {
        "metadata": {
            "version": FORMAT_VERSION,
            "description": "Annotated pairs dataset with annotations from ICAI",
            "created_at": datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"),
            "dataset_name": dataset_name,
        },
        "annotators": {},
        "comparisons": [],
    }

    # Add annotators to the output
    add_annotators(output, principles, filtered_principles, filter_to_constitution)

    # Prepare data needed for annotations
    human_annotator_id = output["metadata"]["default_annotator"]
    active_principles = (
        filtered_principles if filter_to_constitution else list(principles.values())
    )

    # Process each comparison
    for idx, row in train_df.iterrows():
        # Create unique ID for this comparison
        comparison_id = hash_comparison(row["text_a"], row["text_b"], row.get("input"))

        # Initialize annotations dict with human annotation
        annotations = {}
        reference_preference = row["preferred_text"]
        annotations[human_annotator_id] = {"pref": reference_preference}

        # Add principle annotations based on votes
        votes = comparison_votes[idx]
        principle_annotations = votes_to_annotations(
            votes, principles, active_principles, reference_preference
        )
        annotations.update(principle_annotations)

        # Create the comparison entry
        comparison = {
            "id": comparison_id,
            "prompt": row.get("input"),
            "text_a": row["text_a"],
            "text_b": row["text_b"],
            "metadata": {
                "model_a_name": row.get("model_a"),
                "model_b_name": row.get("model_b"),
            },
            "annotations": annotations,
        }
        output["comparisons"].append(comparison)

    return output


def results_to_annotated_pairs(
    results_dir: str,
    dataset_name: str,
    filter_to_constitution: bool = True,
) -> Dict[str, object]:
    """Convert ICAI results to annotated pairs format from files.

    Args:
        results_dir: Path to ICAI results directory
        dataset_name: Name for the dataset
        filter_to_constitution: Only include principles that made it to the constitution

    Returns:
        The annotated pairs format as a dictionary
    """
    results_path = Path(results_dir)

    # Load all required data using the icai loader module
    train_df = icai.load_train_data(results_path)
    principles = icai.load_principles(results_path)
    filtered_principles = icai.load_filtered_principles(results_path)
    comparison_votes = icai.load_votes_per_comparison(results_path)

    # Call the core implementation with loaded data
    result = create_annotated_pairs(
        train_df=train_df,
        principles=principles,
        filtered_principles=filtered_principles,
        comparison_votes=comparison_votes,
        dataset_name=dataset_name,
        filter_to_constitution=filter_to_constitution,
    )

    return result


def save_annotated_pairs_to_file(annotated_pairs: Dict, output_file: str) -> None:
    """Save the annotated pairs to a JSON file.

    Args:
        annotated_pairs: The annotated pairs dataset to save
        output_file: Path to the output file
    """
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(annotated_pairs, f, ensure_ascii=False, indent=2)
    logger.info(f"Created annotated pairs format dataset: {output_file}")
    logger.info(f"- Dataset contains {len(annotated_pairs['comparisons'])} comparisons")
    logger.info(f"- Dataset contains {len(annotated_pairs['annotators'])} annotators")
