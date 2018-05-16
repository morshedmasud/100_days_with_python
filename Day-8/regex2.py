import re

"""Find the all email from complicated string"""
text = "masud.raj6@gmail.com, subeen at book.com, book (at) subeen dot com, masud [at] morshed [dot] com"

temp = re.sub(r'\s+[\(\[]*\s*at\s*[\)\]]*\s+', r'@', text, flags=re.I)

final = re.sub(r'\s+[\(\[]*\s*dot\s*[\)\]]*\s+', r'.', temp, flags=re.I)

final = re.findall(r'([\w.]+@\w+\.\w+)', str(final))
print(final)

