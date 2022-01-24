import sqlite3
from sqlite3 import Error
import logging
import os
from hashlib import sha512
from datetime import datetime
from datetime import timedelta
import time
import pandas as pd
from copy import deepcopy

import bcrypt

from utils import utils
logger = logging.getLogger('robo.sqllitedb')

class SqlLiteDb():
    def __init__(self, mode='rwc', db='database.db', db_loc=None, salt=''):

        if db_loc == None:
            db_loc = os.path.dirname(os.path.abspath(__file__))
            db_loc = os.path.join(db_loc, "dbs")

        db_file = os.path.join(db_loc, db)
        db_file = "file:" + db_file + "?mode=" + mode
        logger.info("Using DB: {}".format(db_file))
        self._db_loc = db_loc
        self._db = db

        self._salt = salt

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
                                    stats text NOT NULL,
                                    statswide text NOT NULL
                                );
                                """

        sql_create_clan_users_table = """CREATE TABLE IF NOT EXISTS clan_users (
                                    account_id integer PRIMARY KEY,
                                    clan_id text NOT NULL
                                );
                                """

        sql_create_clan_invites = """CREATE TABLE IF NOT EXISTS clan_invites (
                                    clan_invitation_id integer PRIMARY KEY,
                                    account_id_invited integer NOT NULL,
                                    clan_id integer NOT NULL,
                                    invite_message text NOT NULL,
                                    response_msg text NOT NULL
                                );
                                """

        sql_create_buddies = """CREATE TABLE IF NOT EXISTS buddies (
                                    id integer PRIMARY KEY,
                                    account_id integer NOT NULL,
                                    buddy_id integer NOT NULL
                                );
                                """

        sql_create_alts = """CREATE TABLE IF NOT EXISTS alts (
                                    id integer PRIMARY KEY,
                                    username text NOT NULL,
                                    hash text NOT NULL
                                );
                                """
        c = self.conn.cursor()
        if mode != 'ro':
            c.execute(sql_create_user_tables)
            c.execute(sql_create_clans_table)
            c.execute(sql_create_clan_users_table)
            c.execute(sql_create_clan_invites)
            c.execute(sql_create_buddies)
            c.execute(sql_create_alts)


        sql = "CREATE UNIQUE INDEX IF NOT EXISTS sym_dt_idx ON users (account_id, session_key);"
        c.execute(sql)



        self.conn.commit()
        c.close()

        self._default_stats = '00C0A84400C0A84400C0A84400C0A8440000AF430000AF430000AF430000AF430000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        self._default_ladderstatswide = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

        self._default_clantag = ''
        self._default_clan_status = 0
        self._default_clan_msg = ''
        self._default_clanstats = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'
        self._default_clanstatswide = '00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'

    def dump_stats(self) -> list:
        logger.info("Updating leaderboards ...")
        start_time = time.time()

        c = self.conn.cursor()
        select = """SELECT account_id, username, stats, ladderstatswide
                    FROM users;
                """
        vals = c.execute(select).fetchall()
        c.close()
        if vals == []:
            logger.warning("No accounts found! Leaderboards disabled")
            return None, None

        accounts = []
        for raw_account in vals:
            ladder_stats_wide = raw_account[3]
            account = {
                'account_id': raw_account[0],
                'username': raw_account[1],
                'stats': raw_account[2],
                'ladder_stats_wide': []
            }
            ladder_stats_split = [ladder_stats_wide[i:i+8] for i in range(0,len(ladder_stats_wide),8)]
            for ladder_stat in ladder_stats_split:
                # Convert to integer
                if ladder_stat == 'FFFFFFFF':
                    account['ladder_stats_wide'].append(-1)
                else:
                    account['ladder_stats_wide'].append(utils.bytes_to_int_little(utils.hex_to_bytes(ladder_stat)))
            accounts.append(account)

        #
        final_account_map = {}

        for ladder_stat_idx in range(100):
            ac = sorted(accounts, key=lambda x: x['ladder_stats_wide'][ladder_stat_idx], reverse=True)
            final_account_map[ladder_stat_idx] = deepcopy(ac)

        # Now do clans...
        c = self.conn.cursor()
        select = """SELECT clan_id, clan_name, stats
                    FROM clans;
                """
        vals = c.execute(select).fetchall()
        c.close()

        if vals != []:
            clans = []
            for raw_clan in vals:
                clans_stats = raw_clan[2]
                clan = {
                    'clan_id': raw_clan[0],
                    'clan_name': raw_clan[1],
                    'stats': []
                }
                ladder_stats_split = [clans_stats[i:i+8] for i in range(0,len(clans_stats),8)]
                for ladder_stat in ladder_stats_split:
                    # Convert to integer
                    if ladder_stat == 'FFFFFFFF':
                        clan['stats'].append(-1)
                    else:
                        clan['stats'].append(utils.bytes_to_int_little(utils.hex_to_bytes(ladder_stat)))
                clans.append(clan)

            final_clan_map = {}
            for ladder_stat_idx in range(20):
                ac = sorted(clans, key=lambda x: x['stats'][ladder_stat_idx], reverse=True)
                final_clan_map[ladder_stat_idx] = deepcopy(ac)
        else:
            final_clan_map = {}
            logger.warning("No clans found! Clan leaderboards disabled")

        end_time = time.time()
        total_time = (end_time - start_time)

        #logger.info(final_account_map)
        logger.info(f"Leaderboards updated! Took {total_time} seconds!")
        return final_account_map, final_clan_map


    def register_ip(self, username, ip):
        c = self.conn.cursor()
        select = """SELECT username
                    FROM alts WHERE username = ? and hash = ?;
                """
        hash = bcrypt.hashpw(ip.encode(), self._salt.encode()).decode()
        vals = c.execute(select, [username, hash]).fetchone()
        c.close()
        if vals: # This already exists in the db
            return
        # Insert new row
        c = self.conn.cursor()
        insert_command = """INSERT INTO alts
                            (username, hash)
                            values(?,?);
                            """
        hash = bcrypt.hashpw(ip.encode(), self._salt.encode()).decode()
        c.execute(insert_command, [username, hash])
        self.conn.commit()
        c.close()

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

    def get_all_user_info_from_account_id(self, account_id: int):
        c = self.conn.cursor()
        select = """SELECT account_id, account_type, username, stats, ladderstatswide
                    FROM users WHERE account_id = ?;
                """
        vals = c.execute(select, [account_id]).fetchone()
        c.close()

        if not vals: # No result
            return {}
        return {
            'account_id': vals[0],
            'account_type': vals[1],
            'username': vals[2],
            'stats': vals[3],
            'ladderstatswide': vals[4]
        }

    def get_all_user_info_from_username(self, username: str):
        c = self.conn.cursor()
        select = """SELECT account_id, account_type, username, stats, ladderstatswide
                    FROM users WHERE lower(username) = lower(?);
                """
        vals = c.execute(select, [username]).fetchone()
        c.close()

        if not vals: # No result
            return {}
        return {
            'account_id': vals[0],
            'account_type': vals[1],
            'username': vals[2],
            'stats': vals[3],
            'ladderstatswide': vals[4]
        }

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
            if vals[0] == '':
                self._update_password(account_id, encrypted_password)
                return True
            return vals[0] == encrypted_password
        raise Exception("Unable to find password for account id: " + str(account_id))

    def _update_password(self, account_id, encrypted_password):
        c = self.conn.cursor()
        update = '''
            UPDATE users
            SET password = ?
            WHERE
                account_id = ?;
        '''
        c.execute(update, [encrypted_password, account_id])
        self.conn.commit()
        c.close()

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
        # First get the players stats
        current_stats = self.get_stats(account_id)
        current_stats = [current_stats[i:i+8] for i in range(0,len(current_stats),8)]

        stats = [stats[i:i+8] for i in range(0,len(stats),8)]

        new_stats = ''
        warn = False
        for i in range(len(stats)):
            if i < 8:
<<<<<<< HEAD
                if stats[i] in ['00C0A844', '0000AF43', '00000000']:
=======
                if stats[i] in ['00C0A844', '0000AF43']:
>>>>>>> 4fba27588eb94b95af1b12e3b22bca7d583b5c29
                    # Ignore. Use current stats
                    warn = True
                    new_stats += current_stats[i]
                else:
                    new_stats += stats[i]
            else:
                # Use new
                new_stats += stats[i]

        if warn:
<<<<<<< HEAD
            logger.warning(f"Using current stats: {current_stats} | {stats} | {new_stats}")
=======
            logger.warning(f"Using current stats: {current_stats} | {stats}")
>>>>>>> 4fba27588eb94b95af1b12e3b22bca7d583b5c29

        stats = new_stats

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

    def create_clan(self, clan_name: str, leader_account_id: int, leader_account_name: str):
        clan_id = self.get_clan_id_from_name(clan_name)

        # Ensure clan doesn't exist
        if clan_id is not None:
            return None

        c = self.conn.cursor()
        insert_command = """INSERT INTO clans
                            (clan_name, leader_account_id, leader_account_name, clan_status, clan_tag, clan_msg, stats, statswide)
                            values(?,?,?,?,?,?,?,?);
                            """
        c.execute(insert_command, [clan_name, leader_account_id, leader_account_name,
                                   self._default_clan_status, self._default_clantag,
                                   self._default_clan_msg, self._default_clanstats,
                                   self._default_clanstatswide])
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

    def update_clan_statswide(self, clan_id, statswide: str):
        # it should be hex already
        # clan_name should be hex
        if type(statswide) != str:
            raise Exception('Clan name is not str!')
        c = self.conn.cursor()
        update = '''
             UPDATE clans
             SET statswide = ?
             WHERE
                 clan_id = ?;
         '''
        c.execute(update, [statswide, clan_id])
        self.conn.commit()
        c.close()

    def get_clan_statswide(self, clan_id: int):
        c = self.conn.cursor()
        select = """SELECT statswide
                    FROM clans WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        c.close()
        if vals:
            return vals[0]
        return self._default_clanstatswide

    def get_clan_name(self, clan_id: int):
        c = self.conn.cursor()
        select = """SELECT clan_name
                    FROM clans WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        c.close()
        if vals:
            return vals[0]
        return ''

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
        c = self.conn.cursor()
        select = """SELECT clan_id, clan_name, leader_account_id, leader_account_name, stats, clan_status, statswide
                    FROM clans WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        c.close()

        if not vals:
            return {}
        clan_info = {
            'clan_id': vals[0],
            'clan_name': vals[1],
            'leader_account_id': vals[2],
            'leader_account_name': vals[3],
            'clan_stats': vals[4],
            'clan_status': vals[5],
            'clan_statswide': vals[6]
        }
        return clan_info

    def get_clan_info_from_name(self, clan_name: str):
        clan_id = self.get_clan_id_from_name(clan_name)
        return self.get_clan_info(clan_id)

    def get_clan_leader_account_id(self, clan_id):
        c = self.conn.cursor()
        select = """SELECT leader_account_id
                    FROM clans WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        c.close()

        # Check if it exists first
        if vals:
            return vals[0]
        return 0

    def disband_clan(self, clan_id: int):
        # Delete the clan
        c = self.conn.cursor()
        select = """DELETE
                    FROM clans WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        self.conn.commit()
        c.close()

        # Delete the clan users
        c = self.conn.cursor()
        select = """DELETE
                    FROM clan_users WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        self.conn.commit()
        c.close()

        # Delete the clan invitations
        c = self.conn.cursor()
        select = """DELETE
                    FROM clan_invites WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchone()
        self.conn.commit()
        c.close()

    def remove_player_from_clan(self, account_id: int, clan_id: int):
        # Delete the clan invitations
        c = self.conn.cursor()
        select = """DELETE
                    FROM clan_users WHERE account_id = ? and clan_id = ?;
                """
        vals = c.execute(select, [account_id, clan_id]).fetchone()
        self.conn.commit()
        c.close()

    def transfer_clan_ownership(self, clan_id: int, new_account_id: int, new_account_name: str):
        c = self.conn.cursor()
        update = '''
             UPDATE clans
             SET leader_account_id = ?
             WHERE
                 clan_id = ?;
         '''
        c.execute(update, [new_account_id, clan_id])
        self.conn.commit()
        c.close()

        c = self.conn.cursor()
        update = '''
             UPDATE clans
             SET leader_account_name = ?
             WHERE
                 clan_id = ?;
         '''
        c.execute(update, [new_account_name, clan_id])
        self.conn.commit()
        c.close()

    def get_clan_member_account_ids(self, clan_id):
        c = self.conn.cursor()
        select = """SELECT account_id
                    FROM clan_users WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchall()
        c.close()

        account_ids = [val[0] for val in vals]
        return account_ids

    def get_clan_invitations_sent(self, clan_id):
        c = self.conn.cursor()
        select = """SELECT account_id_invited
                    FROM clan_invites WHERE clan_id = ?;
                """
        vals = c.execute(select, [clan_id]).fetchall()
        c.close()
        logger.info(vals)
        accounts = []
        for val in vals:
            accounts.append({
                'account_id': val[0],
                'response_msg': '',
                'response_status': 0,
                'response_time': 0
            })
        return accounts

    def check_invite_exists(self, account_id, clan_id):
        c = self.conn.cursor()
        select = """SELECT account_id_invited
                    FROM clan_invites WHERE account_id_invited = ? and clan_id = ?;
                """
        vals = c.execute(select, [account_id, clan_id]).fetchone()
        c.close()

        # Check if it exists first
        if vals == [] or vals == None:
            return False
        return True

    def invite_player_to_clan(self, account_id, clan_id, invite_message):
        c = self.conn.cursor()

        # first ensure this combo is not already in the db
        if self.check_invite_exists(account_id, clan_id):
            logger.info(f"Player already invited!")
            c.close()
            return

        insert_command = """INSERT INTO clan_invites
                            (account_id_invited, clan_id,
                            invite_message, response_msg)
                            values(?,?,?,?);
                            """
        c.execute(insert_command, [account_id, clan_id, invite_message, ''])
        self.conn.commit()
        c.close()

    def get_clan_invitations(self, account_id):
        c = self.conn.cursor()
        select = """SELECT clan_invitation_id, clan_id
                    FROM clan_invites WHERE account_id_invited = ?;
                """
        vals = c.execute(select, [account_id]).fetchall()
        c.close()
        logger.info(vals)
        accounts = []
        for val in vals:
            accounts.append({
                'clan_invitation_id': val[0],
                'clan_id': val[1]
            })
        return accounts


    def respond_clan_invite(self, clan_invitation_id: int, accepted):
        c = self.conn.cursor()
        select = """SELECT account_id_invited, clan_id
                    FROM clan_invites WHERE clan_invitation_id = ?;
                """
        vals = c.execute(select, [clan_invitation_id]).fetchone()
        c.close()

        account_id = vals[0]
        clan_id = vals[1]

        if accepted:
            self.add_user_to_clan(account_id, clan_id)

        # Delete the clan invite
        c = self.conn.cursor()
        select = """DELETE
                    FROM clan_invites WHERE clan_invitation_id = ?;
                """
        c.execute(select, [clan_invitation_id])
        self.conn.commit()
        c.close()

    def remove_clan_invite(self, clan_id, account_id):
        # Delete the clan invite
        c = self.conn.cursor()
        select = """DELETE
                    FROM clan_invites WHERE clan_id = ? and account_id_invited = ?;
                """
        c.execute(select, [clan_id, account_id])
        self.conn.commit()
        c.close()

    #===================== BUDDIES ==========================
    def get_buddies(self, account_id: int):
        c = self.conn.cursor()
        select = """SELECT buddy_id
                    FROM buddies WHERE account_id = ?;
                """
        vals = c.execute(select, [account_id]).fetchall()
        c.close()
        buddy_ids = [val[0] for val in vals]
        return buddy_ids

    def add_buddy(self, account_id: int, buddy_id: int):
        # First check if this buddy already exists
        current_buddies = set(self.get_buddies(account_id))
        if buddy_id in current_buddies:
            return

        # Not currently a buddy!
        c = self.conn.cursor()
        insert_command = """INSERT INTO buddies
                            (account_id, buddy_id)
                            values(?,?);
                            """
        c.execute(insert_command, [account_id, buddy_id])
        self.conn.commit()
        c.close()

    def remove_buddy(self, account_id, buddy_id):
        c = self.conn.cursor()
        select = """DELETE
                    FROM buddies WHERE account_id = ? and buddy_id = ?;
                """
        vals = c.execute(select, [account_id, buddy_id]).fetchone()
        self.conn.commit()
        c.close()

    def check_alts(self, username):
        c = self.conn.cursor()
        select = """SELECT hash
                    FROM alts WHERE lower(username) = lower(?);
                """
        vals = c.execute(select, [username]).fetchall()
        c.close()
        if not vals: # This already exists in the db
            return '[]'
        logger.info(vals)
        # Otherwise, we found some hashes. So let's find all usernames with this hash
        hashes = [f"'{val[0]}'" for val in vals]
        hashes = ', '.join(hashes)

        logger.info(f"Found hashes for username {username}: {hashes}")

        c = self.conn.cursor()
        select = f"""SELECT username
                    FROM alts WHERE hash in ({hashes});
                """
        logger.info(f"Executing: {select}")
        vals = c.execute(select).fetchall()
        logger.info(vals)
        c.close()

        vals = [val[0] for val in vals]
        return list(set(vals))
