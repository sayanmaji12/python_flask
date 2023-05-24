from src.alllib import *
from db.dbconn import connect_db
from src.controllers.employee_controller import EmployeeController
from werkzeug.utils import secure_filename
employee = Blueprint('employee', __name__)
controller = EmployeeController()
ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg'])

# Dictionary to store active tokens for each user
active_tokens = {}

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@employee.route('/login',methods=['POST'])
def login():
    resp = None
    
    try:
        
        _json = request.json
        
        if 'email' not in _json or 'password' not in _json:
            return jsonify({"success": False, "response": None, "message": "parameter missing"})
        # print( _json)
        getUser = controller.login(_json)
        if getUser is not None:
            if getUser['user_id'] in active_tokens:
                del active_tokens[getUser['user_id']]

            token = jwt.encode({'user_id': getUser['user_id'],"timestamp":time.time()}, os.getenv('SECRET_KEY'), algorithm='HS256')
            active_tokens[getUser['user_id']] = token.decode('utf-8')

            resp = jsonify({"success": True, "response": getUser,'token': token.decode('utf-8'), "message": ""})
        else:
            resp = jsonify({"success": False, "response": '', "message": "Your email or password is incorrect"})
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": "Some error occurred"})
    finally:
        return resp

@employee.route('/forgetPass',methods=['POST'])
def forgetPass():
    resp = None
    
    try:
        
        _json = request.json
        
        if 'email' not in _json:
            return jsonify({"success": False, "response": None, "message": "parameter missing"})
        # print( _json)
        getUser = controller.getUserEmail(_json)
        if getUser is not None:
            resp = jsonify({"success": True, "response": getUser, "message": "Otp sent successfully"})
        else:
            resp = jsonify({"success": False, "response": '', "message": "Email not found"})
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": "Some error occurred"})
    finally:
        return resp
    
@employee.route('/resetPassword',methods=['POST'])
def resetPassword():
    resp = None
    
    try:
        _json = request.json
        
        if 'user_id' not in _json or 'otp' not in _json or 'password' not in _json:
            return jsonify({"success": False, "response": None, "message": "parameter missing"})
        # print( _json)
        getUser = controller.updatePassword(_json)
        if getUser is not None:
            resp = jsonify({"success": True, "response": '', "message": "Reset password successfully"})
        else:
            resp = jsonify({"success": False, "response": '', "message": "Invalid Otp"})
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": "Some error occurred"})
    finally:
        return resp
    
@employee.route('/upload', methods=['POST'])
def upload_file():
    try:
        __location__ = os.path.realpath(os.path.join(os.getcwd()))
        token = request.headers.get('Authorization')
        if token:
            print(__location__)
            token = token.split()[1]
            # Decode the token and verify its authenticity
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithm='HS256')
            
            user_id = payload['user_id']

            # Check if the token is the latest active token for the user
            if user_id in active_tokens and active_tokens[user_id] == token:
                if 'file' in request.files:
                    file = request.files['file']
                    print(file.filename)
                    if file and allowed_file(file.filename):
                        filename = secure_filename(file.filename)
                        extension = os.path.splitext(filename)[1]
                        gmt = time.gmtime()
                        ts = calendar.timegm(gmt)
                        # Save the file to a specific location or process it as needed
                        file.save(__location__+'/public/'+str(ts)+extension)
                        resp = jsonify({"success": False, "response": str(ts)+extension, "message": "File uploaded successfully!"})
                    else:
                        resp = jsonify({"success": False, "response": '', "message": "Please upload image file"})
                else:     
                    resp = jsonify({"success": False, "response": '', "message": "No file found in the request."})
            else:
                    resp = jsonify({'message': 'Invalid token',"success": False})
        else:
            resp = jsonify({'message': 'Token missing',"success": False})
    except Exception as e:
        print(e)
        resp = jsonify({"success": False, "message": "Some error occurred"})
    finally:
        return resp
    
@employee.route('/update_image',methods=['POST'])
def update_image():
    resp = None
    token = request.headers.get('Authorization')
    if token:
        try:
            token = token.split()[1]
            # Decode the token and verify its authenticity
            payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithm='HS256')
            
            user_id = payload['user_id']

            _json = request.json
            # Check if the token is the latest active token for the user
            if user_id in active_tokens and active_tokens[user_id] == token:

                
                if 'user_id' not in _json or 'profile_img' not in _json :
                    return jsonify({"success": False, "response": None, "message": "parameter missing"})
                
                update = controller.update_image(_json)
            
                return  jsonify({"success": True, "response": "Image updated successfully", "message": ""})
            else:
                return  jsonify({'message': 'Invalid token',"success": False})
        except Exception as e:
            print(e)
            return jsonify({"success": False, "message": "Some error occurred"})
    else:
        return jsonify({'message': 'Token missing',"success": False})