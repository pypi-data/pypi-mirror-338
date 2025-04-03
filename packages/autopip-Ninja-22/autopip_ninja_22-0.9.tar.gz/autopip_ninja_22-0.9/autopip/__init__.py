"""
AutoPIP: Python modüllerini otomatik yükleyen kütüphane
"""

import ast
import sys
import subprocess
import importlib.util
import os
from typing import List, Set, Optional, Dict, Any
import builtins
import json
import requests

GEMINI_API_KEY = "AIzaSyCG1JXujiOc_zYB-CcwouvYQ0scSJQ2PUc"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

def ask_gemini(question: str) -> Optional[Dict[Any, Any]]:
    """Gemini AI'ya soru sorar ve cevabı döndürür."""
    try:
        headers = {
            "Content-Type": "application/json"
        }
        
        data = {
            "contents": [{
                "parts": [{
                    "text": question
                }]
            }],
            "generationConfig": {
                "temperature": 0.1,
                "topK": 1,
                "topP": 1
            }
        }
        
        response = requests.post(
            f"{GEMINI_URL}?key={GEMINI_API_KEY}",
            headers=headers,
            json=data
        )
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Gemini API hatası: {response.status_code}")
            return None
    except Exception as e:
        print(f"Gemini API hatası: {e}")
        return None

def get_package_info(module_name: str) -> Optional[str]:
    """
    Gemini AI'ya sorarak modülün PyPI paket adını ve diğer bilgilerini alır.
    """
    question = f"""
    Python'da '{module_name}' modülünü kullanmak için hangi PyPI paketi yüklenmeli?
    Sadece paket adını yaz, başka bir şey yazma.
    Örnek cevap formatı: 'pillow' veya 'opencv-python' gibi.
    Eğer emin değilsen, boş bırak.
    """
    
    response = ask_gemini(question)
    if response and 'candidates' in response:
        try:
            package_name = response['candidates'][0]['content']['parts'][0]['text'].strip()
            if package_name and len(package_name) > 0:
                return package_name
        except:
            pass
    return None

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
        spec = importlib.util.find_spec(module_name)
        return spec is not None
    except:
        return False

def install_module(module_name: str) -> bool:
    """Bir modülü pip ile yüklemeye çalışır."""
    try:
        # İlk önce direkt modül adıyla deneme yap
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", module_name],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )
        
        if result.returncode == 0:
            return True
            
        # Başarısız olduysa Gemini'ye sor
        package_name = get_package_info(module_name)
        if package_name and package_name != module_name:
            print(f"'{module_name}' için Gemini'nin önerdiği paket deneniyor: {package_name}")
            result = subprocess.run(
                [sys.executable, "-m", "pip", "install", package_name],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False
            )
            if result.returncode == 0:
                return True
                
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
    
    # Yüklenen modüllerin listesi
    installed = []
    
    # Her bir import için kontrol et
    for module_name in imports:
        # Eğer stdlib modülü ise atla
        if module_name in sys.stdlib_module_names:
            continue
            
        # Modülü yüklemeyi dene
        if not is_module_installed(module_name):
            print(f"{module_name} modülü yükleniyor...")
            if install_module(module_name):
                installed.append(module_name)
                # Modül yüklendikten sonra importlib'i temizle
                importlib.invalidate_caches()
    
    return installed

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
            if module_name not in sys.stdlib_module_names:
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
            raise
    
    # Orijinal import fonksiyonunu kaydet
    global _original_import
    _original_import = builtins.__import__
    
    # Import fonksiyonunu değiştir
    builtins.__import__ = custom_import