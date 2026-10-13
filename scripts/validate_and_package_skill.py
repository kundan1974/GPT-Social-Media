#!/usr/bin/env python3
"""Validate this instruction-only skill and package it in a cloud checkout."""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / ".agents/skills/roohkesur-studio"

def require(condition, message):
    if not condition:
        raise ValueError(message)

def validate():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    require(match is not None, "Missing or invalid YAML frontmatter")
    # This skill deliberately uses JSON-quoted YAML string scalars.
    fields = {}
    for line in match.group(1).splitlines():
        key, value = line.split(":", 1)
        require(key.strip() not in fields, "Duplicate frontmatter key")
        fields[key.strip()] = json.loads(value.strip())
    require(set(fields) == {"name", "description"}, "Unexpected frontmatter keys")
    name, description = fields["name"], fields["description"]
    require(isinstance(name, str) and bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)), "Invalid skill name")
    require(len(name) <= 64 and name == SKILL.name, "Skill name/folder mismatch")
    require(isinstance(description, str) and 0 < len(description) <= 1024, "Invalid description")
    require("<" not in description and ">" not in description, "Angle brackets in description")

    documents = list(SKILL.rglob("*.md"))
    for document in documents:
        body = document.read_text(encoding="utf-8")
        require("[TODO:" not in body, f"Unfinished scaffold: {document.relative_to(ROOT)}")
        for target in re.findall(r"\]\(([^)]+)\)", body):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            path = (document.parent / target.split("#", 1)[0]).resolve()
            require(path.is_relative_to(SKILL.resolve()), "Reference leaves the skill bundle")
            require(path.is_file(), f"Broken internal reference in {document.relative_to(ROOT)}")

    metadata = (SKILL / "agents/openai.yaml").read_text(encoding="utf-8")
    interface = {}
    for line in metadata.splitlines():
        entry = re.fullmatch(r"  (display_name|short_description|default_prompt): (.*)", line)
        if entry:
            interface[entry.group(1)] = json.loads(entry.group(2))
    require(set(interface) == {"display_name", "short_description", "default_prompt"}, "Missing UI metadata")
    require(25 <= len(interface["short_description"]) <= 64, "Invalid UI description length")
    require("$" + name in interface["default_prompt"], "Default prompt must mention skill")
    require("allow_implicit_invocation: true" in metadata, "Discovery policy changed")

    manifest = json.loads((SKILL / "assets/templates/job-manifest.json").read_text(encoding="utf-8"))
    require(manifest["source"]["locked"] is True, "Poem must default to locked")
    require(manifest["source"]["poem_asset_id"] is None and manifest["audio"]["asset_id"] is None, "Public template contains production asset")
    outputs = manifest["requested_outputs"]
    require(outputs["social"] == {"width": 1080, "height": 1920, "duration_seconds": 30}, "Social defaults disagree with brief")
    require(outputs["youtube"]["target_min_seconds"] == 120 and outputs["youtube"]["target_max_seconds"] == 240, "YouTube duration band disagrees with brief")
    require(outputs["youtube"]["width"] == 1920 and outputs["youtube"]["height"] == 1080, "YouTube aspect ratio mismatch")
    require(outputs["artwork"]["line_count_min"] == 4 and outputs["artwork"]["line_count_max"] == 6, "Artwork line count mismatch")
    require(manifest["publication"]["status"] == "not_published", "Template claims publication")
    require(not manifest["outputs"] and not manifest["provider_jobs"], "Public template contains real output/job state")
    require(all(value is False for key, value in manifest["quality_review"].items() if key.endswith("_verified")), "Template falsely claims review")
    return len(documents)

def package():
    out = ROOT / "dist"
    out.mkdir(exist_ok=True)
    destination = out / "roohkesur-studio.zip"
    with zipfile.ZipFile(destination, "w", zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(SKILL.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(SKILL.parent))
    with zipfile.ZipFile(destination) as archive:
        require(archive.testzip() is None, "Invalid ZIP")
        require("roohkesur-studio/SKILL.md" in archive.namelist(), "Missing bundle entrypoint")
    print(f"Package: {destination.relative_to(ROOT)}")
    print(f"SHA256: {hashlib.sha256(destination.read_bytes()).hexdigest()}")

if __name__ == "__main__":
    try:
        count = validate()
        print(f"Validated skill frontmatter, metadata, {count} Markdown files, internal references and template invariants.")
        package()
    except (ValueError, KeyError, OSError, json.JSONDecodeError) as error:
        print(f"Validation failed: {error}", file=sys.stderr)
        sys.exit(1)
