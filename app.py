from flask import *
import pickle
model=pickle.load(open("model.pkl","rb"))

app=Flask(__name__)

@app.route("/")
def hello():
        return render_template("home.html")

@app.route('/predict',methods=["POST"])
def predict():
        param1=request.form["variance"]
        param2=request.form["skewness"]
        param3=request.form["curtosis"]
        param4=request.form["entropy"]
        prediction=model.predict([[param1,param2,param3,param4]])
        return render_template("after.html",data=prediction)

if __name__=='__main__':
          app.run(debug=True)