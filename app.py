from flask import Flask
from Routes.login import login_bp
from Routes.register import register_bp
from Routes.task import task_bp
from db import init_db

app = Flask(__name__)
app.secret_key = 'clave_secreta'  # Necesaria para sesiones

# Inicializa la base de datos
init_db()

# Registra los blueprints
app.register_blueprint(register_bp)
app.register_blueprint(login_bp)
app.register_blueprint(task_bp)

if __name__ == '__main__':
    app.run(debug=True)
