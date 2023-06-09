# docker_compose
Docker containers setup, scrape data from reddit, store data in MongoDB, run Sentiment Analysis, save results in Postgres SQL and build a Slack bot.

The project is structured using Docker and Docker Compose to manage the various services and dependencies. The services defined in the `docker-compose.yml` file include:

1. **reddit_collector**: This service is responsible for collecting data from the Reddit API. It runs a Python script (`milestone_get_reddit.py`) that uses the `requests` library to make API requests and retrieve posts from a specified subreddit. The collected data is stored in a MongoDB database.

2. **mongodb**: This service runs a MongoDB database container. It uses the official MongoDB Docker image and exposes port 27017 to allow connections to the database.

3. **etl_job**: This service performs the ETL (Extract, Transform, Load) process on the collected data. It runs a Python script (`etl.py`) that uses libraries such as `pandas`, `SQLAlchemy`, and `psycopg2` to extract data from the MongoDB database, perform sentiment analysis using the VADER sentiment analyzer, and load the analyzed data into a PostgreSQL database.

4. **postgresdb**: This service runs a PostgreSQL database container. It uses the official PostgreSQL Docker image and exposes port 5555 to allow connections to the database. The environment variables are set to configure the database username, password, and database name.

5. **slackbot**: This service sends notifications to a Slack channel about negative sentiment posts. It runs a Python script (`post_reddit.py`) that uses the `requests` library to send a webhook request to the specified Slack webhook URL. It retrieves the most negatively rated post from the PostgreSQL database and sends a notification containing the post's text and sentiment score.

To run the project, you can use the `docker-compose stop && docker-compose up -d` command. This command stops the running services (if any) and then starts them again in detached mode, allowing them to run in the background.

Please note that the success of the project depends on the correctness of the code and configuration files provided, as well as the availability and accessibility of the required APIs, databases, and Slack webhook URL.
