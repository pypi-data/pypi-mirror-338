import ctypes
import os
import platform
import sys
from pathlib import Path

MODULE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(MODULE_DIR)

def _get_libraries_dir():
    """查找包含库文件的目录"""
    system = platform.system().lower()
    
    # 首先检查脚本执行目录下的libraries
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    cwd = os.getcwd()
    
    # 按优先级顺序定义搜索位置
    search_dirs = [
        os.path.join(cwd, "libraries"),             # 当前工作目录
        os.path.join(script_dir, "libraries"),      # 脚本所在目录
        os.path.join(PROJECT_ROOT, "libraries")     # 包所在目录
    ]
    
    # 在各目录查找库文件
    for dir_path in search_dirs:
        # 检查核心库是否存在
        if system == 'darwin':
            core_lib = os.path.join(dir_path, 'libRapidCore.dylib')
        elif system == 'windows':
            core_lib = os.path.join(dir_path, 'RapidCore.dll')
        elif system == 'linux':
            core_lib = os.path.join(dir_path, 'libRapidCore.so')
        else:
            raise RuntimeError(f"Unsupported system: {system}")
            
        if os.path.exists(core_lib):
            return dir_path
    
    # 如果没找到，给出详细的错误提示
    dirs_exist = [d for d in search_dirs if os.path.exists(d)]
    if not dirs_exist:
        # 没有找到任何libraries目录
        raise RuntimeError(
            f"Could not find libraries directory in any of:\n"
            f"  - {search_dirs[0]} (current directory)\n"
            f"  - {search_dirs[1]} (script directory)\n"
            f"  - {search_dirs[2]} (package directory)\n"
            f"Please create a 'libraries' directory in one of these locations "
            f"and copy the required libraries there."
        )
    else:
        # 目录存在但没有找到库文件
        dirs_str = "\n  - ".join([d for d in dirs_exist])
        if system == 'darwin':
            lib_name = 'libRapidCore.dylib'
        elif system == 'windows':
            lib_name = 'RapidCore.dll'
        elif system == 'linux':
            lib_name = 'libRapidCore.so'
        else:
            lib_name = 'unknown'
            
        raise RuntimeError(
            f"Could not find {lib_name} in existing libraries directories:\n"
            f"  - {dirs_str}\n"
            f"Please copy the required library files into one of these directories."
        )

try:
    # 找到库文件目录
    libraries_dir = _get_libraries_dir()
    
    # 根据平台确定文件名
    system = platform.system().lower()
    if system == 'darwin':
        core_lib = 'libRapidCore.dylib'
        sdl_lib = 'libRapidSDL.dylib'
        media_lib = 'libRapidMedia.dylib'
    elif system == 'windows':
        core_lib = 'RapidCore.dll'
        sdl_lib = 'RapidSDL.dll'
        media_lib = 'RapidMedia.dll'
    elif system == 'linux':
        core_lib = 'libRapidCore.so'
        sdl_lib = 'libRapidSDL.so'
        media_lib = 'libRapidMedia.so'
    else:
        raise RuntimeError(f"Unsupported system: {system}")
    
    # 准备库文件路径
    core_path = os.path.join(libraries_dir, core_lib)
    sdl_path = os.path.join(libraries_dir, sdl_lib)
    media_path = os.path.join(libraries_dir, media_lib)
    
    print(f"Loading libraries from directory: {libraries_dir}")
    
    # 1. 首先加载核心库 - 基础库
    if not os.path.exists(core_path):
        raise RuntimeError(f"Core library not found: {core_path}")
    print(f"Loading core library: {core_lib}")
    # 使用RTLD_GLOBAL标志使符号对后续库可见
    _core_lib = ctypes.CDLL(core_path, mode=ctypes.RTLD_GLOBAL)
    
    # 2. 其次加载SDL库 - 依赖于Core
    if not os.path.exists(sdl_path):
        print(f"Warning: SDL library not found: {sdl_path}")
        _sdl_lib = None
    else:
        print(f"Loading SDL library: {sdl_lib}")
        try:
            _sdl_lib = ctypes.CDLL(sdl_path, mode=ctypes.RTLD_GLOBAL)
        except Exception as e:
            print(f"Warning: Failed to load SDL library: {e}")
            _sdl_lib = None
    
    # 3. 最后加载媒体库 - 依赖于Core和SDL
    if not os.path.exists(media_path):
        print(f"Warning: Media library not found: {media_path}")
        _media_lib = None
    else:
        print(f"Loading media library: {media_lib}")
        try:
            _media_lib = ctypes.CDLL(media_path, mode=ctypes.RTLD_GLOBAL)
        except Exception as e:
            print(f"Warning: Failed to load Media library: {e}")
            _media_lib = None

except Exception as e:
    raise RuntimeError(f"Failed to load RAPID libraries: {e}")

def get_lib():
    """获取核心库"""
    return _core_lib

def get_media_lib():
    """获取媒体库"""
    if _media_lib is None:
        raise RuntimeError("Media library is not loaded")
    return _media_lib

def get_sdl_lib():
    """获取SDL库"""
    if _sdl_lib is None:
        raise RuntimeError("SDL library is not loaded")
    return _sdl_lib

def get_all_loaded_libs():
    """获取所有加载的库"""
    libs = {os.path.basename(core_path): _core_lib}
    
    if _media_lib is not None:
        libs[os.path.basename(media_path)] = _media_lib
        
    if _sdl_lib is not None:
        libs[os.path.basename(sdl_path)] = _sdl_lib
        
    return libs