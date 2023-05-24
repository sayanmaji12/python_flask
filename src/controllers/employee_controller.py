
from src.alllib import *
from src.services.employee_service import EmployeeService
from src.utility.mailTemplate import otp
from src.utility.mailSend import MailSending
import math, random
employee_service = EmployeeService()
# function to generate OTP
def generateOTP() :
 
    # Declare a digits variable 
    # which stores all digits
    digits = "0123456789"
    OTP = ""
 
   # length of password can be changed
   # by changing value in range
    for i in range(4) :
        OTP += digits[math.floor(random.random() * 10)]
 
    return OTP

class EmployeeController:
    
    def login(self,req):
        
        try:
            email = req['email']
            passKey = req['password']
            passMd5 = hashlib.md5(passKey.encode()).hexdigest()
            getUser = employee_service.login(email,passMd5)
            return getUser
        except Exception as e:
            print(e)
            return None
        
    def getUserEmail(self,req):
        
        try:
            email = req['email']
            getUser = employee_service.getUserEmail(email)
            
            if getUser is not None:
                genOtp = generateOTP()
                insertOtp = employee_service.insertOtp(getUser['user_id'],genOtp)
                print(insertOtp)
                msgTemplate = otp
                msgTemplate = msgTemplate.format(
                FIRST_NAME=getUser['name'],otp=genOtp)
                subject = 'Otp'
                mailObj = MailSending()
                mailObj.sendEmail(subject, email, msgTemplate)
                return {"otp":genOtp,"user_id":getUser['user_id']}
            else:
                return None
            
        except Exception as e:
            print(e)
            return None
        
    def updatePassword(self,req):
        
        try:
            user_id = req['user_id']
            otp = req['otp']
            password = req['password']
            passMd5 = hashlib.md5(password.encode()).hexdigest()
            checkOtp = employee_service.checkOtp(user_id,otp)
            if checkOtp is not None:
                getUser = employee_service.updatePassword(user_id,passMd5,checkOtp['otp_id'])
                return getUser
            else:
                return None
            
        except Exception as e:
            print(e)
            return None
    
    def update_image(self,req):
        
        try:
            user_id = req['user_id']
            profile_img = req['profile_img']
            update = employee_service.update_image(user_id,profile_img)
            if update is not None:
                
                return update
            else:
                return None
            
        except Exception as e:
            print(e)
            return None
        

        