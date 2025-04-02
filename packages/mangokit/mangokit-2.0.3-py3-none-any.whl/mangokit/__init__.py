# -*- coding: utf-8 -*-
# @Project: 芒果测试平台
# @Description: 
# @Time   : 2024-09-07 22:15
# @Author : 毛鹏

import sys

python_version = sys.version_info
if f"{python_version.major}.{python_version.minor}" != "3.10":
    raise Exception("必须使用>Python3.10.4")

from mangokit.apidrive import *
from mangokit.tools.log_collector import set_log
from mangokit.tools.data_processor import *
from mangokit.tools.database import *
from mangokit.models.models import *
from mangokit.tools.decorator import *
from mangokit.tools.notice import *
from mangokit.enums.enums import *
from mangokit.exceptions import MangoKitError

# 获取打包后的资源路径
import os
import sys
from pathlib import Path


def _load_pyarmor():
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    runtime_base = Path(base_path) / 'mangos'

    runtime_dir = runtime_base / ('pyarmor_runtime_windows' if sys.platform == 'win32' else 'pyarmor_runtime_linux')

    if not runtime_dir.exists():
        raise RuntimeError(f"PyArmor运行时目录不存在: {runtime_dir}")

    sys.path.insert(0, str(runtime_dir))
    sys.path.insert(0, str(runtime_dir / 'pyarmor_runtime_000000'))


_load_pyarmor()

try:
    from mango import Mango

    mango = Mango()
    mango.v(1)
except ImportError as e:
    raise RuntimeError(f"导入mango模块失败: {str(e)}")

__all__ = [
    'DataProcessor',
    'DataClean',
    'ObtainRandomData',
    'CacheTool',
    'CodingTool',
    'EncryptionTool',
    'JsonTool',
    'RandomCharacterInfoData',
    'RandomNumberData',
    'RandomStringData',
    'RandomTimeData',

    'MysqlConingModel',
    'ResponseModel',
    'EmailNoticeModel',
    'TestReportModel',
    'WeChatNoticeModel',
    'FunctionModel',
    'ClassMethodModel',

    'CacheValueTypeEnum',
    'NoticeEnum',

    'MysqlConnect',
    'SQLiteConnect',
    'requests',
    'async_requests',
    'set_log',
    'WeChatSend',
    'EmailSend',

    'singleton',
    'convert_args',

    'Mango',

    'MangoKitError',
]
