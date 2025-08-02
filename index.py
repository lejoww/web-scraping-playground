import random
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'clave-super-secreta'

# Página de bienvenida
@app.route('/')
def welcome():
    return render_template('welcome.html')

# Página de login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'admin' and password == '12345678':
            return redirect(url_for('dashboard'))
        else:
            flash('Credenciales incorrectas. Intenta de nuevo.', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

# Dashboard protegido
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/random')
def random_number():
    number = random.randint(0, 10)
    return render_template('random.html', number=number)

if __name__ == '__main__':
    app.run(debug=True)
