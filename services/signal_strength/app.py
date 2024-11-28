from flask import Flask
from signal_strength_stronger import signal_strength_blueprint

app = Flask(__name__)

app.register_blueprint(signal_strength_blueprint)


if __name__ == '__main__':
    app.run(port=5002, debug=True)

