from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculate():
    age = ''
    bmi = ''
    children = ''
    smoking = ''
    gender = ''
    gender_female = ''
    gender_male= ''
    insurance = ''

    if request.method == 'POST' and 'age' in request.form and 'bmi' in request.form:
        age = request.form.get('age')
        bmi = request.form.get('bmi')
        children = request.form.get('children')
        smoking = request.form.get('smoking')
        gender = request.form.get('gender')
        if smoking=='yes' or smoking=='Yes' or smoking=='YES':
            smoking_yes=1
        elif smoking=='no' or smoking=='No'or smoking=='NO':
            smoking_yes=0
        if gender=='male' or gender=='Male' or gender=='MALE': 
            gender_male=1
            gender_female=0
        elif gender=='female' or gender=='Female' or gender=='FEMALE': 
            gender_male=0
            gender_female=1

        insurance = round(5633.51+(3715.28*int(age))+(1999.61*int(bmi))+(651.17*int(children))+(23530*int(smoking_yes)+2616.04*int(gender_male)+3017.46*int(gender_female)),2)

    return render_template("index.html", age=age, bmi=bmi, children=children, smoking=smoking,gender=gender,insurance=insurance)

if __name__ == '__main__':
    app.run(debug=True)
