import mysql.connector 
from common.config import MYSQL_CONFIG
from datetime import datetime

class Transactions:
    
    @staticmethod
    def insert_transactions_into_db(transactions):
        conn = mysql.connector.connect(**MYSQL_CONFIG)

        cursor = conn.cursor()
        try:
            for transaction in transactions:
                query = """
                INSERT INTO transactions (id, transaction_date, amount, transaction_type, user_id)
                VALUES (%s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                transaction_date = VALUES(transaction_date),
                amount = VALUES(amount),
                transaction_type = VALUES(transaction_type),
                user_id = VALUES(user_id)
                """
                values = (
                    transaction.id,
                    datetime.strptime(transaction.date, "%m/%d/%Y"),
                    transaction.amount,
                    transaction.type,
                    str(transaction.user_id)
                )
                cursor.execute(query, values)
        finally:
            conn.commit()
            cursor.close()
            conn.close()
