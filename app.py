import random
from flask import Flask, jsonify, render_template, request

print("Hi")

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("rollmultiple.html")


@app.route("/roll")
def roll():
    sides = request.args.get("sides", default=6, type=int)
    amount = request.args.get("amount", default=1, type=int)

    if sides < 2:
        sides = 2
    if amount < 1:
        amount = 1
    elif amount > 6:
        amount = 6

    rolls = [random.randint(1, sides) for _ in range(amount)]

    return jsonify({"results": rolls}) 


if __name__ == "__main__":
    app.run(debug=True)

