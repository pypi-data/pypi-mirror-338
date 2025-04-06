# File: tests/test_cli.py

import subprocess
import tempfile
import json
import sys
from pathlib import Path


def test_cli_validate_hello_message():
    # Create a valid hello message
    hello_message = {
        "protocol": "LOVE/1.0",
        "type": "HELLO",
        "device_id": "test-device",
        "timestamp": 1234567890.0,
        "capabilities": {
            "mic": True,
            "speaker": True
        }
    }

    # Write to a temporary file
    with tempfile.NamedTemporaryFile("w", delete=False, suffix=".json") as f:
        json.dump(hello_message, f)
        tmp_path = Path(f.name)

    # Run CLI command
    result = subprocess.run(
        [sys.executable, "-m", "love_protocol.cli.validate", str(tmp_path)],
        capture_output=True,
        text=True,
        env={"PYTHONPATH": "."}
    )

    # Clean up the temporary file
    tmp_path.unlink()

    assert result.returncode == 0
    assert "✅ Valid LOVE message" in result.stdout
