import streamlit as st

# Set page title
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# App title
st.title("🧮 Simple Calculator")
st.write("A basic calculator built with Streamlit")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# Operation selection
operation = st.selectbox(
    "Select operation",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Calculate button
if st.button("Calculate"):
    if operation == "Addition (+)":
        result = num1 + num2
        st.success(f"The result of addition is: {result}")
    elif operation == "Subtraction (-)":
        result = num1 - num2
        st.success(f"The result of subtraction is: {result}")
    elif operation == "Multiplication (×)":
        result = num1 * num2
        st.success(f"The result of multiplication is: {result}")
    elif operation == "Division (÷)":
        if num2 == 0:
            st.error("Division by zero is not allowed.")
        else:
            result = num1 / num2
            st.success(f"The result of division is: {result}")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit")
