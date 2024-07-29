from flask import Blueprint, request, jsonify
from models.user import User
from utils.database import get_db

user_bp = Blueprint('user', __name__)

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    #check for all the credentials
    not_present=[]
    for ele in ['email','name','mobile_number']:
        if ele not in data:not_present.append(ele)
    
    if len(not_present)==0:
        #check if person with same email already exists
        existing_user = get_db().users.find_one({'email': data['email']})
        if existing_user:
            return jsonify({"error": "User with this email already exists"}), 409

        user = User(data['email'], data['name'], data['mobile_number'])
        user.save()
        return jsonify({'message': 'User created successfully'}), 201
    else:
        return jsonify({f"error": "Missing required {list(ele for ele in not_present)} fields"}), 400
    


@user_bp.route('/users/<email>', methods=['GET'])
def get_user(email):
    db = get_db()
    user = db.users.find_one({'email': email})
    if user:
        user['_id'] = str(user['_id'])
        return jsonify(user), 200
    else:
        return jsonify({'message': 'User not found'}), 404
