from database import mydatabase
from database import log

def main():
    dbms = mydatabase.MyDatabase(mydatabase.SQLITE, dbname='mydb.sqlite', log=log)
    # dbms.create_db_tables()

    # dbms.print_all_data(mydatabase.USERS)
    # dbms.print_all_data(mydatabase.ADDRESSES)

    dbms.sample_query()
    dbms.sample_delete()
    dbms.sample_insert()
    dbms.sample_update()


if __name__ == "__main__":
    log.set_custom_log_info("log_file/error.log")
    main()