import os

import yagmail as yagmail
from flask import Flask, render_template, flash, request, redirect, url_for, jsonify
import utils
from formulario import FormLogin
from mensaje import mensajes

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('register.html')

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method=='POST':
        usuario= request.form['username']
        clave= request.form['password']
        if usuario=="Prueba" and clave=="Prueba123":
            return redirect('/mensaje')
    else :
        return render_template('login.html')

@app.route('/contactanos')
def contactar():
    formulario= FormLogin()
    return render_template('contactenos.html', form= formulario)

@app.route('/mensaje')
def Message():
    return jsonify({"mensajes" : mensajes})

@app.route('/register', methods=('GET', 'POST'))
def register():
    try:
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            email = request.form['correo']
            error = None

            if not utils.isUsernameValid(username):
                error = "El usuario debe ser alfanumerico o incluir solo '.','_','-'"
                flash(error)
                return render_template('register.html')

            if not utils.isPasswordValid(password):
                error = 'La contraseña debe contener al menos una minúscula, una mayúscula, un número y 8 caracteres'
                flash(error)
                return render_template('register.html')

            if not utils.isEmailValid(email):
                error = 'Correo invalido'
                flash(error)
                return render_template('register.html')
                
            #Modificar la siguiente linea con tu informacion personal
            yag = yagmail.SMTP(user='pruebas.ciclo3.uninorte@gmail.com', password='uninorte2021') 
            yag.send(to=email, subject='Activa tu cuenta',
                     contents='Bienvenido, usa este link para activar tu cuenta ')
            flash('Revisa tu correo para activar tu cuenta')
            return render_template('login.html')
        
        print("Llego al final")
        return render_template('register.html')
    except:
        return render_template('register.html')
# Modulo Principal
if __name__=='__main__':
    app.run(debug=True)