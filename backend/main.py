from flask import Flask, jsonify
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)


@app.route('/')
def is_alive():
    return jsonify('live')


@app.route('/api/msg/<string:msg>', methods=['POST'])
def msg_post_api(msg):
    print("msg_post_api")  # tmp
    msg_id = 99  # tmp
    # TODO: store msg in DB and return identifier
    # msg_id = None
    return jsonify(msg_id)


@app.route('/api/msg/<int:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    print(f"msg_get_api > msg_id = {msg_id}")   # tmp
    msg = f"<Message #{msg_id} contents>"   # tmp
    # TODO: get msg from DB and return it
    # msg = None
    return jsonify(msg)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
