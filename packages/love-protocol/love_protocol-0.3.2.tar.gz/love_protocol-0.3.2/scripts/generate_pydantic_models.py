#!/usr/bin/env python3
"""
Generates Pydantic models from all JSON schemas in ./schemas
and writes them into ./love_protocol/types using ALL_CAPS class names.
"""

import subprocess
from pathlib import Path

# Adjust paths
SCHEMA_DIR = Path(__file__).resolve().parent.parent.parent / ".." / "schemas"
OUTPUT_DIR = Path(__file__).resolve().parent.parent / "love_protocol" / "types"
INIT_FILE = OUTPUT_DIR / "__init__.py"

def to_snake_case(name: str) -> str:
    return name.lower()

def to_class_name(name: str) -> str:
    return name.replace("_", "").upper()

def generate_models():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    imports = []

    for schema_file in sorted(SCHEMA_DIR.glob("*.json")):
        name = schema_file.stem
        filename = to_snake_case(name) + ".py"
        classname = to_class_name(name)

        output_path = OUTPUT_DIR / filename

        print(f"🔁 Generating {classname} → {filename}")
        cmd = [
            "datamodel-codegen",
            "--input", str(schema_file),
            "--input-file-type", "jsonschema",
            "--output", str(output_path),
            "--class-name", classname,
            "--use-standard-collections",
            "--disable-timestamp",
            "--target-python-version", "3.9",
        ]
        subprocess.run(cmd, check=True)
        imports.append(f"from .{filename[:-3]} import {classname}")

    # Write __init__.py
    INIT_FILE.write_text("\n".join(imports) + "\n")

if __name__ == "__main__":
    generate_models()

