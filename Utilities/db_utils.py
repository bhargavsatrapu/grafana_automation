from sqlalchemy import create_engine , text
from Utilities.read_config_util import ReadConfig

class DB_Utils:
    # Database connection details
    db_host = ReadConfig.get_config_properties("DB_HOST")
    db_user = ReadConfig.get_config_properties("DB_USER")
    db_password = ReadConfig.get_config_properties("DB_PASSWORD")
    db_name = ReadConfig.get_config_properties("DB_NAME")
    db_port = ReadConfig.get_config_properties("DB_PORT")
    engine=""
    connection=""

    def connect_db(self):
        self.engine = create_engine(f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}")
        self.connection = self.engine.connect()

    def create_table_and_insert_query(self,create_table_query,insert_record_query,records_to_insert):
        create_table_query1 = text(f"""{create_table_query}""")
        self.connection.execute(create_table_query1)

        # Insert hardcoded records into the database
        insert_record_query1 = text(f"""{insert_record_query}""")
        for record in records_to_insert:
            self.connection.execute(insert_record_query1, record)
            self.connection.commit()

    def execute_query(self,query):
        query_to_execute = text(f"""{query}""")
        self.connection.execute(query_to_execute)

    def close_db_connection(self):
        self.connection.close()
        self.engine.dispose()
