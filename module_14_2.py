import sqlite3



connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

# for i in range(10):
#     cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES (?,?,?,?)', (f'User{i+1}'
#     , f'example{i+1}@gmail.com', f'{(i+1)*10}', '1000'))
cursor.execute('UPDATE Users SET balance = ? WHERE id%2 != ?', (500, 0))
cursor.execute('DELETE FROM Users WHERE id%3=1')
cursor.execute('SELECT username, email, age, balance FROM Users WHERE age !=60')
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users WHERE id')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]
print(all_balance/total_users)



connection.commit()
connection.close()