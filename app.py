from flask import Flask # Import Flask package
from flask import render_template # Import render_template function
app = Flask(__name__) # Construct Flask object named 'app'

'''
@app.route() defines the URLs that route to the index() function.
The URLs will be appended to the end of the base URL.
Links within HTML files should use the defined routes (for example '/index') as
the values for href attributes.

URLs that will call the index() function if running app.py on localhost:
http://localhost:5000/
http://localhost:5000/index
'''
@app.route('/') # URL for function (default for home page)
@app.route('/index') # Secondary URL for function
def index():
    return render_template('index.html') # located in templates/

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/bands')
def bands():
    return render_template('bands.html')

@app.route('/venues')
def venues():
    return render_template('venues.html')

@app.route('/festivals')
def festivals():
    return render_template('festivals.html')

@app.route('/festivalsP2')
def festivalsP2():
    return render_template('festivalsP2.html')

@app.route('/festivalsP3')
def festivalsP3():
    return render_template('festivalsP3.html')

@app.route('/page3')
def page3():
    dict = {'string1' : 'Testing.', 'string2' : 'Hello, World!'}
    return render_template('page3.html', strings = dict) # Example of argument passing to HTML template

if __name__ == '__main__':
    app.run() # Run application
