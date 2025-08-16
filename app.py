# Flask App Routing
from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__) # "__..__"entry point of an program

@app.route("/",methods=["GET"]) # "/" = denotes the first url page
def welcome():
    return "<h1>Welcome to the Route Tutorial!</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h2>Welcome to the index page!</h2>"

# Variable Rule: Assign the data type to the parameter or a variable is called variable rule. 
@app.route("/success/<int:score>")  # score is the parameter here
def success(score):
    return "The student has passed and scored marks:" + str(score)  # cuz str here the int is working.

@app.route("/fail/<int:score>")  # score is the parameter here
def fail(score):
    return "The student has failed and scored marks:" + str(score) 

@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template("form.html")
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        avg_marks=(maths+science+history)/3

        res=""
        if avg_marks>=33:
            res = "success"
        else:
            res="fail"
        
        return redirect(url_for(res,score=avg_marks))
        #return render_template('form.html',score=avg_marks)

@app.route("/api", methods=["POST"])
def calcuate_sum():
    data=request.get_json()
    a_val=float(dict(data)['a'])
    b_val=float(dict(data)['b'])
    return jsonify(a_val+b_val)

if __name__ == "__main__":
    app.run(debug=True)
