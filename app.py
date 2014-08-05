from flask import Flask, request, jsonify


app = Flask(__name__)


rules = {}


@app.route('/rules.json', methods=['GET'])
def get_rules():
    current_rules = [each for each in rules.values()]
    return jsonify({'rules': current_rules})


@app.route('/rules.json', methods=['POST'])
def add_rule():
    errors = []
    status = 200
    for rule in request.get_json()['rules']:
        value = rule['value']
        tag = rule['tag']
        if value in rules:
            msg = 'rule "{}" is already present'.format(value)
            errors.append(msg)
            status = 422
            continue
        rules[value] = rule
    return jsonify({'errors': errors}), status


@app.route('/rules.json', methods=['PATCH'])
def update_rule():
    errors = []
    status = 200
    for rule in request.get_json()['rules']:
        value = rule['value']
        tag = rule['tag']
        if value not in rules:
            msg = 'rule "{}" is not present'.format(value)
            errors.append(msg)
            status = 422
            continue
        rules[value] = tag
    return jsonify({'errors': errors}), status

if __name__ == '__main__':
    app.debug = True
    app.run()