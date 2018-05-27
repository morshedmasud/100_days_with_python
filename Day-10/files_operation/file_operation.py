'''text to binary, binary to text'''
# try:
#     with open("temp.txt", 'wb') as f:
#         t = f.write(b'Life is good')
#         print(t)
#     with open("temp.txt", 'rb') as file:
#         n = file.read()
#         print(n.decode("utf-8"), type(n))
# except Exception as e:
#     print(e)

'''TemporaryFile'''
# from tempfile import TemporaryFile

# with TemporaryFile('w+') as f:
#     f.write("LIfe is cool.\n")

#     f.seek(5)
#     data = f.read()
#     print(data)

'''csv file'''
# import csv

# with open("csv_file.csv", 'r') as f:
#     f = csv.reader(f)

#     sum = 0
#     print(type(f))
#     for i, row in enumerate(f):
#         print(i, row[0], row[1])
#         sum += int(row[1] if i > 0 else 0)
#     print("total cost: ", sum)

# list_items = [
# ["name", "age", "country"],
# ["Bill Gates", 45, "US"],
# ["Mark Zuckerberg", 40, "US"],
# ["Swift", 30, "Canada"]
# ]

# import csv
# with open('csv_file.csv', 'w') as f:
#     t = csv.writer(f)
#     t.writerows(list_items)

'''JSON file'''
import json

data = {
        "name" : "Bill Gates",
        "age" : 55,
        "counrty" : "US",
        "is_retired" : True
}
# json_str = json.dumps(data)
# print(json_str, type(json_str))
# json_decode = json.loads(json_str)
# print(json_decode, type(json_decode))

with open('json_data.json', 'w') as f:
    json.dump(data, f)

with open("json_data.json", "r") as t:
    json_d = json.load(t)
    print(json_d)