from flask import Flask
#It creates an instance of the Flask class,
#which will be your WSGI (Web Server Gateway Interface) application.

# Create the Flask instance (the app object)
app = Flask(__name__)

# Route for the home page
@app.route("/")
def welcome():
    return "Welcome to this best Flask course. This should be an amazing course"

# Route for the index page
@app.route("/index")
def index():
    return "Welcome to the index page"

# Run the app only if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)