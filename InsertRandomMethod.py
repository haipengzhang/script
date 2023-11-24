#!/usr/bin/env python3

import os
import random
import string
import re

# 生成随机英文单词
def random_word(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))

# 生成随机变量名，以 'le' 开头，然后是一个随机英文单词，使用驼峰式命名
def random_variable_name():
    return 'le' + ''.join(word.capitalize() for word in random_word(5))

# 指定的目录
code_directory = '../LihuaEdu'

for root, dirs, files in os.walk(code_directory):
    for file in files:
        if file.endswith(".swift"):
            filepath = os.path.join(root, file)
            with open(filepath, 'r+') as f:
                content = f.read()
                # 使用正则表达式匹配 "class xxxNAME: ViewController {"
                match = re.search(r'class (\w+): ViewController {', content)
                if match:
                    # 打印找到的文件
                    print('Found in:', filepath)
                    class_name = match.group(1)
                    # 生成随机的方法名
                    method_names = [random_variable_name() for _ in range(6)]
                    # 指定的代码
                    code = f"""
// MARK: - 添加混淆方法
extension {class_name} {{
    func {method_names[0]}() {{
        let index = arc4random() % 5
        switch index {{
        case 0:
            {method_names[1]}()
        case 1:
            {method_names[2]}()
        case 2:
            {method_names[3]}()
        case 3:
            {method_names[4]}()
        case 4:
            {method_names[5]}()
        default:
            break
        }}
    }}
    func {method_names[1]}() {{
        let index = arc4random() % 40
        let cutomImageV = UIImageView()
        let cutomRed = CGFloat(arc4random() % 256) / 255.0
        let cutomGreen = CGFloat(arc4random() % 256) / 255.0
        let cutomBlue = CGFloat(arc4random() % 256) / 255.0
        cutomImageV.backgroundColor = UIColor(red: cutomRed / 3, green: cutomGreen, blue: cutomBlue, alpha: 1.0)
        cutomImageV.image = UIImage(named: "icon_base_image\(inde)")
    }}

    func {method_names[2]}() {{
        let index = arc4random() % 40
        let cutomImageView = UIImageView()
        let cutomRed = CGFloat(arc4random() % 256) / 255.0
        let cutomGreen = CGFloat(arc4random() % 256) / 255.0
        let cutomBlue = CGFloat(arc4random() % 256) / 255.0
        cutomImageView.backgroundColor = UIColor(red: cutomRed / 3, green: cutomGreen, blue: cutomBlue, alpha: 1.0)
        cutomImageView.image = UIImage(named: "icon_base_image\(inde)")
    }}

    func {method_names[3]}() {{
        let index = arc4random() % 40
        let cutomImageView1 = UIImageView()
        let cutomRed = CGFloat(arc4random() % 256) / 255.0
        let cutomGreen = CGFloat(arc4random() % 256) / 255.0
        let cutomBlue = CGFloat(arc4random() % 256) / 255.0
        cutomImageView1.backgroundColor = UIColor(red: cutomRed / 3, green: cutomGreen, blue: cutomBlue, alpha: 1.0)
        cutomImageView1.image = UIImage(named: "icon_base_image\(inde)")
    }}

    func {method_names[4]}() {{
        let index = arc4random() % 40
        let cutomImageView2 = UIImageView()
        let cutomRed = CGFloat(arc4random() % 256) / 255.0
        let cutomGreen = CGFloat(arc4random() % 256) / 255.0
        let cutomBlue = CGFloat(arc4random() % 256) / 255.0
        cutomImageView2.backgroundColor = UIColor(red: cutomRed / 3, green: cutomGreen, blue: cutomBlue, alpha: 1.0)
        cutomImageView2.image = UIImage(named: "icon_base_image\(inde)")
    }}

    func {method_names[5]}() {{
        let index = arc4random() % 40
        let cutomImageView3 = UIImageView()
        let cutomRed = CGFloat(arc4random() % 256) / 255.0
        let cutomGreen = CGFloat(arc4random() % 256) / 255.0
        let cutomBlue = CGFloat(arc4random() % 256) / 255.0
        cutomImageView3.backgroundColor = UIColor(red: cutomRed / 3, green: cutomGreen, blue: cutomBlue, alpha: 1.0)
        cutomImageView3.image = UIImage(named: "icon_base_image\(inde)")
    }}
}}
"""
                    # 在文件末尾添加代码
                    content += code
                    f.seek(0)
                    f.write(content)
                    f.truncate()