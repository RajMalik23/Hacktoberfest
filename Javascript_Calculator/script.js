let displayValue = '';

function updateDisplay() {
  const display = document.getElementById('display');
  display.value = displayValue;
}

function appendNumber(number) {
  displayValue += number;
  updateDisplay();
}

function appendOperator(operator) {
  displayValue += operator;
  updateDisplay();
}

function clearDisplay() {
  displayValue = '';
  updateDisplay();
}

function calculate() {
  try {
    const result = eval(displayValue);
    displayValue = result;
    updateDisplay();
  } catch (error) {
    displayValue = 'Error';
    updateDisplay();
  }
}