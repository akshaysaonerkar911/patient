from flask import Flask,render_template,request
import pickle

app = Flask(__name__)

model = pickle.load(open("patient.pkl","rb"))


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/patient",methods=["GET","POST"])
def patient():
    Age = int(request.form.get("Age"))
    Gender = int(request.form.get("Gender"))
    Total_Bilirubin = float(request.form.get("Total_Bilirubin"))
    Direct_Bilirubin = float(request.form.get("Direct_Bilirubin"))
    Alkaline_Phosphotase = int(request.form.get("Alkaline_Phosphotase"))
    Alamine_Aminotransferase = int(request.form.get("Alamine_Aminotransferase"))
    Aspartate_Aminotransferase =int(request.form.get("Aspartate_Aminotransferase"))
    Total_Protiens = float(request.form.get("Total_Protiens"))
    Albumin = float(request.form.get("Albumin"))
    Albumin_and_Globulin_Ratio = float(request.form.get("Albumin_and_Globulin_Ratio"))

    result = model.predict([[Age,Gender,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens,Albumin,Albumin_and_Globulin_Ratio]])

    if result[0]==0:
        return "liver is detect"
    else:
        return "liver is not detect"


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
