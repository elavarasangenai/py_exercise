from flask import Flask, request, jsonify
import datetime

app = Flask(__name__)
expenses = []

@app.route("/add_expense", methods=["POST"])
def add_expense():
    data = request.json
    expense = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "category": data["category"],
        "amount": float(data["amount"]),
        "note": data.get("note", "")
    }
    expenses.append(expense)
    return jsonify({"message": "Expense added", "data": expense})

@app.route("/get_expenses", methods=["GET"])
def get_expenses():
    return jsonify(expenses)

if __name__ == "__main__":
    app.run(debug=True)
