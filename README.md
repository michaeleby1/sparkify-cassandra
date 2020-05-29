# Modeling Data using Cassandra

This project models song streaming data for analysis. The data is initially stored in CSV. 

I want to model this dataset as an Apache Cassandra keyspace. I then want to create an ETL pipeline that takes the CSV file and uploads it to the server. This will accomplish two things:

1. It will allow for the tracking of user activity.

2. It will decrease overall latency, optimizing the querying process and providing faster access to song and user data.
