import streamlit as st

# Initial balance (you can make this dynamic later with files/databases)
if "balance" not in st.session_state:
    st.session_state.balance = 1000  # starting balance

st.title("💳 Mini ATM App")
st.subheader("Welcome to Stephin's ATM 💰")

# Show current balance
st.info(f"🧾 Current Balance: ₹{st.session_state.balance}")

# Select operation
operation = st.selectbox("Choose Operation", ["Deposit", "Withdraw"])

# Enter amount
amount = st.number_input("Enter Amount", min_value=1, step=1)

# Perform action on button click
if st.button("Submit"):
    if operation == "Deposit":
        st.session_state.balance += amount
        st.success(f"✅ ₹{amount} deposited successfully!")
    elif operation == "Withdraw":
        if amount > st.session_state.balance:
            st.error("❌ Insufficient balance!")
        else:
            st.session_state.balance -= amount
            st.success(f"✅ ₹{amount} withdrawn successfully!")

# Show updated balance
st.info(f"📊 Updated Balance: ₹{st.session_state.balance}")
