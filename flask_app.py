from flask import Flask, render_template
import os
<<<<<<< Updated upstream
=======
from disorder_model import DisorderPredictor
from explainer import Explainer
import tensorflow
tensorflow.compat.v1.disable_v2_behavior()
>>>>>>> Stashed changes

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', template_folder='templates')

<<<<<<< Updated upstream
=======

@app.route("/", methods=["GET", "POST"])
def predict():

    # get user input
    # age = float(request.form['age'])
    # bcc = float(request.form['bcc'])
    # mother_age = float(request.form['motherAge'])
    # father_age = float(request.form['fatherAge'])
    # abortions = float(request.form['abortions'])
    # wbcc = float(request.form['wbcc'])
    # mother_gene = float(request.form['motherGene'])
    # father_gene = float(request.form['fatherGene'])
    # maternal_gene = float(request.form['maternalGene'])
    # paternal_gene = float(request.form['paternalGene'])
    # status = float(request.form['status'])
    # rr = float(request.form['rr'])
    # hr = float(request.form['hr'])
    # risk = float(request.form['risk'])
    # gender = float(request.form['gender'])
    # folic_acid = float(request.form['folicAcid'])
    # maternal_illness = float(request.form['maternalIllness'])
    # conceptive = float(request.form['conceptive'])
    # anomalies = float(request.form['anomalies'])
    # defects = float(request.form['defects'])
    # blood_test = float(request.form['bloodTest'])
    # symptom1 = float(request.form['symptom1'])
    # symptom2 = float(request.form['symptom2'])
    # symptom3 = float(request.form['symptom3'])
    # symptom4 = float(request.form['symptom4'])
    # symptom5 = float(request.form['symptom5'])

    age = 4
    bcc = 4.5
    mother_age = 41
    father_age = 49
    abortions = 4
    wbcc = 12
    mother_gene = 1
    father_gene = 0
    maternal_gene = 1
    paternal_gene = 0
    status = 0
    rr = 1
    hr = 1
    risk = 1
    gender = 0
    folic_acid = 0
    maternal_illness = 1
    conceptive = 1
    anomalies = 1
    defects = 0
    blood_test = 1
    symptom1 = 1
    symptom2 = 1
    symptom3 = 1
    symptom4 = 1
    symptom5 = 1

    # make prediction
    (prediction, genetic_explainer, subclass_explainer) = model.predict(explainer, age, bcc, mother_age, father_age, abortions, wbcc, mother_gene,
                                                                        father_gene, maternal_gene, paternal_gene, status, rr, hr, risk, gender, folic_acid, maternal_illness,
                                                                        conceptive, anomalies, defects, blood_test, symptom1, symptom2, symptom3, symptom4, symptom5)

    # prediction = model.predict(explainer, age, bcc, mother_age, father_age, abortions, wbcc, mother_gene,
    #                            father_gene, maternal_gene, paternal_gene, status, rr, hr, risk, gender, folic_acid, maternal_illness,
    #                            conceptive, anomalies, defects, blood_test, symptom1, symptom2, symptom3, symptom4, symptom5)  # all the features

    return render_template("result.html", template_folder='templates', result=str(prediction), shap_plot1=genetic_explainer, shap_plot2=subclass_explainer)
    # return render_template("result.html", template_folder='templates', result=str(prediction))

>>>>>>> Stashed changes
###

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
