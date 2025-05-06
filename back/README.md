# 项目环境设置指南

本项目使用 Python 虚拟环境来管理依赖。以下是创建虚拟环境、进入虚拟环境、导出依赖和安装依赖的步骤。

## 创建虚拟环境

在项目目录下运行以下命令以创建虚拟环境：

```bash
python3 -m venv venv
```

## 激活虚拟环境

激活虚拟环境的命令因操作系统不同而有所区别：

- **Linux/macOS**:
    ```bash
    source venv/bin/activate
    ```
- **Windows**:
    ```bash
    .\venv\Scripts\activate
    ```

激活后，命令行前会显示 `(venv)`，表示虚拟环境已启用。

## 导出依赖

在虚拟环境中运行以下命令以导出当前安装的依赖到 `requirements.txt` 文件：

```bash
pip freeze > requirements.txt
```

## 安装依赖

确保虚拟环境已激活，然后运行以下命令以根据 `requirements.txt` 文件安装依赖：

```bash
pip install -r requirements.txt
```

## 退出虚拟环境

完成工作后，可以通过以下命令退出虚拟环境：

```bash
deactivate
```

## 注意事项

- 请确保使用与项目兼容的 Python 版本。
- 定期更新 `requirements.txt` 文件以保持依赖一致性。
- 如果遇到问题，请检查虚拟环境是否正确激活。
