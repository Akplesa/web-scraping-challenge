  
#Importing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mars_scraped

#Creating instance of  the Flask app
app = Flask(__name__)

#Using PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Routing to render index.html template using data from Mongo
@app.route("/")
def home():

    # Finding the mars records from mongo database
    mars_records = mongo.db.collection.find_one()

    # Returning template and data
    return render_template("index.html", mars= mars_records)

# Triggering the scrape function with route
@app.route("/scrape")
def scrape():

    # Running the scrape function
    USGS_Mars_scraped = mars_scraped.scrape()

    # Updating the Mongo database using update and upsert=True
    mongo.db.mars_one.update({}, USGS_Mars_scraped, upsert=True)

    # Redirecting back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)