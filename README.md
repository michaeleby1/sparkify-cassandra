# Modeling Data using Cassandra

This project models song streaming data for analysis. The data is initially stored in CSV format. 

I want to model this dataset as an Apache Cassandra keyspace. I then want to create an ETL pipeline that takes the CSV files and uploads them to the server. This will accomplish two things:

1. It will allow for the tracking of user activity by organizing the data into three denormalized tables.

2. It will prioritize availability over consistency, optimizing the querying process and making the data amenable to horizontal scaling.

## Keyspace

![erd](files/sparkify-cassandra-erd.png)

There are three tables in the keyspace:

1. `music_app_history`: We are looking for all users that listened to song_title = 'All Hangs Against His Own."

We therefore want to use `(song_title, user_id)` as our primary key. 

2. `user_library`: We are looking for the user info and song metadata where user_id = 10 and session_id = 182.

We therefore want to use `(user_id, session_id, item_in_session)` as our primary key. 

3. `song_library`: We are looking for the song metadata where session_id = 338 and item_in_session = 4.

We therefore want to use `(session_id, item_in_session)` as our primary key. 

## Project Organization

This schema can be replicated and populated by running the below two scripts:

- <b>create_tables.py</b>: This script creates and connects to a database named `sparkifydb` and creates the three tables via the <b>cql_queries.py</b> file (CQL is the Cassandra query language).
- <b>etl.py</b>: This script connects to the database, extracts and transforms the CSV files into a single CSV file, and loads the data into the database according to the schema—also via the <b>cql_queries.py</b> file.

The notebook <b>test.ipyb</b> allows for testing the database connection and running CQL queries on it.