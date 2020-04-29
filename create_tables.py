from cassandra.cluster import Cluster
from cql_queries import create_table_queries, drop_table_queries

def create_keyspace():
    """
    - Creates and connects to the keyspace
    - Returns the cluster and session 
    """

    cluster = Cluster(['127.0.0.1'], port=9042)
    session = cluster.connect()

    session.execute("""
    CREATE KEYSPACE IF NOT EXISTS sparkify
    WITH REPLICATION = 
    { 'class' : 'SimpleStrategy', 'replication_factor' : 1 }"""
    )

    session.set_keyspace('sparkify')

    return cluster, session

def drop_tables(session):
    """
    Drops tables in the session keyspace via drop_table_queries list
    """

    for query in drop_table_queries:
        session.execute(query)

def create_tables(session):
    """
    Creates tables in the session keyspace via create_table_queries list
    """

    for query in create_table_queries:
        session.execute(query)

def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify keyspace
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cluster, session = create_keyspace()
    
    drop_tables(session)
    create_tables(session)

    session.shutdown()
    cluster.shutdown()


if __name__ == "__main__":
    main()