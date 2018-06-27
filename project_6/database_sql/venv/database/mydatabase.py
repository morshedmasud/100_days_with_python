
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
import sys


# Global Variable
SQLITE = 'sqlite'

# Table names
USERS = 'users'
ADDRESSES = 'addresses'

class MyDatabase:

    # http://docs.sqlalchemy.org/en/latest/core/engines.html
    __log = None
    DB_ENGINE = {
        SQLITE: 'sqlite:///{DB}'
    }

    # Main DB Connection Ref Obj
    db_engine = None

    def __init__(self, dbtype, username='', password='', dbname='', log=''):
        dbtype = dbtype.lower()
        self.__log = log
        print("db type: ", dbtype)

        if dbtype in self.DB_ENGINE.keys():
            engine_url = self.DB_ENGINE[dbtype].format(DB=dbname)
            print("engin_url: ", engine_url)

            self.db_engine = create_engine(engine_url)
        else:
            # logging.INFO("DBtype is not found in DB_ENGINE")
            print("DBType is not found in  DB_ENGINE")

    def create_db_tables(self):
        metadata = MetaData()
        users = Table(USERS, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('first_name', String),
                      Column('last_name', String)
                      )

        address = Table(ADDRESSES, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('user_id', Integer, nullable=False),
                      Column('email', String, nullable=False),
                      Column('address', String)
                      )

        try:
            metadata.create_all(self.db_engine)
            print("Tables created")
        except Exception as e:
            print("Error occurred during Table creation!")
            self.__log.report(str(e))

    # Insert, Update, Delete
    def execute_query(self, query=''):
        if query == '':
            return

        print("query_obj: ", query)
        with self.db_engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                self.__log.report(str(e))
                print(e)

    def print_all_data(self, table='', query=''):
        query = query if query != '' else "SELECT * FROM '{}';".format(table)
        print(query)

        with self.db_engine.connect() as connection:
            try:
                result = connection.execute(query)
                # self.__log.success()
            except Exception as e:
                print(e)
                self.__log.report(str(e))
            else:
                for row in result:
                    print(row)  # print(row[0], row[1], row[2])
                result.close()
        print("\n")

    def sample_query(self):
        # sample query
        query = "SELECT first_name, last_name FROM {TBL_USR} WHERE last_name LIKE 'I%';".format(TBL_USR=USERS)
        self.print_all_data(query=query)

        # sample query joining
        query = "SELECT u.last_name as last_name, " \
            "a.email as email, a.address as address " \
            "FROM {TBL_USR} AS u " \
            "LEFT JOIN {TBL_ADDR} as a " \
            "WHERE u.id=a.user_id AND u.last_name LIKE 'M%';" \
            .format(TBL_USR=USERS, TBL_ADDR=ADDRESSES)
        self.print_all_data(query=query)

    def sample_delete(self):
        # Delete Data by ID
        query = "DELETE FROM {} WHERE id=3".format(USERS)
        self.execute_query(query)
        self.print_all_data(USERS)

        # Delete all data
        '''
        query = "DELETE FROM {}".format(USERS)
        self.execute_query(query)
        self.print_all_data(USERS)
        '''

    def sample_insert(self):
        # Insert Data
        query = "INSERT INTO {}(id, first_name, last_name) " \
                "VALUES (3, 'Nadim', 'Khan');".format(USERS)
        self.execute_query(query)
        self.print_all_data(USERS)

    def sample_update(self):
        # Update Data
        query = "UPDATE {} set first_name='XXXX' WHERE id={id}".format(USERS, id=3)
        self.execute_query(query)
        self.print_all_data(USERS)


