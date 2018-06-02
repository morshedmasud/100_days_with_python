from database import mydatabase
from database import log

def main():
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='mydb.sqlite', log=log)
    dbms.create_db_tables()


if __name__ == "__main__":
    log.set_custom_log_info("log_file/error.log")
    main()