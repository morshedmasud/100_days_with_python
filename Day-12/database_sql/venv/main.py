from database import mydatabase

def main():
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='mydb.sqlite')

    dbms.create_db_tables()


if __name__ == "__main__":
    main()