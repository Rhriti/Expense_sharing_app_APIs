from flask import Blueprint, jsonify, make_response, request
from io import StringIO
import csv
from utils.database import get_db

bp = Blueprint('balance_sheet', __name__)

@bp.route('/balance_sheet', methods=['GET'])
def get_balance_sheet():
    param = request.args.get('payer')
    expense = get_db().expenses.find_one({"payer": param})
    print(expense)
    balances = {}
    

    payer = expense['payer']
    amount = expense['amount']
    participants = expense['participants']
    split_type = expense['split_type']
    splits = expense.get('splits', [])
    
    if split_type == 'EQUAL':
        share = amount // len(participants)
        for participant in participants:
            balances[participant]=share

    elif split_type == 'EXACT':
        for participant, share in zip(participants, splits):
            balances[participant]=share

    elif split_type == 'PERCENTAGE':
        for participant, percentage in zip(participants, splits):
            share = amount * (percentage // 100)
            balances[participant]=share
            

    return jsonify(balances)

@bp.route('/balance_sheet_download', methods=['GET'])
def download_balance_sheet():
    balances = get_balance_sheet().json
    print(balances)
    si = StringIO()
    cw = csv.writer(si)
    cw.writerow(['User', 'Balance'])
    for user, balance in balances.items():
        cw.writerow([user, balance])
    
    output = make_response(si.getvalue())
    output.headers["Content-Disposition"] = "attachment; filename=balance_sheet.csv"
    output.headers["Content-type"] = "text/csv"
    return output