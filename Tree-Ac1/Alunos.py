import os
from flask import Flask, render_template, request
from flaskext.mysql import MySQL

mysql = MySQL()
app = Flask(__name__)

# Configurações para o DB MySQL
  # Usuário
app.config['MYSQL_DATABASE_USER'] = 'root'
  # Senha
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
  # Nome do banco de dados
app.config['MYSQL_DATABASE_DB'] = 'teste'
  # Host, precisar ser igual ao IP do imagem MySQL caso usando Docker
  # Para pegar o IP: docker network inspect bridge
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.2'
mysql.init_app(app)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/gravarAluno', methods=['POST','GET'])
def gravarAluno():
  Nome = request.form['Nome']
  CPF = request.form['CPF']
  Endereco = request.form['Endereco']
  if Nome and CPF and Endereco:
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('insert into tbl_Alunos (user_name, user_cpf, user_address) VALUES (%s, %s, %s)', (Nome, CPF, Endereco))
    conn.commit()
  return render_template('index.html')


@app.route('/listarAlunos', methods=['POST','GET'])
def listarAlunos():
  conn = mysql.connect()
  cursor = conn.cursor()
  cursor.execute('select user_name, user_cpf, user_address from tbl_Alunos')
  data = cursor.fetchall()
  conn.commit()
  return render_template('lista_Alunos.html', datas=data)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5008))
    app.run(host='0.0.0.0', port=port)