from flask import Flask, request
import jsonify

app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'


@app.route("/model", methods=['POST'])
def model():
   if request.method == 'POST':

      result = {"key":"안녕하세요"}

   return jsonify(result), 200

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)