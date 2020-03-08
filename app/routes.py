from flask.json import jsonify

from app import app
from flask import request
from app.form_utils import validate_form , get_age_group, reverse_name


@app.route('/api/personal_details', methods=['POST'])
def format_personal_details():

    result ={}
    if validate_form(request.form):
        print(request.form.data.get("age"))
        result['Group'] = get_age_group(request.form.data.get("age"))
        result['Name'] = reverse_name(request.form.data.get("name"))
    else:
        result = request.form.errors

    return jsonify(result), 200


