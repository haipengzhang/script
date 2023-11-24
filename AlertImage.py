#!/usr/bin/env python3

import os
import re
import sys
import shutil

print(sys.executable)

assets_directory = '../LihuaEdu/Other/Assets.xcassets'
target_directory = 'edited_color_img'

# 递归遍历assets_directory目录
for foldername, subfolders, filenames in os.walk(assets_directory):
    for filename in filenames:
        if filename.endswith('.pdf'):
            assets_file = os.path.join(foldername, filename)
            for target_folder, _, target_files in os.walk(target_directory):
                if filename in target_files:
                    # 如果找到同名文件，则替换
                    target_file = os.path.join(target_folder, filename)
                    shutil.copy2(target_file, assets_file)

print('All matching PDF files in assets_directory have been replaced by those in target_directory.')