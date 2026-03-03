# Image to WebP Converter

Convert images to WebP format with quality control. Supports single file and batch directory conversion.

## Installation

```bash
npx skills add biu/image-to-webp
```

Or install manually by copying this directory to your `.codebuddy/skills/` folder.

## Features

- 🖼️ Convert PNG, JPG, GIF, BMP, TIFF to WebP
- 📁 Batch process entire directories
- ⚙️ Configurable quality settings (0-100)
- 🚀 Fast and efficient using PIL/Pillow

## Usage

### Single File Conversion

```bash
python scripts/convert_to_webp.py image.png
python scripts/convert_to_webp.py image.jpg output.webp 90
```

### Batch Directory Conversion

```bash
python scripts/convert_to_webp.py --batch ./images
python scripts/convert_to_webp.py --batch ./images ./output 85
```

## Requirements

- Python 3.7+
- Pillow (PIL)

Install dependencies:
```bash
pip install Pillow
```

## Quality Guidelines

- **95-100**: Near-lossless quality
- **85-94**: High quality (recommended default: 85)
- **75-84**: Good quality with better compression
- **60-74**: Medium quality
- **Below 60**: Low quality, maximum compression

## Parameters

### Single File
- `input_file` (required): Path to input image
- `output_file` (optional): Output path (defaults to input name with .webp)
- `quality` (optional): Quality 0-100 (default: 85)

### Batch Mode
- `--batch` flag
- `input_dir` (required): Directory with images
- `output_dir` (optional): Output directory (defaults to input directory)
- `quality` (optional): Quality 0-100 (default: 85)

## Examples

```bash
# Convert with default quality (85)
python scripts/convert_to_webp.py photo.jpg

# Custom output and quality
python scripts/convert_to_webp.py photo.jpg optimized.webp 95

# Batch convert all images in a folder
python scripts/convert_to_webp.py --batch ./photos ./webp-output

# In-place batch conversion with quality
python scripts/convert_to_webp.py --batch ./photos 90
```

## License

MIT

## Author

biu
