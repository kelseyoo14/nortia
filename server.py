from flask import Flask, request, render_template, session, flash
from flask import redirect as flaskredirect
import os
import json

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.config['SECRET_KEY'] = os.environ.get("FLASK_SECRET_KEY", "abcdef")


if __name__ == "__main__":
    app.debug = True

    # connect_to_db(app, os.environ.get("DATABASE_URL"))

    DEBUG = "NO_DEBUG" not in os.environ
    PORT = int(os.environ.get("PORT", 5000))

    app.run(host="0.0.0.0", port=PORT, debug=DEBUG)
