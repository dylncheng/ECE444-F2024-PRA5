from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)


model = None
vectorizer = None
with open('basic_classifier.pkl', 'rb') as fid:
        model = pickle.load(fid)
with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)


@application.route("/")
def index():
    return "Hello World"

@application.route("/predict", methods=['POST'])
def make_prediction():
        data = request.get_json()
        article_text = data.get("article", "")
        prediction = model.predict(vectorizer.transform([article_text]))[0]
        return jsonify({"prediction": 0 if prediction == 'FAKE' else 1})


if __name__ == "__main__":
    application.run(port=5000, debug=True)