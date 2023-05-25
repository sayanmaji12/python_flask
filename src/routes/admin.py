from src.alllib import *
from db.dbconn import connect_db
from src.controllers.admin_controller import AdminController

admin = Blueprint('admin', __name__)
controller = AdminController()

# Dictionary to store active tokens for each user
active_tokens = {}

@admin.route('/login',methods=['POST'])
def login():
    resp = None
    
    try:
        
        _json = request.json
        print(_json)
        if 'email' not in _json or 'password' not in _json:
            return jsonify({"success": False, "response": None, "message": "parameter missing"})
        # print( _json)
        getUser = controller.login(_json)
        if getUser is not None:
            if getUser['user_id'] in active_tokens:
                del active_tokens[getUser['user_id']]

            token = jwt.encode({'user_id': getUser['user_id'],"timestamp":time.time()}, os.getenv('SECRET_KEY'), algorithm='HS256')
            print(token)
            active_tokens[getUser['user_id']] = token

            return jsonify({"success": True, "response": getUser,'token': token, "message": ""})
        else:
            return jsonify({"success": False, "response": '', "message": "Your email or password is incorrect"})
    except Exception as e:
        print(e)
        return jsonify({"success": False, "message": "Some error occurred"})
    
@admin.route('/sign_up',methods=['POST'])
def sign_up():
    resp = None
    token = request.headers.get('Authorization')
    if token:
        try:
            token = token.split()[1]
            print(token)
            # Decode the token and verify its authenticity
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms='HS256')
            
            user_id = payload['user_id']

            _json = request.json
            # Check if the token is the latest active token for the user
            if user_id in active_tokens and active_tokens[user_id] == token:

                
                if 'name' not in _json or 'email' not in _json or 'password' not in _json:
                    return jsonify({"success": False, "response": None, "message": "parameter missing"})
                
                getUser = controller.sign_up(_json)
            
                return  jsonify({"success": True, "response": "User registered successfully", "message": ""})
            else:
                return  jsonify({'message': 'Invalid token',"success": False})
        except Exception as e:
            print(e)
            return jsonify({"success": False, "message": "Some error occurred"})
    else:
        return jsonify({'message': 'Token missing',"success": False})
    
  

