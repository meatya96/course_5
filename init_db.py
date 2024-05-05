import psycopg2

def create_db():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="12345678", host="localhost")
    cursor = conn.cursor()

    conn.autocommit = True
    # команда для создания базы данных homework_hh
    sql1 = "DROP DATABASE IF EXISTS homework_hh;"
    sql2 = "CREATE DATABASE homework_hh"

    # выполняем код sql
    cursor.execute(sql1)
    cursor.execute(sql2)
    print("База данных успешно создана")

    cursor.close()
    conn.close()
def create_tables(user,password):
    conn = psycopg2.connect(dbname="homework_hh", user=user, password=password, host="localhost")
    cursor = conn.cursor()
    fd = open('database_setup.sql', 'r')
    sql = fd.read()
    fd.close()
    cursor.execute(sql)
    # Подтверждение изменений
    conn.commit()
    cursor.close()
    conn.close()
if __name__ == "__main__":
    create_db()
    create_tables('postgres', '12345678')