FROM dromni/nerfstudio:1.1.3

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]

