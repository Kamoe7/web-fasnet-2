from flask import Flask,render_template,jsonify

app=Flask(__name__)


JOBS=[
  {
    'id':'1',
    'title':'SOFTWARE ENGINNER',
    'location':'China,Beijing',
    'salary':'RMB 50,00,000'
  },
  {
    'id':'2',
    'title':'PYTHON DEVELOPER',
    'location':'China,Shanghai',
    'salary':'RMB 40,00,000'
  },
  {
    'id':'3',
    'title':'DATA SCIENCTIC',
    'location':'China,Senzen',
    'salary':'RMB 45,00,000'
  },
  {
    'id':'4',
    'title':'PRODUCT MANAGEMENT',
    'location':'China,Chongqing',
  
  }
]
@app.route("/")


def hello_world():
  return render_template("home.html",jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__=="__main__":
  app.run(host='0.0.0.0',debug=True)