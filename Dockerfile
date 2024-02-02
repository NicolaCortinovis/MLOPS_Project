FROM python:3.9.18

WORKDIR /streamlit_app

COPY /streamlit_app /streamlit_app

RUN pip install --upgrade pip \
    pip install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
