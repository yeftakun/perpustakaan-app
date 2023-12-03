# gui.py
from flask import Flask, render_template, request
from app import user_login, show_nama, total_books, total_users, dipinjam, dikembalikan, levellogin, meminjam #, show_biaya_denda

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_data = user_login(username, password)
    # user_level = levellogin(username)
    level_result = levellogin(username)
    h1 = (level_result[0][0])=='Petugas'
    h2 = (level_result[0][0])=='Anggota'
    user_level1 = h1
    user_level2 = h2
    

    if user_data and user_level1:
        nama_result = show_nama(username)  # Menggunakan username sebagai parameter
        total_buku = total_books()
        total_user = total_users()
        total_dipinjam = dipinjam()
        total_dikembalikan = dikembalikan()
        return render_template('petugas/dashboard.html', 
                               myname=nama_result[0][0], 
                               mylevel=level_result[0][0],
                               countbook=total_buku[0][0], 
                               countuser=total_user[0][0], 
                               countpinjam=total_dipinjam[0][0],
                               countkembali=total_dikembalikan[0][0]
                               )#, data=show_biaya_denda()
    elif user_data and user_level2:     # yang ini buat anggota
        nama_result = show_nama(username)  # Menggunakan username sebagai parameter
        total_buku = total_books()
        total_dipinjam = meminjam(username)
        return render_template('anggota/dashboard.html', 
                               myname=nama_result[0][0], 
                               mylevel=level_result[0][0],
                               countbook=total_buku[0][0], 
                               countpinjam=total_dipinjam[0][0]
                               )
    else:
        return render_template('index.html', error="Login failed. Incorrect username or password.")

if __name__ == '__main__':
    app.run(debug=True)
