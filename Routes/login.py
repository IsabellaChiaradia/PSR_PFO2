from flask import Blueprint, request, render_template, redirect, session, flash
import sqlite3
from utils import verificar_contraseña

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        with sqlite3.connect("tareas.db") as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, contraseña FROM usuarios WHERE usuario = ?", (usuario,))
            datos = cursor.fetchone()

            if datos and verificar_contraseña(datos[1], contraseña):
                session['usuario_id'] = datos[0]
                flash('Login exitoso')
                return redirect('/tareas')
            else:
                flash('Credenciales inválidas')
                return redirect('/login')

    return render_template('login.html')
