#!/bin/bash
# Pre-commit hook wrapper (Unix)
# Python 스크립트 호출

REPO_ROOT="$(git rev-parse --show-toplevel)"
PYTHON_SCRIPT="$REPO_ROOT/scripts/pre_commit_hook.py"

export PYTHONIOENCODING=utf-8

# uv 또는 python으로 실행
if command -v uv &> /dev/null; then
    uv run "$PYTHON_SCRIPT"
elif [ -x "$HOME/.local/bin/uv" ]; then
    "$HOME/.local/bin/uv" run "$PYTHON_SCRIPT"
elif command -v python &> /dev/null; then
    python "$PYTHON_SCRIPT"
else
    python3 "$PYTHON_SCRIPT"
fi
