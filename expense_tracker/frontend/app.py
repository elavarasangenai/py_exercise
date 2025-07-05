import streamlit as st
import requests
import pandas as pd

st.title("💸 Simple Expense Tracker")

# Input Form
st.subheader("Add New Expense")
category = st.selectbox("Category", ["Food", "Transport", "Utilities", "Entertainment", "Others"])
amount = st.number_input("Amount", min_value=0.0, format="%.2f")
note = st.text_input("Note (optional)")

if st.button("Add Expense"):
    payload = {
        "category": category,
        "amount": amount,
        "note": note
    }
    response = requests.post("http://localhost:5000/add_expense", json=payload)
    if response.status_code == 200:
        st.success("Expense added successfully!")
    else:
        st.error("Failed to add expense.")

# Show Expense List
st.subheader("📊 Expense History")

res = requests.get("http://localhost:5000/get_expenses")
if res.status_code == 200:
    data = res.json()
    if data:
        df = pd.DataFrame(data)
        st.dataframe(df)
        total = sum(item['amount'] for item in data)
        st.markdown(f"### 💰 Total Spent: ₹{total:.2f}")
        # Bar chart: Category-wise spent
        category_totals = df.groupby('category')['amount'].sum().reset_index()
        st.bar_chart(category_totals.set_index('category'))
    else:
        st.info("No expenses added yet.")
