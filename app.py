from flask import Flask, render_template

app = Flask(__name__, template_folder='templateFiles', static_folder='staticFiles')

@app.route('/index.html') ## utilizado para definir Rotas(URLS) e nesse caso a rota está fazendo a leitura de um arquivo e renderizando o no HTML
def html1():
    return render_template('index.html')

@app.route('/como-ajudar.html') ## utilizado para definir Rotas(URLS) e nesse caso a rota está fazendo a leitura de um arquivo e renderizando o no HTML
def html2():
    return render_template('como-ajudar.html')

@app.route('/contato.html') ## utilizado para definir Rotas(URLS) e nesse caso a rota está fazendo a leitura de um arquivo e renderizando o no HTML
def html3():
    return render_template('contato.html')

@app.route('/menu_bar.html') ## utilizado para definir Rotas(URLS) e nesse caso a rota está fazendo a leitura de um arquivo e renderizando o no HTML
def html6():
    return render_template('menu_bar.html')

@app.route('/sobre.html') ## utilizado para definir Rotas(URLS) e nesse caso a rota está fazendo a leitura de um arquivo e renderizando o no HTML
def html7():
    return render_template('sobre.html')

@app.route('/eventos.html') ## utilizado para definir Rotas(URLS) e nesse caso a rota está fazendo a leitura de um arquivo e renderizando o no HTML
def html8():
    return render_template('eventos.html')

@app.route('/seja-voluntario.html')
def html9():
    return render_template('seja-voluntario.html')


##inicia o método principal para rodar a aplicação.
if __name__ == '__main__':
    app.run(debug=True)

