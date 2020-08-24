  
#Importing dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scraper_mars

#Creating instance of  the Flask app
app = Flask(__name__)

#Using PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Routing to render index.html template using data from Mongo
@app.route("/")
def home():

    # Finding the mars records from mongo database
     mars_records = mongo.db.mars_one.find_one()

    # Returning template and data
    return render_template("index.html", mars=mars_records)

# Triggering the scrape function with route
@app.route("/scrape")
def scrape():

    # Running the scrape function
    mars_info = scraper_mars.scrape_info()

    # Updating the Mongo database using update and upsert=True
    mongo.db.mars_one.update({}, mars_info, upsert=True)

    # Redirecting back to home page
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)