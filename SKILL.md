---
name: image-to-webp
description: Convert images (PNG, JPG, GIF, BMP, TIFF) to WebP format. Use this skill when the user requests converting images to WebP, optimizing images for web, or batch converting image formats. Supports single file conversion and batch directory conversion with configurable quality settings.
---

# Image to WebP Converter

## Overview

This skill enables conversion of images to WebP format, a modern image format that provides superior compression for images on the web. Supports single file conversion and batch processing of entire directories.

## When to Use This Skill

Use this skill when the user requests:
- Converting a specific image to WebP format
- Batch converting multiple images in a directory
- Optimizing images for web use
- Reducing image file sizes while maintaining quality
- Mentions "webp", "image conversion", or "optimize images"

## Supported Formats

Input formats supported:
- PNG
- JPG/JPEG
- GIF
- BMP
- TIFF/TIF

Output format: WebP (lossy or lossless)

## ⚠️ Important Best Practice

**ALWAYS place converted WebP files in the SAME directory as the source files!**

This is critical for:
- Maintaining organized project structure
- Easy reference management
- Consistent asset paths
- Simplified file management

Example:
```
✅ CORRECT:
/public/images/photo.png  → /public/images/photo.webp

❌ INCORRECT:
/public/images/photo.png  → /public/home/photo.webp
```

**When converting, always specify the output path to match the source file's directory**, only changing the file extension to `.webp`.

## Usage Instructions

### Single File Conversion

To convert a single image file to WebP:

```bash
python scripts/convert_to_webp.py <input_file> [output_file] [quality]
```

**Parameters:**
- `input_file` (required): Path to the input image
- `output_file` (optional): Path for the output WebP file. **IMPORTANT: Should be in the same directory as input_file, only changing the extension to `.webp`**
- `quality` (optional): Quality level 0-100 (default: 85). Higher values = better quality but larger file size

**Examples:**
```bash
# Convert with default settings (quality 85) - output in same directory
python scripts/convert_to_webp.py /path/to/image.png

# Convert keeping same directory structure
python scripts/convert_to_webp.py /public/images/photo.jpg /public/images/photo.webp

# Convert with custom quality, same directory
python scripts/convert_to_webp.py /assets/photo.png /assets/photo.webp 90

# Convert with quality only (outputs to same directory automatically)
python scripts/convert_to_webp.py /images/banner.png 95
```

### Batch Directory Conversion

To convert all images in a directory:

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

## Quality Guidelines

Recommended quality settings:
- **95-100**: Near-lossless, for images where quality is critical
- **85-94**: High quality, good balance (recommended default: 85)
- **75-84**: Good quality, better compression
- **60-74**: Medium quality, significant compression
- **Below 60**: Low quality, maximum compression

## Workflow

1. **Identify the request**: Determine if user wants single file or batch conversion
2. **Check dependencies**: Ensure PIL/Pillow is installed (`pip install Pillow`)
3. **Determine output path**: **CRITICAL - Always place output in the same directory as the source file**
   - Extract the directory path from the source file
   - Keep the same directory, only change the file extension to `.webp`
   - Example: `/public/images/photo.png` → `/public/images/photo.webp`
4. **Execute conversion**: Run the appropriate command with correct parameters
5. **Report results**: Inform user of successful conversion(s) and output location(s)

## Error Handling

Common errors and solutions:
- **PIL not installed**: Run `pip install Pillow`
- **File not found**: Verify the input path is correct
- **Permission denied**: Check write permissions for output directory
- **Unsupported format**: Ensure input file is one of the supported formats

## Resources

### scripts/convert_to_webp.py

Python script that handles image conversion using PIL/Pillow library. Supports both single file and batch directory conversion with configurable quality settings. The script automatically handles transparency, color mode conversion, and directory creation.
