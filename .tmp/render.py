import pymupdf, os
base = r"C:\Users\Lenovo\.dsh\attachments\v1\files"
out = r"C:\Users\Lenovo\Desktop\cars-crud\notes\img"
os.makedirs(out, exist_ok=True)
targets = [
 ("a0", "1-What is devops.pdf", [1,2]),
 ("9f", "7-Docker and containers.pdf", [2,5,6,7,9]),
 ("c7", "4- Version-control.pdf", [6]),
 ("0c", "5-Software testing.pdf", [3,10,26,34]),
]
import glob
for pref, name, pages in targets:
    hits = glob.glob(base + f"\\{pref}\\*\\" + name)
    if not hits:
        print("MISS", name); continue
    doc = pymupdf.open(hits[0])
    for p in pages:
        if p-1 < doc.page_count:
            pix = doc[p-1].get_pixmap(dpi=110)
            fn = os.path.join(out, f"{pref}_p{p}.png")
            pix.save(fn)
            print(fn, pix.width, pix.height)
