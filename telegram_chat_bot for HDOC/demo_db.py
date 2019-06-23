import sqlite3


class DBHelper:
    def __init__(self, dbname="git_repos.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = "CREATE TABLE IF NOT EXISTS users (user text,fname text, username text, days int)"
        self.conn.execute(stmt)
        self.conn.commit()

    def add_user(self, user, fname, username):
        stmt = "INSERT INTO users (user, fname, username, days) VALUES (?,?,?,?)"
        args = (user, fname, username,0, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_user(self, user):
        stmt = "DELETE FROM users WHERE user = (?)"
        args = (user,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_username(self):
        stmt = "SELECT username FROM users"
        return [x[0] for x in self.conn.execute(stmt)]

    def get_users(self):
        stmt = "SELECT user FROM users"
        return [x[0] for x in self.conn.execute(stmt)]

    def get_fname(self, username):
        stmt = "SELECT fname FROM users WHERE username = (?)"
        args = (username,)
        val = self.conn.execute(stmt, args).fetchone()[0]
        return val

    def update_days(self, username,days):
        stmt = "UPDATE users SET days = (?) WHERE username = (?)"
        args = (days,username,)
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_days(self, username):
        stmt = "SELECT days FROM users WHERE username = (?)"
        args = (username,)
        return [x[0] for x in self.conn.execute(stmt,args)]
