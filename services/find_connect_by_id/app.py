from flask import Flask
from connect_devices import find_connect_blueprint

app = Flask(__name__)

app.register_blueprint(find_connect_blueprint)


if __name__ == '__main__':
    app.run(port=5003, debug=True)

