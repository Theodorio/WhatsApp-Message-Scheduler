FROM python:3.8
COPY requirements.txt 
RUN pip install -r requirements.txt && rm requirements.txt
EXPOSE 10000
ENTRYPOINT [ "python", "view.py"]
