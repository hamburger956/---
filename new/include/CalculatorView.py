import ttkbootstrap as ttk
class CalculatorConfig:
    """
    计算器配置类,处理视图配置
    """
    MIN_WIDTH = 320
    MIN_HEIGHT = 520
    MAX_WIDTH = 1000
    MAX_HEIGHT = 1000
    STYLE_FONT_SIZE = 20
    DISPLAY_FONT_SIZE = 30
    INPUT_FONT_SIZE = 15
    BUTTON_WIDTH = 5
    BUTTON_PADDING = 2

class CalculatorView:
    """
    计算器的图形界面，负责创建窗口、标签、按钮，并刷新显示。
    """
    def __init__(self, title: str, size: str, iconPath: str):
        self.root = ttk.Window()
        self.root.title(title)
        self.root.iconbitmap(iconPath)
        self.root.geometry(size)
        self.root.minsize(CalculatorConfig.MIN_WIDTH, CalculatorConfig.MIN_HEIGHT)  # 尺寸限制
        self.root.maxsize(CalculatorConfig.MAX_WIDTH, CalculatorConfig.MAX_HEIGHT)

        self.displayResultVar = ttk.StringVar(master=self.root, value="")
        self.userInputVar = ttk.StringVar(master=self.root, value="")
        self._setup_style()


    def _setup_style(self):
        # ttk风格设置
        style = ttk.Style()
        style.configure("TButton", font=("Arial", CalculatorConfig.STYLE_FONT_SIZE))


    def create_result_label(self):
        """
        创建标签,处理布局
        """
        displayresultLabel = ttk.Label(master=self.root,
                                            bootstyle="dark",
                                            textvariable=self.displayResultVar,
                                            font=("黑体", CalculatorConfig.DISPLAY_FONT_SIZE), anchor='e')
        # 用户输入label
        userInputLabel = ttk.Label(master=self.root,
                                        bootstyle="secondary",
                                        textvariable=self.userInputVar,
                                        font=("黑体", CalculatorConfig.INPUT_FONT_SIZE), anchor='e')

        # 俩个标签共占四行,从第零行开始
        userInputLabel.grid(row=0, column=0,
                            rowspan=2, columnspan=4,  # 一行4个按钮,所以占4列
                            sticky='e')  # 向右对齐

        displayresultLabel.grid(row=1, column=0,  # 这里row=1而不是2是为了更贴近上面
                                rowspan=2, columnspan=4,
                                sticky='e')

        # 配置权重,俩个标签占4行
        for row in range(4):
            self.root.grid_rowconfigure(row, weight=1)


    def create_buttons(self,digits, _on_digit_click, _on_operation_click):
        """
        创建按钮,处理布局
        """
        # 数字键
        digits = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '0', '.', ]

        # 总体布局
        totalPlace = ['C', '÷', '^', '⌫',
                      '7', '8', '9', 'x',
                      '4', '5', '6', '-',
                      '1', '2', '3', '+',
                      "+/-", '0', '.', '=', ]

        # 起始行（前0,1,2,3行已被结果显示标签占用，所以从第4行开始）
        startRow = 4
        startCol = 0

        for i, key in enumerate(totalPlace):
            row = startRow + i // 4  # 一行4个
            col = startCol + i % 4
            if key in digits:  # 处理所有数字按钮
                ttk.Button(master=self.root, text=key, width=CalculatorConfig.BUTTON_WIDTH, bootstyle="dark-link", takefocus=False,
                           command=lambda d=key: _on_digit_click(d)).grid(row=row, column=col, padx=CalculatorConfig.BUTTON_PADDING, pady=CalculatorConfig.BUTTON_PADDING,
                                                                              sticky="nsew")
            else:  # 处理其余符号按钮
                ttk.Button(master=self.root, text=key, width=CalculatorConfig.BUTTON_WIDTH, bootstyle="dark-link", takefocus=False,
                           command=lambda d=key: _on_operation_click(d)).grid(row=row, column=col, padx=CalculatorConfig.BUTTON_PADDING, pady=CalculatorConfig.BUTTON_PADDING,
                                                                                  sticky="nsew")

            # 为放置按钮的单元格配置权重（使按钮可随窗口扩展）
            self.root.grid_rowconfigure(row, weight=1)
            self.root.grid_columnconfigure(col, weight=1)
    

    def update_var(self,displayResult, userInput):
        """
        更新哇
        """
        self.displayResultVar.set(displayResult)
        self.userInputVar.set(userInput)

    
    def run(self):
        self.root.mainloop()

