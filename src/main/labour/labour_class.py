from loguru import logger
from src.main.databases.mysql_connector import MySqlconnection , MySqlCRUDoperations
from src.main.databases.mysql_connector import *
from src.main.encrypt_decrypt.encrypy_decrypt import decrypt
import configparser


class labour:
    def __init__(self,first_name,last_name,wage,role,crud):
        self.first_name = first_name        # instance variable
        self.last_name = last_name
        self.wage = wage
        self.role = role
        self.crud = crud
        self.__save_to_database(self.crud)

    def __save_to_database(self,crud):
        """
        1. CHECK IF USER ALREADY PRESENT IN THE TABLE
        2. IF YES THEN SKIP SAVING
        3. OTHERWISE INSERT INTO QUERY AND WRITE
        """
        query = f"Select ID from labour where lower(first_name) = '{self.first_name}'  AND lower(last_name) = '{self.last_name}'"
        logger.info(f"{query}")
        result = crud.read_from_mysql(query)

        if result:   # IF LABOUR ALREADY EXISTS I,THENRETURN EXISTING ID  
            logger.info(f"Labour alredy exists with ID {result[0][0]}")
            return result[0][0]
        
        email = self.first_name + "." + self.last_name + "@gmail.com"
        logger.info(f"{email}")
        insert_query = f"""
            INSERT INTO labour(FIRST_NAME, LAST_NAME, WAGE, ROLE, EMAIL)
            VALUES('{self.first_name}','{self.last_name}',{self.wage},'{self.role}','{email}')
            """
        logger.info(f"{insert_query}")
        
        crud.insert_from_mysql(insert_query)
        result = crud.read_from_mysql(query)
        logger.info(f"New Labour added with ID: {result[0][0]}")
        return result[0][0]

  
    def login(self):
        pass

config=configparser.ConfigParser()
config.read(r"D:\Newlystart\python_programming\src\resources\config_file.ini")
config.set("mysql_database","password",decrypt(config["mysql_database"]["password"]))

mysql_db_conn_obj = MySqlconnection(config)
mysql_db_conn_obj.connect()
crud = MySqlCRUDoperations(mysql_db_conn_obj.connection)
# Arun_obj =labour("Arun","Badwe",400,"labour")
# logger.info(f"{Arun_obj}")
# Arun_obj.save_to_database(crud)
Ramesh_obj = labour("Sumesh","Singh",600, "mistri",crud)
# Ramesh_obj.save_to_database(crud)
