import math


class CalculatorModel:
    """
    计算器模型类，负责处理计算器的核心逻辑和数据
    """
    def __init__(self):
        self.userInput = ""  # 储存用户输入,即清屏前用户所输入的总表达式
        self.displayResult = ""  # 始终为当前计算器上显示的值,不包含历史值

        self.operationClicked = False  # 用于判断是否点击符号(不包含等于)
        self.equalsClicked = False  # 用于判断是否点击等于符号

        self.digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', ]
        self.operations = ['+', '-', 'x', '÷', '⌫', 'C', '^', '+/-', ]

        self.operation_handlers = {
            "C": self._handle_clear,
            "=": self._solve_number,
            "⌫": self._handle_backspace,
            "+/-": self._handle_toggle_sign,
        }

    def press_digit(self, digit: str):
        """
        处理数字按键点击事件
        """
        if self.operationClicked:
            self._handle_operation_clicked()

        if self.equalsClicked:
            self._handle_equals_clicked()

        if digit in ["."]:
            digit = self._validate_decimal_point(digit)

        self._append_digit(digit)
        self.userInput += digit


    def press_operation(self,operation: str):
        """
        处理符号按键点击事件
        """

        if operation == "C": #优先处理清除符号
            self.operation_handlers[operation]()
            return

        if self.displayResult in ["∞", "Error"]:
            return

        if self.userInput == "":
            self.userInput += "0"

        if operation in self.operation_handlers:
            self.operation_handlers[operation]()
        else:
            self._handle_basic_operation(operation)
            if self.equalsClicked:self.equalsClicked = False 
    
    # 处理一般符号点击事件
    def _handle_operation_clicked(self):
        self.userInput += self.displayResult
        self.operationClicked = False


    # 处理等于符号点击事件
    def _handle_equals_clicked(self):
        self._clear()
        self.equalsClicked = False


    # 处理小数点点击事件
    def _validate_decimal_point(self, digit: str) -> str:
        if digit in self.displayResult:
            return ""
        if self.displayResult in self.operations or not self.displayResult:
            return "0."
        return digit


    # 添加数字
    def _append_digit(self, digit: str):
        if self.displayResult in self.operations:
            self.displayResult = digit
        else:
            self.displayResult += digit


    # 处理清除按钮点击事件
    def _handle_clear(self):
        self._clear()


    # 处理删除按钮点击事件
    def _handle_backspace(self):
        self.displayResult = self.displayResult[:-1]
        self.userInput = self.userInput[:-1]


    # 处理正负符号按钮点击事件
    def _handle_toggle_sign(self):
        length = len(self.displayResult)
        if length and self.displayResult not in self.operations:
            if '-' in self.displayResult:
                self.displayResult = self.displayResult[1:]
            else:
                self.displayResult = "-" + self.displayResult
            self.userInput = self.userInput[:-length] + self.displayResult


    # 处理基本运算符点击事件
    def _handle_basic_operation(self, operation: str):
        self.operationClicked = True
        self.displayResult = operation


    def _replace_operation(self):
        # 替换符号,让eval函数能正常进行
        self.userInput = self.userInput.replace("x", '*').replace("÷", '/').replace("^", "**")

        # 处理用户输入
    def _solve_number(self):
        try:
            self._replace_operation()
            self.displayResult = f"{eval(self.userInput):.10g}"  # 处理精度
            self.userInput = self.displayResult  # 保留最后输出的数字,再点击符号时,能够直接进行符号计算

        except (OverflowError, ZeroDivisionError):  # 处理无穷大
            self.displayResult = "∞"
            self.userInput = ""

        except SyntaxError:  # 处理意外输入
            self.displayResult = "Error"
            self.userInput = ""

        finally:
            self.equalsClicked = True


    # 清空
    def _clear(self):
        self.userInput = ""
        self.displayResult = ""


