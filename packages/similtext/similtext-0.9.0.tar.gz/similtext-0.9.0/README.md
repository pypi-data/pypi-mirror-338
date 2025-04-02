# Instalación y uso de **similtext**

## Instalación:
```bash/powershell
pip install similtext
```

## Ejemplo de uso:
```python
from similtext import SimilText

sw = SimilText()

# Comparación
assert sw.icmp('one twó ThreE foúr',
    'ONE two three FOUR') == 0
assert sw.icmp('melón grande', 'melon pequeño') == -1
```

### Para más información vea la clase **SimilText**.