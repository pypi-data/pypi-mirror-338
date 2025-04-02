# Talos Loader

一个用于创建和管理加载器项目的工具。

## 安装

由于依赖关系，需要使用以下命令安装：

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ talos_loader
```


## 使用方法

### 初始化新项目

```bash
talos_loader init
```

这将启动交互式向导，引导您创建一个新的加载器项目。您需要提供：
- 项目路径（默认为 ~/Downloads）
- 项目名称

执行后，将创建以下目录结构：

```
my_loader_demo/
├── README.md                # 项目说明文档
├── my_loader_demo/          # 主项目目录
│   └── loaders/             # 加载器模块
│       └── my_custom_loaders.py  # 自定义加载器实现
├── pyproject.toml           # 项目配置文件
```

## 开发

### 依赖

- Python 3.10+
- click
- inquirer
- jinja2
- talos-aclient (从TestPyPI安装)
- langchain
- langchain-openai
- pydantic

### 开发设置

```bash
# 克隆仓库
git clone https://github.com/yourusername/talos_loader.git
cd talos_loader

# 安装依赖
pip install -e .

# 运行测试
pytest
```

## 打包和发布

### 使用setuptools和twine打包

1. 构建分发包：

```bash
pip install --upgrade build
python -m build
```

2. 上传到TestPyPI：

```bash
pip install --upgrade twine
twine upload --repository testpypi dist/*
```

3. 上传到PyPI：

```bash
twine upload dist/*
```

### 认证配置

在您的主目录下创建`.pypirc`文件：

```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = your_username
password = your_password

[testpypi]
repository = https://test.pypi.org/legacy/
username = your_username
password = your_password
```

更安全的方法是使用API令牌：

```ini
[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = your_api_token
```

## 许可证

MIT
