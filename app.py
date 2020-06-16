from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
    return "Hello Python!"

if __name__ == '__main__':
    app.run()
