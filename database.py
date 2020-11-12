import sqlite3

connection = sqlite3.connect("myDatabase.db")
#connection.row_factory = sqlite3.Row --> in app.py print(f"{entry['Date']}\n{entry['Content']}\n\n")

def create_table():
    with connection:
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);")

def add_entry(entry_content,entry_date):
    with connection:
        connection.execute(
            "INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)
        )

def get_entries():
    cursor = connection.execute("SELECT * FROM entries")
    return cursor #list

    #or
    #cursor = connection.cursor()
    #cursor.execure("SELECT * FROM entries")