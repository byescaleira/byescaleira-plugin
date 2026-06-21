#!/usr/bin/env python3
"""
byescaleira MCP server
Lightweight programmatic interface for the byescaleira operating system.
"""

import json
import os
import sys
from pathlib import Path

CODENAMES = {
    "projects": [
        "Apollo", "Artemis", "Voyager", "Pioneer", "Nova", "Orion",
        "Kepler", "Hubble", "Sputnik", "Galileo", "Osiris", "Titan"
    ],
    "modules": ["Orbit", "Nova", "Zenith", "Core", "Prism", "Forge"],
    "releases": [
        "Dust", "Breeze", "Atmosphere", "Stratosphere", "Ionosphere",
        "Exosphere", "Magnetosphere", "Aurora", "Eclipse", "Solstice"
    ],
    "branches": ["liftoff", "orbit", "reentry", "impact", "debris"],
    "environments": ["Simulator", "TestFlight", "Production", "GroundControl", "LaunchPad"]
}

SKELETON_FILES = [
    "README.md",
    "PROPOSAL.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "ARCHITECTURE.md",
    "DECISIONS.md",
    "DESIGN.md",
    ".github/workflows/ci.yml",
    ".github/pull_request_template.md",
    ".github/issue_templates/bug_report.md",
    ".github/issue_templates/feature_request.md",
    "scripts/install.sh"
]


def list_codenames(category=None):
    if category is None:
        return CODENAMES
    return {category: CODENAMES.get(category, [])}


def validate_skeleton(path):
    root = Path(path)
    missing = []
    for f in SKELETON_FILES:
        if not (root / f).exists():
            missing.append(f)
    return {
        "valid": len(missing) == 0,
        "checked": len(SKELETON_FILES),
        "missing": missing
    }


def suggest_codename(category, prefix=None):
    names = CODENAMES.get(category, [])
    if not names:
        return {"error": f"unknown category: {category}"}
    # Naive suggestion: pick first unused is not tracked; just return a shortlist
    if prefix:
        names = [n for n in names if n.lower().startswith(prefix.lower())]
    return {
        "category": category,
        "suggestions": names[:3]
    }


def handle_request(request: dict):
    method = request.get("method")
    params = request.get("params", {})

    if method == "list_codenames":
        return list_codenames(params.get("category"))
    if method == "validate_skeleton":
        return validate_skeleton(params.get("path", "."))
    if method == "suggest_codename":
        return suggest_codename(params.get("category"), params.get("prefix"))

    return {"error": f"unknown method: {method}"}


def main():
    print("byescaleira MCP server ready", file=sys.stderr)
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            request = json.loads(line)
            response = handle_request(request)
        except json.JSONDecodeError as e:
            response = {"error": f"invalid JSON: {e}"}
        print(json.dumps(response), flush=True)


if __name__ == "__main__":
    main()
