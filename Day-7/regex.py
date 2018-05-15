import re
""" Find the phone number in a string"""
# s = "House no: 4, phone no: 016  70397894 ihgoeri giiof 00000000654 fggifdg01821598697 jgkgj 01857457130"
# result = re.findall(r'01[56789]\s*\d{8}', s)
# print(result)
""" Find the full word with space"""
# s = "Bangladesh, India, South Koria, New Zealand, America,"
# r = re.findall(r'(\w+\s*\w+)', s)
# print(r)

"""Make a list from multiline text file"""
# with open('file.txt', 'r') as f:
    # temp = f.read()
# r = re.findall(r'^.+?$', temp, re.MULTILINE)
# print(r)
"""Find only word or name in html list element"""
# s = '<li>Morshed masud</li><li>Kamrul </li><li>Tanvir</li><li>Tamim</li>'
# r = re.findall(r'<li>(.*?)</li>', s)
# print(r)

""" re.compile"""
# s = "This is line 1: Date is 2017/06/18. and there in another Date : 2020-02-09. The third and final date is 2222/07/25."
# pat = re.compile(r"(\d{4})[/-](\d{2})[/-](\d{2})")
# r = pat.findall(s)
# print(r)

""" Change anything in string with re.sub()"""
s = "Abcd, 12345 - 22"
r = re.sub(r'\d', '1', s)
print(r)