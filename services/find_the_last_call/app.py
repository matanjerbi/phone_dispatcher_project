from flask import Flask
from connect_devices import find_last_call_blueprint

app = Flask(__name__)

app.register_blueprint(find_last_call_blueprint)


if __name__ == '__main__':
    app.run(port=5005, debug=True)

