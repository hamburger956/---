from include.CalculatorView import CalculatorView
from include.CalculatorView import ScientificCalculatorView
from include.CalculatorModel import CalculatorModel
from include.CalculatorModel import ScientificCalculatorModel
from src.CalculatorController import CalculatorController

class CalculatorConfig:
    """
    计算器配置类,处理初始化配置
    """
    TITLE = "简易计算器"
    SIZE = "400x600"
    ICONPATH = r'.\favicon.ico'


def normal_calculator():
    model = CalculatorModel()
    view = CalculatorView(title=CalculatorConfig.TITLE,
                        size=CalculatorConfig.SIZE ,
                        iconPath=CalculatorConfig.ICONPATH)
    return model,view

def scientific_calculator():
    model = ScientificCalculatorModel()
    view = ScientificCalculatorView(title=CalculatorConfig.TITLE,
                                              size=CalculatorConfig.SIZE,
                                              iconPath=CalculatorConfig.ICONPATH)
    return model,view


if __name__ == "__main__":
    controller = CalculatorController(*scientific_calculator())
    controller.run()
