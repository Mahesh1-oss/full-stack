import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Akingbmaheswar_1",
        database="payment_db"
    )