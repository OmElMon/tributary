FROM python:3.11

# Copy the requirements.txt and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the entrypoint.py script
COPY entrypoint.py .

# Set the command to run the app
CMD ["gunicorn", "entrypoint:app"]

