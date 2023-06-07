from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__) # Sets up/Creates an instance of a Flask app

@app.route('/')
def default_home():
    return render_template('index.html')

@app.route('/<string:page_name>') # Dynamic routing for html pages
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() # The to_dict method returns a dictionary with the entirety of the forms data
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return 'Something went wrong. Try again!'

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        name = data['name']
        email = data['email']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, message])