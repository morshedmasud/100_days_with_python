import re
p = r"[A-Z](.*)"
a = []
with open('file.txt', 'r') as f:
    for i in f:
        a.append(i.split())



for i in a:
    for j in i:
        if j[0]>"A" and j<"Z":
            with open("new_list.txt", "a") as f2:
                f2.write(("%s\n"%j))

