from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/profile/<name>')
def profile(name):
    return render_template('profile.html', name=name)

@app.route('/user/<name>')
def show(name):
    return f"Hi {name}"

if __name__ == '__main__':
    app.run(debug=True)