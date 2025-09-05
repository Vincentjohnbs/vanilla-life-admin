import os
import re

def hide_sidebar_in_html(file_path):
    """隐藏HTML文件中的左侧导航栏"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否已经添加了隐藏样式
        if 'sidebar-hidden' in content:
            print(f"跳过 {file_path} - 已经处理过")
            return False
        
        # 在head标签中添加CSS样式来隐藏侧边栏
        css_style = '''
    <style>
        /* 隐藏侧边栏 */
        #sidebar, .sidebar-hidden { display: none !important; }
        /* 调整主内容区域 */
        .lg\\:ml-64 { margin-left: 0 !important; }
        /* 隐藏侧边栏切换按钮 */
        #sidebarToggle, #sidebar-toggle { display: none !important; }
    </style>
</head>'''
        
        # 替换</head>标签
        content = re.sub(r'</head>', css_style, content)
        
        # 写回文件
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"已处理: {file_path}")
        return True
        
    except Exception as e:
        print(f"处理文件 {file_path} 时出错: {e}")
        return False

def main():
    """批量处理所有HTML文件"""
    directory = r"c:\Users\Administrator\Desktop\工作\program\github-pages-deploy"
    
    # 获取所有HTML文件
    html_files = []
    for file in os.listdir(directory):
        if file.endswith('.html') and file not in ['index.html', 'preview.html', '总览.html']:
            html_files.append(os.path.join(directory, file))
    
    print(f"找到 {len(html_files)} 个HTML文件需要处理")
    
    processed_count = 0
    for file_path in html_files:
        if hide_sidebar_in_html(file_path):
            processed_count += 1
    
    print(f"\n处理完成！共处理了 {processed_count} 个文件")
    print("所有单页HTML文件的左侧导航栏已隐藏")

if __name__ == "__main__":
    main()