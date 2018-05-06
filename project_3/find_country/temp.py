import re
p = r"([\d\.-]+)"
a = []
with open('file.txt', 'r') as f:
    a = f.readline()
    temp = re.findall(p, a)
    print(temp)

#     for i in f:
#         a.append(i.split())
# for i in a:
#     with open("new_list.txt", "a") as n:




# for i in a:
#     for j in i:
#         if j[0]>"A" and j<"Z":
#             with open("new_list.txt", "a") as f2:
#                 f2.write(("%s\n"%j))

