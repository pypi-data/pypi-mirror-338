#!/usr/bin/env python3
"""
RAPID Kit Library Diagnostic Tool

This tool helps diagnose issues with loading the RAPID dynamic libraries.
"""

import os
import sys
import platform
import shutil
import subprocess

# Add parent directory to module search path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parent_dir)

def get_lib_extension():
    """Get the appropriate library extension for the current platform"""
    system = platform.system().lower()
    if system == "darwin":
        return ".dylib"
    elif system == "windows":
        return ".dll"
    elif system == "linux":
        return ".so"
    else:
        return None

def check_libraries_dir():
    """Check for libraries directory and its contents"""
    # 按优先级顺序定义搜索位置
    script_dir = os.path.dirname(os.path.abspath(__file__))
    cwd = os.getcwd()
    
    search_dirs = [
        os.path.join(cwd, "libraries"),             # 当前工作目录
        os.path.join(script_dir, "libraries"),      # 脚本所在目录
        os.path.join(parent_dir, "libraries")       # 包所在目录
    ]
    
    print(f"\n🔍 Checking for libraries directory...")
    
    # 查找第一个存在的libraries目录
    found_dir = None
    for dir_path in search_dirs:
        print(f"Checking: {dir_path}")
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            found_dir = dir_path
            print(f"  ✅ Found libraries directory: {found_dir}")
            break
        else:
            print(f"  ❌ Not found at: {dir_path}")
    
    # 如果没找到，提示创建目录
    if not found_dir:
        print("\n  📝 No libraries directory found. You need to create one.")
        
        # 默认在当前工作目录创建
        target_dir = search_dirs[0]
        
        # 询问用户是否创建
        if input(f"  Would you like to create a libraries directory at {target_dir}? (y/n): ").lower() == 'y':
            try:
                os.makedirs(target_dir, exist_ok=True)
                print(f"  ✅ Created libraries directory at: {target_dir}")
                found_dir = target_dir
                print(f"  🔍 Now you need to place your library files in this directory")
                
                # 列出需要的库文件
                system = platform.system().lower()
                if system == "darwin":
                    print(f"  Required files:")
                    print(f"    - libRapidCore.dylib")
                    print(f"    - libRapidMedia.dylib")
                    print(f"    - libRapidSDL.dylib")
                elif system == "windows":
                    print(f"  Required files:")
                    print(f"    - RapidCore.dll")
                    print(f"    - RapidMedia.dll")
                    print(f"    - RapidSDL.dll")
                elif system == "linux":
                    print(f"  Required files:")
                    print(f"    - libRapidCore.so")
                    print(f"    - libRapidMedia.so")
                    print(f"    - libRapidSDL.so")
            except Exception as e:
                print(f"  ❌ Failed to create directory: {e}")
                return False
        else:
            return False

    # 至此已经找到或创建了libraries目录
    extension = get_lib_extension()
    if not extension:
        print(f"  ⚠️ Unsupported platform: {platform.system()}")
        return False
        
    # 检查核心库文件
    system = platform.system().lower()
    if system == "darwin":
        core_lib = "libRapidCore.dylib"
    elif system == "windows":
        core_lib = "RapidCore.dll"
    elif system == "linux":
        core_lib = "libRapidCore.so"
    else:
        core_lib = None
    
    if core_lib and os.path.exists(os.path.join(found_dir, core_lib)):
        print(f"  ✅ Found core library: {core_lib}")
        
        # 列出其他库文件
        lib_files = [f for f in os.listdir(found_dir) if f.endswith(extension)]
        if len(lib_files) > 1:
            print(f"  ✅ Found {len(lib_files)} library files:")
            for lib in lib_files:
                if lib != core_lib:
                    print(f"     - {lib}")
        
        return True, found_dir
    else:
        print(f"  ❌ Core library {core_lib} not found in {found_dir}")
        print(f"  📝 Please place {core_lib} in the libraries directory")
        
        # 检查是否有其他库文件
        lib_files = [f for f in os.listdir(found_dir) if f.endswith(extension)]
        if lib_files:
            print(f"  ⚠️ Found {len(lib_files)} library files, but not the core library:")
            for lib in lib_files:
                print(f"     - {lib}")
        else:
            print("  ❌ No library files found")
        
        # 提供寻找库文件的提示
        if system == "darwin":
            print("\n  💡 Tips for finding library files:")
            print("    - Check if they're in a RapidKit-xxxx.zip file")
            print("    - Look in /usr/local/lib or ~/Downloads for the libraries")
            print("    - If you have the libraries elsewhere, copy them to:")
            print(f"      {found_dir}")
            
        return False, found_dir

