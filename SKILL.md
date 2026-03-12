---
name: image-to-webp
description: 将图片（PNG、JPG、GIF、BMP、TIFF）转换为 WebP 格式。当用户请求将图片转换为 WebP、优化网页图片或批量转换图片格式时使用此技能。支持单文件转换和批量目录转换，可配置质量设置。
---

# 图片转 WebP 转换器

## 概述

此技能可将图片转换为 WebP 格式，这是一种现代图片格式，为网页图片提供卓越的压缩效果。支持单文件转换和整个目录的批量处理。

## 何时使用此技能

当用户请求以下内容时使用此技能：
- 将特定图片转换为 WebP 格式
- 批量转换目录中的多个图片
- 优化网页图片
- 在保持质量的同时减小图片文件大小
- 提到 "webp"、"图片转换" 或 "优化图片"

## 支持的格式

支持的输入格式：
- PNG
- JPG/JPEG
- GIF
- BMP
- TIFF/TIF

输出格式：WebP（有损或无损）

## 使用说明

### 单文件转换

将单个图片文件转换为 WebP：

```bash
python scripts/convert_to_webp.py <input_file> [output_file] [quality]
```

**参数：**
- `input_file`（必需）：输入图片的路径
- `output_file`（可选）：输出 WebP 文件的路径。如果未指定，则使用输入文件名加 `.webp` 扩展名
- `quality`（可选）：质量级别 0-100（默认值：85）。值越高 = 质量越好但文件越大

**示例：**
```bash
# 使用默认设置转换（质量 85）
python scripts/convert_to_webp.py image.png

# 使用自定义输出路径转换
python scripts/convert_to_webp.py image.jpg output/image.webp

# 使用自定义质量转换
python scripts/convert_to_webp.py photo.png photo.webp 90

# 仅指定质量转换
python scripts/convert_to_webp.py image.png 95
```

### 批量目录转换

转换目录中的所有图片：

```bash
python scripts/convert_to_webp.py --batch <input_dir> [output_dir] [quality]
```

**参数：**
- `input_dir`（必需）：包含要转换图片的目录
- `output_dir`（可选）：输出 WebP 文件的目录。如果未指定，则使用输入目录
- `quality`（可选）：质量级别 0-100（默认值：85）

**示例：**
```bash
# 转换目录中的所有图片（就地转换）
python scripts/convert_to_webp.py --batch ./images

# 转换到不同的输出目录
python scripts/convert_to_webp.py --batch ./images ./webp-output

# 使用自定义质量批量转换
python scripts/convert_to_webp.py --batch ./images ./webp-output 90

# 使用质量参数就地批量转换
python scripts/convert_to_webp.py --batch ./images 95
```

## 质量指南

推荐的质量设置：
- **95-100**：接近无损，适用于对质量要求严格的图片
- **85-94**：高质量，良好的平衡（推荐默认值：85）
- **75-84**：良好质量，更好的压缩
- **60-74**：中等质量，显著压缩
- **低于 60**：低质量，最大压缩

## 工作流程

1. **识别请求**：确定用户是要单文件转换还是批量转换
2. **检查依赖**：确保已安装 PIL/Pillow（`pip install Pillow`）
3. **执行转换**：使用正确的参数运行相应的命令
4. **报告结果**：通知用户转换成功并告知输出位置

## 错误处理

常见错误及解决方案：
- **PIL 未安装**：运行 `pip install Pillow`
- **文件未找到**：验证输入路径是否正确
- **权限被拒绝**：检查输出目录的写入权限
- **不支持的格式**：确保输入文件是支持的格式之一

## 资源

### scripts/convert_to_webp.py

使用 PIL/Pillow 库处理图片转换的 Python 脚本。支持单文件和批量目录转换，可配置质量设置。该脚本自动处理透明度、颜色模式转换和目录创建。
