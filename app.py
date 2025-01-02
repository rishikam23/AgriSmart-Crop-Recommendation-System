from flask import Flask,request, url_for, redirect, render_template,config
import requests
import pickle
import numpy as np

def weather_fetch():
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    api_key = "9d7cde1f6d07ec55650544be1631307e"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + "bengaluru"
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None

app = Flask(__name__)

nbmodel=pickle.load(open('NaiveBayes.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method=="GET": 
        return redirect("/")
    if request.method=="POST":
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorous'])
        K = int(request.form['potassium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        if weather_fetch() != None:
            temperature, humidity = weather_fetch()    
        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = nbmodel.predict(data)
        prediction = my_prediction[0]
        return render_template('index.html',predictionnb=prediction,N=N,P=P,K=K,ph=ph,rainfall=rainfall,temperature=temperature,humidity=humidity)


if __name__ == '__main__':
    app.run(debug=True)