# Use an official Python runtime as a parent image
FROM python:3.9.18-slim-bullseye

# Set environment variables for Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Nginx
RUN apt-get update && apt-get install -y nginx

# Remove the default Nginx configuration
RUN rm /etc/nginx/nginx.conf

# Copy your custom Nginx configuration
COPY nginx.conf /etc/nginx/nginx.conf

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Start both Django and Nginx
CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:8000 oc_lettings_site.wsgi:application & nginx -g 'daemon off;'"]
