from flask import Flask, request, render_template,redirect

app = Flask(__name__)

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Hello {name}!"
    return render_template("form.html")

@app.route("/")
def home():
    return render_template("index.html")

#jinga 2 technique
   #variable rule

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>50:
        res='PASSED'
    else:
        res='FAILED'

    return render_template('result.html', results=res)


@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])  # <-- missing closing quote fixed
        total_score = (science + maths + c + data_science) / 4

    return render_template('result1.html', results=total_score)



if __name__ == "__main__":
    app.run(debug=True)
