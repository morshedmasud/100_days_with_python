

# field_name = ["name", "Authon", "Publisher","Price", "Categorey"]
# book1 = ["Computer Programming, Part 1", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "240.00", "Programming"]
# book2 = ["Computer Programming Part 2", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "250.00", "Programming"]
# book3 = ["Computer Programming Part 3", "Tamim Shahriar Subeen", "Onnorokom Prokashoni", "200.00", "Programming",]
# book_list = [book1, book2, book3]

# with open("books.csv", 'w') as csvf:
#     csv_writer = csv.writer(csvf, delimiter=',', quotechar="\"", quoting=csv.QUOTE_MINIMAL)

#     csv_writer.writerow(field_name)
#     csv_writer.writerows(book_list)

# with open("books.csv", newline='') as csvfile:
#     csv_reader = csv.reader(csvfile)
#     for i in csv_reader:
#         for j in i:
#             print(j)
#         print()


import csv

field_name = ["name", "roll", "result"]
sd = {"name": "masud", "roll": 771582, "result": 3.25}
sd2 = {"name": "nizam", "roll": 771782, "result": 3.15}
sd_list = [sd, sd2]
with open("books.csv", "w") as csvf:
    csv_writer = csv.DictWriter(csvf, fieldnames = field_name)
    csv_writer.writeheader()
    csv_writer.writerows(sd_list)
