from include.CalculatorModel import CalculatorModel
from include.CalculatorView import CalculatorView

class CalculatorController:
    """
    控制器,连接 Model 和 View,将按钮事件路由到具体业务方法。
    """

    def __init__(self,model: CalculatorModel, view: CalculatorView):
        self.model = model
        self.view = view


    def on_digit_click(self, digit: str):
        """
        处理数字点击事件
        """
        self.model.press_digit(digit)
        self.view.update_var(self.model.displayResult, self.model.userInput)

    def on_operation_click(self, operation: str):
        """
        处理运算符点击事件
        """
        self.model.press_operation(operation)
        self.view.update_var(self.model.displayResult, self.model.userInput)


    def create_result_label(self):
        """
        创建label
        """
        self.view.create_result_label()

    
    def create_buttons(self):
        """
        创建按钮
        """
        self.view.create_buttons(self.model.digits, self.on_digit_click, self.on_operation_click)

    def _pack(self):
        self.create_buttons()
        self.create_result_label()

    def run(self):
        """
        运行
        """
        self._pack()
        self.view.run()