

# viConfig

一个可以进行数据验证的服务器配置信息库
 
## 目录

- [安装](#安装)
- [使用](#使用)
  - [定义配置信息](#定义配置信息)
  - [配置信息获取](#配置信息获取)
- [依赖库](#依赖库)
- [版权说明](#版权说明)

## 安装

```powershell
pip install viconfig
```

## 使用

### 定义配置信息

```python
import pathlib
from Config import Config, Field, f_string, f_int, f_folder


def init_config():
    config = Config()
    config.add_fields([
        Field('app', 'name', f_string, 'DATA-API'),
        Field('app', 'version', f_string, '1.0.0'),
        Field('app', 'description', f_string, '数据表信息管理系统（服务器）'),
        Field('app', 'port', f_int, 8005),
    ])

    config_obj = pathlib.Path('config.json')
    if config_obj.exists():
        config.load_from_json('config.json')
    else:
        config.save_to_json("config.json")

    return config
```

### 配置信息获取

```python
config.get('app', 'description')
```

## 依赖库

- `json`
- `pathlib`
- `decimal`

## 版权说明

该项目签署了MIT 授权许可。详细请查看LICENSE
