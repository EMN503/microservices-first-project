from socket import *
from telnetlib import IP
from flask import Flask, jsonify, render_template

app = Flask(__name__)

def fetchDetails():
    hostname = gethostname()
    ip = gethostbyname(hostname)
    return str(hostname), str(ip)

@app.route("/")
def hello_world():
    return "<p>HelloWorld</p>"

@app.route("/health")
def health():
    return jsonify(
        STATUS="UP"
    )

@app.route("/details")
def details():
    hostname, ip=fetchDetails()
    return render_template("index.html", HOSTNAME=hostname, ip=ip)  

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='9090')

