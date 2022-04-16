''''
'''

class DatabaseConn:

    def __init__(self) -> None:
        self.__database = 'Postgres' # Private
        self._conn = '//connection_string'# Protected
        self.user = 'admin' # Public

    
    def get_database(self):
        print(self.__database)
    

    def _testing_connection(self):
        print('Connection Ok!')


class Repository(DatabaseConn):

    def __init__(self) -> None:
        super().__init__()
        print(self.user)
       # print(self.__database) #Error
        print(self._conn)

    def select(self):
        self._testing_connection()
        print('Connecting to {}'.format(self._conn))
        print('SELECT * FROM users')


repo = Repository()
repo.select()


print('\n')

db = DatabaseConn()
print(db.user)
# print(self.__database) - Error
print(db._conn)

db._testing_connection()