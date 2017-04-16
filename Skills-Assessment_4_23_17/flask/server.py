from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

app.secret_key = "ABC"

@app.route("/", methods=['GET', 'POST'])
def index():
    """Show an index page."""
    #Render the template in the html/css =>route   
    return render_template("application-form.html")

@app.route("/application", methods=['GET', 'POST'])
def response_page():
    """Show the user a response to their application"""
    #Rendered info from form to Jinja template =>route
    #Get responses assign to variable names
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    jobtitle = request.form.get("jobtitle")
    salaryrequirement = request.form.get("salaryrequirement")
    salaryrequirement = str(salaryrequirement)

    #Render to response template
    return render_template("application-response.html", firstname = firstname, lastname = lastname, jobtitle = jobtitle, salaryrequirement = salaryrequirement)




if __name__ == "__main__":
    app.debug = True

    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
