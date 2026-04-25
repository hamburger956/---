import ttkbootstrap as ttk
class CalculatorViewConfig:
    """
    计算器配置类,处理视图配置
    """
    MIN_WIDTH = 320  # 最小宽度
    MIN_HEIGHT = 520  # 最小高度
    MAX_WIDTH = 1000  # 最大宽度
    MAX_HEIGHT = 1000  # 最大高度
    STYLE_FONT_SIZE = 20  # 总体风格字体大小
    DISPLAY_FONT_SIZE = 30  # 显示标签字体大小
    INPUT_FONT_SIZE = 15  # 历史输入标签字体大小
    BUTTON_WIDTH = 5  # 按钮宽度
    BUTTON_PADDING = 5  # 按钮内边距
    BUTTON_PADDING = 2  # 按钮内边距
    LABEL_COLUMNSPAN = 4  # 标签占用的列数，与每行按钮的数量相同


class CalculatorView:
    """
    计算器的图形界面，负责创建窗口、标签、按钮，并刷新显示。
    """
    def __init__(self, title: str, size: str, iconPath: str):
        self.root = ttk.Window()
        self.root.title(title)
        self.root.iconbitmap(iconPath)
        self.root.geometry(size)
        self.root.minsize(CalculatorViewConfig.MIN_WIDTH, CalculatorViewConfig.MIN_HEIGHT)  # 尺寸限制
        self.root.maxsize(CalculatorViewConfig.MAX_WIDTH, CalculatorViewConfig.MAX_HEIGHT)

        self.displayResultVar = ttk.StringVar(master=self.root, value="")
        self.userInputVar = ttk.StringVar(master=self.root, value="")
        self._setup_style()

        #总体布局
        self.totalPlace = ['C', '÷', '^', '⌫',
                          '7', '8', '9', 'x',
                          '4', '5', '6', '-',
                          '1', '2', '3', '+',
                          "+/-", '0', '.', '=', ]

    def _setup_style(self):
        # ttk风格设置
        style = ttk.Style()
        style.configure("TButton", font=("Arial", CalculatorViewConfig.STYLE_FONT_SIZE))


    def create_result_label(self):
        """
        创建标签,处理布局
        """
        displayresultLabel = ttk.Label(master=self.root,
                                            bootstyle="dark",
                                            textvariable=self.displayResultVar,
                                            font=("黑体", CalculatorViewConfig.DISPLAY_FONT_SIZE), anchor='e')
        # 用户输入label
        userInputLabel = ttk.Label(master=self.root,
                                        bootstyle="secondary",
                                        textvariable=self.userInputVar,
                                        font=("黑体", CalculatorViewConfig.INPUT_FONT_SIZE), anchor='e')

        # 俩个标签共占四行,从第零行开始
        userInputLabel.grid(row=0, column=0,
                            rowspan=2, columnspan=CalculatorViewConfig.LABEL_COLUMNSPAN,  # 一行4个按钮,所以占4列
                            sticky='e')  # 向右对齐

        displayresultLabel.grid(row=1, column=0,  # 这里row=1而不是2是为了更贴近上面
                                rowspan=2, columnspan=CalculatorViewConfig.LABEL_COLUMNSPAN,
                                sticky='e')

        # 配置权重,俩个标签占4行
        for row in range(4):
            self.root.grid_rowconfigure(row, weight=1)


    def create_buttons(self,digits, _on_digit_click, _on_operation_click):
        """
        创建按钮,处理布局
        """

        # 起始行（前0,1,2,3行已被结果显示标签占用，所以从第4行开始）
        startRow = 4
        startCol = 0

        for i, key in enumerate(self.totalPlace):
            row = startRow + i // CalculatorViewConfig.LABEL_COLUMNSPAN  # 标签占用的列数，与每行按钮的数量相同
            col = startCol + i % CalculatorViewConfig.LABEL_COLUMNSPAN
            if key in digits:  # 处理所有数字按钮
                ttk.Button(master=self.root, text=key, width=CalculatorViewConfig.BUTTON_WIDTH, bootstyle="dark-link", takefocus=False,
                           command=lambda d=key: _on_digit_click(d)).grid(row=row, column=col, padx=CalculatorViewConfig.BUTTON_PADDING, pady=CalculatorViewConfig.BUTTON_PADDING,
                                                                              sticky="nsew")
            else:  # 处理其余符号按钮
                ttk.Button(master=self.root, text=key, width=CalculatorViewConfig.BUTTON_WIDTH, bootstyle="dark-link", takefocus=False,
                           command=lambda d=key: _on_operation_click(d)).grid(row=row, column=col, padx=CalculatorViewConfig.BUTTON_PADDING, pady=CalculatorViewConfig.BUTTON_PADDING,
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


class ScientificCalculatorView(CalculatorView):
    def __init__(self, title: str, size: str, iconPath: str):
        super().__init__(title, size, iconPath)
        self.totalPlace = [
            "sin",  "π",  "e",  "C",   "⌫",
            "cos",  "(",  ")",  "^" ,"mod",
            "tan",  "7",  "8",  "9",   "x",
            "log",  "4",  "5",  "6",   "-",
            "n!" , "1", "2", "3",  "+",
            "ln" , "+/-","0", ".",   "=",
        ]
        CalculatorViewConfig.LABEL_COLUMNSPAN = 5



