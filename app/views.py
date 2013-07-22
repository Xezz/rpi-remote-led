from flask.templating import render_template
from app import app


@app.route('/')
def hello_world():
    return render_template('default.html')


if __name__ == '__main__':
    app.run()
