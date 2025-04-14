from flask import Flask, render_template, request

app = Flask(__name__)

PRECO_POR_KG = 121

@app.route('/', methods=['GET', 'POST'])
def calcular():
    custo = None
    gramas = ''
    if request.method == 'POST':
        try:
            gramas = float(request.form['gramas'])
            if gramas <= 0:
                custo = "O peso deve ser maior que zero."
            else:
                preco_por_grama = PRECO_POR_KG / 1000
                custo = gramas * preco_por_grama
        except ValueError:
            custo = "Por favor, insira um valor numérico válido."
    return render_template('index.html', custo=custo, gramas=gramas)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
