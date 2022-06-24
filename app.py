from flask import *
import pickle
import numpy as np

app = Flask(__name__,template_folder='templates', static_folder='static')

model=pickle.load(open('knn.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/predict',methods=['POST'])
def predict():
    int_features=[int(x) for x in request.form.values()]
    final=[np.array(int_features)]
    prediction=model.predict(final)
    return render_template('index.html',pred = float(prediction) )
    
if __name__ == '__main__':
    app.run(debug=True)