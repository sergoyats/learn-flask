from flask import Flask, jsonify, request


app = Flask(__name__)  

storage = dict()
storage.update(
    {
        "username1": {},
        "username2": {},
        "username3": {},
        "username4": {}
    }
)


@app.route('/')
def hello_world():
    return jsonify({'msg': 'Hello, World!'})


@app.route('/users/list/')
def user_list():
    return jsonify(storage)


@app.route('/users/delete/<username>')
def delete_user(username):
    old_users = storage.copy()
    storage.pop(username, False)
    if username in old_users:
        return 'User  was deleted'
    else:
        return 'User doesn\'t exist or already deleted'


@app.route('/users/add/', methods=["POST"])
def add_user_list():
    data = request.get_json()
    try:
        username = data['username']
    except Exception as e:
        response = {'msg': f'The field {e} is required'}
        username = False

    if username:
        storage[username] = dict()
        response = {'msg': 'User was added'}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
