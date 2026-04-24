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
        operation_handlers = {
            "C": self._handle_clear,
            "=": self._solve_number,
            "⌫": self._handle_backspace,
            "+/-": self._handle_toggle_sign,
        }
 
        if operation == "C": #优先处理清除符号
            operation_handlers[operation]()
            return

        if self.displayResult in ["∞", "Error"]:
            return

        if operation in operation_handlers:
            operation_handlers[operation]()   
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

    
    # 处理用户输入
    def _solve_number(self):
        try:
            self.userInput = self.userInput.replace("x", '*').replace("÷", '/').replace("^", "**")  # 替换符号,让eval函数能正常进行
            self.displayResult = f"{eval(self.userInput):.10g}"  # 处理精度
            self.userInput = self.displayResult  # 保留最后输出的数字,能够直接进行符号计算

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