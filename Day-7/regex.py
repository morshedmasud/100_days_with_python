import re
s = "House no: 4, phone no: 016  70397894 ihgoeri giiof 00000000654 fggifdg01821598697 jgkgj 01857457130"
result = re.findall(r'01[56789]\s*\d{8}', s)
print(result)

