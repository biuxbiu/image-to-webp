# Image to WebP Converter

A powerful image format conversion tool that converts various common image formats to the modern WebP format. Supports single file conversion and batch processing.

## ✨ Features

- 🖼️ Support multiple input formats: PNG, JPG/JPEG, GIF, BMP, TIFF
- 📦 Support single file and batch directory conversion
- ⚙️ Customizable quality parameters (0-100)
- 🚀 Efficient compression, reduce file size while maintaining good quality
- 🎯 Automatic handling of transparency and color mode conversion

## 📋 Supported Formats

**Input formats:**
- PNG
- JPG/JPEG
- GIF
- BMP
- TIFF/TIF

**Output format:** WebP (lossy or lossless)

## 🔧 Installation

```bash
pip install Pillow
```

## 📖 Usage

### Single File Conversion

```bash
python scripts/convert_to_webp.py <input_file> [output_file] [quality]
```

**Parameters:**
- `input_file` (required): Path to the input image
- `output_file` (optional): Path for the output WebP file. If not specified, uses the input filename with `.webp` extension
- `quality` (optional): Quality level 0-100 (default: 85)

**Examples:**

```bash
# Convert with default settings (quality 85)
python scripts/convert_to_webp.py image.png

# Convert with custom output path
python scripts/convert_to_webp.py image.jpg output/image.webp

# Convert with custom quality
python scripts/convert_to_webp.py photo.png photo.webp 90

# Convert with quality only
python scripts/convert_to_webp.py image.png 95
```

### Batch Directory Conversion

```bash
python scripts/convert_to_webp.py --batch <input_dir> [output_dir] [quality]
```

**Parameters:**
- `input_dir` (required): Directory containing images to convert
- `output_dir` (optional): Directory for output WebP files. If not specified, uses the input directory
- `quality` (optional): Quality level 0-100 (default: 85)

**Examples:**

```bash
# Convert all images in a directory (in-place)
python scripts/convert_to_webp.py --batch ./images

# Convert to a different output directory
python scripts/convert_to_webp.py --batch ./images ./webp-output

# Batch convert with custom quality
python scripts/convert_to_webp.py --batch ./images ./webp-output 90

# Batch convert in-place with quality
python scripts/convert_to_webp.py --batch ./images 95
```

## 🎨 Quality Guidelines

| Quality Range | Description | Use Case |
|--------------|-------------|----------|
| 95-100 | Near-lossless, highest quality | Images where quality is critical |
| 85-94 | High quality, balanced | Recommended default (85) |
| 75-84 | Good quality, better compression | General web usage |
| 60-74 | Medium quality, high compression | Size-sensitive scenarios |
| <60 | Low quality, maximum compression | Thumbnails or low-quality needs |

## 🚨 Troubleshooting

| Error | Solution |
|-------|----------|
| PIL not installed | Run `pip install Pillow` |
| File not found | Verify the input path is correct |
| Permission denied | Check write permissions for output directory |
| Unsupported format | Ensure input file is one of the supported formats |

## 💡 About WebP

WebP is a modern image format developed by Google. Compared to traditional JPEG and PNG formats:
- Smaller file size at the same quality (typically 25-35% reduction)
- Supports both lossy and lossless compression
- Supports transparency (Alpha channel)
- Widely supported by all modern browsers

## 📄 License

MIT

## 🤝 Contributing

Issues and Pull Requests are welcome!
