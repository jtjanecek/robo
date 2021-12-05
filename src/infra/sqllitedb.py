import sqlite3
from sqlite3 import Error
import logging
import os
from hashlib import sha512

from datetime import datetime
from datetime import timedelta
import time
import pandas as pd
from utils import utils
logger = logging.getLogger('robo.sqllitedb')

class SqlLiteDb():
    def __init__(self, mode='rwc', db='database.db', db_loc=None):

        if db_loc == None:
            db_loc = os.path.dirname(os.path.abspath(__file__))
            db_loc = os.path.join(db_loc, "dbs")

        db_file = os.path.join(db_loc, db)
        db_file = "file:" + db_file + "?mode=" + mode
        logger.info("Using DB: {}".format(db_file))

        # This will raise an error if it can't connect
        self.conn = sqlite3.connect(db_file, uri=True, check_same_thread=False)

        self._cols = ['account_id', 'username', 'password', 'session_key']

        sql_create_user_tables = """CREATE TABLE IF NOT EXISTS users (
                                    account_id integer PRIMARY KEY,
                                    account_type integer NOT NULL,
                                    username text NOT NULL,
                                    password text NOT NULL,
                                    session_key text NOT NULL,
                                    stats text NOT NULL,
                                    ladderstatswide text NOT NULL
                                );
                                """

        sql_create_clans_table = """CREATE TABLE IF NOT EXISTS clans (
                                    clan_id integer PRIMARY KEY,
                                    clan_name text NOT NULL,
                                    leader_account_id integer NOT NULL,
                                    leader_account_name text NOT NULL,
                                    clan_status integer NOT NULL,
                                    clan_tag text NOT NULL,
                                    clan_msg text NOT NULL,
                                    stats text NOT NULL
                                );
                                """

        sql_create_clan_users_table = """CREATE TABLE IF NOT EXISTS clan_users (
                                    account_id integer PRIMARY KEY,
                                    clan_id text NOT NULL
                                );
                                """

        sql_create_clan_invites = """CREATE TABLE IF NOT EXISTS clan_invites (
                                    account_id integer PRIMARY KEY,
                                    clan_id text NOT NULL
                                );
                                """

        c = self.conn.cursor()
        if mode != 'ro':
            c.execute(sql_create_user_tables)
            c.execute(sql_create_clans_table)
            c.execute(sql_create_clan_users_table)

        sql = "CREATE UNIQUE INDEX IF NOT EXISTS sym_dt_idx ON users (account_id, session_key);"
        c.execute(sql)

        self.conn.commit()
        c.close()

        self._default_stats = '00C0A84400C0A84400C0A84400C0A8440000AF430000AF430000AF430000AF4300000000FFFFFFFFEF42000037FA0000EF000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        self._default_ladderstatswide = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        self._default_clantag = ''
        self._default_clan_status = 0
        self._default_clan_msg = ''
        self._default_clanstats = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

    def check_login(self, username: str, password: str, session_key: bytes) -> bool:
        account_id = self.get_account_id(username=username)

        if account_id != None: # user exists
            if self._password_match(account_id, password):
                # Update the session key in the db
                self._update_session_key(account_id, session_key)
                return True
            else: # Invalid password
                return False

        # New account login
        self._create_new_user(username, password, session_key)
        return True

    def get_account_id(self, username=None, session_key=None):
        c = self.conn.cursor()
        if username != None:
            select = """SELECT account_id
                        FROM users WHERE lower(username) = lower(?);
                    """
            vals = c.execute(select, [username]).fetchone()
        else:
            select = """SELECT account_id
                        FROM users WHERE session_key = ?;
                    """
            vals = c.execute(select, [session_key.decode()]).fetchone()
        c.close()

        # Check if it exists first
        if vals:
            return vals[0]
        return None

    def get_username(self, account_id=None, session_key=None):
        c = self.conn.cursor()
        if account_id != None:
            select = """SELECT username
                        FROM users WHERE account_id = ?;
                    """
            vals = c.execute(select, [account_id]).fetchone()
        else:
            select = """SELECT username
                        FROM users WHERE session_key = ?;
                    """
            vals = c.execute(select, [session_key.decode()]).fetchone()
        c.close()

        # Check if it exists first
        if vals:
            return vals[0]
        return ''

    def _create_new_user(self, username: str, encrypted_password: str, session_key: bytes):
        c = self.conn.cursor()
        insert_command = """INSERT INTO users
                            (account_type, username, password, session_key, stats, ladderstatswide)
                            values(?,?,?,?,?,?);
                            """
        account_type = 2
        stats = self._default_stats
        ladderstatswide = self._default_ladderstatswide
        c.execute(insert_command, [account_type, username, encrypted_password, session_key.decode(), stats, ladderstatswide])
        self.conn.commit()
        c.close()
        logger.info(f"Created new user: {username}")

    def _password_match(self, account_id, encrypted_password):
        c = self.conn.cursor()
        select = """SELECT password
                    FROM users WHERE account_id = ?;
                """
        vals = c.execute(select, [account_id]).fetchone()
        c.close()

        if vals:
            return vals[0] == encrypted_password
        raise Exception("Unable to find password for account id: " + str(account_id))


    def _update_session_key(self, account_id, session_key):
        c = self.conn.cursor()
        update = '''
            UPDATE users
            SET session_key = ?
            WHERE
                account_id = ?;
        '''
        c.execute(update, [session_key.decode(), account_id])
        self.conn.commit()
        c.close()


    def get_account_type(self, account_id: int):
        c = self.conn.cursor()
        select = """SELECT account_type
                    FROM users WHERE account_id = ?;
                """
        vals = c.execute(select, [account_id]).fetchone()
        c.close()
        if vals:
            return vals[0]
        return None

    def get_stats(self, account_id: int):
        c = self.conn.cursor()
        select = """SELECT stats
                    FROM users WHERE account_id = ?;
                """
        vals = c.execute(select, [account_id]).fetchone()
        c.close()
        if vals:
            return vals[0]
        return self._default_stats

    def update_stats(self, account_id, stats):
        c = self.conn.cursor()
        update = '''
            UPDATE users
            SET stats = ?
            WHERE
                account_id = ?;
        '''
        c.execute(update, [stats, account_id])
        self.conn.commit()
        c.close()

    def get_ladderstatswide(self, account_id: int):
        c = self.conn.cursor()
        select = """SELECT ladderstatswide
                    FROM users WHERE account_id = ?;
                """
        vals = c.execute(select, [account_id]).fetchone()
        c.close()
        if vals:
            return vals[0]
        return self._default_ladderstatswide

    def update_ladderstatswide(self, account_id, ladderstatswide):
        c = self.conn.cursor()
        update = '''
            UPDATE users
            SET ladderstatswide = ?
            WHERE
                account_id = ?;
        '''
        c.execute(update, [ladderstatswide, account_id])
        self.conn.commit()
        c.close()

    def create_clan(self, clan_name: bytes, leader_account_id: int, leader_account_name: str):
        # Ensure clan name is not taken
        clan_name = utils.bytes_to_hex(clan_name)
        clan_id = self.get_clan_id_from_name(clan_name)

        # Ensure clan doesn't exist
        if clan_id is not None:
            return None

        c = self.conn.cursor()
        insert_command = """INSERT INTO clans
                            (clan_name, leader_account_id, leader_account_name, clan_status, clan_tag, clan_msg, stats)
                            values(?,?,?,?,?,?,?);
                            """
        c.execute(insert_command, [clan_name, leader_account_id, leader_account_name, self._default_clan_status, self._default_clantag, self._default_clan_msg, self._default_clanstats])
        self.conn.commit()
        c.close()

        new_clan_id = self.get_clan_id_from_name(clan_name)
        logger.info(f"Created new clan: {clan_name} | clan_id: {new_clan_id}")

        # Add the leader to the clan
        self.add_user_to_clan(leader_account_id, new_clan_id)

        return new_clan_id

    def add_user_to_clan(self, account_id, clan_id):
        logger.info(f"Adding account_id: {account_id} to clan: {clan_id}")
        c = self.conn.cursor()
        insert_command = """INSERT INTO clan_users
                            (account_id, clan_id)
                            values(?,?);
                            """
        c.execute(insert_command, [account_id, clan_id])
        self.conn.commit()
        c.close()

    def get_clan_id_from_name(self, clan_name: str):
        # clan_name should be hex
        if type(clan_name) != str:
            raise Exception('Clan name is not str!')

        c = self.conn.cursor()
        select = """SELECT clan_id
                    FROM clans WHERE lower(clan_name) = lower(?);
                """
        vals = c.execute(select, [clan_name]).fetchone()
        c.close()

        # Check if it exists first
        if vals:
            return vals[0]
        return None

    def get_clan_id_from_account_id(self, account_id: int):
        c = self.conn.cursor()
        select = """SELECT clan_id
                    FROM clan_users WHERE account_id = ?;
                """
        vals = c.execute(select, [account_id]).fetchone()
        c.close()

        # Check if it exists first
        if vals:
            return vals[0]
        return None

    def update_clan_stats(self, clan_id: int, stats: str):
        c = self.conn.cursor()
        update = '''
             UPDATE clans
             SET stats = ?
             WHERE
                 clan_id = ?;
         '''
        c.execute(update, [stats, clan_id])
        self.conn.commit()
        c.close()

    def update_clan_message(self, clan_id: int, clan_message: str):
        c = self.conn.cursor()
        update = '''
             UPDATE clans
             SET clan_msg = ?
             WHERE
                 clan_id = ?;
         '''
        c.execute(update, [clan_message, clan_id])
        self.conn.commit()
        c.close()

    def get_clan_message(self, clan_id: int):
        c = self.conn.cursor()
        select = """SELECT clan_msg
                    FROM clans WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        c.close()

        # Check if it exists first
        if vals:
            return vals[0]
        return ''

    def get_clan_info(self, clan_id: int):
        '''
            clan_info['clan_id'], # Clan id
            10684, # app id
            clan_info['clan_name'],
            clan_info['leader_account_id'], # leader account id
            clan_info['leader_account_name'], # Leader account name
            clan_info['clan_stats'], # stats
            clan_info['clan_status'], # clan status
        '''

        c = self.conn.cursor()
        select = """SELECT clan_id, clan_name, leader_account_id, leader_account_name, stats, clan_status
                    FROM clans WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        c.close()

        clan_info = {
            'clan_id': vals[0],
            'clan_name': vals[1],
            'leader_account_id': vals[2],
            'leader_account_name': vals[3],
            'clan_stats': vals[4],
            'clan_status': vals[5]
        }
        return clan_info