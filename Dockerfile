# base image  
FROM python:3.8   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1 
ENV SENTRY_DSN $SENTRY_DSN
ENV HEROKU_APP_NAME $HEROKU_APP_NAME
ENV PORT 8000 

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME  

# run this command to install all dependencies  
RUN pip install -r requirements.txt && \
    python3 manage.py collectstatic --noinput --clear && \
    python3 manage.py dumpdata -o data.json

# port where the Django app runs  
EXPOSE $PORT

# start server
CMD python manage.py runserver 0.0.0.0:$PORT
