import re
# p = r"[A-Z](.*)"
p = r""
a = []
with open('file.txt', 'r') as f:
    a = f.readline(5)
    print(a)
    # temp = re.findall(p, a)
    # print(temp)


#     for i in f:
#         a.append(i.split())
# for i in a:
#     with open("new_list.txt", "a") as n:




# for i in a:
#     for j in i:
#         if j[0]>"A" and j<"Z":
#             with open("new_list.txt", "a") as f2:
#                 f2.write(("%s\n"%j))

