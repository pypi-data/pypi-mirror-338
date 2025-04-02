"""
Talos Loader - 一个用于创建和管理加载器项目的工具
"""

__version__ = "0.1.0"

# 直接从src模块导入需要暴露的类
from talos_loader.src import TalosLoader, Block, ContentType

# 明确指定要导出的类
__all__ = ["TalosLoader", "Block", "ContentType"]
