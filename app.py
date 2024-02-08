from flask import Flask, render_template, request
from search_logic import search_paragraph 

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    search_term = request.form['search_term']

    search_result = search_paragraph(search_term)

    return render_template('index.html', search_result=search_result, search_term=search_term)

if __name__ == "__main__":
    app.run(debug=True)