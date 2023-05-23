FROM python:3.11

WORKDIR /app 

COPY requirements.txt /app

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["python", "milestone_get_reddit.py"]
