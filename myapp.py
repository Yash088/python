from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
	return render_template("index.html")
@app.route('/form',methods=["post"])
def fb():
	name= request.form["name"]
	enroll= request.form["enroll"]
	mail= request.form["pwd"]
	print(enroll,name,mail)
	return render_template("new.html",enroll=enroll,name=name,mail=mail)
if(__name__=='__main__'):
	app.run(debug=True)

