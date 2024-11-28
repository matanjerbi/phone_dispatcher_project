from flask import Flask
from signal_strength_stronger import phone_blueprint

app = Flask(__name__)

app.register_blueprint(phone_blueprint)


if __name__ == '__main__':
    app.run(port=5002, debug=True)

