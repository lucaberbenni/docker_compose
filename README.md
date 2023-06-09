This Docker Compose project sets up a data pipeline for collecting, processing, and analyzing data from the popular social media platform Reddit. The project consists of three subfolders, `etl_job`, `reddit_collector`, and `slackbot`, each containing their respective components.

### etl_job
The `etl_job` subfolder contains the necessary files to perform Extract, Transform, and Load (ETL) operations on the collected Reddit data. It includes a Dockerfile specifying the environment, a Python script (`etl.py`) for connecting to MongoDB, extracting data, performing sentiment analysis using VADER Sentiment Analyzer, and storing the results in a PostgreSQL database. The `requirements.txt` file lists the required dependencies, including `pymongo`, `SQLAlchemy`, `psycopg2`, `pandas`, and `vaderSentiment`.

### reddit_collector
The `reddit_collector` subfolder is responsible for collecting data from Reddit's API. It contains a Dockerfile for building the environment, a Python script (`milestone_get_reddit.py`) for authenticating with Reddit's API using OAuth2, retrieving the hottest posts from a specified subreddit, and storing them in a MongoDB database. The `requirements.txt` file specifies the dependencies needed, including `requests` and `pymongo`.

### slackbot
The `slackbot` subfolder implements a Slack bot that retrieves the most negatively rated post from the PostgreSQL database and sends it to a designated Slack channel. It consists of a Dockerfile for the environment, a Python script (`post_reddit.py`) for connecting to the PostgreSQL database, retrieving the relevant post using SQL, and sending it to Slack using the Slack API. The `requirements.txt` file includes the necessary dependencies: `SQLAlchemy`, `requests`, and `psycopg2`.

### docker-compose.yml
The `docker-compose.yml` file describes the services and their configurations for the Docker Compose project. It sets up the following services:
- `reddit_collector`: Builds and runs the Reddit data collector using the Dockerfile in the `reddit_collector` subfolder. It depends on the `mongodb` service.
- `mongodb`: Uses the MongoDB official image and exposes port 27017 to allow communication with the collector service.
- `etl_job`: Builds and runs the ETL job using the Dockerfile in the `etl_job` subfolder. It depends on both the `mongodb` and `postgresdb` services.
- `postgresdb`: Utilizes the PostgreSQL official image, exposing port 5555 for communication. It sets environment variables for the PostgreSQL user, password, and database name.
- `slackbot`: Builds and runs the Slack bot using the Dockerfile in the `slackbot` subfolder. It depends on the `postgresdb` service.

### script.sh
The `script.sh` file contains a simple shell script to stop any running Docker Compose containers and start the project in detached mode.

This Docker Compose project provides a seamless data pipeline for collecting Reddit data, performing sentiment analysis, storing the results, and sending notifications to a Slack channel. It encapsulates each component in separate Docker containers, ensuring portability and ease of deployment.
