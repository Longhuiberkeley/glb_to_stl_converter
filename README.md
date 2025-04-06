# GLB to STL Converter

A simple Python tool to convert GLB (GL Transmission Binary Format) files to STL (Standard Triangle Language) format.

## Requirements

- Python 3.7 or higher
- trimesh
- numpy

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/glb_to_stl_converter.git
cd glb_to_stl_converter
```

2. Install the required packages:
```bash
pip install trimesh numpy
```

## Directory Setup

The converter requires two directories:
- `glb_files`: Where you place your GLB files for conversion
- `stl_files`: Where the converted STL files will be saved

Create these directories if they don't exist:
```bash
mkdir -p glb_files stl_files
```

## Usage

1. Place your GLB files in the `glb_files` directory.

2. Run the converter script:
```bash
python glb_to_stl_converter.py
```

3. The converted STL files will be available in the `stl_files` directory.

## How It Works

The script automatically:
- Scans the `glb_files` directory for all files with the `.glb` extension
- Converts each GLB file to STL format
- Saves the resulting STL files in the `stl_files` directory with the same base filename
- Creates the output directory if it doesn't exist

## Troubleshooting

If you encounter any issues:
- Ensure your GLB files are valid
- Check that you have the required dependencies installed
- Verify that you have read/write permissions for both directories
