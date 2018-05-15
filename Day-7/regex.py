import re
""" Find the phone number in a string"""
# s = "House no: 4, phone no: 016  70397894 ihgoeri giiof 00000000654 fggifdg01821598697 jgkgj 01857457130"
# result = re.findall(r'01[56789]\s*\d{8}', s)
# print(result)
""" Find the full word with space"""
# s = "Bangladesh, India, South Koria, New Zealand, America,"
# r = re.findall(r'(\w+\s*\w+)', s)
# print(r)


with open('temp.txt', 'r') as f:
    temp = f.read()
    print(temp)

