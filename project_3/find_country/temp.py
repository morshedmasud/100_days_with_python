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
        # with open('new.txt', 'a') as n:
        #     n.write(temp.group())
        #     n.write('\n')
        # for i in j:
        #     if i.isalpha():
        #         new = open('new.txt', 'a')
        #         new.write(i)
        # new.write("\n")


# for i in a:
#     with open("new_list.txt", "a") as n:




# for i in a:
#     for j in i:
#         if j[0]>"A" and j<"Z":
#             with open("new_list.txt", "a") as f2:
#                 f2.write(("%s\n"%j))

