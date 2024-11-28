from flask import Flask
from phone_service import phone_blueprint

app = Flask(__name__)

app.register_blueprint(phone_blueprint)


if __name__ == '__main__':
    app.run(port=5000, debug=True)

