#!/bin/bash

# 1. 设置 Python 路径（默认使用系统 Python3，可修改）
PYTHON_PATH=$(which python3.11)

# 2. 检查并创建虚拟环境
VENV_NAME=".venv"
if [ ! -d "$VENV_NAME" ]; then
    echo "创建虚拟环境..."
    $PYTHON_PATH -m venv $VENV_NAME
else
    echo "虚拟环境已存在."
fi

# 3. 激活虚拟环境
source "$VENV_NAME/bin/activate"

# 4. 安装依赖（如果存在 requirements.txt）
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
    echo "已安装依赖项."
else
    echo "未找到requirements.txt,跳过依赖项安装."
fi

# # 5. 导出依赖（可选）
# echo "To export dependencies, run: pip freeze > requirements.txt"

# # 保持虚拟环境激活状态
# echo "Virtual environment activated. Run 'deactivate' to exit."
