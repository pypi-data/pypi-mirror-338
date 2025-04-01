#!/usr/bin/env python3
"""
pyrcodio - A CLI utility that generates names by combining subjects and attributes.
"""
import argparse
import random
import sys
import os
import pkg_resources
from typing import List, Optional


def get_default_data_path() -> str:
    """Get the default path for data files."""
    # When installed as a package, use the package data
    try:
        return pkg_resources.resource_filename('pyrcodio', 'data')
    except (ImportError, pkg_resources.DistributionNotFound):
        # During development, use a relative path
        base_dir = os.path.dirname(os.path.abspath(__file__))
        return os.path.join(base_dir, 'data')


def load_words_from_file(filename: str) -> List[str]:
    """Load words from a file, one word per line."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)


def generate_name(subjects: List[str], attributes: List[str], count: int = 1, separator="-") -> List[str]:
    """Generate 'count' number of names by combining random subjects and attributes."""
    if not subjects or not attributes:
        print("Error: Subject or attribute list is empty.")
        sys.exit(1)
    
    names = []
    for _ in range(count):
        subject = random.choice(subjects)
        attribute = random.choice(attributes)
        names.append(f"{subject}{separator}{attribute}")
    
    return names


def get_available_wordlists(data_dir: str) -> dict:
    """Get available subject and attribute files in the data directory."""
    wordlists = {'subjects': [], 'attributes': []}
    
    if not os.path.exists(data_dir):
        return wordlists
    
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        if os.path.isfile(file_path):
            if file.startswith('subjects_'):
                wordlists['subjects'].append(file)
            elif file.startswith('attributes_'):
                wordlists['attributes'].append(file)
    
    return wordlists


def main():
    data_dir = get_default_data_path()
    available_wordlists = get_available_wordlists(data_dir)
    
    subject_files = available_wordlists['subjects']
    attribute_files = available_wordlists['attributes']
    
    parser = argparse.ArgumentParser(
        description="Generate names by combining subjects and attributes."
    )
    
    parser.add_argument(
        "-s", "--subject-list",
        choices=subject_files if subject_files else None,
        default=subject_files[0] if subject_files else None,
        help="Specify which subject list to use"
    )
    
    parser.add_argument(
        "-a", "--attribute-list",
        choices=attribute_files if attribute_files else None,
        default=attribute_files[0] if attribute_files else None,
        help="Specify which attribute list to use"
    )
    
    parser.add_argument(
        "-c", "--count",
        type=int,
        default=1,
        help="Number of names to generate (default: 1)"
    )
    
    parser.add_argument(
        "-o", "--output",
        help="Output file to write generated names (default: print to stdout)"
    )
    
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available wordlists and exit"
    )
    
    parser.add_argument(
        "-d", "--data-dir",
        default=data_dir,
        help=f"Custom data directory (default: {data_dir})"
    )
    
    args = parser.parse_args()
    
    # If data directory is specified, update wordlists
    if args.data_dir != data_dir:
        data_dir = args.data_dir
        available_wordlists = get_available_wordlists(data_dir)
        subject_files = available_wordlists['subjects']
        attribute_files = available_wordlists['attributes']
    
    # List available wordlists if requested
    if args.list:
        print("Available subject lists:")
        for file in subject_files:
            print(f"  - {file}")
        print("\nAvailable attribute lists:")
        for file in attribute_files:
            print(f"  - {file}")
        sys.exit(0)
    
    # Check if wordlists are available
    if not subject_files:
        print("Error: No subject lists found in data directory.")
        print(f"Expected files starting with 'subjects_' in {data_dir}")
        sys.exit(1)
    
    if not attribute_files:
        print("Error: No attribute lists found in data directory.")
        print(f"Expected files starting with 'attributes_' in {data_dir}")
        sys.exit(1)
    
    # Use default wordlists if not specified
    subject_file = args.subject_list or subject_files[0]
    attribute_file = args.attribute_list or attribute_files[0]
    
    # Load subjects and attributes from files
    subjects = load_words_from_file(os.path.join(data_dir, subject_file))
    attributes = load_words_from_file(os.path.join(data_dir, attribute_file))
    
    # Generate names
    names = generate_name(subjects, attributes, args.count)
    
    # Output the generated names
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as file:
                for name in names:
                    file.write(f"{name}\n")
            print(f"Generated {len(names)} names and saved to {args.output}")
        except Exception as e:
            print(f"Error writing to output file: {e}")
            sys.exit(1)
    else:
        for name in names:
            print(name)


if __name__ == "__main__":
    main()