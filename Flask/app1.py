from flask import Flask, request, render_template_string

app1 = Flask(__name__)

@app1.route("/hello")   # default: GET only
def hello():
    return "Hello via GET!"

@app1.route("/submit", methods=["POST"])
def submit():
    data = request.form["name"]
    return f"Received: {data}"

@app1.route("/both", methods=["GET", "POST"])
def both():
    if request.method == "POST":
        name = request.form.get("name", "Anonymous")
        return f"Handled POST request, got: {name}"
    else:
        # Show a simple HTML form when accessed via GET
        return render_template_string("""
            <h2>Enter your name</h2>
            <form method="POST">
                <input type="text" name="name" placeholder="Your name">
                <button type="submit">Submit</button>
            </form>
        """)

if __name__ == "__main__":
    print("Starting Flask server...")

    app1.run(debug=True)
