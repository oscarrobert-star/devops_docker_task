import os
from flask import Flask, jsonify, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_migrate import Migrate

from dotenv import load_dotenv

load_dotenv(".env")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL")

CORS(app)
db = SQLAlchemy(app)

migrate = Migrate(app, db)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return '<Task %r>' % self.id


@app.route('/')
def is_alive():
    return jsonify('live')


@app.route('/api/msg/<string:msg>', methods=['POST'])
def msg_post_api(msg):
    print(f"msg_post_api with message: {msg}")

    # TODO: store msg in DB and return identifier
    msg_content = request.get_json()
    msg_text = msg_content.get('message')
    new_msg = Todo(content=msg_text)

    db.session.add(new_msg)
    db.session.commit()

    msg_id = new_msg.id
    return jsonify({'msg_id': msg_id})


@app.route('/api/msg/<int:msg_id>', methods=['GET'])
def msg_get_api(msg_id):
    print(f"msg_get_api > msg_id = {msg_id}")

    item = Todo.query.get(msg_id)
    return jsonify({'msg': item.content})


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1")
