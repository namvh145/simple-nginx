import os
from flask import Flask, send_file

tmpl_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
print(tmpl_dir)
app = Flask(__name__, template_folder=tmpl_dir)

@app.route('/tree.jpg', methods=["GET"])
def index():
    return send_file("static/tree.jpg")

if __name__ == "__main__":
    app.run()