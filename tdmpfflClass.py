# import json
# import pycurl
# import StringIO
# import urllib
# import mysql.connector
# import sys
import pg
import os

DBUSER=os.environ.get('DBUSER', True)
DBPASS=os.environ.get('DBPASS', True)
DBHOST=os.environ.get('DBHOST', True)
DBNAME=os.environ.get('DBNAME', True)

db = pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)

# class Database(object):
#     @staticmethod
#     def getConnection():
#         db = pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)
#         return
#     @staticmethod
#     def escape(value):
#         return value.replace("'","''")
#     @staticmethod
#     def getResult(query,getOne=False):
#
#         Cursor.close()
#         return result_set
#     @staticmethod
#     def doQuery(query):
#         conn = Database.getConnection()
#         cur = conn.cursor()
#         cur.execute(query)
#         conn.commit()
#         lastId = cur.lastrowid
#         cur.close()
#         conn.close()
#         return lastId

class Owners(object):
    def __init__(self,):
        self.name = ""
        self.yearstarted = 0
        self.yearended = 0
        self.idowners = 0
    @staticmethod
    def getOwners():
        db = pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)
        query = db.query("SELECT * FROM owners order by yearstarted asc")
        result_list = query.namedresult()
        db.close()
        return result_list
    @staticmethod
    def alltime():
        db = pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)
        query = db.query("select owner,sum(wins) wins,sum(loss) loss,idowners from winloss group by owner,idowners order by sum(wins) desc")
        result_list = query.namedresult()
        db.close()
        return result_list
    # @staticmethod
    # def owneryears(idowners):
    #     db = pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)
    #     query = db.query("select 'year',sum(wins) wins,sum(loss) loss,idowners from winloss where idowners='%d' group by 'year',idowners order by year asc" % idowners)
    #     result_list = query.namedresult()
    #     db.close()
    #     return result_list

class Teams(object):
    def __init__(self,idowners=0):
        self.idteamnames=0
        self.teamname = ""
        self.yearstarted = 0
        self.yearended = 0
        self.idowners = idowners
    @staticmethod
    def get_team_list(idowners):
        db = pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)
        query = db.query("SELECT * FROM teamnames where idowners='%s' order by yearstarted asc" % idowners)
        result_list = query.namedresult()
        db.close()
        return result_list

    # working on stats for each team
    # @staticmethod
    # def get_team_list(idowners):
    #     db = pg.DB(host=DBHOST, user=DBUSER, passwd=DBPASS, dbname=DBNAME)
    #     query = db.query("SELECT * FROM teamnames left join where idowners='%s' order by yearstarted asc" % idowners)
    #     result_list = query.namedresult()
    #     db.close()
    #     return result_list