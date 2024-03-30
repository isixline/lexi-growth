from lexi_auth.core.user import User
import csv

db_path = 'db/user.csv'
fields = ['id', 'username', 'encoded_password']

def save_user(user: User):
    with open(db_path, mode='a') as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writerow({"id": user.id, "username": user.username, "encoded_password": user.encoded_password})   

def update_user(user: User):
    pass

def find_user_by_id(id):
    pass