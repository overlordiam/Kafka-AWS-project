# Data streaming for stock market analysis

## Overview
This is an end-to-end project on Real-Time Stock Market Data using Python, Kafka and AWS. It takes in streaming stock data and stores the data in a S3 bucket via Kafka brokers. The data is then extracted, trasnformed and loaded into AWS Athena using AWS Glue. In Athena, the data is ready for Adhoc analysis using SQL.

## Architecture
![image](https://github.com/user-attachments/assets/c36b4aef-59c7-411c-b59c-1f000fab0dbd)


## A preview
<div>
    <a href="https://www.loom.com/share/752458dfb62b498aab8294f1e8477dba">
      <p>Data streaming with AWS and Kafka - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/752458dfb62b498aab8294f1e8477dba">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/752458dfb62b498aab8294f1e8477dba-b9e4cc0f1953bfe3-full-play.gif">
    </a>
  </div>

## Components

#### Data Source: Stock market data
- The application emulates streaming data by sampling records from a CSV file in quick intervals.

#### Kafka Configuration:
- This configuration includes one producer and one consumer allows for easy execution as the required data throughput is low.
- The producer reads from a CSV file and emulates real time streaming. It sends the data to the Kafka broker.
- The consumer reads the data from the Kafka broker and stores the data into an S3 bucket, which is achieved through AWS CLI. 

#### AWS Glue:
- The Glue instance provides us with a crawler which crawls the S3 bucket for data. It creates a database and stores the data in a table for further probing.

#### AWS Athena:
- With the Athena service, we can query the data using SQL to acquire deeper insights into the trends and dynamics.

## Technologies used
- Python
- Kafka
- AWS Glue
- AWS Athena
- AWS EC2
- AWS S3 buckets
- SQL

## How to run
1) Create an AWS account
2) Download Kafka and Zookeeper in an EC2 instance
3) Run the following command in a terminal to start Zookeeper
   ```bash
   zookeeper-server-start.sh ~/kafka_2.13-3.8.0/config/zookeeper.properties
4) Run the following command in a terminal to start Kafka
    ```bash
    kafka-server-start.sh ~/kafka_2.13-3.8.0/config/server.properties
5) Clone and download the code in from repository and run it in a Python IDE (preferably VScode)
6) Create an S3 bucket to store the data, a Glue service to crawl the bucket and an Athena instance to use SQL and query data.
7) Run the Consumer file followed by the Producer file
