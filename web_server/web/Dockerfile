FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

# Specify the command to run on container start
#CMD ["uwsgi", "--ini", "myapp.ini"]
