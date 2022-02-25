from sanic_template import app

app.run(host="0.0.0.0", port=8000, debug=app.config.DEBUG)
