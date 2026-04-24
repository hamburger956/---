from include.CalculatorView import CalculatorView
from include.CalculatorModel import CalculatorModel
from src.CalculatorController import CalculatorController

class CalculatorConfig:
    """
    计算器配置类,处理初始化配置
    """
    TITLE = "简易计算器"
    SIZE = "400x600"
    ICONPATH = r'.\favicon.ico'

if __name__ == "__main__":
    model = CalculatorModel()
    view = CalculatorView(title=CalculatorConfig.TITLE,
                        size=CalculatorConfig.SIZE ,
                        iconPath=CalculatorConfig.ICONPATH)
    
    controller = CalculatorController(model, view)
    controller.run()
