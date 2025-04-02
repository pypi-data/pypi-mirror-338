"""Command-line interface for FileMint."""

import os
import argparse
import sys
from typing import List, Optional

from filemint.generators import generate_test_files


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """Parse command line arguments.
    
    Args:
        args: Command line arguments (defaults to sys.argv[1:])
        
    Returns:
        Parsed command line arguments
    """
    parser = argparse.ArgumentParser(
        description="FileMint - Generate test files in various formats",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    
    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default="test_files",
        help="Directory where test files will be saved",
    )
    
    parser.add_argument(
        "--csv",
        type=int,
        default=10,
        help="Number of CSV files to generate",
    )
    
    parser.add_argument(
        "--txt",
        type=int,
        default=10,
        help="Number of text files to generate",
    )
    
    parser.add_argument(
        "--bin",
        type=int,
        default=10,
        help="Number of binary files to generate",
    )
    
    parser.add_argument(
        "--invalid",
        type=int,
        default=10,
        help="Number of invalid CSV files to generate",
    )
    
    return parser.parse_args(args)


def main(args: Optional[List[str]] = None) -> int:
    """Main entry point for the CLI.
    
    Args:
        args: Command line arguments (defaults to sys.argv[1:])
        
    Returns:
        Exit code (0 for success, non-zero for errors)
    """
    parsed_args = parse_args(args)
    
    try:
        # Generate the test files
        generated_files = generate_test_files(
            output_dir=parsed_args.output_dir,
            num_csv=parsed_args.csv,
            num_txt=parsed_args.txt,
            num_binary=parsed_args.bin,
            num_invalid=parsed_args.invalid,
        )
        
        # Print summary
        print(f"Generated {len(generated_files)} files in '{os.path.abspath(parsed_args.output_dir)}':")
        print(f"  - CSV files: {parsed_args.csv}")
        print(f"  - Text files: {parsed_args.txt}")
        print(f"  - Binary files: {parsed_args.bin}")
        print(f"  - Invalid CSV files: {parsed_args.invalid}")
        
        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main()) 