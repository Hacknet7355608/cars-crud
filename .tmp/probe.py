import re, zlib, sys, glob, os
p = sys.argv[1]
data = open(p,'rb').read()
print("size", len(data))
print("header", data[:20])
print("num stream", data.count(b'stream'))
print("Font refs", len(re.findall(rb'/Font', data)))
print("Filter", set(re.findall(rb'/Filter\s*/(\w+)', data)))
print("Image", len(re.findall(rb'/Subtype\s*/Image', data)))
print("ToUnicode", len(re.findall(rb'/ToUnicode', data)))
print("kids/pages", len(re.findall(rb'/Type\s*/Page[^s]', data)))
