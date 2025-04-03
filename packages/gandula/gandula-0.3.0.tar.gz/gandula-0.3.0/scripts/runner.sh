#!/bin/bash
set -e

# Configuration
INPUT_PATH="/path/to/pff/data"
OUTPUT_DIR="/path/to/output/parquet"
FORMAT="WIDE"  # or "LONG"

# Log file
LOG_FILE="pipeline_run_$(date +%Y%m%d_%H%M%S).log"

echo "Starting PFF data pipeline at $(date)" | tee -a "$LOG_FILE"
echo "Input path: $INPUT_PATH" | tee -a "$LOG_FILE"
echo "Output directory: $OUTPUT_DIR" | tee -a "$LOG_FILE"
echo "Format: $FORMAT" | tee -a "$LOG_FILE"

source .venv/bin/activate

python -c "
from pathlib import Path
from gandula.pipeline.runner import run_pipeline
from gandula.pipeline.transform import TransformFormat

output_files = run_pipeline(
    input_path='$INPUT_PATH',
    output_dir='$OUTPUT_DIR',
    transform_format=TransformFormat.$FORMAT
)

print(f'Successfully processed {len(output_files)} files:')
for path in output_files:
    print(f'  - {path}')
" 2>&1 | tee -a "$LOG_FILE"

echo "Pipeline completed at $(date)" | tee -a "$LOG_FILE"
