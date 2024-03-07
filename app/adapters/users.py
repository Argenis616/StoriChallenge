import pandas as pd
import mysql.connector 
from entities.transaction_entity import Transaction
from common.config import MYSQL_CONFIG

class Users:
    
    @staticmethod
    def get_user_id_by_account(account):
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()

        try:
            query = "SELECT id FROM users WHERE account = %s"
            cursor.execute(query, (account,))
            result = cursor.fetchone()
            user_id = result[0] if result else None

            return user_id
        finally:
            cursor.close()
            conn.close()
    
    
    @staticmethod
    def get_email_by_user_id(user_id):
        conn = mysql.connector.connect(**MYSQL_CONFIG)
        cursor = conn.cursor()

        try:
            query = "SELECT email FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()
            email = result[0] if result else None

            return email
        finally:
            cursor.close()
            conn.close()