class ScientificCalculatorModel(CalculatorModel):
    """
    科学计算器模型类，负责处理科学计算器的核心逻辑和数据
    """
    def __init__(self):
        super().__init__()
        self.ScientificOperations = ["n!", "sin", "cos", "tan", "log", "ln", "mod"]
        self.ScientificDigits = ["π", "e", "(", ")"]
        self.digits.extend(self.ScientificDigits)
        self.operations.extend(self.ScientificOperations)

        self.operation_handlers = {
                "C": self._handle_clear,
                "=": self._solve_number,
                "⌫": self._handle_backspace,
                "+/-": self._handle_toggle_sign,
            "n!": self._handle_factorial,
            "sin": lambda: self._handle_trigonometric_functions("sin"),
            "cos": lambda: self._handle_trigonometric_functions("cos"),
            "tan": lambda: self._handle_trigonometric_functions("tan"),
            "log": lambda: self._handle_logarithm("log"),
            "ln": lambda: self._handle_logarithm("ln"),
                "mod": self._handle_mod,
        }

    def press_digit(self, digit: str):
        """
        处理数字按键点击事件
        """
        if self.operationClicked:
            self._handle_operation_clicked()

        if self.equalsClicked:
            self._handle_equals_clicked()

        if digit in ["."]:
            digit = self._validate_decimal_point(digit)

        if digit not in ["(",")"]:
            self._append_digit(digit)
        self.userInput += digit

    def _replace_operation(self):
        super()._replace_operation()
        self.userInput = self._replace_constants(self.userInput)
        self.userInput = self.userInput.replace("fact(", "math.factorial(")
        self.userInput = self.userInput.replace("sin(", "math.sin(")
        self.userInput = self.userInput.replace("cos(", "math.cos(")
        self.userInput = self.userInput.replace("tan(", "math.tan(")
        self.userInput = self.userInput.replace("log(", "math.log10(")
        self.userInput = self.userInput.replace("ln(", "math.log(")

    def _replace_constants(self, expression: str) -> str:
        import re

        expression = expression.replace("π", f"{math.pi}")
        # 仅替换独立常量 e，避免破坏科学计数法（例如 1e+10）
        return re.sub(r"(?<![0-9A-Za-z_\.])e(?![0-9A-Za-z_\.])", f"{math.e}", expression)

    def _safe_set_result(self, result_value: float):
        result_text = f"{result_value:.10g}"
        self.displayResult = result_text
        self.equalsClicked = True
        self.operationClicked = False

    def _is_binary_operator(self, char: str) -> bool:
        return char in ["+", "-", "x", "÷", "^", "%"]

    def _extract_last_operand_span(self):
        expression = self.userInput
        if not expression:
            return None

        end = len(expression)
        index = end - 1

        if expression[index] == ")":
            depth = 0
            while index >= 0:
                current_char = expression[index]
                if current_char == ")":
                    depth += 1
                elif current_char == "(":
                    depth -= 1
                    if depth == 0:
                        break
                index -= 1
            if index < 0:
                return None

            start = index
            prefix_start = start
            while prefix_start - 1 >= 0 and expression[prefix_start - 1].isalpha():
                prefix_start -= 1

            if prefix_start < start:
                prefix_name = expression[prefix_start:start]
                if prefix_name in ["sin", "cos", "tan", "log", "ln", "fact"]:
                    start = prefix_start
            return start, end

        allowed_chars = set("0123456789.πe")
        while index >= 0 and expression[index] in allowed_chars:
            index -= 1

        start = index + 1
        if start >= end:
            return None

        if index >= 0 and expression[index] == "-":
            if index == 0 or self._is_binary_operator(expression[index - 1]) or expression[index - 1] == "(":
                start = index

        return start, end

    def _safe_eval_expression(self, expression: str):
        if not expression:
            return None

        converted = expression.replace("x", "*").replace("÷", "/").replace("^", "**")
        converted = self._replace_constants(converted)
        converted = (
            converted.replace("fact(", "math.factorial(")
            .replace("sin(", "math.sin(")
            .replace("cos(", "math.cos(")
            .replace("tan(", "math.tan(")
            .replace("log(", "math.log10(")
            .replace("ln(", "math.log(")
        )
        try:
            return eval(converted, {"__builtins__": {}}, {"math": math})
        except Exception:
            return None

    def _resolve_scientific_operand(self):
        if (
            self.equalsClicked
            and self.displayResult
            and self.displayResult not in self.operations
            and self.displayResult not in ["∞", "Error"]
        ):
            display_value = self._safe_eval_expression(self.displayResult)
            if display_value is not None:
                return self.displayResult, display_value, None

        span = self._extract_last_operand_span()
        if not span:
            return None, None, None

        start, end = span
        operand_text = self.userInput[start:end]
        operand_value = self._safe_eval_expression(operand_text)
        if operand_value is None:
            return None, None, None

        return operand_text, operand_value, span

    def _apply_unary_function(self, function_name: str, calculator):
        operand_text, operand_value, span = self._resolve_scientific_operand()
        if operand_text is None:
            return

        try:
            result_value = calculator(float(operand_value))
        except Exception:
            return

        wrapped_operand = f"{function_name}({operand_text})"
        if span is None:
            self.userInput = wrapped_operand
        else:
            start, end = span
            self.userInput = self.userInput[:start] + wrapped_operand + self.userInput[end:]
        self._safe_set_result(result_value)

    def _handle_factorial(self):
        operand_text, operand_value, span = self._resolve_scientific_operand()
        if operand_text is None:
            return

        if isinstance(operand_value, bool) or operand_value < 0 or int(operand_value) != operand_value:
            return

        try:
            result_value = math.factorial(int(operand_value))
        except Exception:
            return

        wrapped_operand = f"fact({operand_text})"
        if span is None:
            self.userInput = wrapped_operand
        else:
            start, end = span
            self.userInput = self.userInput[:start] + wrapped_operand + self.userInput[end:]
        self._safe_set_result(result_value)

    def _handle_trigonometric_functions(self, operation: str):
        function_map = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
        }
        calculator = function_map.get(operation)
        if calculator is None:
            return
        self._apply_unary_function(operation, calculator)

    def _handle_logarithm(self, operation: str):
        if operation == "log":
            self._apply_unary_function("log", math.log10)
        elif operation == "ln":
            self._apply_unary_function("ln", math.log)

    def _handle_mod(self):
        if not self.userInput:
            self.userInput = "0"

        if self.userInput[-1] == "(":
            self.userInput += "0"

        if self._is_binary_operator(self.userInput[-1]):
            return

        self.userInput += "%"
        self.displayResult = "mod"
        self.operationClicked = True
        self.equalsClicked = False

    def _sanitize_expression_before_eval(self, expression: str) -> str:
        if not expression:
            return "0"

        sanitized = expression
        while sanitized and self._is_binary_operator(sanitized[-1]):
            sanitized = sanitized[:-1]

        if not sanitized:
            return "0"

        open_count = sanitized.count("(")
        close_count = sanitized.count(")")
        if open_count > close_count:
            sanitized += ")" * (open_count - close_count)

        return sanitized

    def _solve_number(self):
        self.userInput = self._sanitize_expression_before_eval(self.userInput)
        try:
            self._replace_operation()
            result_value = eval(self.userInput, {"__builtins__": {}}, {"math": math})
            self.displayResult = f"{result_value:.10g}"
            self.userInput = self.displayResult
        except (OverflowError, ZeroDivisionError):
            self.displayResult = "∞"
            self.userInput = ""
        except Exception:
            self.displayResult = "0"
            self.userInput = "0"
        finally:
            self.equalsClicked = True
            self.operationClicked = False






