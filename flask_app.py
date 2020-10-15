from flask import Flask, render_template, request, jsonify
#import psycopg2
from datetime import datetime
from pytz import timezone

app = Flask(__name__)

# configurar o banco de dados

class Aluno():
    def __init__(self,ra, nome, email, logradouro, numero,complemento):
        self.ra = ra
        self.nome = nome
        self.email = email
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento

sql_create = '''CREATE TABLE Hair2you (RA integer 
                PRIMARY KEY NOT NULL, nome varchar(50) NOT NULL, email_do_aluno 
                varchar(50) NOT NULL, Logradouro varchar(50) NOT NULL,
                numero varchar(5) NOT NULL, cep varchar(10) NOT NULL,
                complemento varchar(20)
                )'''


'''def create_table():
    connection = psycopg2.connect(
       
        host = "dbimpacta.postgresql.dbaas.com.br",
        user = "dbimpacta",
        password = "impacta#2020",
        dbname = "dbimpacta"

        
    )
    cursor = connection.cursor()
    cursor.execute(sql_create)
    connection.commit()
    cursor.close()
    connection.close()

create_table()'''


@app.route('/inicio')
@app.route('/')
def inicio():
    return render_template('index.html')


@app.route('/login1', methods=['GET', 'POST'])
def login1():
    return render_template('obrigado.html')


@app.route('/aluno', methods=['GET', 'POST'])
def aluno():
    if request.method == "POST":
        ra = request.form['ra']
        nome = request.form['nome']
        email = request.form['email_do_aluno'] 
        logradouro = request.form['endereço'] 
        numero = request.form['numero']
        complemento = request.form['complemento']
        return render_template('contato.html')
    if ra and nome and email and logradouro and numero and complemento:
        a = Aluno(ra, nome, email, logradouro, numero,complemento)
        sql_create.session.add(a)
        sql_create.commit()
    return render_template('obrigado.html') 


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/obrigado')
def obrigado():
    return render_template('obrigado.html')
    

@app.route('/login')
def login():
    return render_template('login.html')




## Para rodar o projeto em desenvolvimento

if __name__ == '__main__':
    app.run(debug=True)
