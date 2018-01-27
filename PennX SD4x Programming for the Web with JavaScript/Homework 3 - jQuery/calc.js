var calcController = (function () {

    var functionMap = {
        "addButton" : (a, b) => a + b,
        "subtractButton" : (a, b) => a - b,
        "multiplyButton" : (a, b) => a * b,
        "divideButton" : (a, b) => a / b
    };

    var InputTypeEnum = {
        DIGIT: 1,
        NONDIGIT: 2
    };
    var stack = [];
    var previousInputType = InputTypeEnum.NONDIGIT;

    // values at index 0 and 2, operator at index 1
    var calculate = function() {
        return functionMap[stack[1]](stack[0], stack[2]);
    };

    var reset = function() {
        stack = [];
        previousInputType = InputTypeEnum.NONDIGIT;
    };

    return {

        requireResetStack: function() { // Starting a new operation (previous input is equals, and is called only when current input is digit)
            return stack.length === 1 || stack.length === 3; 
        },
        
        requrieResetDisplay: function() {
            return previousInputType == InputTypeEnum.NONDIGIT;
        },

        digitInput: function() {
            previousInputType = InputTypeEnum.DIGIT;
        },

        operatorInput: function(operator, numDisplay) {
            var result;
            if (stack.length === 3) { // Continuing an operation after having completed the previous one with equals
                stack = [];
                stack.push(numDisplay);
                stack.push(operator);
            } else if (stack.length == 2) { // First operand and the operator is ready
                if (previousInputType == InputTypeEnum.NONDIGIT) { // User enters an operator, and then a different operator, the first operator should be ignored and the second operator should be used in the operation.
                    stack[1] = operator;
                } else { // User has inputted the second operand and then another operator, performing an operation on multiple numbers
                    stack.push(numDisplay);
                    result = calculate();
                    stack = [result, operator];
                }
            } else if (stack.length == 1) { // User enters the first operand and then the equals and then the operator
                stack.push(operator);
            } else { // Stack is empty, user enters the first operand and then the operator
                stack = [numDisplay, operator];
            }
            previousInputType = InputTypeEnum.NONDIGIT;

            return result;
        },

        equalsInput: function(numDisplay) {
            var result;
            if (stack.length == 0) {
                if (previousInputType == InputTypeEnum.DIGIT) { // User have inputted some digits and then the equals
                    stack = [numDisplay];
                }
            } else if (stack.length == 2) {  
                if (previousInputType == InputTypeEnum.DIGIT) { // Performing an operation on two numbers
                    stack.push(numDisplay);
                    result = calculate(stack);
                }
            } else if (stack.length == 3) { // If the user has just completed an operation using the equals button and then clicks the equals button again, the previous operation should be repeated using the result of the operation and the most recently entered operand.
                stack[0] = numDisplay;
                result = calculate(stack);
            }
            return result;
        },

        reset: function() {
            reset();
        }
    };
})();

var UIController = (function() {

    var DOMstrings = {
        digitBtn: '.digit',
        operatorBtn: '.operator',
        displayInput: '#display',
        clearBtn: '#clearButton',
        equalsBtn: '#equalsButton'
    };

    return {
        getDOMstrings: function() {
            return DOMstrings;
        },

        updateDisplay: function(number) {
            if (number != null)
                $(DOMstrings.displayInput).val(number);
        },

        appendDigit: function(digit) {
            var display = $(DOMstrings.displayInput).val();
            display += digit;
            $(DOMstrings.displayInput).val(display);
        },

        reset: function() {
            $(DOMstrings.displayInput).val('');
        },
        
        getDisplayNum: function() {
            return Number($(DOMstrings.displayInput).val());
        }
    };
})();

var controller = (function(calcCtrl, UICtrl) {

    var setupEventListeners = function() {
        var DOM = UICtrl.getDOMstrings();

        $(DOM.digitBtn).click(digitClickHandler);
        $(DOM.clearBtn).click(clearClickHandler);
        $(DOM.operatorBtn).click(operatorClickHandler);
        $(DOM.equalsBtn).click(equalsClickHandler);
    };

    var digitClickHandler = function() {
        if (calcCtrl.requireResetStack()) {
            calcCtrl.reset();
        }
        if (calcCtrl.requrieResetDisplay()) {
            UICtrl.reset();
        }

        UICtrl.appendDigit($(this).val());
        calcCtrl.digitInput();
    };

    var clearClickHandler = function() {
        calcCtrl.reset();
        UICtrl.reset();
    };

    var operatorClickHandler = function() {
        var result = calcCtrl.operatorInput(this.id, UICtrl.getDisplayNum());
        UICtrl.updateDisplay(result);
    };

    var equalsClickHandler = function() {
        var result = calcCtrl.equalsInput(UICtrl.getDisplayNum());
        UICtrl.updateDisplay(result);
    };

    return {
        init: function() {
            console.log('Application has started.');
            setupEventListeners();
        }
    };

})(calcController, UIController);

controller.init();