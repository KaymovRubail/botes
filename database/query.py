CREATE_USER_TABLE = '''
CREATE TABLE IF NOT EXISTS telegram_users(
id INTEGER PRIMARY KEY,
telegram_user_id INTEGER,
username CHAR(20) ,
first_name CHAR(20),
last_name CHAR(20),
UNIQUE(telegram_user_id)
)
'''
INSERT_USER_TABLE = '''
INSERT OR IGNORE INTO telegram_users  VALUES (?,?, ?, ?, ?)
'''

CREATE_ANSWER_TABLE = '''
CREATE TABLE IF NOT EXISTS answers(
id INTEGER PRIMARY KEY,
telegram_user_id INTEGER,
transport_type CHAR(20) ,
model CHAR(20),
experience CHAR(20),
UNIQUE(telegram_user_id)
)
'''
INSERT_ANSWER_TABLE = '''
INSERT OR IGNORE INTO telegram_users  VALUES (?,?, ?, ?, ?)
'''