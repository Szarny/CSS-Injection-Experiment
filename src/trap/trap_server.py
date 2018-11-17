from flask import Flask, request, jsonify, make_response
app = Flask(__name__)

secret = ""

@app.route('/register')
def register():
    global secret
    secret = request.args.get('secret')
    print(secret)
    print("[SECRET] {}".format(secret))

    return make_response(jsonify({
        "status": 1
    }))

@app.route('/get', methods=['GET'])
def get():
    print(secret)
    return make_response(jsonify({
        "secret": secret
    }))


app.run(debug=True, port=8082)