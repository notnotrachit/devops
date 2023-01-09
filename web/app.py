from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rachit:rachit@database:5432/flask_api'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class task(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    task = db.Column(db.String(255))
    priority = db.Column(db.String(255))

    def __repr__(self):
        return '<Task %r>' % self.task


@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = db.session.query(task).all()
    return render_template('tasks.html', tasks=tasks)

@app.route('/tasks_n', methods=['POST'])
def add_task():
    task_c = task(task=request.form['name'], priority=request.form['priority'])
    db.session.add(task_c)
    db.session.commit()
    return redirect('tasks')

@app.route('/tasks/new', methods=['GET'])
def add_create_task():
    return render_template('add_task.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)