from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def is_alive():
    return jsonify('live')


@app.route('/api/msg/<string:msg>', methods=['POST'])
def msg_post_api(msg):
    # TODO: store msg in DB and return identifier
    msg_id = None
    return jsonify(msg_id)


@app.route('/api/msg/<integer:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    # TODO: get msg from DB and return it
    msg = None
    return msg


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
