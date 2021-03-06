from flask import (
    Blueprint, request, jsonify
)
from .db import *

from flask_jwt_extended import jwt_required

banks = Blueprint('banks', __name__, url_prefix='/api')

@banks.route('/getBankDetails', methods=['GET'])
@jwt_required
def get_bank_details():
    ifsc = request.args.get('ifsc')
    query = "SELECT * FROM bank_branches WHERE ifsc='%s'"%(ifsc)
    try:
        res = select_query(query).fetchone()
        if res:
            res = {"result": dict(res)}
        else:
            res = {"result": "Please enter a valid IFSC"}
    except Exception as e:
        return str(e)
    return jsonify(res)

@banks.route('/getBranchDetails')
@jwt_required
def get_branch_details():
    bank_name = request.args['bank_name']
    city = request.args['city']
    limit = int(request.args['limit'])
    offset = int(request.args['offset'])
    query = "SELECT address, branch, district, ifsc, state  FROM bank_branches WHERE bank_name='%s' AND city='%s' LIMIT %d OFFSET %d"%(bank_name, city, limit, offset)
    try:
        res = select_query(query).fetchall()
        res = [dict(i) for i in res]
        if res:
            res = {"result": res}
        else:
            res = {"result": "No data found."}
    except Exception as e:
        return str(e)
    return jsonify(res)