from flask import Flask
from bluetooth_service import bluetooth_blueprint

app = Flask(__name__)

app.register_blueprint(bluetooth_blueprint)


if __name__ == '__main__':
    app.run(port=5001, debug=True)

