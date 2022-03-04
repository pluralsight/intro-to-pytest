FROM python:latest
WORKDIR /app
COPY . .
RUN pip install -r requirement.txt
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]