"""
AutoPIP: Python modüllerini otomatik yükleyen kütüphane
"""

import ast
import sys
import subprocess
import importlib.util
from typing import List, Set
import builtins

def find_imports(code: str) -> Set[str]:
    """Python kodundaki import ifadelerini analiz eder."""
    tree = ast.parse(code)
    imports = set()
    
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for name in node.names:
                imports.add(name.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
    
    return imports

def is_module_installed(module_name: str) -> bool:
    """Bir modülün yüklü olup olmadığını kontrol eder."""
    try:
        importlib.util.find_spec(module_name)
        return True
    except ImportError:
        return False

def install_module(module_name: str) -> bool:
    """Bir modülü pip ile yüklemeye çalışır."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        return True
    except subprocess.CalledProcessError:
        return False

def auto_install(code: str) -> List[str]:
    """
    Verilen Python kodundaki eksik modülleri tespit edip yüklemeye çalışır.
    
    Args:
        code (str): Python kodu
        
    Returns:
        List[str]: Yüklenen modüllerin listesi
    """
    # Stdlib modülleri (bunları yüklemeye çalışmayacağız)
    stdlib_modules = sys.stdlib_module_names
    
    # Import edilen modülleri bul
    imports = find_imports(code)
    
    # Yüklenen modüllerin listesi
    installed = []
    
    # Her bir import için kontrol et
    for module_name in imports:
        # Eğer stdlib modülü ise veya zaten yüklüyse atla
        if module_name in stdlib_modules:
            continue
            
        # Modülü yüklemeyi dene
        if not is_module_installed(module_name):
            print(f"{module_name} modülü yükleniyor...")
            if install_module(module_name):
                installed.append(module_name)
                print(f"{module_name} başarıyla yüklendi!")
    
    return installed

def watch():
    """
    Çalışan kodda import edilen modülleri otomatik olarak yükler.
    Bu fonksiyonu kodunuzun başında çağırın.
    """
    def custom_import(name, globals=None, locals=None, fromlist=(), level=0):
        # Önce modülün yüklü olup olmadığını kontrol et
        module_name = name.split('.')[0]
        
        # Stdlib modüllerini kontrol etme
        if module_name not in sys.stdlib_module_names:
            if not is_module_installed(module_name):
                # Yüklü değilse yüklemeyi dene
                print(f"{module_name} modülü yükleniyor...")
                if install_module(module_name):
                    print(f"{module_name} başarıyla yüklendi!")
                    # Modül yüklendikten sonra importlib'i temizle
                    importlib.invalidate_caches()
        
        # Orijinal import işlemini yap
        return original_import(name, globals, locals, fromlist, level)
    
    # Orijinal import fonksiyonunu kaydet
    try:
        # Önce builtins modülünden deneyelim
        original_import = builtins.__import__
    except AttributeError:
        # Olmazsa __builtins__ sözlüğünden alalım
        if isinstance(__builtins__, dict):
            original_import = __builtins__['__import__']
        else:
            original_import = __builtins__.__import__
    
    # Import fonksiyonunu değiştir
    builtins.__import__ = custom_import 