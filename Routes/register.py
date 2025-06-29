from flask import Blueprint, request, render_template, redirect, flash
import sqlite3
from utils import hash_contraseña

register_bp = Blueprint('register', __name__)

@register_bp.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario = request.form['usuario']
        contraseña = request.form['contraseña']

        if not usuario or not contraseña:
            flash('Faltan datos')
            return redirect('/registro')

        try:
            with sqlite3.connect("tareas.db") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO usuarios (usuario, contraseña) VALUES (?, ?)",
                               (usuario, hash_contraseña(contraseña)))
                conn.commit()
                flash('Registro exitoso')
                return redirect('/login')
        except sqlite3.IntegrityError:
            flash('Usuario ya existe')
            return redirect('/registro')

    return render_template('register.html')
