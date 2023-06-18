from flask import Flask
from View import example

def create_app():
    app = Flask(__name__)
    app.register_blueprint(example.example_blueprint)

    return app

if __name__ == "__main__":
    create_app().run()