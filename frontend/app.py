from flask import Flask, render_template, flash, request
import requests
from os import environ

app = Flask(__name__)

def tfserving_request(req_input, model_name): #1
    url = f"http://localhost:8501/v1/models/{model_name}:predict" #2
    input_request = {"instances": [req_input]} #3
    response = requests.post(url=url, json=input_request) #4
    return response


@app.route("/home",methods=["GET","POST"]) #1
def home():
    if request.method == "POST": #2

        inp1 = int(request.form["inp1"]) #3
        inp2 = int(request.form["inp2"])

        response = tfserving_request([inp1,inp2], "1602624873") #4

        resp = response.json() #5
        flash(f"obtained {inp1} and {inp2} have a prediction of {resp['predictions']}", 'success') #6

    return render_template("index.html") #7

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(environ.get('PORT', 8080)))