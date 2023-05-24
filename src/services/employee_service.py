from db.dbconn import connect_db

class EmployeeService:

   

    def login(self,email,passMd5):
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = "SELECT id as user_id,name,created_at FROM user_details WHERE email = %s AND password = %s and is_admin = 0 "
            cursor.execute(sql, (email,passMd5))
            user = cursor.fetchone()
            conn.close()
            if user is not None:
                return user
            else:
                return None
        except Exception as e:
            print(e)
            return None
        
    def getUserEmail(self,email):
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = "SELECT id as user_id,name,created_at FROM user_details WHERE email = %s "
            cursor.execute(sql, (email))
            user = cursor.fetchone()
            conn.close()
            if user is not None:
                return user
            else:
                return None
        except Exception as e:
            print(e)
            return None
        
    def insertOtp(self,user_id,otp):
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = "insert into user_otp (`user_id`, `otp`) values (%s,%s)"
            
            cursor.execute(sql, (user_id,otp))
            return cursor
        except Exception as e:
            print(e)
            return None
            
    def checkOtp(self,user_id,otp):
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = "SELECT id as otp_id from  user_otp WHERE user_id = %s and otp =%s and isactive = 1 ORDER BY id DESC"
            cursor.execute(sql, (user_id,otp))
            user = cursor.fetchone()
            conn.close()
            if user is not None:
                return user
            else:
                return None
        except Exception as e:
            print(e)
            return None
        
    def updatePassword(self,user_id,passMd5,otp_id):
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            
            sql = "UPDATE `user_details` SET `password` = %s WHERE id = %s"
            cursor.execute(sql, (passMd5,user_id))

            sql = "UPDATE `user_otp` SET `isactive` = 0 WHERE id = %s"
            cursor.execute(sql, (otp_id))

            return cursor
        except Exception as e:
            print(e)
            return None
        
    def update_image(self,user_id,profile_img):
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            
            sql = "UPDATE `user_details` SET `profile_img` = %s WHERE id = %s"
            cursor.execute(sql, (profile_img,user_id))

            return cursor
        except Exception as e:
            print(e)
            return None