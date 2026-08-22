#!/usr/bin/env python3
"""Maintain review gates, decisions, and per-artifact states for career assets."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path

GATES = (
    "task_contract",
    "evidence_position",
    "content",
    "structure",
    "visual",
    "qa",
    "final_confirmation",
)
STATUSES = ("pending", "approved", "waived", "not_required")
DECISION_STATUSES = ("proposal", "recommended", "confirmed", "rejected", "constraint", "open")
DECISION_AREAS = ("task", "fact", "position", "content", "structure", "visual", "language", "release")
ARTIFACT_STATUSES = (
    "draft",
    "candidate",
    "confirmed",
    "release_ready",
    "deployed",
    "real_world_validated",
    "on_hold",
    "not_required",
    "rejected",
)
PROJECT_PHASES = ("intake", "modeling", "production", "qa", "release", "feedback", "complete")
CONTRACT_NAMES = (
    "task",
    "market",
    "privacy",
    "evidence",
    "claims",
    "carrier",
    "terminology",
    "structure",
    "visual",
    "validation",
    "release",
)
CONTRACT_STATUSES = ("missing", "draft", "current", "frozen")
ACTION_REQUIREMENTS = {
    "build-resume": ("task_contract", "evidence_position", "content", "structure", "visual"),
    "build-website": ("task_contract", "evidence_position", "content", "structure", "visual"),
    "release": GATES,
}


def load_state(path: Path) -> dict:
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SystemExit(f"state file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SystemExit(f"invalid JSON in state file: {path}: {exc}") from exc
    if state.get("schema_version") not in {1, 2} or not isinstance(state.get("gates"), dict):
        raise SystemExit("unsupported or incomplete career-assets state")
    state.setdefault("decisions", [])
    state.setdefault("artifacts", {})
    state.setdefault("contracts", {})
    state.setdefault("project_phase", "legacy")
    state.setdefault("excluded_inputs", [])
    return state


def write_state(path: Path, state: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def command_init(args: argparse.Namespace) -> None:
    path = Path(args.state)
    if path.exists() and not args.force:
        raise SystemExit(f"state file already exists: {path}; use --force only for an intentional restart")
    state = {
        "schema_version": 2,
        "project": args.project,
        "scope": [item.strip() for item in args.scope.split(",") if item.strip()],
        "project_phase": "intake",
        "artifacts": {
            item: {"status": "draft", "source": "", "destination": "", "updated_at": ""}
            for item in [part.strip() for part in args.scope.split(",") if part.strip()]
        },
        "contracts": {
            name: {"status": "missing", "path": "", "updated_at": ""} for name in CONTRACT_NAMES
        },
        "decisions": [],
        "excluded_inputs": [],
        "gates": {
            gate: {"status": "pending", "note": "", "evidence": "", "decided_at": ""}
            for gate in GATES
        },
    }
    write_state(path, state)
    print(f"initialized: {path}")


def command_decide(args: argparse.Namespace) -> None:
    if not args.note.strip():
        raise SystemExit("--note is required so the decision remains auditable")
    state_path = Path(args.state)
    state = load_state(state_path)
    state["gates"][args.gate] = {
        "status": args.status,
        "note": args.note.strip(),
        "evidence": args.evidence.strip(),
        "decided_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    if state.get("schema_version") == 1 and args.gate == "final_confirmation" and args.status == "approved":
        state["artifact_status"] = "confirmed"
    write_state(state_path, state)
    print(f"recorded: {args.gate}={args.status}")


def command_reopen(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    start = GATES.index(args.gate)
    for gate in GATES[start:]:
        state["gates"][gate] = {"status": "pending", "note": "", "evidence": "", "decided_at": ""}
    if state.get("schema_version") == 1:
        state["artifact_status"] = "candidate"
    write_state(state_path, state)
    print(f"reopened: {', '.join(GATES[start:])}")


def command_record(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    statement = args.statement.strip()
    reason = args.reason.strip()
    if not statement or not reason:
        raise SystemExit("--statement and --reason are required")
    next_id = max((item.get("id", 0) for item in state["decisions"]), default=0) + 1
    state["decisions"].append(
        {
            "id": next_id,
            "area": args.area,
            "status": args.status,
            "statement": statement,
            "reason": reason,
            "affects": [item.strip() for item in args.affects.split(",") if item.strip()],
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    write_state(state_path, state)
    print(f"recorded decision: {next_id} {args.area}/{args.status}")


def command_artifact(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    current = state["artifacts"].setdefault(args.name, {})
    current.update(
        {
            "status": args.status,
            "source": args.source.strip() or current.get("source", ""),
            "destination": args.destination.strip() or current.get("destination", ""),
            "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    write_state(state_path, state)
    print(f"recorded artifact: {args.name}={args.status}")


def command_contract(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    contracts = state.setdefault("contracts", {})
    contracts[args.name] = {
        "status": args.status,
        "path": args.path.strip(),
        "updated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    write_state(state_path, state)
    print(f"recorded contract: {args.name}={args.status}")


def command_phase(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    state["project_phase"] = args.phase
    write_state(state_path, state)
    print(f"recorded project phase: {args.phase}")


def command_exclude(args: argparse.Namespace) -> None:
    state_path = Path(args.state)
    state = load_state(state_path)
    state.setdefault("excluded_inputs", []).append(
        {
            "description": args.description.strip(),
            "reason": args.reason.strip(),
            "replacement": args.replacement.strip(),
            "recorded_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        }
    )
    write_state(state_path, state)
    print("recorded excluded input")


def command_check(args: argparse.Namespace) -> None:
    state = load_state(Path(args.state))
    missing = []
    for gate in ACTION_REQUIREMENTS[args.action]:
        item = state["gates"].get(gate, {})
        valid_status = item.get("status") in {"approved", "waived"}
        if not valid_status or not item.get("note", "").strip():
            missing.append(gate)
    if missing:
        print(f"BLOCKED {args.action}: pending or unaudited gates: {', '.join(missing)}")
        raise SystemExit(2)
    if args.action == "release" and (
        state["gates"]["qa"]["status"] != "approved"
        or state["gates"]["final_confirmation"]["status"] != "approved"
    ):
        print("BLOCKED release: qa and final_confirmation must both be approved")
        raise SystemExit(2)
    print(f"PASS {args.action}")


def command_show(args: argparse.Namespace) -> None:
    state = load_state(Path(args.state))
    print(f"project: {state.get('project', '')}")
    print(f"scope: {', '.join(state.get('scope', []))}")
    print(f"project_phase: {state.get('project_phase', 'legacy')}")
    if "artifact_status" in state:
        print(f"legacy_artifact_status: {state.get('artifact_status', '')}")
    for gate in GATES:
        item = state["gates"].get(gate, {})
        print(f"{gate}: {item.get('status', 'missing')} | {item.get('note', '')}")
    for name, item in state.get("artifacts", {}).items():
        print(f"artifact {name}: {item.get('status', 'missing')} | {item.get('destination', '')}")
    for name, item in state.get("contracts", {}).items():
        print(f"contract {name}: {item.get('status', 'missing')} | {item.get('path', '')}")
    print(f"decisions: {len(state.get('decisions', []))}")
    print(f"excluded_inputs: {len(state.get('excluded_inputs', []))}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)

    init = sub.add_parser("init")
    init.add_argument("--state", required=True)
    init.add_argument("--project", required=True)
    init.add_argument("--scope", required=True, help="comma-separated deliverable scopes")
    init.add_argument("--force", action="store_true")
    init.set_defaults(func=command_init)

    decide = sub.add_parser("decide")
    decide.add_argument("--state", required=True)
    decide.add_argument("--gate", required=True, choices=GATES)
    decide.add_argument("--status", required=True, choices=STATUSES[1:])
    decide.add_argument("--note", required=True)
    decide.add_argument("--evidence", default="", help="path or identifier of the reviewed artifact")
    decide.set_defaults(func=command_decide)

    reopen = sub.add_parser("reopen")
    reopen.add_argument("--state", required=True)
    reopen.add_argument("--gate", required=True, choices=GATES)
    reopen.set_defaults(func=command_reopen)

    record = sub.add_parser("record")
    record.add_argument("--state", required=True)
    record.add_argument("--area", required=True, choices=DECISION_AREAS)
    record.add_argument("--status", required=True, choices=DECISION_STATUSES)
    record.add_argument("--statement", required=True)
    record.add_argument("--reason", required=True)
    record.add_argument("--affects", default="", help="comma-separated affected artifacts or layers")
    record.set_defaults(func=command_record)

    artifact = sub.add_parser("artifact")
    artifact.add_argument("--state", required=True)
    artifact.add_argument("--name", required=True)
    artifact.add_argument("--status", required=True, choices=ARTIFACT_STATUSES)
    artifact.add_argument("--source", default="")
    artifact.add_argument("--destination", default="")
    artifact.set_defaults(func=command_artifact)

    contract = sub.add_parser("contract")
    contract.add_argument("--state", required=True)
    contract.add_argument("--name", required=True, choices=CONTRACT_NAMES)
    contract.add_argument("--status", required=True, choices=CONTRACT_STATUSES)
    contract.add_argument("--path", default="")
    contract.set_defaults(func=command_contract)

    phase = sub.add_parser("phase")
    phase.add_argument("--state", required=True)
    phase.add_argument("--phase", required=True, choices=PROJECT_PHASES)
    phase.set_defaults(func=command_phase)

    exclude = sub.add_parser("exclude")
    exclude.add_argument("--state", required=True)
    exclude.add_argument("--description", required=True, help="descriptor only; do not copy sensitive content")
    exclude.add_argument("--reason", required=True)
    exclude.add_argument("--replacement", default="", help="redacted summary or safer evidence to request")
    exclude.set_defaults(func=command_exclude)

    check = sub.add_parser("check")
    check.add_argument("--state", required=True)
    check.add_argument("--action", required=True, choices=tuple(ACTION_REQUIREMENTS))
    check.set_defaults(func=command_check)

    show = sub.add_parser("show")
    show.add_argument("--state", required=True)
    show.set_defaults(func=command_show)
    return parser


if __name__ == "__main__":
    parsed = build_parser().parse_args()
    parsed.func(parsed)
