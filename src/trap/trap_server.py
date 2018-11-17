from flask import Flask, jsonify
app = Flask(__name__)
app.run(debug=True, port=8082)

secret = ""

@app.route('/register')
def register():
    global secret
    secret = request.args.get('secret')
    print("[SECRET] {}".format(secret))

@app.route('/get')
def get():
    return jsonify({
        "secret": secret
    })