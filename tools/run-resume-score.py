#!/usr/bin/env python3
import os
import sys
import argparse

_ORIGINAL_CWD = os.getcwd()
HIRING_AGENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hiring-agent")
sys.path.insert(0, HIRING_AGENT_DIR)
os.chdir(HIRING_AGENT_DIR)

import config as hiring_config  # noqa: E402

# Patched here, not in providers.json: edits inside the submodule's working tree
# are silently dropped on a fresh clone or `git submodule update`.
_EXTRA_GEMINI_MODELS = {
    "gemini-3.6-flash": {"temperature": 0.1, "top_p": 0.9},
    "gemini-3.5-flash": {"temperature": 0.1, "top_p": 0.9},
    "gemini-3.5-flash-lite": {"temperature": 0.1, "top_p": 0.9},
}
hiring_config._config["providers"]["gemini"]["models"].update(_EXTRA_GEMINI_MODELS)
hiring_config.MODEL_PARAMETERS.update(_EXTRA_GEMINI_MODELS)

import models as hiring_models  # noqa: E402
from roles import load_role, list_available_roles  # noqa: E402
from score import main as score_main  # noqa: E402


def inline_refs(schema):
    # Gemini's structured-output endpoint 503s on $ref/$defs (what pydantic emits
    # for nested models like Basics.location); inline them before sending.
    defs = schema.get("$defs", {})

    def resolve(node):
        if isinstance(node, dict):
            if "$ref" in node:
                ref_name = node["$ref"].split("/")[-1]
                resolved = resolve(defs[ref_name])
                return {**resolved, **{k: v for k, v in node.items() if k != "$ref"}}
            return {k: resolve(v) for k, v in node.items() if k != "$defs"}
        if isinstance(node, list):
            return [resolve(v) for v in node]
        return node

    result = resolve(schema)
    result.pop("$defs", None)
    return result


_original_chat = hiring_models.OpenAICompatibleProvider.chat


def _patched_chat(self, model, messages, options=None, **kwargs):
    if kwargs.get("format"):
        kwargs["format"] = inline_refs(kwargs["format"])
    return _original_chat(self, model, messages, options=options, **kwargs)


hiring_models.OpenAICompatibleProvider.chat = _patched_chat


if __name__ == "__main__":
    available_roles = list_available_roles()
    parser = argparse.ArgumentParser(description="Score a resume against a role's rubric.")
    parser.add_argument("pdf_path", help="Path to the resume PDF to evaluate")
    parser.add_argument(
        "--role",
        required=True,
        help="Role to score against. Available: " + ", ".join(available_roles),
    )
    args = parser.parse_args()

    pdf_path = os.path.abspath(os.path.join(_ORIGINAL_CWD, args.pdf_path))
    if not os.path.exists(pdf_path):
        print(f"Error: File '{pdf_path}' does not exist.")
        sys.exit(1)

    try:
        role = load_role(args.role)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    score_main(pdf_path, role)
