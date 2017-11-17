import json

from flask import Flask, current_app

import beergen

app = Flask(__name__)


@app.route('/')
def index():
    """Main app entry point"""
    return current_app.send_static_file("index.html")

@app.route("/beer/")
def beer():
    """REST interface to get a random beer"""
    wrapper = "update({})"
    return wrapper.format(
        json.dumps({'name': beergen.name(), 'desc': beergen.description()}))
    

if __name__ == "__main__":

    print(description())
