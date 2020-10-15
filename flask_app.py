from flask import Flask, render_template, request, jsonify
import psycopg2
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




def create_table():
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

create_table()


@app.route('/inicio')
@app.route('/')
def inicio():
    return render_template('index.html')



@app.route('/aluno', methods=['GET', 'POST'])
def seus_dados():
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
