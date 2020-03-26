from flask import Flask, render_template, jsonify
import scraping
import pandas as pd
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

### initialize db connection & ORM

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", )


### needs to be tested
@app.route("/data")
def data_access():
    """return a JSON of all stored data"""  # doesn't make a lot of sense. adding filtering here (or sub-endpoints like "today" or "latest") is a subject of future work.

    query = session.query(Data)  # query all rows and columns
    df = pd.read_sql(query.statement, con=engine)

    return jsonify(df.to_dict)

# non-time data vs. time data
@app.route("/timeseries")
def plot1():
    return render_template("plot1.html", )


# non-time data vs. non-time data
@app.route("/correlation/<query>")
def plot2(query):

    ### per Erin's testing specifications
    
    return render_template("plot2.html", )


@app.route("/scrape")
def scrape():

    ### query db to find date of most recent scrape

    # scrape
    lambda_scrape = scraping.get_data(scraping.LAMBDA_URL, since=last_date)
    wind_scrape = scraping.get_data(scraping.WIND_5MIN_URL, since=last_date)

    ### get necessary data and create new df to put in db
    ### necessary data is time of scrape + df contents
    ### wind data only need 1st row
    ### put in db

    return render_template("scrape.html", )


if __name__ == "__main__":
    app.run(debug=True)