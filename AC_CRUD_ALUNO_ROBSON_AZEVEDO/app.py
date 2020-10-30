from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__)

POSTGRES = {'host' : "dbimpacta.postgresql.dbaas.com.br",
            'user' : "dbimpacta",
            'password' : "impacta#2020",
            'dbname' : "dbimpacta",
            'port': "5432"
}

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(password)s@%(host)s:%(port)s/%(dbname)s' % POSTGRES
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

'''app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Impacta.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)'''


class Robson_azevedo(db.Model):
    ra = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50),  unique=True)
    email = db.Column(db.String(50), unique=True)
    logradouro = db.Column(db.String(50) )
    numero = db.Column(db.String(5) )
    cep = db.Column(db.String(10))
    complemento = db.Column(db.String(20))

    def __init__(self, ra, nome, email, logradouro, numero, cep, complemento ):
        self.ra = ra
        self.nome = nome
        self.email = email
        self.logradouro = logradouro
        self.numero = numero
        self.cep = cep
        self.complemento = complemento

db.create_all()

@app.route('/')
def index():
    alunos = Robson_azevedo.query.all()
    return render_template("index.html", alunos=alunos)



@app.route("/add", methods=['GET','POST'])
def add():
    if request.method == 'POST':
        aluno = Robson_azevedo(ra = request.form['ra'], 
                        nome = request.form['nome'],
                        email = request.form['email'], 
                        logradouro = request.form['logradouro'], 
                        numero = request.form['numero'],
                        cep = request.form['cep'],
                        complemento = request.form['complemento'])
        db.session.add(aluno)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')



@app.route("/edit/<int:ra>", methods=['GET','POST'])
def edit(ra):
    aluno = Robson_azevedo.query.get(ra)
    if request.method == 'POST':
        aluno.ra = request.form['ra']
        aluno.nome = request.form['nome']
        aluno.email = request.form['email']
        aluno.logradouro = request.form['logradouro'] 
        aluno.numero = request.form['numero']
        aluno.cep = request.form['cep']
        aluno.complemento = request.form['complemento']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', aluno=aluno)



@app.route("/delete/<int:ra>")
def delete(ra):
    cliente = Robson_azevedo.query.get(ra)
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('index'))

    



if __name__ == '__main__':
    app.run(debug=True)