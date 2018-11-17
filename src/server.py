import base64

from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    css = base64.b64decode(request.args.get('css')).decode()
    return render_template('./index.html', css=css)

if __name__ == '__main__':
    app.run(debug=True, port=8080)