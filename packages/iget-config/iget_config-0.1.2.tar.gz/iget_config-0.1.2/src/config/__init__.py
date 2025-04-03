"""
iget-config Package

Provides configuration management classes.
"""

from .config import Config, Mode, TrainConfig, DataConfig, OptimizerConfig

# 如果 CnnConfig 也需要作为公共 API 的一部分被导入，取消下面的注释
# from .cnn_config import CnnConfig

__all__ = [
    "Config",
    "Mode",
    "TrainConfig",
    "DataConfig",
    "OptimizerConfig",
    # 'CnnConfig', # 如果取消上面注释，也取消这里的注释
]

__version__ = "0.1.2"  # 与 pyproject.toml 同步版本号
