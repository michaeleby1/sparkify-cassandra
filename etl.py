import pandas as pd
from cassandra.cluster import Cluster
import os
import glob
import csv
from cql_queries import *

def process_csvs():
    """
    Returns a list of all the rows in the events_data csv files
    """
    filepath = os.getcwd() + '/event_data'
    
    # join the file path and roots with the subdirectories using glob
    file_path_list = glob.glob(os.path.join(filepath,'*'))
 
    full_data_rows_list = [] 
    
    # for every filepath in the file path list 
    for f in file_path_list:

        # reading csv file 
        with open(f, 'r', encoding = 'utf8', newline='') as csvfile: 
            # creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            next(csvreader)
            
            # extracting each data row one by one and append it        
            for line in csvreader:
                #print(line)
                full_data_rows_list.append(line) 
    
    return full_data_rows_list

def write_csv(full_data_rows_list):
    """
    Creates a smaller csv file in the directory for song entries
    """

    csv.register_dialect('myDialect', quoting=csv.QUOTE_ALL, skipinitialspace=True)

    with open('event_datafile_new.csv', 'w', encoding = 'utf8', newline='') as f:
        writer = csv.writer(f, dialect='myDialect')
        writer.writerow(['artist','firstName','gender','itemInSession','lastName','length',
                         'level','location','sessionId','song','userId'])

        for row in full_data_rows_list:
            if (row[0] == ''):
                continue
            
            writer.writerow((row[0], row[2], row[3], row[4], row[5], row[6], 
                             row[7], row[8], row[12], row[13], row[16]))

def insert_data(session):
    """
    Inserts data from transformed csv into three new tables
    """
    with open('event_datafile_new.csv', encoding = 'utf8') as f:
        csvreader = csv.reader(f)
        next(csvreader) # skip header

        for line in csvreader:

            session.execute(insert_song_library, 
                        (int(line[8]), int(line[3]), line[0], line[9], float(line[5])))

            session.execute(insert_user_library, 
                        (int(line[10]), int(line[8]), int(line[3]), line[0], line[9],
                         line[1], line[4]))
            
            session.execute(insert_music_app_history, 
                        (line[9], int(line[10]), line[1], line[4]))

def main():
    """
    Connects to keyspace, performs ETL, closes connection
    """
    # Create a connection to the cassandra docker container, set the keyspace
    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()
    session.set_keyspace('sparkify')

    # Extract and transform raw data
    full_data_rows_list = process_csvs()
    write_csv(full_data_rows_list)


    # Load into Cassandra tables
    insert_data(session)

    # End the session and connection
    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()

            