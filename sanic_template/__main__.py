from sanic_template import app

server = app.create()
server.run(host="0.0.0.0", port=8000, debug=server.config.DEBUG)
