import json
import os
from datetime import datetime
from jinja2 import Environment, FileSystemLoader

def load_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_html_files(config):
    # 设置Jinja2环境
    env = Environment(loader=FileSystemLoader('.'))
    
    # 更新index.html
    template = env.get_template('index.html')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(template.render(config=config))
    
    # 更新en.html
    template = env.get_template('en.html')
    with open('en.html', 'w', encoding='utf-8') as f:
        f.write(template.render(config=config))
    
    # 更新404.html
    template = env.get_template('404.html')
    with open('404.html', 'w', encoding='utf-8') as f:
        f.write(template.render(config=config))
    
    # 更新最后更新时间
    update_time = datetime.now().strftime('%Y年%m月%d日')
    for file in ['index.html', 'en.html', '404.html']:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('<span id="last-update"></span>', update_time)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

def main():
    print("开始更新网站内容...")
    config = load_config()
    update_html_files(config)
    print("网站内容更新完成！")

if __name__ == "__main__":
    main() 