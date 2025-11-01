import streamlit as st
import math

# ---- PAGE CONFIG ----
st.set_page_config(page_title="Casio fx-991EX (Simulator)", page_icon="🧮", layout="centered")

# ---- STYLING ----
st.markdown("""
    <style>
        .main {
            background-color: #1c1c1c;
            color: white;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        .stTextInput>div>div>input {
            background-color: #333333;
            color: #00ffcc;
            text-align: right;
            font-size: 24px;
            border: 2px solid #00ffcc;
            border-radius: 10px;
            height: 60px;
        }
        div[data-testid="stHorizontalBlock"] > div {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 6px;
        }
        button[kind="secondary"] {
            background-color: #2a2a2a !important;
            color: white !important;
            border-radius: 8px !important;
            height: 50px !important;
            width: 70px !important;
            font-size: 18px !important;
        }
        button[kind="secondary"]:hover {
            background-color: #00b894 !important;
            color: black !important;
        }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.title("🧮 Casio fx-991EX (Simulator)")
st.write("A Streamlit-based scientific calculator")

# ---- INPUT DISPLAY ----
expression = st.text_input("Expression", value="", placeholder="Enter expression or use buttons below")

# ---- BUTTON GRID ----
buttons = [
    ["7", "8", "9", "/", "sin"],
    ["4", "5", "6", "*", "cos"],
    ["1", "2", "3", "-", "tan"],
    ["0", ".", "(", ")", "+"],
    ["sqrt", "log", "ln", "^", "!"],
    ["π", "e", "C", "⌫", "="]
]

# Maintain session state
if "exp" not in st.session_state:
    st.session_state.exp = ""

def evaluate_expression(exp):
    """Safely evaluate mathematical expression."""
    try:
        exp = exp.replace("^", "**").replace("π", str(math.pi)).replace("e", str(math.e))
        exp = exp.replace("sin", "math.sin").replace("cos", "math.cos").replace("tan", "math.tan")
        exp = exp.replace("log", "math.log10").replace("ln", "math.log")
        exp = exp.replace("sqrt", "math.sqrt")
        if "!" in exp:
            parts = exp.split("!")
            exp = str(math.factorial(int(eval(parts[0]))))
        return eval(exp)
    except:
        return "Error"

# ---- BUTTON HANDLER ----
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            if btn == "=":
                st.session_state.exp = str(evaluate_expression(st.session_state.exp))
            elif btn == "C":
                st.session_state.exp = ""
            elif btn == "⌫":
                st.session_state.exp = st.session_state.exp[:-1]
            elif btn == "!":
                st.session_state.exp += "!"
            else:
                st.session_state.exp += btn

# Display the updated expression
st.text_input("Result", value=st.session_state.exp, key="result_display")

# ---- FOOTER ----
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Casio-style UI")

