#!/usr/bin/env python3
"""
RAPID Python SDK 基本用法示例

使用前请确保在以下位置放置了所需的所有dylib文件：
1. 执行脚本目录下的libraries子目录
2. 当前工作目录下的libraries子目录
3. 其他系统路径

推荐使用方式：
- 在脚本所在目录创建libraries子目录
- 将librapid_core.dylib和所有相关依赖库都放在该目录下
- SDK会自动加载该目录下的所有库文件
"""

import os
import sys
import time

# 添加父目录到模块搜索路径，以便导入rapid_kit模块
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

from rapid_kit import Core
from rapid_kit.core import Auth, PipeProxy, LiveStream
from rapid_kit.core.log import log_info, LogLevel

def main():

    version = Core.version_name()
    build_id = Core.build_id()
    commit_hash = Core.commit_hash()
    
    print(f"RAPID Core版本: {version}")
    print(f"构建ID: {build_id}")
    print(f"提交哈希: {commit_hash}")    
    
    # 初始化RAPID Core库
    success = Core.initialize(
        app_id="5920020",
        package_name="com.tange365.icam365"
    )
    
    if not success:
        print("RAPID Core初始化失败")
        return
    
    
    # 使用日志系统
    log_info("EXAMPLE", "RAPID Core初始化成功")
    
    # # 连接设备
    # device_id = "device_123"  # 替换为实际的设备ID
    # pipe = PipeProxy(device_id)
    
    # # 设置状态回调
    # def on_status_change(status):
    #     print(f"管道状态变更: {status}")
    
    # pipe.set_status_callback(on_status_change)
    
    # # 建立连接
    # pipe.establish()
    
    # # 等待连接建立
    # print("正在建立连接...")
    # for _ in range(10):
    #     time.sleep(0.5)
    #     status = pipe.get_status()
    #     if status == 2:  # 已连接（你可能需要检查实际的状态码）
    #         print("连接已建立!")
    #         break
    # else:
    #     print("连接建立失败")
    #     pipe.destroy()
    #     return
    
    # # 开始直播流
    # try:
    #     stream = LiveStream(pipe)
        
    #     # 开始流媒体传输
    #     stream.start()
    #     print("流媒体传输已开始")
        
    #     # 让它运行一段时间
    #     print("流媒体传输将持续10秒...")
    #     time.sleep(10)
        
    #     # 停止流媒体传输
    #     stream.stop()
    #     print("流媒体传输已停止")
        
    #     # 释放资源
    #     stream.release()
    # except Exception as e:
    #     print(f"流媒体传输过程中出错: {e}")
    
    # # 清理资源
    # pipe.abolish()
    # pipe.destroy()
    # print("资源已清理")

if __name__ == "__main__":
    main()