from projects.bank_accountsql.prostgresssql.Create import Create
from projects.bank_accountsql.prostgresssql.Insert import Inserting
from projects.bank_accountsql.prostgresssql.Delete import Deleting
from projects.bank_accountsql.prostgresssql.Read import  Reading
from projects.bank_accountsql.prostgresssql.update import Update
from projects.bank_accountsql.prostgresssql.Altering_columns import Alter

class DataBase:
    @staticmethod
    def rename_column(table:str,column_name:str,new_column_name:str):
        Alter.rename_column(table, column_name, new_column_name)
    @staticmethod
    def add_column(table:str,column_name:str,type:str):
        Alter.add_column(table, column_name, type)
    @staticmethod
    def drop_column(table:str,column:str):
        Alter.drop_column(table, column)
    @staticmethod
    def change_column_type(table:str,column_name:str,type:str):
        Alter.change_column_type(table, column_name, type)
    @staticmethod
    def insert(table:str,keys:str,value:str):
        Inserting(table, keys, value)

    @staticmethod
    def create(table_name:str,keys:str):
        Create(table_name, keys)

    @staticmethod
    def delete(table:str):
        Deleting(table)

    @staticmethod
    def read(table):
        u = Reading.read(table)
        return u

    @staticmethod
    def update(table:str,column:str,new_value:str,condition:str):
        Update(table, column, new_value, condition)