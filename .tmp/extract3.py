import pymupdf, glob, os, re, traceback
files = sorted(glob.glob(r"C:\Users\Lenovo\.dsh\attachments\v1\files\**\*.pdf", recursive=True))
out = r"C:\Users\Lenovo\Desktop\cars-crud\notes\raw"
os.makedirs(out, exist_ok=True)
log = open(r"C:\Users\Lenovo\Desktop\cars-crud\.tmp\diag.log","w",encoding="utf-8")
for f in files:
    try:
        doc = pymupdf.open(f)
        base = os.path.splitext(os.path.basename(f))[0]
        safe = re.sub(r'[^A-Za-z0-9._-]', '_', base)
        lines = []
        short = []
        for i, page in enumerate(doc):
            t = page.get_text("text")
            lines.append(f"\n===== PAGE {i+1} =====\n" + t)
            if len(t.strip()) < 40:
                short.append((i+1, len(t.strip()), len(page.get_images())))
        with open(os.path.join(out, safe + ".txt"), "w", encoding="utf-8") as fh:
            fh.write("".join(lines))
        log.write(f"{base}: pages={doc.page_count} chars={sum(len(x) for x in lines)} lowtext={short[:15]}\n")
    except Exception as e:
        log.write(f"ERROR {f}: {e}\n{traceback.format_exc()}\n")
log.close()
print("done")
