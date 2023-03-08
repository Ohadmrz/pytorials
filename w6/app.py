import spacy
from flask import Flask, request, jsonify

app = Flask('nlp_app')
nlp = spacy.load("en_core_web_sm")


@app.route('/api/v1/sentences', methods=['POST'])
def sentences():
    doc = nlp(request.form['text'])
    response = {}
    for i, sent in enumerate(doc.sents):
        response[i+1] = sent.text
    return jsonify(response)


@app.route('/api/v1/pos', methods=['POST'])
def pos():
    print(request.args)
    return "hi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005, debug=True)