
from src.alllib import *
from src.services.admin_service import AdminService
from src.utility.mailTemplate import welcome
from src.utility.mailSend import MailSending

admin_service = AdminService()

class AdminController:

    def login(self,req):
        
        try:
            print(req)
            email = req['email']
            passKey = req['password']
            passMd5 = hashlib.md5(passKey.encode()).hexdigest()
            
            getUser = admin_service.login(email,passMd5)
            return getUser
        except Exception as e:
            print(e)
            return None
        
    def sign_up(self,req):
        
        try:
            name = req['name']
            email = req['email']
            password = req['password']
            passMd5 = hashlib.md5(password.encode()).hexdigest()
            sign_up = admin_service.sign_up(name,email,passMd5)
            msgTemplate = welcome
            msgTemplate = msgTemplate.format(
            FIRST_NAME=req['name'])
            subject = 'Welcome'
            mailObj = MailSending()
            mailObj.sendEmail(subject, req['email'], msgTemplate)
            return sign_up
        except Exception as e:
            print(e)
            return None
        