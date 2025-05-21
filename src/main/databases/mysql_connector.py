print("prograaming")
from loguru import logger

import mysql.connector
from src.main.encrypt_decrypt.encrypy_decrypt import decrypt

class MySqlconnection:
    def __init__(self,config):
          self.config =config
          self.connection = None

    def connect(self):
        try:
            self.connection= mysql.connector.connect(host=self.config["mysql_database"]["host"] ,
                                            user=self.config["mysql_database"]["user"], 
                                            password=self.config["mysql_database"]["password"] ,
                                            database=self.config["mysql_database"]["database"])
            logger.info(f"connection successful")

        except Exception as e:
             logger.info(f"Mysql Error occured: {e}")
             raise e
        
    def close(self):
         if self.connection.is_connected():
              self.connection.close()
              logger.info(f"Mysql database close")

class MySqlCRUDoperations:
    def __init__(self,mysql_connection):
        self.connection=mysql_connection 

    def read_from_mysql(self,query):
        logger.info(f"query sent to read {query}")
        try:
            cursor=self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            # logger.info(f"{result}")
            return result

        except Exception as e:
            logger.info(f"error occured in mysql query run   {e}")
            raise e
        
        finally:
            cursor.close()
    
    def insert_from_mysql(self,query):
        try:
            cursor=self.connection.cursor()
            cursor.execute(query)
            result=cursor.fetchall()
            # logger.info(f"{result}")
            return result
        except Exception as e:
            logger.info(f"error occured in mysql insert query run {e}")
            raise e
        
        finally:
            self.connection.commit()
            
        

           
          

# def read_from_mysql(config,query):

#     try:
#         cursor=connection.cursor()
#         cursor.execute(query)
#         result=cursor.fetchall()
#         logger.info(f"{result}")
#         return result
    
#     except Exception as e:
#         logger.info(f"error occured in mysql DB   {e}")
#         raise e
    
#     finally :
#             connection.close()
#             cursor.close()
            

    # insert_query = "select * from labours_table"
    # cursor.execute(insert_query)
    # result=cursor.fetchall()
    # print(result)