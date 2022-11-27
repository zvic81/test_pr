from flask import Flask, jsonify,request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'BEEERRRR, Cheese, Pizza, Fruit, Tylenol',
        'done': True
    },
    {
        'id': 2,
        'title': u'Learn Java',
        'description': u'learn java!!!',
        'done': True
    }
]
@app.route('/todo/api/v1.0/tasks', methods=['put'])
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=False)
