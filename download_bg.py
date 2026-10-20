# -*- coding: utf-8 -*-
"""下载 5 张原神国家元素主题背景图到 assets/bg/"""
import urllib.request, os, ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

imgs = {
    'bg-liyue':     'https://aka.doubaocdn.com/s/4nhFFc1Bn1',      # 璃月·翠黛峰 1920x1080
    'bg-mondstadt': 'https://aka.doubaocdn.com/s/rw1lQSuybx',      # 蒙德·风起地 2675x1670
    'bg-inazuma':   'https://aka.doubaocdn.com/s/qCgKXCg01X',      # 稻妻·初雷寻踪 2304x1440
    'bg-sumeru':    'https://aka.doubaocdn.com/s/7dcCi0IHvB',      # 须弥·初临雨林 2448x1530
    'bg-fontaine':  'https://aka.doubaocdn.com/s/qguYj3236U',      # 枫丹·格式塔 2474x1549
}

out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets', 'bg')
os.makedirs(out_dir, exist_ok=True)

for name, url in imgs.items():
    path = os.path.join(out_dir, name + '.jpg')
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, context=ctx, timeout=60) as r:
            data = r.read()
        with open(path, 'wb') as f:
            f.write(data)
        print(name, len(data), 'bytes ->', path)
    except Exception as e:
        print(name, 'FAILED:', e)
