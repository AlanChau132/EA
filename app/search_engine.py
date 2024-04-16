from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['query']
  
 
    search_results = ['Result 1', 'Result 2', 'Result 3']
    
    return render_template('results.html', query=query, results=search_results)

if __name__ == '__main__':
    app.run(debug=True)
