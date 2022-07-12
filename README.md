# WEbola

pip install --upgrade pip
pip install -r requirements.txt

export FLASK_RUN_PORT=8000
export FLASK_APP=main

python main.py

gunicorn -b 127.0.0.1:8000 main:app --worker-class gevent;2D


```
Open http://localhost:8000/gene_level_analsys
