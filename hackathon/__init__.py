from flask import Flask


def create_app():
    app = Flask(__name__)

    from hackathon.index import index_bp
    from hackathon.search import search_bp

    app.register_blueprint(index_bp)
    app.register_blueprint(search_bp)

    return app
