class Calc():
    def __init__(self):
        self.total = 0
        self.op = ""
        self.current = ""
        self.eq = False
        self.op_pending = False
        self.new_no = True
        
    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_no:
            self.current = temp2
            self.new_no = False
        else:
            if temp2 = '.':
                if temp2 in temp:
                    return
            self.current = temp + temp2
        self.display(self.current)
    
