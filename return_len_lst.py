class LenVal():
    def __init__(self, lst_len):
        self.lst_len = lst_len
        self.lenght_lst = len(lst_len)

    def sho_val(self):
        print(str(self.lenght_lst))


L1 = LenVal('Head')
L2 = LenVal([1, 9, 4, 2, 6])
L3 = LenVal((1,))
print(L1.sho_val())
print(L2.sho_val())
print(L3.sho_val())
