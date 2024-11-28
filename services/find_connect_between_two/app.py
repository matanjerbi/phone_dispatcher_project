from flask import Flask
from find_connect import connect_blueprint

app = Flask(__name__)

app.register_blueprint(connect_blueprint)


if __name__ == '__main__':
    app.run(port=5004, debug=True)

