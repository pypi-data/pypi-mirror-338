# File: love_protocol/cli/validate.py

"""
Command-line tool for validating LOVE protocol messages.

This CLI tool accepts a path to a JSON file and validates the contents
as a LOVE protocol message using the `validate_message_dict()` function.

Usage:
    python -m love_protocol.cli.validate path/to/message.json [--strict]

The tool returns exit code 0 if valid, or 1 on failure.
"""

import json
import sys
from pathlib import Path
import argparse
from love_protocol.core.validate import validate_message_dict


def main():
    """
    Main entry point for the LOVE message validator CLI.

    This function:
    - Parses command-line arguments.
    - Loads and parses the input JSON file.
    - Validates the content against the LOVE message schema.
    - Outputs the result and exits with appropriate status code.

    Command-line arguments:
        file: Path to the JSON message file to validate.
        --strict: If set, raises on validation errors instead of collecting them.
    """
    parser = argparse.ArgumentParser(description="Validate a LOVE message JSON file.")
    parser.add_argument("file", help="Path to the JSON message file")
    parser.add_argument("--strict", action="store_true", help="Raise error on invalid messages")
    args = parser.parse_args()

    file_path = Path(args.file)
    if not file_path.exists():
        print(f"❌ File not found: {file_path}")
        sys.exit(1)

    try:
        with open(file_path, "r") as f:
            obj = json.load(f)
    except json.JSONDecodeError as e:
        print(f"❌ Invalid JSON: {e}")
        sys.exit(1)

    result = validate_message_dict(obj, strict=args.strict)
    if result["valid"]:
        print("✅ Valid LOVE message")
        sys.exit(0)
    else:
        print("❌ Invalid LOVE message:")
        for err in result["errors"]:
            print(f"  - {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
