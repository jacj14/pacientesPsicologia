from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def saludo():
    return render_template("index.html")

@app.route("/admin/pacientes")
def pacientes():
    return render_template("pacientes.html")

@app.route("/admin/terapias")
def terapias():
    return render_template("terapias.html")

app.run(debug=True)