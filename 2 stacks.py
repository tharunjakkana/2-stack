class twostacks:
    def __init__(self, n):
        self. size = n
        self.arr = [None]*n
        self. topl = -1
        self. top2 = self.size
    def push1(self,x):
        if self.top1 < self.top2-1:
            self.topl +=1
            self. arr[self.top1]=x
            print ("pushed:",x)
        else:
            print("stack1 Overflow")
    def push2(self,x):
        if self.top1<self.top2-1:
            self.top2-=1
            self.arr[self.top2]=x
            print ("Pushed: ", x)
        else:
            print ("Stack2 Overflow")
    def pop1(self):
        if self.top1>= 0:
            x = self.arr[self.top1]
            self.top1-=1
            return x
        else:
            print ("Stack1 Underllow")
    def Pop2(Self):
        if self.top2 < self.Size:
            x= self.arr[self.top2]
            self.top2+=1
            return x
        else:
            print (" stack2 Underflow")

Stacks=twostacks
Stacks.push1(1)
Stacks.push1(2)
Stacks.push2(11)
Stacks.push2(12)
Stacks.push1(4)
Stacks.push2(8)
Stacks.push1(6)
print("popped from stack1:", stacks.popl())
print("popped from stack2:", stacks.pop2())
print("popped from stack1:", stacks.pop1())
print("popped from stack2:", stacks.pop2())
print("popped from stack1:", stacks.pop1())
print("popped from stack2:", stacks.pop2())
print("popped from stack1:", stacks.pop1())
