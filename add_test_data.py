import sqlite3

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("INSERT INTO tasks (name, quantity, time) VALUES (?, ?, ?)",
               ("Сделать домашку", "1", "18:00"))

cursor.execute("INSERT INTO tasks (name, quantity, time) VALUES (?, ?, ?)",
               ("Тренировка", "1", "20:00"))

conn.commit()
conn.close()

print("Данные добавлены")