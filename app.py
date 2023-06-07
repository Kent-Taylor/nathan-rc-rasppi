from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    direction = request.args.get('direction', '')
    return render_template('index.html', direction=direction)

@app.route('/up')
def up():
    direction = 'up'
    return render_template('index.html', direction=direction)

@app.route('/down')
def down():
    direction = 'down'
    return render_template('index.html', direction=direction)

@app.route('/left')
def left():
    direction = 'left'
    return render_template('index.html', direction=direction)

@app.route('/right')
def right():
    direction = 'right'
    return render_template('index.html', direction=direction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    # app.run(host='192.168.5.159', port=5000)
    # Nathan, we will need to IP address to the raspi