import pandas as pd
from entities.transaction_entity import Transaction
import mysql.connector 
import boto3
from common.config import MYSQL_CONFIG

class FileProcessor:
    
    @staticmethod
    def get_s3_file(filename):
        s3 = boto3.client('s3')
        file = s3.get_object(Bucket='stori-challege-argenis', Key=f"{filename}.csv")
        return file['Body']
        
    @staticmethod
    def read_csv(filename):
        try:
            file = FileProcessor.get_s3_file(filename)
            df = pd.read_csv(file)
        except Exception as e:
            print(str(e))
            raise e
        transactions = []

        for _, row in df.iterrows():
            transaction = row.to_dict()
            transactions.append(transaction)
        return transactions
    
    @staticmethod
    def insert_transactions_into_db(transactions):
        conn = mysql.connector.connect(**MYSQL_CONFIG)

        cursor = conn.cursor()

        for transaction in transactions:
            query = """
            INSERT INTO transactions (id, date, amount, type, user_id)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE
            date = VALUES(date),
            amount = VALUES(amount),
            type = VALUES(type),
            user_id = VALUES(user_id)
            """
            values = (
                transaction.id,
                transaction.date,
                transaction.amount,
                transaction.type,
                transaction.user_id
            )
            cursor.execute(query, values)

        conn.commit()
        cursor.close()
        conn.close()
