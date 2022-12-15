from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'pacientes_psicologia'
app.config['MYSQL_PORT'] = 3306
mysql = MySQL(app)


@app.route("/")
def saludo():
    return render_template("index.html")

@app.route("/admin/pacientes")
def pacientes(datos = dict()):
    try:
        sql = """
                SELECT codigo, nombre, apellido, correo, telefono
                FROM paciente
            """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        datos["pacientes"] = cursor.fetchall()
        cursor.close()
    except:
        datos['error'] = 'Error al consultar al paciente'
        
    return render_template("pacientes.html", modelo = datos)

@app.route("/admin/terapias")
def terapias():
    return render_template("terapias.html")

@app.route("/admin/pacientes/nuevo", methods = ["POST"])
def nuevoPaciente():
    codigo = request.form["codigo"]
    nombre = request.form["nombre"]
    apellidos = request.form["apellidos"]
    correo = request.form["correo"]
    telefono = request.form["telefono"]
    
    datos = dict()
    
    try:
        sql = f"""
                INSERT INTO paciente (codigo, nombre, apellido, correo, telefono)
                VALUES ('{codigo}', '{nombre}','{apellidos}','{correo}',{telefono} )
            """
        cursor = mysql.connection.cursor()
        cursor.execute(sql)
        filas = cursor.rowcount
        mysql.connection.commit()
        cursor.close()
        if filas != 1:
            datos['error'] = 'Número de filas afectadas no es correcto'
    except:
        datos['error'] = 'Error al insertar los datos del paciente'
           
    return pacientes(datos)

app.run(debug=True)