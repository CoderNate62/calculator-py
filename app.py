# Catculator - A cute cat-themed scientific calculator
# Coded by Nate

import streamlit as st
from calculator import Calculator
import math
import base64

def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def main():
    st.set_page_config(page_title="Catculator", page_icon="🐱")
    st.title("Catculator")
    
    # Load background image
    try:
        bin_str = get_base64_of_bin_file("cat_bg.png")
    except Exception:
        st.error("Could not load cat background.")
        bin_str = ""

    # Custom CSS for Catculator (Grid and Buttons) - Enhanced version
    st.markdown("""
        <style>
        /* Keyframe Animations */
        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(10deg); }
        }

        @keyframes float-reverse {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-15px) rotate(-10deg); }
        }

        @keyframes pulse-glow {
            0%, 100% { box-shadow: 0 0 10px rgba(255, 200, 100, 0.5), 0 3px 8px rgba(0,0,0,0.3); }
            50% { box-shadow: 0 0 20px rgba(255, 200, 100, 0.8), 0 3px 12px rgba(0,0,0,0.4); }
        }

        @keyframes title-bounce {
            0%, 100% { transform: translateX(-50%) scale(1); }
            50% { transform: translateX(-50%) scale(1.05); }
        }

        @keyframes wiggle {
            0%, 100% { transform: rotate(-3deg); }
            50% { transform: rotate(3deg); }
        }

        @keyframes button-press {
            0% { transform: scale(1); }
            50% { transform: scale(0.9); }
            100% { transform: scale(1); }
        }

        /* Custom paw cursor */
        .stApp, .stApp * {
            cursor: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'%3E%3Cellipse cx='16' cy='20' rx='8' ry='6' fill='%23D2691E'/%3E%3Ccircle cx='8' cy='12' r='4' fill='%23D2691E'/%3E%3Ccircle cx='16' cy='8' r='4' fill='%23D2691E'/%3E%3Ccircle cx='24' cy='12' r='4' fill='%23D2691E'/%3E%3Ccircle cx='10' cy='18' r='3' fill='%23FFB6C1'/%3E%3Ccircle cx='16' cy='16' r='3' fill='%23FFB6C1'/%3E%3Ccircle cx='22' cy='18' r='3' fill='%23FFB6C1'/%3E%3Cellipse cx='16' cy='23' rx='5' ry='4' fill='%23FFB6C1'/%3E%3C/svg%3E") 16 16, auto !important;
        }

        /* Lock everything to fixed dimensions */
        .stApp {
            background: linear-gradient(180deg, #87CEEB 0%, #B0E0E6 50%, #87CEEB 100%) !important;
            display: flex !important;
            justify-content: center !important;
            align-items: center !important;
            min-height: 100vh !important;
            overflow: hidden !important;
        }

        .block-container {
            position: relative !important;
            width: 450px !important;
            height: 800px !important;
            max-width: 450px !important;
            max-height: 800px !important;
            min-width: 450px !important;
            min-height: 800px !important;
            padding: 0 !important;
            margin: 20px auto !important;
            background-image: url("data:image/png;base64,__BG_IMAGE_B64__");
            background-size: 100% 100%;
            background-repeat: no-repeat;
            background-position: center;
            overflow: visible !important;
        }

        /* Floating decorations */
        .floating-decorations {
            position: fixed !important;
            top: 0 !important;
            left: 0 !important;
            width: 100% !important;
            height: 100% !important;
            pointer-events: none !important;
            z-index: 0 !important;
            overflow: hidden !important;
        }

        .paw-print {
            position: absolute !important;
            font-size: 30px !important;
            opacity: 0.3 !important;
            animation: float 4s ease-in-out infinite !important;
        }

        .fish {
            position: absolute !important;
            font-size: 25px !important;
            opacity: 0.4 !important;
            animation: float-reverse 5s ease-in-out infinite !important;
        }

        .yarn {
            position: absolute !important;
            font-size: 28px !important;
            opacity: 0.35 !important;
            animation: wiggle 2s ease-in-out infinite !important;
        }

        /* Hide default Streamlit title and padding */
        h1, .stTitle { display: none !important; }
        .stMainBlockContainer { padding: 0 !important; }

        /* Collapse Streamlit wrappers for fixed/absolute positioned content */
        .element-container:has(.floating-decorations) {
            height: 0 !important;
            min-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: visible !important;
        }

        /* Fallback for browsers without :has() - target first element container */
        .block-container > div > div:first-child .element-container:first-child {
            height: 0 !important;
            min-height: 0 !important;
            margin: 0 !important;
            padding: 0 !important;
            overflow: visible !important;
        }

        /* Catculator Title - Animated bounce */
        .catculator-title {
            position: absolute !important;
            top: 10px !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            font-family: 'Comic Sans MS', cursive, sans-serif !important;
            font-size: 38px !important;
            font-weight: bold !important;
            color: #663300 !important;
            text-shadow:
                2px 2px 0px #fff,
                -2px -2px 0px #fff,
                2px -2px 0px #fff,
                -2px 2px 0px #fff,
                3px 3px 6px rgba(0,0,0,0.3) !important;
            z-index: 1001 !important;
            white-space: nowrap !important;
            display: inline-block !important;
            animation: title-bounce 2s ease-in-out infinite !important;
        }

        /* Display Screen - Glowing effect */
        .calc-display {
            position: absolute !important;
            top: 165px !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            width: 250px !important;
            height: 55px !important;

            background: linear-gradient(145deg, #fffef5 0%, #fff8dc 100%) !important;
            color: #333 !important;
            padding: 8px 15px !important;
            border-radius: 15px !important;
            font-size: 28px !important;
            font-family: 'Comic Sans MS', sans-serif !important;
            font-weight: bold !important;
            text-align: right !important;
            border: 3px solid #8B4513 !important;
            animation: pulse-glow 2s ease-in-out infinite !important;
            z-index: 1000 !important;

            display: flex !important;
            align-items: center !important;
            justify-content: flex-end !important;
            overflow: visible !important;
        }

        /* Cat reaction emoji - positioned relative to the display */
        .cat-reaction {
            position: absolute !important;
            top: -40px !important;
            right: -25px !important;
            font-size: 32px !important;
            z-index: 1002 !important;
            animation: wiggle 0.5s ease-in-out !important;
            filter: drop-shadow(2px 2px 3px rgba(0,0,0,0.3)) !important;
        }

        /* Large invisible spacer to push buttons down to belly */
        .belly-spacer {
            height: 340px !important;
            min-height: 340px !important;
            max-height: 340px !important;
        }

        /* Force Grid Alignment */
        div[data-testid="stHorizontalBlock"] {
            flex-wrap: nowrap !important;
            white-space: nowrap !important;
            justify-content: center !important;
            gap: 6px !important;
            margin-bottom: 6px !important;
            padding-left: 20px !important;
            padding-right: 20px !important;
        }

        div[data-testid="stColumn"] {
            min-width: 64px !important;
            max-width: 64px !important;
            flex: 0 0 64px !important;
        }

        /* Button styling - Paw pad style */
        div[data-testid="stColumn"] button {
            width: 60px !important;
            height: 60px !important;
            min-height: 60px !important;
            max-height: 60px !important;
            border-radius: 45% 45% 50% 50% !important;
            padding: 0 !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            border: 3px solid rgba(0,0,0,0.2) !important;
            box-shadow:
                0 4px 8px rgba(0,0,0,0.3),
                inset 0 2px 4px rgba(255,255,255,0.3),
                inset 0 -2px 4px rgba(0,0,0,0.1) !important;
            font-size: 20px !important;
            font-weight: bold !important;
            margin: 0 auto !important;
            transition: all 0.15s ease !important;
            position: relative !important;
        }

        /* Button hover effect */
        div[data-testid="stColumn"] button:hover {
            transform: scale(1.1) !important;
            box-shadow:
                0 6px 15px rgba(0,0,0,0.4),
                inset 0 2px 4px rgba(255,255,255,0.4),
                0 0 20px rgba(255,200,100,0.5) !important;
        }

        /* Button active/press effect */
        div[data-testid="stColumn"] button:active {
            transform: scale(0.95) !important;
            box-shadow:
                0 2px 4px rgba(0,0,0,0.3),
                inset 0 1px 2px rgba(0,0,0,0.2) !important;
        }

        /* Number buttons - Brown paw pad gradient */
        button[kind="secondary"], div[data-testid="baseButton-secondary"] > button {
            background: linear-gradient(145deg, #CD853F 0%, #A0522D 50%, #8B4513 100%) !important;
            color: white !important;
            border-color: #5D4037 !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.5) !important;
        }

        button[kind="secondary"]:hover, div[data-testid="baseButton-secondary"] > button:hover {
            background: linear-gradient(145deg, #DEB887 0%, #CD853F 50%, #A0522D 100%) !important;
        }

        /* Function buttons - Coral/salmon paw pad gradient */
        button[kind="primary"], div[data-testid="baseButton-primary"] > button {
            background: linear-gradient(145deg, #FFA07A 0%, #FA8072 50%, #E9967A 100%) !important;
            color: white !important;
            border-color: #CD5C5C !important;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.4) !important;
        }

        button[kind="primary"]:hover, div[data-testid="baseButton-primary"] > button:hover {
            background: linear-gradient(145deg, #FFB6A0 0%, #FFA07A 50%, #FA8072 100%) !important;
        }

        /* Footer credit */
        .footer-credit {
            position: fixed !important;
            bottom: 15px !important;
            left: 50% !important;
            transform: translateX(-50%) !important;
            font-family: 'Comic Sans MS', cursive, sans-serif !important;
            font-size: 14px !important;
            color: #663300 !important;
            opacity: 0.8 !important;
            text-shadow: 1px 1px 2px rgba(255,255,255,0.9) !important;
            z-index: 9999 !important;
            white-space: nowrap !important;
            background: rgba(255,255,255,0.6) !important;
            padding: 5px 15px !important;
            border-radius: 15px !important;
        }
        </style>
    """.replace("__BG_IMAGE_B64__", bin_str), unsafe_allow_html=True)


    # Initialize calculator logic
    calc = Calculator()

    # Session State Initialization
    if 'display' not in st.session_state:
        st.session_state.display = '0'
    if 'stored_value' not in st.session_state:
        st.session_state.stored_value = None
    if 'pending_operator' not in st.session_state:
        st.session_state.pending_operator = None
    if 'reset_next' not in st.session_state:
        st.session_state.reset_next = False

    # Logic functions (Callbacks)
    def input_number(digit):
        if st.session_state.reset_next:
            st.session_state.display = str(digit)
            st.session_state.reset_next = False
        else:
            if st.session_state.display == '0':
                st.session_state.display = str(digit)
            else:
                st.session_state.display += str(digit)

    def set_operator(op):
        if st.session_state.pending_operator is not None and not st.session_state.reset_next:
             calculate()
        
        st.session_state.stored_value = float(st.session_state.display)
        st.session_state.pending_operator = op
        st.session_state.reset_next = True

    def calculate():
        if st.session_state.pending_operator and st.session_state.stored_value is not None:
            try:
                current_val = float(st.session_state.display)
                result = 0
                op = st.session_state.pending_operator
                
                if op == '+':
                    result = calc.add(st.session_state.stored_value, current_val)
                elif op == '-':
                    result = calc.subtract(st.session_state.stored_value, current_val)
                elif op == '*':
                    result = calc.multiply(st.session_state.stored_value, current_val)
                elif op == '/':
                    result = calc.divide(st.session_state.stored_value, current_val)
                elif op == '^':
                    result = calc.power(st.session_state.stored_value, current_val)
                
                # Format result
                if result.is_integer():
                    st.session_state.display = str(int(result))
                else:
                    st.session_state.display = str(result)
                
                st.session_state.stored_value = None
                st.session_state.pending_operator = None
                st.session_state.reset_next = True
                
            except Exception as e:
                st.session_state.display = "Error"
                st.session_state.stored_value = None
                st.session_state.pending_operator = None
                st.session_state.reset_next = True

    def clear():
        st.session_state.display = '0'
        st.session_state.stored_value = None
        st.session_state.pending_operator = None
        st.session_state.reset_next = False

    # Unary Operations (Immediate execution)
    def unary_operation(op_func):
        try:
            current_val = float(st.session_state.display)
            result = op_func(current_val)
             # Format result
            if result.is_integer():
                st.session_state.display = str(int(result))
            else:
                st.session_state.display = str(result)
            st.session_state.reset_next = True
        except Exception as e:
             st.session_state.display = "Error"
             st.session_state.reset_next = True

    # Helper function to get cat reaction based on result
    def get_cat_reaction(display_value):
        try:
            val = float(display_value)
            if val == 0:
                return "😺"  # Neutral cat
            elif val < 0:
                return "🙀"  # Shocked cat for negatives
            elif val > 1000000:
                return "😻"  # Heart eyes for big numbers
            elif val > 1000:
                return "😸"  # Grinning cat
            elif val == 42:
                return "😹"  # Joy cat - meaning of life!
            elif val == 69 or val == 420:
                return "😼"  # Smirking cat
            elif val < 1 and val > 0:
                return "🐱"  # Simple cat for small decimals
            else:
                return "😺"  # Happy cat
        except:
            if display_value == "Error":
                return "😿"  # Crying cat for errors
            return "😺"

    cat_reaction = get_cat_reaction(st.session_state.display)

    # UI Layout

    # All header elements combined in one st.markdown to minimize wrapper impact
    st.markdown(f'''
        <div class="floating-decorations">
            <span class="paw-print" style="top: 10%; left: 5%;">🐾</span>
            <span class="paw-print" style="top: 30%; right: 8%; animation-delay: 1s;">🐾</span>
            <span class="paw-print" style="top: 70%; left: 3%; animation-delay: 2s;">🐾</span>
            <span class="fish" style="top: 15%; right: 5%;">🐟</span>
            <span class="fish" style="top: 50%; left: 2%; animation-delay: 1.5s;">🐟</span>
            <span class="fish" style="bottom: 20%; right: 3%; animation-delay: 3s;">🐟</span>
            <span class="yarn" style="top: 25%; left: 8%;">🧶</span>
            <span class="yarn" style="bottom: 30%; right: 6%; animation-delay: 0.5s;">🧶</span>
        </div>
        <div class="catculator-title">🐱 Catculator 🐱</div>
        <div class="calc-display">
            <span class="cat-reaction">{cat_reaction}</span>
            {st.session_state.display}
        </div>
    ''', unsafe_allow_html=True)

    # Spacer to push buttons down to cat's belly
    st.markdown('<div class="belly-spacer"></div>', unsafe_allow_html=True)

    # Grid Layout - 5 columns for Scientific Calculator
    # Row 1: 7, 8, 9, /, ^ (Power)
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.button("7", on_click=input_number, args=('7',))
    c2.button("8", on_click=input_number, args=('8',))
    c3.button("9", on_click=input_number, args=('9',))
    c4.button("÷", on_click=set_operator, args=('/',), type="primary")
    c5.button("^", on_click=set_operator, args=('^',), type="primary")

    # Row 2: 4, 5, 6, *, √ (Sqrt)
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.button("4", on_click=input_number, args=('4',))
    c2.button("5", on_click=input_number, args=('5',))
    c3.button("6", on_click=input_number, args=('6',))
    c4.button("×", on_click=set_operator, args=('*',), type="primary")
    c5.button("√", on_click=unary_operation, args=(calc.sqrt,), type="primary")

    # Row 3: 1, 2, 3, -, log
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.button("1", on_click=input_number, args=('1',))
    c2.button("2", on_click=input_number, args=('2',))
    c3.button("3", on_click=input_number, args=('3',))
    c4.button("−", on_click=set_operator, args=('-',), type="primary")
    c5.button("log", on_click=unary_operation, args=(calc.log,), type="primary")

    # Row 4: C, 0, =, +, sin
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.button("C", on_click=clear)
    c2.button("0", on_click=input_number, args=('0',))
    c3.button("=", on_click=calculate, type="primary")
    c4.button("＋", on_click=set_operator, args=('+',), type="primary")
    c5.button("sin", on_click=unary_operation, args=(calc.sin,), type="primary")

    # Row 5: Extra Scientific: cos, tan, pi, e
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.button("cos", on_click=unary_operation, args=(calc.cos,), type="primary")
    c2.button("tan", on_click=unary_operation, args=(calc.tan,), type="primary")
    c3.button("π", on_click=input_number, args=(math.pi,), type="primary")
    c4.button("e", on_click=input_number, args=(math.e,), type="primary")
    # Empty 5th button
    c5.empty()

    # Footer credit
    st.markdown('<div class="footer-credit">Coded by Nate</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
