FROM python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y default-libmysqlclient-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of your application code to the container
COPY . .

# Run your Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#913c78ae5e5a41211fe79a2ae8c900e230bdf9cf4d6d60d655ab8cc055e9406f
#a64952318c02