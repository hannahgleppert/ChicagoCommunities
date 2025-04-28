#load_data
import requests
import duckdb
import pandas as pd
from dotenv import load_dotenv 
import os


def load_data_to_duckdb(table_name, df):
    db_path = '/ChicagoCommunities/sources/community/community_db.duckdb'
    
    try:
        con = duckdb.connect(db_path, read_only = False)
        con.execute(f'DROP TABLE IF EXIST {table_name}')
        con.execute(f'CREATE TABLE {table_name} AS SELECT * FROM read_csv_auto(df)')
        # Save the DuckDB file
        con.commit()
    except Exception as e:
        print(e)
    finally:
        con.close()

    return db_path



#load_data_to_duckdb('codes', 'codes.csv')