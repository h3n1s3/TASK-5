from flask import Flask , request
import os

app = Flask(__name__)

@app.route('/ping')
def ping():
    target = request.args.get('ip' , '127.0.0.1')
    cmd = f"ping -c 1 {target}"
    output = os.popen(cmd).read()
    return f"{output}"
if ( __name__ == '__main__'):
    app.run(host='0.0.0.0' , port=5000)
