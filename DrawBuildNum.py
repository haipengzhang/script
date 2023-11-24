#!/usr/bin/env python3
import sys
from PIL import Image, ImageDraw, ImageFont

print(sys.executable)
# 检查是否提供了足够的命令行参数
if len(sys.argv) < 3:
    print("Usage: python your_script.py VERSION and BUILD_NUMBER")
    sys.exit(1)

# 获取 build 号
version_number = sys.argv[1]
build_number = sys.argv[2]

print(f"The version number is {version_number}")
print(f"The build number is {build_number}")

# icon_file
icon_file = '../Lihua/Other/Assets.xcassets/AppIcon.appiconset/Icon-60@3x.png'
plist_file = '../Lihua/Other/Info.plist'

def draw_build_number_on_icon(icon_path, version_number, build_number, output_path):
    image = Image.open(icon_path).convert("RGBA")
    width, height = image.size
    font_size = 25

    overlay = Image.new('RGBA', image.size, (255, 255, 255, 0)) # 全透明的背景
    draw = ImageDraw.Draw(overlay)
    font = ImageFont.truetype("/System/Library/Fonts/SFNSMono.ttf", font_size)
    draw.rectangle([(0, height*2 // 3), (width, height)], fill=(255, 255, 255, 200))

    text_bbox_0 = draw.textbbox((0, 0), str(version_number), font=font)
    text_width_0 = text_bbox_0[2] - text_bbox_0[0]
    text_height_0 = text_bbox_0[3] - text_bbox_0[1]
    x = (width - text_width_0) / 2
    y = height*2 // 3
    draw.text((x, y), str(version_number), fill="black", font=font)
    
    text_bbox = draw.textbbox((0, 0), str(build_number), font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = height - (height // 2 - text_height) / 2 + 5
    draw.text((x, y), str(build_number), fill="black", font=font)

    image = Image.alpha_composite(image, overlay)
    image.save(output_path)

draw_build_number_on_icon(icon_file, version_number, build_number, icon_file)