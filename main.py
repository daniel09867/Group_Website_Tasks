from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_task():
    task = request.form.get("task")
    print("Получена задача:", task)
    return "Задача получена!"


if __name__ == "__main__":
    app.run(debug=True)