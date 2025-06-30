# Sistema de Gestión de Tareas (PFO2)

Este proyecto es un sistema básico de gestión de tareas con autenticación de usuarios.  
Está desarrollado con **Flask** para el backend, **SQLite** para la persistencia de datos, y usa hashing seguro para las contraseñas.

---


## Características

- Registro de usuarios con almacenamiento seguro de contraseñas (hash).
- Inicio de sesión con verificación de credenciales.
- Gestión de tareas (agregar y listar tareas) por usuario autenticado.
- Uso de SQLite para persistencia ligera y sencilla.
- Interfaces web simples para registro, login y tareas.
- Estructura organizada en controladores, modelos y plantillas.

---

## Estructura del proyecto

PFO2/
│
├── Routes/                # Rutas separadas por funcionalidad
│   ├── login.py           # Lógica de inicio de sesión
│   ├── register.py        # Lógica de registro de usuario
│   └── task.py            # Ruta protegida de bienvenida
│
├── Templates/             # Plantillas HTML
│   ├── login.html
│   ├── register.html
│   └── tasks.html
│
├── static/                # Archivos estáticos como CSS
│   └── styles.css
│
├── app.py                 # Punto de entrada y configuración de la app Flask
├── cliente.py             # Cliente en consola
├── db.py                  # Conexión a la base de datos SQLite
├── utils.py               # Funciones auxiliares como hashing de contraseñas
├── requirements.txt       # Lista de dependencias del proyecto
└── README.md              # Documentación del proyecto




## Requisitos

- Python 3.8 o superior
- Paquetes listados en `requirements.txt`

---

## Instalación

1. Clonar el repositorio:

```bash
   git clone https://github.com/IsabellaChiaradia/PSR_PFO2.git
   cd pfo2
   ```

2. Crear y activar un entorno virtual:

```bash
   python3 -m venv env
   env/bin/activate
   ```
3. Instalar dependencias:

```bash
   pip install -r requirements.txt
   ```

4. Inicializar la base de datos: 

```bash
   python db.py
   ```


## Uso 

1. Ejecutar la app:

```bash
   python app.py
   ```

2. Abrir el navegador y navegar a:

Registro: http://localhost:5000/registro

Login: http://localhost:5000/login

Gestión de tareas: http://localhost:5000/tareas (requiere login)


