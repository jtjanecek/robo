import sqlite3

try:
    sqliteConnection = sqlite3.connect('database.db')
    cursor = sqliteConnection.cursor()
    print("Database connected to SQLite")

    sqlite_select_Query = "select * from users;"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    for r in record:
        print(r)
    cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)
finally:
    if (sqliteConnection):
        sqliteConnection.close()
        print("The SQLite connection is closed")
