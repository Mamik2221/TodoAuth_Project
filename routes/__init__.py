from routes.task_routes import routes


def init_routes(app):
    app.register_blueprint(routes, url_prefix="/tasks")