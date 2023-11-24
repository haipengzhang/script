#!/usr/bin/env python3

import os
import re
import sys
import shutil

print(sys.executable)

# 指定包含 R.generated 文件的路径和需要搜索的文件夹
r_generated_file = '../LihuaEdu/Other/R.generated.swift'
folder_to_search = '../LihuaEdu'
folder_to_exclude = ['../LihuaEdu/Other']
# Assets.xcassets 目录路径
assets_directory = '../LihuaEdu/Other/Assets.xcassets'

def find_unused_variables(directory, variables, excluded_dirs):
    # 存储没有用到的变量
    unused_variables = set(variables)

    # 遍历目录中的所有文件
    for root, dirs, files in os.walk(directory):
        # 排除特定的目录
        dirs[:] = [d for d in dirs if d not in excluded_dirs]

        for file in files:
            if file.endswith('.swift') or file.endswith('.xib') or file.endswith('.storyboard'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    content = f.read()
                    for variable in variables:
                        if file.endswith('.swift') and ('R.image.' + variable + '()' in content):
                            unused_variables.discard(variable)
                        elif (file.endswith('.xib') or file.endswith('.storyboard')) and (variable in content):
                            unused_variables.discard(variable)
    return unused_variables

# Entry
with open(r_generated_file, 'r') as file:
    content = file.read()
image_struct = re.search(r'struct image \{(.*?)\}', content, re.DOTALL)

if image_struct:
    variables = re.findall(r'static let (.*?) =', image_struct.group(1))
    for variable in variables:
        print(variable)
else:
    print("No 'struct image' found")

# 找出没有用到的变量
unused_variables = find_unused_variables(folder_to_search, variables, folder_to_exclude)

for variable in unused_variables:
    print(f'Variable {variable} in R.generated struct Image is not used')

# 递归地遍历 Assets.xcassets 目录，删除
for root, dirs, files in os.walk(assets_directory):
    for dir in dirs:
        if dir.endswith('.imageset'):
            variable = dir[:-len('.imageset')]
            
            if variable in unused_variables:
                folder_path = os.path.join(root, dir)
                shutil.rmtree(folder_path)
                print(f"Removed {folder_path}")