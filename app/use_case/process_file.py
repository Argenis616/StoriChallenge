from common.notification_service.templates import EmailTemplate
from adapters.file_processor import FileProcessor
from adapters.users import Users
from adapters.transactions import Transactions
from entities.transaction_entity import Transaction
from common.notification_service.notifications import Notifications

class ProcessFileUseCase:
    def __init__(self, filename, account):
        self.filename = filename
        self.account = account

    def execute(self):
        try:
            csv_file = FileProcessor.read_csv(self.filename)
            user_id = Users.get_user_id_by_account(self.account)
        except Exception as e:
            print(str(e))
            raise e

        transactions = []
        for row in csv_file:
            amount = float(row['Amount'])
            transaction_type = 'debit' if amount < 0 else 'credit'
            transaction = Transaction(
                date=row['Date'] + '/2024',
                amount=amount,
                type=transaction_type,
                user_id=user_id
            )

            transactions.append(transaction)
        try:
            email = Users.get_email_by_user_id(user_id)
            self._send_summary_email(transactions, email)
            Transactions.insert_transactions_into_db(transactions)
        except Exception as e:
            raise e

        return transactions
    

    def _send_summary_email(self, transactions, email):
        balance = sum([transaction.amount for transaction in transactions])
        debit_transactions = [transaction.amount for transaction in transactions if transaction.type == 'debit']
        credit_transactions = [transaction.amount for transaction in transactions if transaction.type == 'credit']
        debit_average = sum(debit_transactions) / len(debit_transactions)
        credit_average = sum(credit_transactions) / len(credit_transactions)
        months = {1:"January", 2:"February", 3:"March", 4:"April", 5:"May", 6:"June", 7:"July", 8:"August", 9:"September", 10:"October", 11:"November", 12:"December"}
        transactions_by_month = {}
        for transaction in transactions:
            month = int(transaction.date.split('/')[0])
            transactions_by_month[months[month]] = transactions_by_month.get(months[month], 0) + 1
        
        email_months_content = ""
        for month, count in transactions_by_month.items():
            email_months_content += f"<p>Number of transactions in {month}: {count}</p>"
            
        email_data = {
            "balance": balance,
            "debit_average": debit_average,
            "credit_average": credit_average,
            "transactions_by_month": email_months_content
        }
        email_metadata = {
            "subject": "Summary of your transactions",
            "to": email,
        }
        try:
            Notifications.send_email(EmailTemplate.SUMMARY_EMAIL,email_data, email_metadata)
        except Exception as e:
            raise e
        
                
        
        
    

