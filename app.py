from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def calculate():
    age = ''
    bmi = ''
    children = ''
    smoking = ''
    insurance = ''

    if request.method == 'POST' and 'age' in request.form and 'bmi' in request.form:
        age = request.form.get('age')
        bmi = request.form.get('bmi')
        children = request.form.get('children')
        smoking = request.form.get('smoking')

        insurance = 8167.9  + (3194.18 * float(age)) + (1086.33 * float(bmi)) + (311.49 * int(children)) + (25050 * int(smoking))

    return render_template("index.html", age=age, bmi=bmi, children=children, smoking=smoking, insurance=insurance)

if __name__ == '__main__':
    app.run(debug=True)
