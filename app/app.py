from flask import Flask
from src.route.blueprint import blueprint


server = Flask(__name__)

server.register_blueprint(blueprint, url_prefix="/api/v1")

if __name__ == "__main__":
    server.run(port=4000)
