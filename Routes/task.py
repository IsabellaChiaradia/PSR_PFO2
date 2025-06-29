from flask import Blueprint, render_template, session, redirect

task_bp = Blueprint('task', __name__)

@task_bp.route('/tareas')
def tareas():
    if 'usuario_id' not in session:
        return redirect('/login')
    return render_template('tasks.html')
