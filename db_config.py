import sqlite3
class Config:
    def __init__(self, db_file):
        connection = sqlite3.connect('users.db')
        curser = connection.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users(
                id integer PRIMARY KEY,
                first_name text,
                last_name text,
                phone_number text
            );
        """
        curser.execute(create_table_query)
        connection.commit()
        connection.close()
    def AddUser(self, first_name, last_name, phone_number):
        sample_data_query = """
            INSERT INTO users (id, first_name, last_name, phone_number)
            VALUES (?, ?, ?, ?)
        """
        sample_data = [
            (12344, 'ehsan', 'ghadiri', '0911122339'),
            (14343, "Erfan", "Saberi", "123456789"),
            (24344, "Ali", "Rezaei", "987654321"),
        ]
        with sqlite3.connect('users.db') as connection:
            curser = connection.cursor()
            curser.executemany(sample_data_query, sample_data)
    @staticmethod
    def GetUsers():
        fetch_data_query = """
            SELECT * FROM users;

        """
        rows = []
        with sqlite3.connect('users.db') as connection:
            curser = connection.cursor()
            curser.execute(fetch_data_query)
            rows = curser.fetchall()
        for row in rows:
            print(f'ID:{row[0]}, fname:{row[1]}, lname:{row[2]}, phone_number:{row[3]}')
