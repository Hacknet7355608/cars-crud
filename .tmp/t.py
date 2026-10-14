import glob, os
p = r"C:\Users\Lenovo\.dsh\attachments\v1\files"
print("isdir", os.path.isdir(p))
print("listdir", os.listdir(p)[:5])
print("glob1", glob.glob(p + r"\*\*.pdf"))
print("glob2", glob.glob(p + r"\**\*.pdf", recursive=True))
