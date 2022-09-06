import os
from flask import Flask, request, abort, render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('calc.html')

@app.route('/calc')
def calculadorawebparametro():
    valor1=request.args.get('v1')
    valor2=request.args.get('v2')
    operacao=request.args.get('operacao')

    try:
        v1 = int(valor1)
    except:
        abort(404)

    try:
        v2 = int(valor2)
    except:
        abort(404)

    if (operacao == "soma"):
        Calculo = v1 + v2
    elif (operacao == "subtracao"):
        Calculo = v1 - v2
    elif (operacao == "divisao"):
        if(v2 == 0 & v1 == 0):
            abort(422)
        else:
            Calculo = v1 / v2
    elif (operacao == "multiplicacao"):
        Calculo = v1 * v2
    else:
        abort(404)

    return str(Calculo)
    #Para serialização, o retorno sempre será string

@app.route('/calculaform', methods=['POST','GET'])
def calculadoracomform():
    valor1=request.form['v1']
    valor2=request.form['v2']
    operacao=request.form['operacao']

    try:
        v1 = int(valor1)
    except:
        abort(404)

    try:
        v2 = int(valor2)
    except:
        abort(404)

    if (operacao == "soma"):
        Calculo = v1 + v2
    elif (operacao == "subtracao"):
        Calculo = v1 - v2
    elif (operacao == "divisao"):
        if(v2 == 0 & v1 == 0):
            abort(422)
        else:
            Calculo = v1 / v2
    elif (operacao == "multiplicacao"):
        Calculo = v1 * v2
    else:
        abort(404)

    return str(Calculo)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    app.run(host='0.0.0.0', port=port)
