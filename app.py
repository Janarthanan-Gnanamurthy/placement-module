from flask import Flask, render_template, jsonify

app = Flask(__name__)

QUES=[{
    'qno':1,
    'q':'You are a legend'
},
{
    'qno':2,
    'q':'what is your name'
},
{
    'qno':3,
    'q':'what is your problem'
},
{
    'qno':4,
    'q':'you are awesome'
},
{
    'qno':5,
    'q':'you '
}]

@app.route('/')
def hello():
    return render_template('login.html')

@app.route('/course')
def course():
    return render_template('course.html',ques=QUES)

@app.route('/api/question')
def list_ques():
    return jsonify(QUES)

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True)
