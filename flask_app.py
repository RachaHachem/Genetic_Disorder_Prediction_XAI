from flask import Flask, render_template, request
import os
from disorder_model import DisorderPredictor

app = Flask(__name__)

model_path1 = 'genetic_disorder_model.h5'
model_path2 = 'subclass_model.h5'


model = DisorderPredictor(model_path1, model_path2)

# @app.route('/')
# def home():
#     return render_template('index.html', template_folder='templates')


@app.route("/", methods=["GET", "POST"])
def predict():

    # get user input
    age = request.form['age']
    # continue with all the features

    # make prediction
    prediction = model.predict(age, )  # all the features

    return render_template("index.html", result=str(prediction))

###


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
