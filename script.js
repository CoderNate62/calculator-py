// Catculator - A cute cat-themed scientific calculator
// Coded by Nate

// Calculator State
let display = '0';
let storedValue = null;
let pendingOperator = null;
let resetNext = false;

// DOM Elements
const displayElement = document.getElementById('display');
const catReactionElement = document.getElementById('catReaction');

// Update Display
function updateDisplay() {
    displayElement.textContent = display;
    catReactionElement.textContent = getCatReaction(display);
}

// Get cat reaction based on result
function getCatReaction(displayValue) {
    try {
        const val = parseFloat(displayValue);
        if (isNaN(val)) {
            if (displayValue === 'Error') {
                return '😿'; // Crying cat for errors
            }
            return '😺';
        }
        if (val === 0) {
            return '😺'; // Neutral cat
        } else if (val < 0) {
            return '🙀'; // Shocked cat for negatives
        } else if (val > 1000000) {
            return '😻'; // Heart eyes for big numbers
        } else if (val > 1000) {
            return '😸'; // Grinning cat
        } else if (val === 42) {
            return '😹'; // Joy cat - meaning of life!
        } else if (val === 69 || val === 420) {
            return '😼'; // Smirking cat
        } else if (val < 1 && val > 0) {
            return '🐱'; // Simple cat for small decimals
        } else {
            return '😺'; // Happy cat
        }
    } catch {
        return '😺';
    }
}

// Format result (remove trailing zeros for integers)
function formatResult(result) {
    if (Number.isInteger(result)) {
        return String(result);
    }
    // Round to avoid floating point issues, max 10 decimal places
    return String(Math.round(result * 1e10) / 1e10);
}

// Input a number digit
function inputNumber(digit) {
    if (resetNext) {
        display = digit;
        resetNext = false;
    } else {
        if (display === '0') {
            display = digit;
        } else {
            display += digit;
        }
    }
    updateDisplay();
}

// Input mathematical constants
function inputConstant(constant) {
    let value;
    if (constant === 'pi') {
        value = Math.PI;
    } else if (constant === 'e') {
        value = Math.E;
    }
    display = formatResult(value);
    resetNext = true;
    updateDisplay();
}

// Set operator for binary operations
function setOperator(op) {
    if (pendingOperator !== null && !resetNext) {
        calculate();
    }
    storedValue = parseFloat(display);
    pendingOperator = op;
    resetNext = true;
}

// Calculate result
function calculate() {
    if (pendingOperator && storedValue !== null) {
        try {
            const currentVal = parseFloat(display);
            let result = 0;

            switch (pendingOperator) {
                case '+':
                    result = storedValue + currentVal;
                    break;
                case '-':
                    result = storedValue - currentVal;
                    break;
                case '*':
                    result = storedValue * currentVal;
                    break;
                case '/':
                    if (currentVal === 0) {
                        throw new Error('Cannot divide by zero');
                    }
                    result = storedValue / currentVal;
                    break;
                case '^':
                    result = Math.pow(storedValue, currentVal);
                    break;
            }

            display = formatResult(result);
            storedValue = null;
            pendingOperator = null;
            resetNext = true;
        } catch (e) {
            display = 'Error';
            storedValue = null;
            pendingOperator = null;
            resetNext = true;
        }
    }
    updateDisplay();
}

// Unary operations (immediate execution)
function unaryOperation(op) {
    try {
        const currentVal = parseFloat(display);
        let result;

        switch (op) {
            case 'sqrt':
                if (currentVal < 0) {
                    throw new Error('Cannot calculate square root of negative');
                }
                result = Math.sqrt(currentVal);
                break;
            case 'log':
                if (currentVal <= 0) {
                    throw new Error('Log undefined for non-positive');
                }
                result = Math.log(currentVal);
                break;
            case 'sin':
                result = Math.sin(currentVal);
                break;
            case 'cos':
                result = Math.cos(currentVal);
                break;
            case 'tan':
                result = Math.tan(currentVal);
                break;
        }

        display = formatResult(result);
        resetNext = true;
    } catch (e) {
        display = 'Error';
        resetNext = true;
    }
    updateDisplay();
}

// Clear calculator
function clearCalc() {
    display = '0';
    storedValue = null;
    pendingOperator = null;
    resetNext = false;
    updateDisplay();
}

// Initialize display on load
updateDisplay();
