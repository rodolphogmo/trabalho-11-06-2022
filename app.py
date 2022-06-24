from flask import Flask, render_template, send_file, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'rodolpho'

@app.route("/")
def home():
    return render_template("template.html")

@app.route("/diferenciais")
def diferenciais():
    return render_template("diferenciais.html")

@app.route("/mercado")
def mercado():
    return render_template("mercado.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/professores")
def team():
    return render_template("professores.html")

@app.route("/cursar")
def curso():
    return render_template("cursar.html")

@app.route("/contato", methods=['POST', 'GET'])
def contact():
    myform = Form()
    if myform.is_submitted():
        resultado = request.form
        return render_template("ty.html", resultado=resultado)
    return render_template("contact.html", form=myform)

@app.route("/calendario")
def calendario():
    return render_template("calendario.html")

####################################################

@app.route("/grade")
def grade():
    return render_template("grade.html")

@app.route("/download")
def download_file():
    caminho = 'matriz.pdf'
    return send_file(caminho,as_attachment=True)

####################################################


class Form(FlaskForm):
    nome = StringField('nome')
    email = StringField('email')
    phone = StringField('phone')
    msg = StringField('msg')
    submit = SubmitField("send")

"""
class Form:

    def __init__(self, nome:str, email:str, phone:int, msg:str):
        self__nome = nome
        self__email = email
        self__phone = phone
        self__msg = msg

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__nome = value

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, value):
        self.__nome = value

    @property
    def msg(self):
        return self.__msg

    @msg.setter
    def nmsg(self, value):
        self.__nome = value
"""



