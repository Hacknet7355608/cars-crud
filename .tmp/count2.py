import re
p = r"C:\Users\Lenovo\Desktop\cars-crud\quiz\quiz-题目与解答.md"
lines = open(p, encoding="utf-8").read().split("\n")
mode = None
counts = {}
order = []
for ln in lines:
    if ln.startswith("## 第一部分"):
        mode = "single"; continue
    if ln.startswith("## 第二部分"):
        mode = "multi"; continue
    if ln.startswith("## 第三部分"):
        mode = "tf"; continue
    if ln.startswith("## 第四部分"):
        mode = "fill"; continue
    if ln.startswith("## 第五部分"):
        mode = "short"; continue
    if ln.startswith("### ") and mode:
        order.append((mode, ln[4:].strip()))
        counts.setdefault((mode, ln[4:].strip()), 0)
    m = re.match(r'^\*\*(\d+)\. ', ln)
    if m and mode:
        counts[order[-1]] += 1
for k in order:
    print(k, counts[k])
