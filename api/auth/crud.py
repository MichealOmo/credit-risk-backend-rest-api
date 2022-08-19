from api.utils.dbUtil import database
# from api.auth import schema
from auth import schema
from utils.dbUtil import database

def find_user_exists(email: str):
    query = "SELECT * FROM my_users WHERE status='1' AND email=:email"
    return database.fetch_one(query, values = {"email": email})

def save_user(user: schema.UserCreate):
    query = "INSERT INTO my_users VALUES (nextval('user_id_seq'), :email, :password, :fullname, now() at time zone 'UTC', '1')"
    return database.execute(query, values={"email": user.email, "password": user.password, "fullname": user.fullname})

def create_reset_code(email: str, reset_code: str):
    query = "INSERT INTO my_codes VALUES (nextval('codes_id_seq'), :email, :reset_code, '1', now() at time zone 'UTC')"
    return database.execute(query, values={"email": email, "reset_code": reset_code})

def check_reset_password_token(token: str):
    query = "SELECT * FROM my_codes WHERE status='1' AND reset_code=:token AND expired_in>=now() at time zone 'UTC' - interval '10 minutes'"
    return database.fetch_one(query, values={"token":token})

def reset_password(new_password: str, email: str):
    query = "UPDATE my_users SET password=:password WHERE email=:email"
    return database.execute(query=query, values={"password": new_password, "email": email})

def disable_reset_code(reset_password_token: str, email: str):
    query = "UPDATE my_codes SET status='9' WHERE status='1' AND reset_code=:reset_password_token and email=:email"
    return database.execute(query, values={"reset_code": reset_password_token, "email": email})