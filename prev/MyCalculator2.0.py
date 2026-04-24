#ttk做的计算器
import ttkbootstrap as ttk
class MyCalculator:
    def __init__(self,title:str,size:str,iconPath:str):
        self.root = ttk.Window()
        self.root.title(title)
        self.root.iconbitmap(iconPath)
        self.root.geometry(size)
        self.root.minsize(320,520) #尺寸限制
        self.root.maxsize(1000,1000)
        self.operationClicked = False #用于判断是否点击符号(不包含等于)
        self.equalsClicked = False #用于判断是否点击等于符号
        self.userInput = "" #储存用户输入,即清屏前用户所输入的总表达式
        self.displayResult = "" #始终为当前计算器上显示的值,不包含历史值
        #ttk风格设置
        style = ttk.Style()
        style.configure("TButton", font=("Arial", 20))
            

    #处理数字点击
    def on_digit_click(self, digit):
        if self.operationClicked: #仅仅加入最后点击的符号,避免多次点击不同的符号而产生无效结果
            self.userInput += self.displayResult
            self.operationClicked = False 
        
        if self.equalsClicked: #保证点击等于符号后再输入数字能够清屏
            self.clear()
            self.equalsClicked = False
        
        if digit in ["."]: #特殊处理"."
            if digit in self.displayResult: #避免多次输入点
                digit = ""
        
            elif self.displayResult in self.operations or not self.displayResult: #确保输入符号后再输入点能有效
                digit = "0."

        if self.displayResult in self.operations: #判断此时显示的是否是符号
            self.displayResult = digit #让符号单独显示
        else:
            self.displayResult += digit
        
        self.userInput += digit 
        self.updateVar()


    #处理符号点击
    def on_operation_click(self,operation:str):
        if operation in ["C"]: #处理清屏符号
            self.clear()
        
        elif self.displayResult in ["∞","Error"]: #处理当结果无效的情况
            return

        elif operation in ["="]:
            self.solve_number()
            return
        
        elif operation in ["⌫"]:
            self.displayResult = self.displayResult[:-1]
            self.userInput = self.userInput[:-1]
            self.updateVar()
        
        elif operation in ["+/-"]:
            #转换符号
            length = len(self.displayResult)
            if length and self.displayResult not in self.operations:
                self.displayResult = "-" + self.displayResult if '-' not in self.displayResult else self.displayResult[1:]
                self.userInput = self.userInput[:-length] + self.displayResult #对原来的部分进行替换
                self.updateVar()

        else:
            self.operationClicked = True
            self.displayResult = operation
            self.updateVar()
        
        if self.equalsClicked: #保证点击等于符号后再输入符号能继续进行计算
            self.equalsClicked = False

    #处理用户输入
    def solve_number(self):
        try:
            self.userInput = self.userInput.replace("x",'*').replace("÷",'/').replace("^","**") #替换符号,让eval函数能正常进行
            self.displayResult = f"{eval(self.userInput):.10g}" #处理精度
            self.userInput = self.displayResult #保留最后输出的数字,能够直接进行符号计算
            
        except (OverflowError,ZeroDivisionError): #处理无穷大
            self.displayResult = "∞"
            self.userInput = ""

        except SyntaxError: #处理意外输入
            self.displayResult = "Error"
            self.userInput = ""

        finally:
            self.equalsClicked = True
            self.displayResultVar.set(self.displayResult)

    #创建label
    def create_result_label(self):
        #哇
        self.displayResultVar = ttk.StringVar(master=self.root,value=self.displayResult)
        self.userInputVar = ttk.StringVar(master=self.root,value=self.userInput) 
        
        #计算结果label
        self.displayresultLabel = ttk.Label(master=self.root,
                                    bootstyle="dark",
                                    textvariable=self.displayResultVar,
                                    font=("黑体",30),anchor='e')
        
        self.userInputLabel = ttk.Label(master=self.root,
                                        bootstyle="secondary",
                                        textvariable=self.userInputVar,
                                        font=("黑体",15),anchor='e')
        
        #俩个标签共占四行,从第零行开始
        self.userInputLabel.grid(row=0,column=0,
                                rowspan=2,columnspan=4, #一行4个按钮,所以占4列
                                sticky='e') #向右对齐
        
        self.displayresultLabel.grid(row=1,column=0, #这里row=1而不是2是为了更贴近上面
                                rowspan=2,columnspan=4,
                                sticky='e')
        
        #配置权重,俩个标签占4行
        for row in range(4):
            self.root.grid_rowconfigure(row, weight=1)


    #创建按钮,处理布局
    def create_buttons(self):
        #功能键
        self.digits = ['7', '8', '9','4', '5', '6', '1', '2', '3','0', '.',]
        self.operations =['+','-','x','÷','⌫','C','^','+/-',] 
        #总体布局
        totalPlace = [   'C',  '÷',  '^',  '⌫',
                         '7',  '8',  '9',  'x',
                         '4',  '5',  '6',  '-',
                         '1',  '2',  '3',  '+',
                       "+/-",  '0',  '.',  '=',]
        
        # 起始行（前0,1,2,3行已被结果显示标签占用，所以从第4行开始）
        startRow= 4
        startCol = 0
        
        for i, key in enumerate(totalPlace):
            row = startRow + i // 4   #一行4个       
            col = startCol + i % 4
            if key in self.digits: #处理数字按钮
                ttk.Button(master=self.root, text=key, width=5,bootstyle="dark-link",takefocus=False,
                                command=lambda d=key: self.on_digit_click(d)).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                
            elif key in ["+/-"]: #为了保证美观性,单独设置此符号的样式 
                ttk.Button(master=self.root, text=key, width=5,bootstyle="dark-link",takefocus=False,
                                command=lambda d=key: self.on_operation_click(d)).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                
            else:#处理其余符号按钮
                ttk.Button(master=self.root, text=key, width=5,bootstyle="dark-link",takefocus=False,
                                command=lambda d=key: self.on_operation_click(d)).grid(row=row, column=col, padx=2, pady=2, sticky="nsew")
                
            # 为放置按钮的单元格配置权重（使按钮可随窗口扩展）
            self.root.grid_rowconfigure(row, weight=1)
            self.root.grid_columnconfigure(col, weight=1)


    #更新哇
    def updateVar(self):
        self.displayResultVar.set(self.displayResult)
        self.userInputVar.set(self.userInput)


    #清空
    def clear(self):
        self.userInput = ""
        self.displayResult = ""
        self.updateVar()
    

    #管理放置
    def pack(self):
        self.create_result_label()
        self.create_buttons()

    #运行
    def run(self):
        self.pack()
        self.root.mainloop()


if __name__ == "__main__":
    myCalculator = MyCalculator(title="简易计算器",
                                size="400x600",
                                iconPath=r'D:\自己的项目\计算器\favicon.ico')
    myCalculator.run()