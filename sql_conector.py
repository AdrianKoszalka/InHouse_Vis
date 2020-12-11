import mysql.connector
import datetime
import numpy as np
import pandas as pd
from sql_login import Login

class SQLConnector():
    def __init__(self, *args, **kwargs):
        sql_login = Login()
        
        self.hostname = sql_login.hostname
        self.username = sql_login.username
        self.password = sql_login.password
        self.database = sql_login.database
        self.connection_status = 0

        try:
            self.mydb = mysql.connector.connect(
                host = self.hostname[0],
                user = self.username[0],
                passwd = self.password[0],
                database = self.database
                )

            self.my_cursor = self.mydb.cursor()
            self.connection_status = 1 
        except:
            self.connection_status = 0 

        print(self.connection_status)

    def import_workers(self):

        self.my_cursor.execute("SELECT worker_id, name, sec_name, work_station FROM workers_list;")
        self.result = self.my_cursor.fetchall()

        self.workers_df = pd.DataFrame(self.result, columns=["workers_id", "name", "sec_name", "work_station"])
        self.workers_df.set_index("workers_id", inplace=True)

        print(self.workers_df)

    def import_log_records(self, parent):
        self.my_cursor.execute("SELECT * FROM card_records WHERE date = '{}';".format(str(parent.current_date.strftime('%Y-%m-%d'))))
        self.result_2 = self.my_cursor.fetchall()

        self.cards_records = pd.DataFrame(self.result_2, columns=["record", "in_out", "date", "hour", "worker_id"])
        self.cards_records.set_index("record")

        print(self.cards_records)

    def workers_in_or_out(self):

        self.workers_all = []
        self.workers_in = []
        self.workers_temp_in = []
        self.workers_out = []
        self.workers_temp_out = []

        for ids in self.workers_df.index:
            self.workers_all.append(ids)

        for in_out in self.cards_records[self.cards_records["in_out"]== "IN"]["worker_id"]:
            self.workers_temp_in.append(in_out)

        for in_out in self.cards_records[self.cards_records["in_out"]== "OUT"]["worker_id"]:
            self.workers_temp_out.append(in_out)
        
        for all_rec in self.workers_temp_in:
            if all_rec not in self.workers_temp_out:
                self.workers_in.append(all_rec)

        for out_rec in self.workers_all:
            if out_rec not in self.workers_in:
                self.workers_out.append(out_rec)
    
    def calculate_capacity(self, parent):

        self.workers_quantity = len(self.workers_all)
        self.workers_in_quantity = len(self.workers_in)

        self.workers_in_percent = int((round((self.workers_in_quantity/self.workers_quantity), 2))*100)

        self.work_station_quantity = len(parent.location_dic)
        self.work_station_in_quantity = len(parent.area_in)

        self.work_station_in_percent = int((round((self.work_station_in_quantity/self.work_station_quantity), 2))* 100)
