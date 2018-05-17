import os
import re
import sys
import requests

def create_directory(name):
    try:
        os.mkdir(name)
    except Exception as e:
        print(e,"\nname already exists")

def down_img(img_url, file_name):
    print("Downloading", img_url)
    r = requests.get(img_url)
    with open(file_name, 'wb') as f:
        f.write(r.content)

def get_directory_name(regex, url):
    result = re.findall(regex, url)
    dir_name = "_".join(result[0])
    return dir_name


def process():
    # create home directory
    main_dir = "dimik_pub"
    create_directory(main_dir)

    # collection of book information from http://dimik.pub
    url = "http://dimik.pub"
    response = requests.get(url)
    if response.ok is False:
        sys.exit("Could no get response from server")
    page_content = response.text

    # create a regexp pattern for get the full information for all book
    regexp = re.compile(r'<div class="book-cover">\s*<a href="(.*?)">\s*<img src="(.*?)">.*?<h2 class="sd-title">\s*<.*?>(.*?)<', re.S)

    # create dir_regex for dir name
    dir_regex = re.compile(r'book/(\d+)/(\w+)-(\w+)-(\w+)-')

    # Finding full information about all book
    book_info = re.findall(regexp, page_content)

    # separate name, img_url and url for book information
    print(len(book_info))
    for item in book_info:
        name = item[2]
        img_url = item[1]
        book_url = item[0]


        # making directory name for create_directory()
        dir_name = main_dir + "/" + get_directory_name(dir_regex, book_url)
        create_directory(dir_name)

        # making file_name and create info text file to store all information about each book
        file_name = dir_name + "/" + "info.text"
        with open(file_name, 'w') as fp:
            fp.write(name + "\n")
            fp.write(book_url)

        # making image file name and using down_img() for download  each book image
        img_file_name = dir_name + "/" + "image.jpg"
        print(img_file_name)
        down_img(img_url, img_file_name)


if __name__ == "__main__":
    process()










