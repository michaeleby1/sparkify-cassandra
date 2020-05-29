# Modeling Data using Cassandra

This project models song streaming data for analysis. The data is initially stored in CSV format. 

I want to model this dataset as an Apache Cassandra keyspace. I then want to create an ETL pipeline that takes the CSV file and uploads it to the server. This will accomplish two things:

1. It will allow for the tracking of user activity by organizing the data into three denormalized tables.

2. It will prioritize availability over consistency, optimizing the querying process and making the data amenable to horizontal scaling.

## Keyspace

