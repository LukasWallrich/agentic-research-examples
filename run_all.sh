#!/usr/bin/env bash
# Rerun the whole study from the raw data: ./run_all.sh
# Steps 02-03 regenerate the model predictions (about 15 minutes on 8 cores); they are
# deterministic, so the rerun reproduces the preregistered predictions.
set -euo pipefail
cd "$(dirname "$0")"
Rscript R/00_fetch.R                  # download OpAQ and verify its SHA-256
Rscript R/01_design_inventory.R       # design-only inventory (no estimates)
Rscript R/02_calibrate_models.R       # calibrate models to Jacowitz & Kahneman (1995)
Rscript R/03_simulate_predictions.R   # model predictions on the OpAQ designs
Rscript R/03b_decision_properties.R   # operating characteristics of the decision rules
Rscript R/03c_prereg_tables.R         # prediction tables used in the preregistration
Rscript R/04_confirmatory.R           # preregistered confirmatory analyses
Rscript R/05_exploratory.R            # exploratory analyses (labelled as such)
Rscript R/05b_sensitivity.R           # post-hoc sensitivity analyses
Rscript R/05c_within_cells_table.R    # descriptive table of within-item cells
Rscript R/05d_raw_scale_model.R       # exploratory raw-scale constant-weight model (E6)
Rscript R/05e_review_checks.R         # post-hoc checks requested in review round 1
Rscript R/05f_round2_checks.R         # exploratory analyses requested in review round 2
Rscript R/06_figures.R                # figures
quarto render manuscript/manuscript.qmd   # manuscript (docx and html)
