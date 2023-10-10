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

const moonSVG = ``

function darkModeToggle() {
  if (!document.body.classList.contains("dark")) {
    document.body.classList.add("dark")
    document.getElementById("darkToggle").innerText = "Light"
  } else {
    document.body.classList.remove("dark")
    document.getElementById("darkToggle").innerText = "Dark"
  }
}