from loguru import logger

class labour:
    def __init__(self,first_name,last_name,wage):
        self.first_name = first_name        # instance variable
        self.last_name = last_name
        self.wage = wage

    def save_to_database(self):
        pass
        query = "Select ID from labour where lower(first_name) = %s AND lower(last_name) = %s"
        result = self.crud.read_from_mysql(query, (self.first_name, self.last_name))

        if result:   # IF LABOUR ALREADY EXISTS I,THENRETURN EXISTING ID  
            logger.info(f"Labour alredy exists with ID {result[0][0]}")
            return result[0][0]



    """
    1. CHECK IF USER ALREADY PRESENT IN THE TABLE
    2. IF YES THEN SKIP SAVING
    3. OTHERWISE INSERT INTO QUERY AND WRITE

    """


    def login(self):
        pass

Arun_obj =labour("Arun","Badwe",400)
Ramesh_obj = labour("Ramesh","Singh",600)


