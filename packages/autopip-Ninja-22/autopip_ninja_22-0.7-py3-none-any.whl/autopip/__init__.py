"""
AutoPIP: Python modüllerini otomatik yükleyen kütüphane
"""

import ast
import sys
import subprocess
import importlib.util
import os
from typing import List, Set
import builtins

def get_stdlib_modules() -> Set[str]:
    """Standart kütüphane modüllerini belirler."""
    try:
        # Python 3.10+ için
        return sys.stdlib_module_names
    except AttributeError:
        # Python 3.10 öncesi için
        stdlib_path = os.path.dirname(os.path.dirname(sys.__file__)) + "/lib"
        if not os.path.exists(stdlib_path):
            # Windows için alternatif yol
            stdlib_path = os.path.dirname(sys.executable) + "/Lib"
        
        stdlib_modules = set()
        if os.path.exists(stdlib_path):
            for name in os.listdir(stdlib_path):
                if name.endswith(".py"):
                    stdlib_modules.add(name[:-3])
        return stdlib_modules

# Standart kütüphane modüllerini global olarak belirle
STDLIB_MODULES = get_stdlib_modules()

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
    spec = importlib.util.find_spec(module_name)
    return spec is not None

def install_module(module_name: str) -> bool:
    """Bir modülü pip ile yüklemeye çalışır."""
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", module_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        if result.returncode == 0:
            print(f"Yükleme başarılı: {result.stdout}")
            return True
        else:
            print(f"Yükleme hatası: {result.stderr}")
            return False
    except Exception as e:
        print(f"Beklenmeyen hata: {e}")
        return False

def auto_install(code: str) -> List[str]:
    """
    Verilen Python kodundaki eksik modülleri tespit edip yüklemeye çalışır.
    
    Args:
        code (str): Python kodu
        
    Returns:
        List[str]: Yüklenen modüllerin listesi
    """
    # Import edilen modülleri bul
    imports = find_imports(code)
    print("Bulunan importlar:", imports)
    
    # Yüklenen modüllerin listesi
    installed = []
    
    # Her bir import için kontrol et
    for module_name in imports:
        # Eğer stdlib modülü ise atla
        if module_name in STDLIB_MODULES:
            print(f"{module_name} stdlib modülü, atlanıyor...")
            continue
            
        # Modülü yüklemeyi dene
        if not is_module_installed(module_name):
            print(f"{module_name} modülü yükleniyor...")
            if install_module(module_name):
                installed.append(module_name)
                print(f"{module_name} başarıyla yüklendi!")
                # Modül yüklendikten sonra importlib'i temizle
                importlib.invalidate_caches()
        else:
            print(f"{module_name} zaten yüklü...")
    
    return installed

# Global olarak orijinal import fonksiyonunu sakla
_original_import = builtins.__import__

def watch():
    """
    Çalışan kodda import edilen modülleri otomatik olarak yükler.
    Bu fonksiyonu kodunuzun başında çağırın.
    """
    def custom_import(name, globals=None, locals=None, fromlist=(), level=0):
        # Önce modülün yüklü olup olmadığını kontrol et
        module_name = name.split('.')[0]
        
        try:
            # Stdlib modüllerini kontrol etme
            if module_name not in STDLIB_MODULES:
                if not is_module_installed(module_name):
                    # Yüklü değilse yüklemeyi dene
                    print(f"{module_name} modülü yükleniyor...")
                    if install_module(module_name):
                        print(f"{module_name} başarıyla yüklendi!")
                        # Modül yüklendikten sonra importlib'i temizle
                        importlib.invalidate_caches()
                    else:
                        print(f"{module_name} yüklenemedi!")
            
            # Orijinal import işlemini yap
            return _original_import(name, globals, locals, fromlist, level)
        except Exception as e:
            print(f"Import hatası: {e}")
            raise  # Orijinal hatayı tekrar fırlat
    
    print("AutoPIP watch modu aktif...")
    print("Orijinal import fonksiyonu:", _original_import)
    
    # Import fonksiyonunu değiştir
    builtins.__import__ = custom_import
    
    print("Yeni import fonksiyonu:", builtins.__import__) 