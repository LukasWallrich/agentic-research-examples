#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
if ! command -v uv >/dev/null; then
  echo 'Install uv, then rerun. This script also requires pandoc and XeLaTeX or tectonic.' >&2
  exit 1
fi
if [[ ! -x .venv/bin/python ]]; then uv venv --python 3.14 .venv; fi
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/python scripts/simulate.py run
.venv/bin/python scripts/verify.py
.venv/bin/python scripts/independent_check.py
.venv/bin/python scripts/exploratory_checks.py
.venv/bin/python scripts/exploratory_grid.py
.venv/bin/python scripts/build_manuscript.py
./scripts/render_manuscript.sh
.venv/bin/python scripts/package_audit.py