def run_command(cmd):
    """运行系统命令并返回输出"""
    try:
        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error executing command: {e}"

def check_library_symbols(lib_path, search_prefix="RAPID_Media"):
    """使用nm命令检查库文件中的符号"""
    print(f"\n🔍 Checking symbols in {os.path.basename(lib_path)}...")
    
    if not os.path.exists(lib_path):
        print(f"  ❌ Library file not found: {lib_path}")
        return
    
    # 检查文件是否为动态库
    file_command = f"file '{lib_path}'"
    file_output = run_command(file_command)
    print(f"  File info: {file_output}")
    
    # 使用nm命令列出符号
    symbols_cmd = f"nm -g '{lib_path}' | grep '{search_prefix}'"
    symbols = run_command(symbols_cmd)
    
    if symbols:
        print(f"  ✅ Found symbols matching '{search_prefix}':")
        for line in symbols.splitlines()[:20]:  # 限制显示行数
            print(f"     {line}")
        
        # 特别检查MediaChat_Create
        if "RAPID_MediaChat_Create" in symbols:
            print("  ✅ Symbol RAPID_MediaChat_Create found in library!")
        else:
            print("  ❌ Symbol RAPID_MediaChat_Create NOT found in library!")
            
        # 尝试匹配类似的符号
        chat_symbols = [s for s in symbols.splitlines() if "Chat" in s]
        if chat_symbols:
            print("  💡 Found Chat-related symbols that might be relevant:")
            for s in chat_symbols:
                print(f"     {s}")
    else:
        print(f"  ❌ No symbols found matching '{search_prefix}'")
        
        # 尝试列出所有导出符号
        all_symbols_cmd = f"nm -g '{lib_path}' | head -20"
        all_symbols = run_command(all_symbols_cmd)
        if all_symbols:
            print("  Here are some symbols from the library:")
            print(all_symbols)
            
    # 检查是否是C++库
    cpp_check = f"nm -g '{lib_path}' | grep -E '(std::|\\.cpp)'"
    cpp_symbols = run_command(cpp_check)
    if cpp_symbols:
        print("  ⚠️ This appears to be a C++ library with name mangling")
        
        # 检查是否存在demangled符号
        demangle_cmd = f"nm -g '{lib_path}' | c++filt | grep '{search_prefix}'"
        demangled = run_command(demangle_cmd)
        if demangled:
            print("  Demangled symbols:")
            for line in demangled.splitlines()[:10]:
                print(f"     {line}")

