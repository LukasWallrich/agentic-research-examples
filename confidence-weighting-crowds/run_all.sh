#!/usr/bin/env bash
# Reproduce the whole analysis from raw data with one command.
# Requires: uv, python3.12+. Network needed only for the first dependency
# install and for the (CC0) Confidence Database download if data are absent.
set -euo pipefail
cd "$(dirname "$0")"

PY=.venv/bin/python
if [ ! -x "$PY" ]; then
  uv venv --python 3.12 .venv
  uv pip install --python "$PY" numpy pandas scipy matplotlib openpyxl
fi

# Data: download the Confidence Database per-study CSVs if absent.
if [ "$(ls -1 data/confidence_database/*.csv 2>/dev/null | wc -l | tr -d ' ')" -lt 180 ]; then
  "$PY" analysis/scripts/download_confidence.py
fi

echo "== empirical =="   && "$PY" analysis/scripts/empirical.py
echo "== simulation =="  && "$PY" analysis/scripts/simulate.py
echo "== h6 =="          && "$PY" analysis/scripts/h6.py
echo "== figures =="     && "$PY" analysis/scripts/figures.py
echo "== verify =="      && "$PY" analysis/scripts/verify.py
echo "ALL DONE"