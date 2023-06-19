from flask import Flask
from view import routes
from dotenv import load_dotenv

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.register_blueprint(routes.main)

    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=int('3000'), debug=True)