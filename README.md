# Face Expression Editor

## Goal
Edit a person's facial expression in a photo while preserving
their identity and the photo's realistic appearance.

## Initial scope
- One clearly visible face in a still photo.
- Expressions: smile, laugh, cry, sad, surprised, angry,
  tired, wink, disgust, and kiss.
- Preserve hairstyle, clothing, background, and camera angle.

## Approach
Start with a pretrained model and measure its performance.
Consider fine-tuning only if evaluation identifies a problem
that simpler improvements do not resolve.

## Evaluation
Assess expression recognition, identity, realism, and preservation.
Natural variations within each expression are acceptable.

The planned baseline uses five photos and ten expressions.
A smaller feasibility experiment will come first.

## Current status
- Requirements and initial evaluation criteria agreed.
- Five input photos collected and source links recorded.
- Local Git repository initialized.
- University GPU access being investigated.
- No model selected or run yet.

## Data
Input photos are stored locally in data/baseline_inputs/.
Source records are in data/input_manifest.csv.
Input photos are excluded from Git.

