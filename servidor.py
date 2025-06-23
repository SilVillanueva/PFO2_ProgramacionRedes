
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    usuario = db.Column(db.String(80), unique=True, nullable=False)
    contraseña = db.Column(db.String(200), nullable=False)

@app.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({'error': 'Faltan datos'}), 400
    
    usuario = datos['usuario']
    contraseña = datos['contraseña']

    if Usuario.query.filter_by(usuario=usuario).first():
        return jsonify({'error': 'Usuario ya existe'}), 400
    
    contraseña_hash = generate_password_hash(contraseña)

    nuevo_usuario = Usuario(usuario=usuario, contraseña=contraseña_hash)
    db.session.add(nuevo_usuario)
    db.session.commit()

    return jsonify({'mensaje': f'Usuario {usuario} creado exitosamente'}), 201

@app.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    if not datos or 'usuario' not in datos or 'contraseña' not in datos:
        return jsonify({'error': 'Faltan datos'}), 400
    
    usuario = datos['usuario']
    contraseña = datos['contraseña']

    usuario_encontrado = Usuario.query.filter_by(usuario=usuario).first()

    if not usuario_encontrado or not check_password_hash(usuario_encontrado.contraseña, contraseña):
        return jsonify({'error': 'Usuario o contraseña incorrectos'}), 401

    return jsonify({'mensaje': f'Login exitoso. ¡Bienvenido {usuario}!' })

@app.route('/')
def index():
    return '¡Bienvenido al Sistema de Gestión de Tareas!'

@app.route('/tareas', methods=['GET'])
def tareas():
    html = """
    <html>
    <head><title>Gestión de Tareas</title></head>
    <body>
    <h1>¡Bienvenido a la gestión de tareas!</h1>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crear tablas antes de arrancar el servidor
    app.run(debug=True)