# 图片转 WebP 转换器

将图片转换为 WebP 格式，支持质量控制。支持单文件和批量目录转换。

## 安装

```bash
npx skills add biu/image-to-webp
```

或者手动安装，将此目录复制到你的 `.codebuddy/skills/` 文件夹中。

## 功能特性

- 🖼️ 将 PNG、JPG、GIF、BMP、TIFF 转换为 WebP
- 📁 批量处理整个目录
- ⚙️ 可配置质量设置（0-100）
- 🚀 使用 PIL/Pillow，快速高效

## 使用方法

### 单文件转换

```bash
python scripts/convert_to_webp.py image.png
python scripts/convert_to_webp.py image.jpg output.webp 90
```

### 批量目录转换

```bash
python scripts/convert_to_webp.py --batch ./images
python scripts/convert_to_webp.py --batch ./images ./output 85
```

## 环境要求

- Python 3.7+
- Pillow (PIL)

安装依赖：
```bash
pip install Pillow
```

## 质量指南

- **95-100**：接近无损质量
- **85-94**：高质量（推荐默认值：85）
- **75-84**：良好质量，更好的压缩
- **60-74**：中等质量
- **低于 60**：低质量，最大压缩

## 参数说明

### 单文件模式
- `input_file`（必需）：输入图片的路径
- `output_file`（可选）：输出路径（默认为输入文件名加 .webp）
- `quality`（可选）：质量 0-100（默认值：85）

### 批量模式
- `--batch` 标志
- `input_dir`（必需）：包含图片的目录
- `output_dir`（可选）：输出目录（默认为输入目录）
- `quality`（可选）：质量 0-100（默认值：85）

## 示例

```bash
# 使用默认质量转换（85）
python scripts/convert_to_webp.py photo.jpg

# 自定义输出和质量
python scripts/convert_to_webp.py photo.jpg optimized.webp 95

# 批量转换文件夹中的所有图片
python scripts/convert_to_webp.py --batch ./photos ./webp-output

# 就地批量转换并指定质量
python scripts/convert_to_webp.py --batch ./photos 90
```

## 许可证

MIT

## 作者

biu
