# Pull base image
FROM python:3.7

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies
COPY requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project
COPY . /code/

# Unknown commands
EXPOSE 8000

COPY ./custom.py /usr/local/lib/python3.7/site-packages/django/core/mail/backends

# cp -f custom.py /usr/local/lib/python3.7/site-packages/django/core/mail/backends/custom.py