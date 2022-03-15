from flask import Flask, send_file, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route("/test", methods=['GET'])
def test():
    return send_file(
            'image/bus.jpg',
            as_attachment=True,
            attachment_filename='image/bus.jpg',
            mimetype='image/jpeg'
        )

@app.route("/show")
def show():
    return render_template('img_static.html')
    #return render_template('show.html', image_file="image/bus.jpg")


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
    # app.run(debug=True, host='192.168.137.89')