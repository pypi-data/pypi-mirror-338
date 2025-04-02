#!/bin/bash
set -euo pipefail

# Default configuration
OPENCONFIG_REPO="${OPENCONFIG_REPO:-https://github.com/openconfig/public.git}"
REPO_DIR="${REPO_DIR:-openconfig-public}"
MODELS=""
EXCLUDE=""
OUTPUT_PATH="${OUTPUT_PATH:-ocbindings}"

# Usage info
usage() {
    echo "Usage: $0 [-o output_path] [-m models] [-e exclude] [-r repo_url] [-d repo_dir]"
    echo "  -o output_path : Output directory (or .py file for single-file output)."
    echo "  -m models      : Space-separated list of models to include. Default is all."
    echo "  -e exclude     : Space-separated keywords to filter from included files."
    echo "  -r repo_url    : URL of the OpenConfig repository."
    echo "  -d repo_dir    : Directory name for the cloned repository."
    exit 1
}

# Parse CLI options
while getopts ":o:m:e:r:d:" opt; do
    case ${opt} in
        o ) OUTPUT_PATH=$OPTARG ;;
        m ) MODELS=$OPTARG ;;
        e ) EXCLUDE=$OPTARG ;;
        r ) OPENCONFIG_REPO=$OPTARG ;;
        d ) REPO_DIR=$OPTARG ;;
        \? ) echo "Invalid option: -$OPTARG" >&2; usage ;;
        : ) echo "Option -$OPTARG requires an argument." >&2; usage ;;
    esac
done
shift $((OPTIND -1))

# Tool checks
for tool in git pyang; do
  if ! command -v $tool &>/dev/null; then
    echo "Error: $tool is not installed."
    exit 1
  fi
done

# Clone or update repo
if [ -d "$REPO_DIR" ]; then
    echo "Repository exists. Pulling latest..."
    git -C "$REPO_DIR" pull
else
    echo "Cloning repository from $OPENCONFIG_REPO..."
    git clone --depth 1 "$OPENCONFIG_REPO" "$REPO_DIR"
fi

# Define paths
MODELS_DIR="$REPO_DIR/release/models"
TYPES_DIR="$MODELS_DIR/types"
TRANSPORT_DIR="$MODELS_DIR/transport"
IETF_DIR="$REPO_DIR/third_party/ietf"

# Locate PyangBind plugin
PYBINDPLUGIN=$(python3 -c 'import pyangbind; import os; print("{}/plugin".format(os.path.dirname(pyangbind.__file__)))')
if [[ -z "$PYBINDPLUGIN" ]]; then
    echo "Error: Unable to locate PyangBind plugin directory."
    exit 1
fi

# Gather all matching YANG files
ALL_YANG_FILES=()
if [[ -z "$MODELS" ]]; then
    echo "Including all models..."
    while IFS= read -r file; do
        ALL_YANG_FILES+=("$file")
    done < <(find "$MODELS_DIR" -name "openconfig-*.yang")
else
    echo "Including only specified models: $MODELS"
    for model in $MODELS; do
        while IFS= read -r file; do
            ALL_YANG_FILES+=("$file")
        done < <(find "$MODELS_DIR" -path "*$model*" -name "openconfig-*.yang")
    done
fi

# Apply exclusion filter
YANG_FILES=()
for yf in "${ALL_YANG_FILES[@]}"; do
    skip=false
    for pattern in $EXCLUDE; do
        if [[ "$yf" == *"$pattern"* ]]; then
            skip=true
            break
        fi
    done
    if ! $skip; then
        YANG_FILES+=("$yf")
    fi
done

# Final check
if [[ ${#YANG_FILES[@]} -eq 0 ]]; then
    echo "No YANG files found after filtering. Exiting."
    exit 1
fi

# Set output method
if [[ "$OUTPUT_PATH" == *.py ]]; then
    PYANG_OUTPUT_OPT="-o"
else
    mkdir -p "$OUTPUT_PATH"
    PYANG_OUTPUT_OPT="--split-class-dir"
fi

# Run Pyang
echo "Generating Python bindings..."
pyang --plugindir "$PYBINDPLUGIN" \
      --path "$MODELS_DIR" \
      --path "$TYPES_DIR" \
      --path "$TRANSPORT_DIR" \
      --path "$IETF_DIR" \
      -f pybind \
      $PYANG_OUTPUT_OPT "$OUTPUT_PATH" \
      "${YANG_FILES[@]}"

echo "Bindings written to: $OUTPUT_PATH"
