'''
########################################################
# Name Project: Attendance List                        #
# Developer Name: Mário Wessen                         #
# Contact: mrfwn@cin.ufpe.br                           #
# Date last Modify:  24/06/2019                        #
# Description File: This is Generic Class for          #
# integrated bettwen BeckEnd and Firebase.             #
# Consult Methods implemented                          #
########################################################
'''
import pyrebase

class Database:

    dbName = ''
    configConection = {
        "apiKey": '',
        "authDomain": '',
        "databaseURL": '',
        "projectId": '',
        "storageBucket": '',
        "messagingSenderId": '',
        "appId": ''
    }

    def __init__(self,dbName):
        self.dbName = dbName
        try:
            self.instanceDB = pyrebase.initialize_app(self.configConection).database()
        except:
            print("Error in Starting Instance Firebase")

    def get_datas(self):
        return  self.instanceDB.child(self.dbName).get().val()

    def push_data(self,data):
        self.instanceDB.child(self.dbName).push(data)

    def push_list_data(self,list_data):
        for data in list_data:
            self.instanceDB.child(self.dbName).push(data)

    def remove_data(self,key):
        self.instanceDB.child(self.dbName).child(key).remove()

    def remove_all_data(self):
        self.instanceDB.child(self.dbName).child().remove()

    def update_data(self,key,data):
        self.instanceDB.child(self.dbName).child(key).update(data)



