import streamlit as st
import math

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Casio fx-991EX", page_icon="🧮", layout="centered")

# ---------- STYLE ----------
st.markdown("""
<style>
    .main {
        background: radial-gradient(circle at top, #2f3542, #1e272e);
        color: white;
        font-family: 'Poppins', sans-serif;
    }
    .calc-container {
        margin: auto;
        background: linear-gradient(160deg, #2c3e50, #1e272e);
        border-radius: 25px;
        padding: 25px 25px 35px 25px;
        width: 370px;
        box-shadow: 8px 8px 20px #00000080, inset -2px -2px 8px #404956;
    }
    .casio-label {
        text-align: center;
        color: #00e5ff;
        font-weight: 700;
        font-size: 26px;
        letter-spacing: 3px;
        text-shadow: 0 0 10px #00e5ff;
        margin-bottom: 5px;
    }
    .model-label {
        text-align: center;
        color: #ddd;
        font-size: 14px;
        margin-bottom: 20px;
        letter-spacing: 1px;
    }
    .display-area {
        background: linear-gradient(145deg, #0b0c10, #111418);
        border: 2px solid #00bcd4;
        border-radius: 12px;
        color: #00ffcc;
        font-size: 23px;
        text-align: right;
        padding: 14px;
        height: 80px;
        line-height: 30px;
        box-shadow: inset 0 0 10px #00e5ff40, 0 0 8px #00e5ff40;
        margin-bottom: 15px;
    }
    .stButton>button {
        background: linear-gradient(160deg, #3a3d42, #232528);
        color: #ffffff;
        border: 1px solid #444;
        border-radius: 10px;
        height: 58px;
        width: 72px;
        font-size: 18px;
        margin: 3px;
        box-shadow: 2px 2px 6px #00000080, inset -1px -1px 4px #555;
        transition: 0.1s;
    }
    .stButton>button:hover {
        background: #00bcd4;
        color: black;
        box-shadow: 0 0 10px #00e5ff;
        transform: scale(1.03);
    }
    .shift-btn {background: #ffcb05 !important;color: black !important;font-weight: bold;}
    .alpha-btn {background: #ff4b5c !important;color: white !important;font-weight: bold;}
    .equal-btn {background: #00e676 !important;color: black !important;font-weight: bold;}
    .brand-footer {text-align: center;margin-top: 15px;font-size: 13px;color: #aaa;}
</style>
""", unsafe_allow_html=True)

# ---------- STATE ----------
if "exp" not in st.session_state:
    st.session_state.exp = ""
if "result" not in st.session_state:
    st.session_state.result = ""

# ---------- DISPLAY ----------
st.markdown("<div class='calc-container'>", unsafe_allow_html=True)
st.markdown("<div class='casio-label'>CASIO</div>", unsafe_allow_html=True)
st.markdown("<div class='model-label'>fx-991EX | Scientific Calculator</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='display-area'>
    {st.session_state.exp or '&nbsp;'}<br>
    <span style='font-size:18px;color:#00ffaa;'>{st.session_state.result or ''}</span>
</div>
""", unsafe_allow_html=True)

# ---------- EVALUATION ----------
def evaluate_expression(exp):
    try:
        exp = exp.replace("π", str(math.pi))
        exp = exp.replace("e", str(math.e))
        exp = exp.replace("^", "**")
        exp = exp.replace("√", "math.sqrt")
        exp = exp.replace("log", "math.log10")
        exp = exp.replace("ln", "math.log")
        exp = exp.replace("sin", "math.sin")
        exp = exp.replace("cos", "math.cos")
        exp = exp.replace("tan", "math.tan")
        exp = exp.replace("×", "*").replace("÷", "/")

        if "!" in exp:
            parts = exp.split("!")
            exp = str(math.factorial(int(eval(parts[0]))))

        result = eval(exp, {"__builtins__": None}, {"math": math})
        return round(result, 10)
    except ZeroDivisionError:
        return "Cannot divide by 0"
    except:
        return "Error"

# ---------- BUTTON GRID ----------
buttons = [
    ["SHIFT", "ALPHA", "MODE", "DEL", "AC"],
    ["sin", "cos", "tan", "ln", "log"],
    ["√", "^", "(", ")", "/"],
    ["7", "8", "9", "*", "π"],
    ["4", "5", "6", "-", "e"],
    ["1", "2", "3", "+", "!"],
    ["0", ".", "Ans", "EXP", "="],
]

# ---------- BUTTON ACTION ----------
clicked = None
for row in buttons:
    cols = st.columns(len(row))
    for i, btn in enumerate(row):
        css = ""
        if btn == "SHIFT": css = "shift-btn"
        elif btn == "ALPHA": css = "alpha-btn"
        elif btn == "=": css = "equal-btn"

        if cols[i].button(btn, key=f"{btn}-{i}"):
            clicked = btn

# ---------- HANDLE ACTION ----------
if clicked:
    if clicked == "AC":
        st.session_state.exp = ""
        st.session_state.result = ""
    elif clicked == "DEL":
        st.session_state.exp = st.session_state.exp[:-1]
    elif clicked == "=":
        st.session_state.result = str(evaluate_expression(st.session_state.exp))
    elif clicked == "Ans":
        if st.session_state.result:
            st.session_state.exp += st.session_state.result
    else:
        st.session_state.exp += clicked
    st.rerun()  # safe re-run only once after update

# ---------- FOOTER ----------
st.markdown("<div class='brand-footer'>🧮 Casio fx-991EX Simulator | Built with ❤️ using Streamlit</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
