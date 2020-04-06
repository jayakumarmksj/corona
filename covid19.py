from flask import Flask,render_template,request
from results import results
app = Flask(__name__)


@app.route('/')
def stats():
    d=dict(zip(['Active Cases','Cured / Discharged','Deaths','Migrated'],results()))
    return render_template('front.html',data=d)

if __name__ == '__main__':
    app.run()
