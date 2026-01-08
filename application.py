from flask import Flask, render_template

# AWS Elastic Beanstalk looks for a variable named 'application' specifically
application = Flask(__name__)

@application.route('/')
def home():
    # This shows your HTML file to visitors
    return render_template('index.html')

if __name__ == "__main__":
    application.run()
