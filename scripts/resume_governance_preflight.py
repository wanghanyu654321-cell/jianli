#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = ROOT / "resume-workspace" / "CURRENT_VERSION_INDEX.md"
REGISTRY_PATH = ROOT / "resume-workspace" / "GATE_REGISTRY.json"

ALLOWED_GATE_STATES = {"PASS", "PARTIAL", "FAIL", "BLOCKED", "NOT_RUN"}


def fail(message: str) -> None:
    print(f"GOVERNANCE PREFLIGHT FAIL: {message}", file=sys.stderr)
    sys.exit(1)


def extract_backtick_value(text: str, label: str) -> str:
    match = re.search(rf"^- {re.escape(label)}: `([^`]+)`", text, re.MULTILINE)
    if not match:
        fail(f"cannot find '{label}' in CURRENT_VERSION_INDEX.md")
    return match.group(1)


def git_branch() -> str | None:
    try:
        result = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        branch = result.stdout.strip()
        return branch if branch and branch != "HEAD" else None
    except Exception:
        return None


def main() -> None:
    if not INDEX_PATH.exists():
        fail(f"missing {INDEX_PATH.relative_to(ROOT)}")
    if not REGISTRY_PATH.exists():
        fail(f"missing {REGISTRY_PATH.relative_to(ROOT)}")

    index_text = INDEX_PATH.read_text(encoding="utf-8")
    try:
        registry = json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"GATE_REGISTRY.json is invalid JSON: {exc}")

    if registry.get("registry_status") != "CANONICAL_CURRENT_STATE":
        fail("registry_status must be CANONICAL_CURRENT_STATE")

    expected_repo = "wanghanyu654321-cell/jianli"
    if registry.get("repository") != expected_repo:
        fail(f"registry repository must be {expected_repo}")

    branch_from_index = extract_backtick_value(index_text, "Active branch")
    branch_from_registry = registry.get("branch")
    if branch_from_index != branch_from_registry:
        fail(
            f"branch mismatch: index={branch_from_index}, registry={branch_from_registry}"
        )

    actual_branch = git_branch()
    if actual_branch and actual_branch != branch_from_registry:
        fail(
            f"working tree branch mismatch: actual={actual_branch}, registry={branch_from_registry}"
        )

    source = registry.get("source") or {}
    epoch_registry = source.get("last_frozen_epoch")
    fingerprint_registry = source.get("last_frozen_sha256")
    currency_registry = source.get("source_currency")

    epoch_index = extract_backtick_value(index_text, "Last frozen source epoch")
    fingerprint_index = extract_backtick_value(index_text, "Last repository-frozen fingerprint")
    currency_index = extract_backtick_value(index_text, "Current source currency")

    if epoch_index != epoch_registry:
        fail(f"source epoch mismatch: index={epoch_index}, registry={epoch_registry}")
    if fingerprint_index != fingerprint_registry:
        fail("source fingerprint mismatch between index and registry")
    if currency_index != currency_registry:
        fail(
            f"source currency mismatch: index={currency_index}, registry={currency_registry}"
        )

    vocabulary = set(registry.get("gate_status_vocabulary") or [])
    if vocabulary != ALLOWED_GATE_STATES:
        fail(
            "gate_status_vocabulary must be exactly PASS/PARTIAL/FAIL/BLOCKED/NOT_RUN"
        )

    for role in ("R1", "R2", "R3"):
        state = registry.get(role)
        if not isinstance(state, dict):
            fail(f"missing registry state for {role}")

        artifact = state.get("artifact")
        if not artifact:
            fail(f"missing artifact path for {role}")
        artifact_path = ROOT / artifact
        if not artifact_path.exists():
            fail(f"current artifact for {role} does not exist: {artifact}")
        if f"`{artifact}`" not in index_text:
            fail(f"{role} artifact in registry is not listed in CURRENT_VERSION_INDEX.md")

        for key, value in state.items():
            if key.endswith("_gate") and value not in ALLOWED_GATE_STATES:
                fail(f"invalid gate state: {role}.{key}={value}")

        if state.get("application_ready") not in (True, False):
            fail(f"{role}.application_ready must be boolean")

    if registry.get("single_jd_gate") not in ALLOWED_GATE_STATES:
        fail("single_jd_gate has invalid state")

    if currency_registry != "CURRENT":
        ready_roles = [
            role
            for role in ("R1", "R2", "R3")
            if registry[role].get("application_ready") is True
        ]
        if ready_roles:
            fail(
                "source is not CURRENT but application_ready=true for: "
                + ", ".join(ready_roles)
            )

    print("GOVERNANCE PREFLIGHT PASS")
    print(f"repository={expected_repo}")
    print(f"branch={branch_from_registry}")
    print(f"source_epoch={epoch_registry}")
    print(f"source_currency={currency_registry}")
    for role in ("R1", "R2", "R3"):
        state = registry[role]
        print(
            f"{role}: artifact={state['artifact']} | "
            f"fact_currency={state['fact_currency_gate']} | "
            f"claim_mapping={state['claim_mapping_integrity_gate']} | "
            f"career_substance={state['career_substance_gate']} | "
            f"recruiter_quality={state['recruiter_quality_gate']} | "
            f"application_ready={state['application_ready']}"
        )


if __name__ == "__main__":
    main()
