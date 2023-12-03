# app.py
import mysql.connector

# Fungsi untuk membuat koneksi ke database
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",  # Ganti dengan username MySQL Anda
        password="",  # Ganti dengan password MySQL Anda
        database="new_perpus"
    )

# Fungsi untuk melakukan login
def user_login(username, password):
    connection = create_connection()
    cursor = connection.cursor()    
    query = "SELECT * FROM tbl_login WHERE user = %s AND pass = %s"
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    connection.close()
    return result

# Fungsi untuk menampilkan data biaya denda
def show_biaya_denda():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM tbl_biaya_denda")
    result = cursor.fetchall()
    connection.close()
    return result

def show_nama(username):
    connection = create_connection()
    cursor = connection.cursor()
    query = "SELECT nama FROM tbl_login WHERE user = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchall()
    connection.close()
    return result