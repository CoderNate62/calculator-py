import streamlit as st
from calculator import Calculator

def main():
    st.set_page_config(page_title="Calculator", page_icon="🧮")
    st.title("Physical Calculator")

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

    # UI Layout
    
    # Display Screen
    # Using markdown to create a styled box or just a large text
    st.markdown(
        f"""
        <div style="
            border: 2px solid #555;
            padding: 10px;
            border-radius: 5px;
            font-size: 30px;
            text-align: right;
            margin-bottom: 20px;
            background-color: #222;
        ">
            {st.session_state.display}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Grid Layout
    # Row 1: 7, 8, 9, /
    c1, c2, c3, c4 = st.columns(4)
    c1.button("7", on_click=input_number, args=('7',), use_container_width=True)
    c2.button("8", on_click=input_number, args=('8',), use_container_width=True)
    c3.button("9", on_click=input_number, args=('9',), use_container_width=True)
    c4.button("÷", on_click=set_operator, args=('/',), use_container_width=True)

    # Row 2: 4, 5, 6, *
    c1, c2, c3, c4 = st.columns(4)
    c1.button("4", on_click=input_number, args=('4',), use_container_width=True)
    c2.button("5", on_click=input_number, args=('5',), use_container_width=True)
    c3.button("6", on_click=input_number, args=('6',), use_container_width=True)
    c4.button("×", on_click=set_operator, args=('*',), use_container_width=True)

    # Row 3: 1, 2, 3, -
    c1, c2, c3, c4 = st.columns(4)
    c1.button("1", on_click=input_number, args=('1',), use_container_width=True)
    c2.button("2", on_click=input_number, args=('2',), use_container_width=True)
    c3.button("3", on_click=input_number, args=('3',), use_container_width=True)
    c4.button("-", on_click=set_operator, args=('-',), use_container_width=True)

    # Row 4: C, 0, =, +
    c1, c2, c3, c4 = st.columns(4)
    c1.button("C", on_click=clear, use_container_width=True)
    c2.button("0", on_click=input_number, args=('0',), use_container_width=True)
    c3.button("=", on_click=calculate, use_container_width=True)
    c4.button("+", on_click=set_operator, args=('+',), use_container_width=True)

if __name__ == "__main__":
    main()
