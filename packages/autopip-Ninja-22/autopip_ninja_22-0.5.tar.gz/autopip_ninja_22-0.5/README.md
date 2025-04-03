# AutoPIP

Python modüllerini otomatik yükleyen kütüphane. Import edilen modüller eksikse otomatik olarak pip ile yükleme yapar.

## Kurulum

```bash
pip install autopip-Ninja-22
```

## Kullanım

İki farklı kullanım şekli var:

1. Kod çalışırken otomatik yükleme:
```python
import autopip
autopip.watch()  # Bu satırı kodunuzun başına ekleyin

# Artık eksik modüller otomatik yüklenecek
import pandas  # pandas yüklü değilse otomatik yüklenir
```

2. Belirli bir kod parçası için yükleme:
```python
import autopip

kod = """
import pandas
import numpy
"""

# Eksik modülleri yükle
yuklenenler = autopip.auto_install(kod)
print("Yüklenen modüller:", yuklenenler)
```

## Özellikler

- Python kodundaki import ifadelerini otomatik tespit eder
- Eksik modülleri pip ile otomatik yükler
- Standart kütüphane modüllerini yüklemeye çalışmaz
- İki farklı kullanım modu (watch ve auto_install)

## Lisans

MIT License 