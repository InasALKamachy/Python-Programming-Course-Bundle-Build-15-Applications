class Guest:
    regs = {'John':'A011',
            'Kyle':'A009',
            'Jake': 'BQ02',
            'Tamra': 'A015',
            'Josh': 'BQ13'}

    kys = ['A010', 'A012', 'A014', 'BQ01']

    def __init__(self, gname):
        self.name = (gname.lower()).capitalize()
        self.regd = self.name in self.regs

    def is_regd(self):
        if self.regd:
            print("Registered")
        else:
            print("Not Registered")
    def get_key(self):
        if self.regd:
            print(f"Key : {self.regs[self.name]}")
    def reg(self):
        if len(self.keys):
            self.regs[self.name] = self.key[0]
            self.kys.pop(0)
            self.regd = True
        else:
            print("Sorry, no vacant rooms available")
            
for guest_name in ['Josh', 'Hans', 'Evan', 'Kyle', 'Ted', 'Karl', 'Sam']:
    guest = Guest(guest_name)
    print(guest.name)
    guest.is_regd()
    if guest.regd:
        guest.get_key()
    else:
        guest.reg()
        guest.get_key()
        


