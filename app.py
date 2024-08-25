from flask import Flask, render_template, request
from process import sno
import os
from prediction import predict
from postprocess import make_further_processes
from categorize_suggest import categorize_tumor
from sheety import sheet
from mail import send_email

app = Flask(__name__, static_folder='static')

app.config['UPLOAD_FOLDER'] = 'pics'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def getvalue():
    name = request.form['name']
    email = request.form['email']
    phoneno = request.form['phno']
    age = request.form['age']
    gender = request.form['message']
    image = request.files['image']

    number_report = sno()
    filename = f"{number_report}.jpg"  # Adding the file extension
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    image.save(file_path)

    # Predict and process the image
    result = predict(file_path)

    if result == 'yes':
        postprocess = make_further_processes(file_path)
        suggest = categorize_tumor(postprocess['width'], postprocess['height'])
    else:
        postprocess = {
            "location": "No tumor detected",
            "width": "N/A",
            "height": "N/A",
            "area": "N/A"
        }
        suggest = {
            "result": "N/A",
            "description": "N/A",
            "what_to_do": ["You're all good to go!!, have a great life ahead"],
            "who_to_consult": ["Get regular checkups"]
        }

    # Log details in the sheet and send an email with the results
    sheet(number_report, name, email, age, gender, phoneno, result, postprocess)
    send_email(number_report, email, name, gender, age, result, postprocess["height"], postprocess["width"], postprocess["area"], postprocess["location"], suggest["description"], suggest["what_to_do"], suggest["who_to_consult"], suggest["result"])

    return render_template('pass.html', n=name, id=number_report)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0")