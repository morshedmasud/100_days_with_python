import os

def create_directory(name):
    try:
        os.mkdir(name)
    except Exception as e:
        print(e,"\nname already exists")

create_directory('dimik_pub')