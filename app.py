from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    today = datetime.now()
    today_date = today.strftime("%dth, %Y %H:%M:%S")
    day_of_week  = today.weekday()
    if (day_of_week == 0):
        day_of_week = "Monday"
    if (day_of_week == 1):
        day_of_week = "Tuesday"
    if (day_of_week == 2):
        day_of_week = "Wednesday"
    if (day_of_week == 3):
        day_of_week = "Thursday"
    if (day_of_week == 4):
        day_of_week = "Friday"
    if (day_of_week == 5):
        day_of_week = "Saturday"
    if (day_of_week == 6):
        day_of_week = "Sunday"
    return render_template('index.html',day_of_week=day_of_week,today_date=today_date)

if __name__ == "__main__":
    app.run(debug=True)