# -*- coding: utf-8 -*-
"""检测下载素材的真实图片格式，重命名为带扩展名的文件名。"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(BASE, 'assets', 'raw')

def sniff(path):
    with open(path, 'rb') as f:
        head = f.read(16)
    if head[:3] == b'\xff\xd8\xff':
        return 'jpg'
    if head[:8] == b'\x89PNG\r\n\x1a\n':
        return 'png'
    if head[:4] == b'GIF8':
        return 'gif'
    if head[:4] == b'RIFF' and head[8:12] == b'WEBP':
        return 'webp'
    return 'bin'

for name in sorted(os.listdir(RAW)):
    p = os.path.join(RAW, name)
    if os.path.isfile(p) and not name.startswith('.'):
        ext = sniff(p)
        new = p + '.' + ext
        os.replace(p, new)
        print(name, '->', ext, os.path.getsize(new), 'bytes')
