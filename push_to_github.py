from scraper import *
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
from git import Repo



functions = [league_table,top_scorers,detail_top,player_table,all_time_table,all_time_winner_club,top_scorers_seasons,goals_per_season]

def to_github(func):

    file_name = func.__name__
    file = f"{file_name}.parquet"
    func = func()
    
    #Create directory if it doesn't exist
    os.makedirs("data", exist_ok=True)
    
    # Convert DataFrame to Arrow Table
    table = pa.Table.from_pandas(func)

    # write table to parquet file
    pq.write_table(table, f"data/{file}")

    # push to github repo
    # repo = Repo('.')
    # repo.index.add([f"data/{file}"])
    # repo.index.commit(f"Updated {file} data")
    # origin = repo.remote(name='origin')
    # origin.push()


    print(f"repo successfully updated")


for items in functions:
    to_github(items)