def check_import():
    """Try to import the RAPID Kit module"""
    print("\n🔍 Attempting to import RAPID Kit...")
    try:
        # 1. 首先尝试加载lib模块
        from rapid_kit.lib import get_lib, get_all_loaded_libs
        lib = get_lib()
        print("  ✅ Successfully loaded RAPID Core library")
        
        all_libs = get_all_loaded_libs()
        if all_libs:
            print(f"  ✅ Loaded {len(all_libs)} libraries:")
            for lib_name in all_libs:
                print(f"     - {lib_name}")
        
        # 直接检查动态库的符号
        try:
            from rapid_kit.lib import get_media_lib
            media_lib = get_media_lib()
            
            # 获取库文件路径
            import ctypes
            if hasattr(media_lib, '_name'):
                media_lib_path = media_lib._name
            elif hasattr(media_lib, '__file__'):
                media_lib_path = media_lib.__file__
            else:
                # 使用已知路径替代
                libraries_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
                if system == 'darwin':
                    media_lib_path = os.path.join(libraries_dir, 'libraries', 'libRapidMedia.dylib')
                elif system == 'windows':
                    media_lib_path = os.path.join(libraries_dir, 'libraries', 'RapidMedia.dll')
                else:
                    media_lib_path = os.path.join(libraries_dir, 'libraries', 'libRapidMedia.so')
                    
            if os.path.exists(media_lib_path):
                check_library_symbols(media_lib_path)
            else:
                print(f"  ❌ Could not determine path to Media library")
        except Exception as e:
            print(f"  ❌ Failed to check Media library symbols: {e}")
        
        # 2. 直接测试RAPID_MediaChat_Create函数
        try:
            import ctypes
            from rapid_kit.lib import get_media_lib
            
            media_lib = get_media_lib()
            print("  ✅ Successfully got Media library handle")
            
            # 尝试获取函数指针，不定义返回类型
            media_chat_create = getattr(media_lib, "RAPID_MediaChat_Create", None)
            if media_chat_create:
                print("  ✅ Function RAPID_MediaChat_Create exists in the Media library")
                # 不尝试调用，只检查存在性
            else:
                print("  ❌ Function RAPID_MediaChat_Create NOT FOUND in Media library")
                
            # 尝试获取可用函数列表
            print("  📊 Listing available functions in Media library:")
            functions_found = 0
            for item in dir(media_lib):
                if not item.startswith('_'):  # 跳过内部属性
                    functions_found += 1
                    if functions_found <= 10:  # 只显示前10个函数
                        print(f"     - {item}")
            if functions_found > 10:
                print(f"     ... and {functions_found-10} more functions")
            if functions_found == 0:
                print("     No public functions found in Media library!")
            
            # 直接尝试获取地址
            try:
                import sys
                if sys.platform == 'darwin':
                    import ctypes.util
                    address = ctypes.cdll.LoadLibrary(ctypes.util.find_library('c')).dlsym(
                        ctypes.c_void_p.in_dll(media_lib, '_handle').value, 
                        'RAPID_MediaChat_Create'
                    )
                    if address:
                        print(f"  ✅ Found RAPID_MediaChat_Create at address: {address}")
                    else:
                        print("  ❌ Could not find RAPID_MediaChat_Create symbol address")
            except Exception as addr_e:
                print(f"  ❌ Error checking symbol address: {addr_e}")
            
        except Exception as media_e:
            print(f"  ❌ Failed to access Media library: {media_e}")
        
        # 3. 尝试直接导入和使用MediaChat
        try:
            from rapid_kit import MediaChat
            print("  ✅ Successfully imported MediaChat class")
            try:
                chat = MediaChat()
                print("  ✅ Successfully created MediaChat instance")
            except Exception as inst_e:
                print(f"  ❌ Failed to create MediaChat instance: {inst_e}")
        except Exception as import_e:
            print(f"  ❌ Failed to import MediaChat: {import_e}")
            
    except Exception as e:
        print(f"  ❌ Failed to load library: {e}")
        # Don't show the full traceback to keep things clean
        print(f"     Error: {str(e)}")
        
        # 尝试更基本的导入来诊断问题
        try:
            import rapid_kit
            print(f"  ✅ Basic import of rapid_kit package succeeded")
            print(f"  ⚠️ Issue may be with specific modules, not the package itself")
        except Exception as pkg_e:
            print(f"  ❌ Cannot import rapid_kit package: {pkg_e}")
            print(f"  ⚠️ Check your Python path and package installation")

def show_summary(libs_found, libraries_dir):
    """Show a summary of findings and next steps"""
    print("\n📝 Summary:")
    
    if libs_found:
        print("  ✅ Libraries directory and core library found")
        print(f"  ✅ Using libraries from: {libraries_dir}")
        print("  ✅ You should be able to use the rapid_kit package")
    else:
        print("  ❌ There are issues with your library setup")
        print("  📝 To use rapid_kit, you need to:")
        print(f"    1. Ensure the libraries directory exists at:")
        print(f"       {libraries_dir}")
        print(f"    2. Place the correct library files in this directory")
        
        system = platform.system().lower()
        if system == "darwin":
            print(f"       - libRapidCore.dylib")
            print(f"       - libRapidMedia.dylib")
            print(f"       - libRapidSDL.dylib")
        elif system == "windows":
            print(f"       - RapidCore.dll")
            print(f"       - RapidMedia.dll")
            print(f"       - RapidSDL.dll")
        elif system == "linux":
            print(f"       - libRapidCore.so")
            print(f"       - libRapidMedia.so")
            print(f"       - libRapidSDL.so")

def main():
    print("=" * 60)
    print("RAPID Kit Library Diagnostic Tool")
    print("=" * 60)
    
    print(f"🖥️ System information:")
    print(f"  OS: {platform.system()} {platform.release()}")
    print(f"  Python: {platform.python_version()}")
    print(f"  Script directory: {os.path.dirname(os.path.abspath(__file__))}")
    print(f"  Current directory: {os.getcwd()}")
    print(f"  Package directory: {parent_dir}")
    
    libs_found, libraries_dir = check_libraries_dir()
    
    if libs_found:
        check_import()
    else:
        print("\n🔍 Not attempting import because libraries were not found")
    
    show_summary(libs_found, libraries_dir)
    
    print("\n=" * 60)

if __name__ == "__main__":
    main() 