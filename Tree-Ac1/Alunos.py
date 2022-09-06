import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# Configurações para o MySQL
# define o nome do user
app.config['MYSQL_DATABASE_USER'] = 'root'
# define a senha
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
# define o nome do DB
app.config['MYSQL_DATABASE_DB'] = 'Alunos'
# caso usando o docker, o ip precisar ser o da imagem do MySQL
# docker network inspect bridge
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravarAluno', methods=['POST','GET'])
def gravarAluno():
  nome = request.form['nome']
  cpf = request.form['cpf']
  endereco = request.form['endereco']
  if nome and cpf and endereco:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_alunos (nome_aluno, cpf_aluno, endereco_aluno) VALUES (%s, %s, %s)', (nome, cpf, endereco))
    conn.commit()
  return render_template('index.html')


@app.route('/listar', methods=['POST','GET'])
def listar():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select nome_aluno, cpf_aluno, endereco_aluno from tbl_alunos')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)
