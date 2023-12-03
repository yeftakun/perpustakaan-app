# gui.py
from flask import Flask, render_template, request
from app import user_login, show_biaya_denda, show_nama

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user_data = user_login(username, password)

    if user_data:
        nama_result = show_nama(username)  # Menggunakan username sebagai parameter
        return render_template('dashboard.html', myname=nama_result[0][0], data=show_biaya_denda())
    else:
        return render_template('index.html', error="Login failed. Incorrect username or password.")
    


if __name__ == '__main__':
    app.run(debug=True)
