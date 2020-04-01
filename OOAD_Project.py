from flask import Flask,render_template

app = Flask(__name__)
# from flaskext.mysql import MySQL
# mysql = MySQL()

@app.route('/')
def hello_world():
    # return 'Hello World!'
    return render_template("index.html")

@app.route('/saveinformation')
def saveinfo():
    # return 'Hello World!'
    return render_template("Save_Information.html")

@app.route('/disaster_report')
def disaster_report():
    # return 'Hello World!'
    return render_template("Disaster_Report.html")

@app.route('/weather_report')
def weather_report():
    # return 'Hello World!'
    return render_template("Weather_Report.html")

if __name__ == '__main__':
    app.run()
