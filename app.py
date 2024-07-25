# from flask import Flask, request, jsonify
# from flask_sqlalchemy import SQLAlchemy
# import os

# app = Flask(__name__)

# # Configuring the PostgreSQL database
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# class Task(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(100), nullable=False)
#     description = db.Column(db.String(200), nullable=True)

# @app.route('/tasks', methods=['POST'])
# def add_task():
#     data = request.get_json()
#     new_task = Task(title=data['title'], description=data.get('description'))
#     db.session.add(new_task)
#     db.session.commit()
#     return jsonify({'message': 'Task created successfully'}), 201

# @app.route('/tasks', methods=['GET'])
# def get_tasks():
#     tasks = Task.query.all()
#     return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configuring the PostgreSQL database
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    new_task = Task(title=data['title'], description=data.get('description'))
    db.session.add(new_task)
    db.session.commit()
    return jsonify({'message': 'Task created successfully'}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{'id': task.id, 'title': task.title, 'description': task.description} for task in tasks])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

