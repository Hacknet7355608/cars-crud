import re
p = r"C:\Users\Lenovo\Desktop\cars-crud\quiz\quiz-题目与解答.md"
t = open(p, encoding="utf-8").read()
sc = len(re.findall(r'^\*\*\d+\. ', t, re.M))
mc = len(re.findall(r'^\*\*\d+\. .*（多选）', t, re.M))
tf = len(re.findall(r'^\| \d+ \|', t, re.M))
fb = len(re.findall(r'^\d+\. .+→ \*\*', t, re.M))
print("single", sc, "multi", mc, "tf", tf, "fill", fb)
q = len(re.findall(r'^### [A-F]\.', t, re.M))
print("subsections", q)
print("chars", len(t))
