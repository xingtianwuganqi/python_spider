from flask import Flask,g
from ipcontent.RedisClient import RedisClient


__all__ = ['app']
app = Flask(__name__)

def get_conn():
    if not hasattr(g,"redis"):
        g.redis = RedisClient()
    return g.redis

@app.route("/")
def index():
    return "<h2>welcome to home<h2>"

@app.route('/random')
def get_proxy():
    conn = get_conn()
    return conn.random()

@app.route('/count')
def get_counts():
    conn = get_conn()
    count = conn.count()
    return str(count)

if __name__ == "__main__":
    app.run()
    # app.get_proxy()