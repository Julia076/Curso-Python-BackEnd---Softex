from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def formulario():
    erros = {}
    nome = ''
    idade = ''
    altura = ''

    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        altura = request.form['altura']

        if not idade.isdigit():
            erros['idade'] = 'Idade deve ser um número inteiro.'
        if not altura.replace('.', '', 1).isdigit():
            erros['altura'] = 'Altura deve ser um número válido.'

        if not erros:
            return render_template('resultado.html',
                                   nome=nome,
                                   idade=int(idade),
                                   altura=float(altura))

    return render_template('formulario.html',
                           nome=nome,
                           idade=idade,
                           altura=altura,
                           erros=erros)

if __name__ == '__main__':
    app.run(debug=True)
