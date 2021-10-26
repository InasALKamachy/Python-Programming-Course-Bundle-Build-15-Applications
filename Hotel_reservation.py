# Attempt this with paitience and remeber that you'll only succed when you fail
# Start off by creating the Guest class and it's methods
class Guest():
    DT = {'John': 'A011',
          'Kyle': 'A009',
          'Jake': 'BQ02',
          'Tamara': 'AO15',
          'Josh': 'BQ13'}
    kys = ['A010', 'A012', 'A014', 'BQ01']

    def __init__(self, name):
        self.name = (name.lower()).capitalize()
        self.regd = self.name in self.DT

    def is_regd(self):
        if self.regd:
            print('Registered')
        else:
            print('Not Registered')

    def get_key(self):
        if self.regd:
            print(f"key : {self.DT[self.name]}")
        elif len(self.DT):
            pass
        else:
            print('Not Registered')

    def reg(self):
        if len(self.kys):
            self.DT[self.name] = self.kys[0]
            self.kys.pop(0)
            self.regd = True
        else:
            print('Sorry, no vacant rooms available')


for guest_name in ['Josh', 'Hans', 'Evan', 'Kyle', 'Ted', 'Karl', 'Sam']:
    guest = Guest(guest_name)
    print(guest.name)
    guest.is_regd()
    if guest.regd:
        guest.get_key()
    else:
        guest.reg()
        guest.get_key()

# very similar to what you posted except for my elif statement
# I noticed that after the sorry no vacant rooms available under sam it still printed 'not registered' ant thoughts?
