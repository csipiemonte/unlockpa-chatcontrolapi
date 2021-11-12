FROM python:3.7


WORKDIR /app
RUN mkdir /app/data
# Install requirements
ADD requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

# Copy files
ADD chatcontrolapi /app/chatcontrolapi

#ADD data /app/data
ADD config.ini /app/config.ini
ADD configSql.ini /app/configSql.ini
ADD main.py /app/main.py
ADD wait-for-it.sh /app/wait-for-it.sh
RUN chmod +x  /app/wait-for-it.sh

# Run
#CMD ["python", "main.py", "botmanager", "--host", "0.0.0.0"]
