from flask import Blueprint, request, jsonify
from models.expense import Expense
from utils.database import get_db

expense_bp = Blueprint('expense', __name__)

@expense_bp.route('/expenses', methods=['POST'])
def add_expense():
    data = request.get_json()
    print(type(data))

    #check for the splits , if equal then empty , % or exact amount in other cases
    if not all(key in data for key in ('amount','payer', 'participants', 'split_type')):
        return jsonify({"error": "Missing required fields"}), 400
    
    #check split_type
    if data['split_type'] not in ['EQUAL', 'EXACT', 'PERCENTAGE']:
        return jsonify({"error": "Invalid split type"}), 400
    
    # Validate split details based on split_type
    if data['split_type'] == 'EXACT':
        if 'splits' not in data:return jsonify({'error':'no exact split found'}), 400

        if sum(data['splits']) != data['amount']:
            return jsonify({"error": "Sum of exact amounts does not match total"}), 400
    elif data['split_type'] == 'PERCENTAGE':
        if 'splits' not in data:return jsonify({'error':'no percentage split found'}), 400

        if sum(data['splits']) != 100:
            return jsonify({"error": "Sum of percentages must be 100"}), 400
    
        

    payer = data['payer']
    amount = data['amount']
    split_method = data['split_type']
    participants = data['participants']
    splits=[]
    if 'splits' in data:splits=data['splits']

    expense = Expense(payer, amount, split_method, participants,splits)
    expense.save()
    # #updating user document for total_paid
    # user_who_paid=get_db().users.find_one({'email':data['payer']})
    # get_db().users.update_one(
    #     {'email': payer},
    #     {'$set': {'total_paid': user_who_paid['total_paid']+amount}}
    # )


    return jsonify({'message': 'Expense added successfully'}), 201

@expense_bp.route('/expenses/<eid>', methods=['GET'])
def get_user_expenses(eid):
    db = get_db()
    expenses = db.expenses.find_one({'payer': eid})
    print(expenses)
    if expenses:
        expenses['_id'] = str(expenses['_id'])
        return jsonify(expenses), 200
    else:
        return jsonify({'message': 'User not found'}), 404
    
