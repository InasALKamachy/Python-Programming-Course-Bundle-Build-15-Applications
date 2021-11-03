class Greeting():
    def __init__(self,name):
        self.name = name

gr = Greeting('jack')
print(gr.name)
print(getattr(gr,'name'))
