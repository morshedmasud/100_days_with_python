import re
p = r"([\d\.-]+)"
a = []
with open('file.txt', 'r') as f:
    for j in f:
        temp = re.search(r'([\w\.-]+)\B([\D\.-]+)', j)
        n = temp.group()
        with open(n[0]+'.text', 'a') as f:
            f.write(n)
            f.write("\n")