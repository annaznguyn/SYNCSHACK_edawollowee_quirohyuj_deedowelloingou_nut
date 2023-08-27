from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selected_category = request.form.get('category')
        print(f'You selected: {selected_category}')
    return render_template('homepage.html')

@app.route('/login')
def login():
    return "Loginnnnnn"

if __name__ == '__main__':
    app.run()