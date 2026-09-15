from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Show the form when visiting the root
    return render_template('form.html')

@app.route('/submit', methods=['POST'])   # ✅ Only POST allowed here
def submit():
    # Process form data only on POST
    science = float(request.form.get('science', 0))
    maths = float(request.form.get('maths', 0))
    c = float(request.form.get('c', 0))
    data_science = float(request.form.get('datascience', 0))

    total_score = (science + maths + c + data_science) / 4

    # Redirect to result2 route with query parameters
    return redirect(url_for(
        'result2',
        science=science,
        maths=maths,
        c=c,
        datascience=data_science,
        score=total_score
    ))

@app.route('/result2', methods=['GET'])   # ✅ GET allowed here
def result2():
    # Retrieve query parameters from redirect
    science = float(request.args.get('science', 0))
    maths = float(request.args.get('maths', 0))
    c = float(request.args.get('c', 0))
    datascience = float(request.args.get('datascience', 0))
    score = float(request.args.get('score', 0))

    return render_template(
        'result2.html',
        science=science,
        maths=maths,
        c=c,
        datascience=datascience,
        results=score
    )

if __name__ == "__main__":
    app.run(debug=True)
