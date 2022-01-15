from flask import Flask, url_for, render_template
from socketio import Server, WSGIApp

# Create Flask Application
app = Flask(
    __name__,
    static_url_path="/static/",
    static_folder=STATIC_FOLDER,
    template_folder=TEMPLATE_FOLDER
)

# Create SocketIO Server
sio = Server(
    async_mode="threading",
    logger=app.logger,
    engineio_logger=app.logger
)

# Set SocketIO WSGI Application
app.wsgi_app = WSGIApp(sio, app.wsgi_app)


if __name__ == "__main__":
    app.run(host="localhost", port=3000, threaded=True)
