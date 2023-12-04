from python:3.10.6-slim-buster
RUN apt-get update -y
RUN apt-get -y install gcc python3-dev
RUN pip install --upgrade pip
WORKDIR app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./ /app/streamlit_tutorial/
EXPOSE 8501
ENTRYPOINT ["bash", "/app/streamlit_tutorial/entry.sh"]