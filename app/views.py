from flask.templating import render_template
from app import app


@app.route('/')
def hello_world():
    return render_template('default.html')

@app.route('/led')
def light_led():
    # led.light(15)
    # LED's anschalten
    return render_template('default.html')

if __name__ == '__main__':
    app.run()
