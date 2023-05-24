from db.dbconn import connect_db

class AdminService:

    def login(self,email,passMd5):
        
        try:
            print(email)
            conn = connect_db()
            cursor = conn.cursor()
            sql = "SELECT id as user_id,name,created_at FROM user_details WHERE email = %s AND password = %s and is_admin = 1"
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
            
        
    def sign_up(self,name,email,passMd5):
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            sql = "insert into user_details (`name`, `email`, `password`) values (%s,%s,%s)"
            cursor.execute(sql, (name,email,passMd5))
            row = cursor
        except Exception as e:
            print(e)
            return None
        finally:
            conn.close()
            return row