FROM python:3.12-slim                

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "prodexa.wsgi:application", "--bind", "0.0.0.0:8000"]
 


#Starts with a lightweight version of Python 3.12.
#Prevents Python from writing .pyc files(keeps the container clean).
#Ensures console logs are sent straight to the terminal to see errors in real-time.
#Creates a folder called /app inside the "box" and moves into it.
#Copies the requirements file from computer into the box.
#Installs all libraries (DRF, Celery, etc.) inside the box.
#Copies the rest of your project code into the box.

#What are .pyc files ?
#When you run a Python script, Python doesn't actually read your code directly every single time.

#Compilation: First, Python translates your human-readable code (.py) into "Bytecode".
#Storage: It saves this bytecode in .pyc files (usually hidden in a __pycache__ folder).
#Purpose: The next time you run the script, Python checks if the .py file has changed. If not, it loads the .pyc file instead. This makes your app start up much faster because the translation step is already done.
#In Docker: We use PYTHONDONTWRITEBYTECODE=1 in your Dockerfile because, in a container, we want to keep the file size small and don't need to save those files for "next time" since containers are often deleted and recreated.


#Djangorunserver	
#Purpose	   Development / Testing	
#Performance   Single-threaded (handles one request at a time)	
#Stability	   If one request crashes, the server might stop	
#Security	   Not audited for security; high risk

#Gunicorn
#Purpose		Production / Real Users
#Performance	Multi-worker (handles many requests at once)
#Stability	    If one worker crashes, Gunicorn kills it and starts a new one
#Security		Hardened and designed to face the open internet