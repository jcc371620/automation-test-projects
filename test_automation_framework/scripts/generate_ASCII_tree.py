# run: python generate_ASCII_tree.py
import os
import time

# --------------------------
# 获取文件信息（大小 + 修改时间）
# --------------------------
def get_file_info(path):
    if os.path.isdir(path):
        return "目录"
    size = os.path.getsize(path)
    mtime = time.strftime("%Y-%m-%d %H:%M", time.localtime(os.path.getmtime(path)))
    return f"{size} bytes | {mtime}"

# --------------------------
# 递归生成树状结构 + 注释
# --------------------------
def generate_tree(path, prefix="", rel_path=""):
    entries = sorted(os.listdir(path))
    entries_count = len(entries)
    lines = []

    for index, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        current_rel = os.path.join(rel_path, entry) if rel_path else entry

        connector = "└─" if index == entries_count - 1 else "├─"
        line = f"{prefix}{connector} {entry}"

        # 获取自定义注释
        custom_comment = comments.get(current_rel, "")

        # 获取自动文件信息
        file_info = get_file_info(full_path)

        # 合并自定义注释 + 文件信息
        if custom_comment:
            comment = f"{custom_comment} | {file_info}"
        else:
            comment = file_info

        lines.append((line, comment))

        # 如果是文件夹，递归
        if os.path.isdir(full_path):
            extension = "    " if index == entries_count - 1 else "│   "
            lines.extend(generate_tree(full_path, prefix + extension, current_rel))

    return lines

# --------------------------
# 对齐树状结构 + 注释
# --------------------------
def format_tree_markdown(tree_lines):
    max_len = max(len(line) for line, _ in tree_lines)
    formatted = [f"{line.ljust(max_len)}  # {comment}" for line, comment in tree_lines]
    return "```markdown\n" + "\n".join(formatted) + "\n```"

# --------------------------
# 自动插入到 README.md
# --------------------------
def insert_tree_into_readme(readme_path, tree_markdown, marker_start="<!-- TREE_START -->", marker_end="<!-- TREE_END -->"):
    """
    自动在 README.md 中插入树状结构
    - 如果存在标记 <!-- TREE_START --> 和 <!-- TREE_END -->，替换中间内容
    - 如果不存在标记，追加到文件末尾
    """
    if not os.path.exists(readme_path):
        print(f"{readme_path} 不存在，将创建新文件")
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(tree_markdown)
        return

    with open(readme_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    output_lines = []
    inside_marker = False
    marker_found = False

    for line in lines:
        if marker_start in line:
            marker_found = True
            inside_marker = True
            output_lines.append(line.rstrip("\n"))
            output_lines.append(tree_markdown)
            continue
        if marker_end in line:
            inside_marker = False
            output_lines.append(line.rstrip("\n"))
            continue
        if not inside_marker:
            output_lines.append(line.rstrip("\n"))

    # 如果没有标记，追加到末尾
    if not marker_found:
        output_lines.append(marker_start)
        output_lines.append(tree_markdown)
        output_lines.append(marker_end)

    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("\n".join(output_lines))
    print(f"树状结构已插入 {readme_path}")

# --------------------------
# 主程序
# --------------------------
if __name__ == "__main__":
    project_path = input("请输入项目路径：").strip()
    if not os.path.exists(project_path):
        print("路径不存在！")
        exit()

    readme_path = os.path.join(project_path, "README.md")

    # --------------------------
    # 自定义注释字典
    # --------------------------
    comments = {
        "README.md": "项目总说明",
        "api": "API 接口模块",
        "api/README.md": "API 模块说明",
        "api/login_api.py": "登录接口",
        "api/user_api.py": "用户接口",
        "api/test.py": "API 测试脚本",
        "config": "配置文件目录",
        "config/README.md": "配置模块说明",
        "config/config.yaml": "主配置文件",
        "config/env.yaml": "环境配置文件",
        "config/test.py": "配置测试脚本",
        "data": "测试数据目录",
        "data/README.md": "数据模块说明",
        "data/login.json": "登录测试数据",
        "data/users.json": "用户数据",
        "data/test.py": "数据测试脚本",
        "generate_ASCII_tree.py": "生成树状结构脚本并插入到README.md",
        "pages": "页面对象模块",
        "pages/README.md": "页面模块说明",
        "pages/login_page.py": "登录页面对象",
        "pages/dashboard_page.py": "仪表盘页面对象",
        "pages/test.py": "页面模块测试脚本",
        "pytest.ini": "Pytest 配置文件",
        "reports": "测试报告目录",
        "reports/README.md": "报告说明",
        "reports/test.py": "报告测试脚本",
        "requirements.txt": "依赖列表",
        "tests": "测试用例目录",
        "tests/README.md": "测试用例说明",
        "tests/api_validation": "API 验证用例",
        "tests/api_validation/README.md": "API 验证说明",
        "tests/api_validation/test.py": "API 验证脚本",
        "tests/database_validation": "数据库验证用例",
        "tests/database_validation/README.md": "数据库验证说明",
        "tests/database_validation/test.py": "数据库验证脚本",
        "tests/ui_validation": "UI 验证用例",
        "tests/ui_validation/README.md": "UI 验证说明",
        "tests/ui_validation/test.py": "UI 验证脚本",
        "utils": "工具函数目录",
        "utils/README.md": "工具模块说明",
        "utils/config_util.py": "配置工具",
        "utils/db_util.py": "数据库工具",
        "utils/logger.py": "日志工具",
        "utils/request_util.py": "请求工具",
        "utils/test.py": "工具测试脚本",
    }

    # --------------------------
    # 生成树状结构
    # --------------------------
    tree_lines = generate_tree(project_path)
    tree_markdown = format_tree_markdown(tree_lines)

    # --------------------------
    # 自动插入到 README.md
    # --------------------------
    insert_tree_into_readme(readme_path, tree_markdown)