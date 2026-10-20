# -*- coding: utf-8 -*-
"""下载原神角色头像素材，居中裁剪为 256x256 方形 PNG。"""
import os
import urllib.request

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, 'assets', 'raw')
OUT = os.path.join(BASE, 'assets')
os.makedirs(RAW, exist_ok=True)
os.makedirs(OUT, exist_ok=True)

URLS = {
    'zhongli': 'https://aka.doubaocdn.com/s/ipT7GDPad1',
    'hutao':   'https://aka.doubaocdn.com/s/jmaBSziVhF',
    'raiden':  'https://aka.doubaocdn.com/s/zrMfzoB8kY',
    'ganyu':   'https://aka.doubaocdn.com/s/XyoP8oY9EI',
    'furina':  'https://aka.doubaocdn.com/s/SKeGOaEiQD',
    'nahida':  'https://aka.doubaocdn.com/s/ouz7LtrcAH',
    'venti':   'https://aka.doubaocdn.com/s/KLp67D2yVy',
    'klee':    'https://aka.doubaocdn.com/s/V8I1W7t9d0',
}

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}

for name, url in URLS.items():
    raw_path = os.path.join(RAW, name)
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        data = urllib.request.urlopen(req, timeout=30).read()
        with open(raw_path, 'wb') as f:
            f.write(data)
        print(f'[ok] downloaded {name}: {len(data)} bytes')
    except Exception as e:
        print(f'[fail] {name}: {e}')

try:
    from PIL import Image
    print('PIL available')
except ImportError:
    print('PIL missing')

print('RAW dir:', RAW)
print('OUT dir:', OUT)
