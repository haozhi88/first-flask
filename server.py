from flask import Flask, render_template
app = Flask(__name__)
signed_in = False

@app.route("/")
def index():
    return render_template('index.html', signed_in=signed_in)

@app.route('/profile/<name>')
def profile(name):
    num = len(name)
    return render_template('profile.html', name=name, signed_in=signed_in, num=num)

@app.route('/login')
def login():
    return render_template('login.html', signed_in=signed_in)

@app.route('/layout')
def layout():
    return render_template('extend_layout.html')

@app.route('/user/<name>')
def show(name):
    return f"Hi {name}"

if __name__ == '__main__':
    app.run(debug=True)