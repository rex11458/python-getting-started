from flask import Flask, abort, request, jsonify

app = Flask(__name__)

tasks = []


@app.route('/')
def hello_world():
    return 'Hello World'


@app.route('/user/<user_name>')
def get_user_name(user_name):
    return 'User %s' % user_name


@app.route('/add_task/', methods=['GET', 'POST'])
def add_task():
    if not request.json or 'id' not in request.json:
        abort(400)
    task = {'id': request.json['id'], 'info': request.json['info']}
    tasks.append(task)
    return jsonify({'result': 'success'})


@app.route('/get_task/', methods=['GET'])
def get_task():
    if not request.args or 'id' not in request.args:
        return jsonify(tasks)
    else:
        task_id = request.args['id']
        task = filter(lambda t: t['id'] == int(task_id), tasks)
        return jsonify(task) if task else jsonify({'result': 'not found'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
