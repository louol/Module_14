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

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', f'{i * 10}', '1000'))

cursor.execute('UPDATE Users SET balance = 500 WHERE id % 2 = 1')

cursor.execute('DELETE FROM Users WHERE id % 3 = 1')

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != 60')
records = cursor.fetchall()

for record in records:
    print(f'Имя: {record[0]} | Почта: {record[1]} | Возраст: {record[2]} | Баланс: {record[3]}')

cursor.execute('DELETE FROM Users WHERE id  == 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total = cursor.fetchone()[0]
print(f'Общее количество записей -  {total}')

cursor.execute('SELECT SUM(balance) FROM Users')
sum_balans = cursor.fetchone()[0]
print(f'Cумма всех балансов - {sum_balans}')

print(f'Средний баланс всех пользователей -  {sum_balans / total}')


connection.commit()
connection.close()
