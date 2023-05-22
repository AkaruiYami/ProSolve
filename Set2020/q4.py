import re

N = int(input())

sentences = [input() for _ in range(N)]

p = re.compile(r"\((\w+)\)")
for s in sentences:
    m = p.findall(s)
    if not m:
        print(0)
        continue
    words = "_".join(m).split("_")
    print(len(max(words, key=len)))
