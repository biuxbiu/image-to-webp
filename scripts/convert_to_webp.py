#!/usr/bin/env python3
"""
Convert images to WebP format.
Supports: PNG, JPG, JPEG, GIF, BMP, TIFF
"""

import sys
import os
from pathlib import Path
from PIL import Image


def convert_to_webp(input_path: str, output_path: str = None, quality: int = 85) -> str:
    """
    Convert an image to WebP format.
    
    Args:
        input_path: Path to input image
        output_path: Path to output WebP file (optional, defaults to input_path with .webp extension)
        quality: WebP quality (0-100, default 85)
    
    Returns:
        Path to the output WebP file
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    
    # Generate output path if not provided
    if output_path is None:
        output_path = input_path.with_suffix('.webp')
    else:
        output_path = Path(output_path)
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Convert image
    with Image.open(input_path) as img:
        # Convert RGBA to RGB if necessary
        if img.mode in ('RGBA', 'LA', 'P'):
            # Keep transparency for WebP
            img.save(output_path, 'WEBP', quality=quality, lossless=False)
        else:
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.save(output_path, 'WEBP', quality=quality)
    
    return str(output_path)


def batch_convert(input_dir: str, output_dir: str = None, quality: int = 85):
    """
    Batch convert all images in a directory to WebP format.
    
    Args:
        input_dir: Directory containing input images
        output_dir: Directory for output WebP files (optional, defaults to input_dir)
        quality: WebP quality (0-100, default 85)
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir) if output_dir else input_dir
    
    supported_formats = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff', '.tif'}
    image_files = [f for f in input_dir.rglob('*') if f.suffix.lower() in supported_formats]
    
    if not image_files:
        print(f"No supported images found in {input_dir}")
        return
    
    print(f"Found {len(image_files)} images to convert")
    
    for img_file in image_files:
        relative_path = img_file.relative_to(input_dir)
        output_path = output_dir / relative_path.with_suffix('.webp')
        
        try:
            result = convert_to_webp(str(img_file), str(output_path), quality)
            print(f"✓ Converted: {relative_path} -> {output_path.name}")
        except Exception as e:
            print(f"✗ Failed: {relative_path} - {str(e)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  Single file:  python convert_to_webp.py <input_file> [output_file] [quality]")
        print("  Batch mode:   python convert_to_webp.py --batch <input_dir> [output_dir] [quality]")
        print("\nExamples:")
        print("  python convert_to_webp.py image.png")
        print("  python convert_to_webp.py image.png output.webp 90")
        print("  python convert_to_webp.py --batch ./images ./webp-images 85")
        sys.exit(1)
    
    if sys.argv[1] == "--batch":
        if len(sys.argv) < 3:
            print("Error: --batch requires input directory")
            sys.exit(1)
        
        input_dir = sys.argv[2]
        output_dir = sys.argv[3] if len(sys.argv) > 3 and not sys.argv[3].isdigit() else None
        quality = int(sys.argv[4]) if len(sys.argv) > 4 else (int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3].isdigit() else 85)
        
        batch_convert(input_dir, output_dir, quality)
    else:
        input_file = sys.argv[1]
        output_file = None
        quality = 85
        
        if len(sys.argv) > 2:
            if sys.argv[2].isdigit():
                quality = int(sys.argv[2])
            else:
                output_file = sys.argv[2]
                if len(sys.argv) > 3:
                    quality = int(sys.argv[3])
        
        try:
            result = convert_to_webp(input_file, output_file, quality)
            print(f"✓ Converted successfully: {result}")
        except Exception as e:
            print(f"✗ Error: {str(e)}")
            sys.exit(1)
