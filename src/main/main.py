from loguru import logger
from src.main.databases.mysql_connector import *
from src.main.encrypt_decrypt.encrypy_decrypt import decrypt

import configparser

config=configparser.ConfigParser()
config.read(r"D:\Newlystart\python_programming\src\resources\config_file.ini")
config.set("mysql_database","password",decrypt(config["mysql_database"]["password"]))


def main():
    mysql_db_connection = MySqlconnection(config)
    mysql_db_connection.connect()

    crud_operation_obj = MySqlCRUDoperations(mysql_db_connection.connection)
    final_result =  crud_operation_obj.read_from_mysql("select * from labours_table")
    logger.info(f"{final_result}")
    mysql_db_connection.close()


if __name__ == "__main__":
    main()