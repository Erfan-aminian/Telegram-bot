import sqlite3

class Config:
    def __init__(self, db_file='users.db'):
        self.db_file = db_file
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            create_table_query = """
                CREATE TABLE IF NOT EXISTS users(
                    id integer PRIMARY KEY,
                    first_name text,
                    last_name text,
                    phone_number text
                );
            """
            cursor.execute(create_table_query)
            connection.commit()

    def AddUser(self, user_data):
        """
        user_data یک تاپل است که شامل (id, first_name, last_name, phone_number) می‌باشد.
        """
        insert_query = """
            INSERT INTO users (id, first_name, last_name, phone_number)
            VALUES (?, ?, ?, ?)
        """
        with sqlite3.connect(self.db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(insert_query, user_data)
            connection.commit()

    @staticmethod
    def GetUsers(db_file='users.db'):
        fetch_data_query = """
            SELECT * FROM users;
        """
        with sqlite3.connect(db_file) as connection:
            cursor = connection.cursor()
            cursor.execute(fetch_data_query)
            rows = cursor.fetchall()

        # نمایش اطلاعات کاربران
        for row in rows:
            print(f'ID: {row[0]}, First Name: {row[1]}, Last Name: {row[2]}, Phone Number: {row[3]}')

        return rows  # بازگرداندن داده‌ها برای استفاده‌های بعدی











# import sqlite3
# class Config:
#     def __init__(self, db_file):
#         connection = sqlite3.connect('users.db')
#         curser = connection.cursor()
#         create_table_query = """
#             CREATE TABLE IF NOT EXISTS users(
#                 id integer PRIMARY KEY,
#                 first_name text,
#                 last_name text,
#                 phone_number text
#             );
#         """
#         curser.execute(create_table_query)
#         connection.commit()
#         connection.close()
#     def AddUser(self, id, first_name, last_name, phone_number):
#         sample_data_query = """
#             INSERT INTO users (id, first_name, last_name, phone_number)
#             VALUES (?, ?, ?, ?)
#         """
#         sample_data = [
#             (12344, 'ehsan', 'ghadiri', '0911122339'),
#             (14343, "Erfan", "Saberi", "123456789"),
#             (24344, "Ali", "Rezaei", "987654321"),
#         ]
#         with sqlite3.connect('users.db') as connection:
#             curser = connection.cursor()
#             curser.executemany(sample_data_query, sample_data)
#     @staticmethod
#     def GetUsers():
#         fetch_data_query = """
#             SELECT * FROM users;
#
#         """
#         rows = []
#         with sqlite3.connect('users.db') as connection:
#             curser = connection.cursor()
#             curser.execute(fetch_data_query)
#             rows = curser.fetchall()
#         for row in rows:
#             print(f'ID:{row[0]}, fname:{row[1]}, lname:{row[2]}, phone_number:{row[3]}')
