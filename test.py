from tkinter import *

ws = Tk()
ws.geometry('900x600')
ws.config(bg='#9FD996')
ws.title("D&D Alchemy")

# ingredients = ['Bloodgrass', 'ChromusSlime',' DriedEphedra', 'EmeticWax', 'FennelSilk', 'GengkoBrush', 'HyancinthNectar', 'LavenderSprig', 'MadrakeRoot', 'MilkweedSeeds', 'WildSageroot']
Bloodgrass, ChromusSlime, DriedEphedra, EmeticWax, FennelSilk, GengkoBrush, HyancinthNectar, LavenderSprig, MadrakeRoot, MilkweedSeeds, WildSageroot = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

ingredients = {'Bloodgrass': 0, 'ChromusSlime': 0, ' DriedEphedra': 0, 'EmeticWax': 0, 'FennelSilk': 0,
               'GengkoBrush': 0, 'HyancinthNectar': 0, 'LavenderSprig': 0, 'MadrakeRoot': 0,
               'MilkweedSeeds': 0, 'WildSageroot': 0}
ingredientsValues = ingredients.values()
r = 0
v = 0

# Ingredient Column
Label(
    ws,
    text='Ingredient',
    bg='#9FD996'
).grid(row=0, column=0)
for i in ingredients:
    Label(text=i, relief=RIDGE, width=15).grid(row=r + 1, column=0)
    r = r + 1

# Quantity Column
Label(
    ws,
    text='Quantity',
    bg='#9FD996'
).grid(row=0, column=1)

for i in ingredientsValues:
    Label(text=i, relief=RIDGE, width=5).grid(row=v + 1, column=1)
    v = v + 1

# for i in ingredients:
#    Label(text=i, relief=RIDGE, width=15).grid(row=r+1, column=0)
#    Label(text=, relief=RIDGE, width=15).grid(row=r + 1, column=1)
#    r = r + 1


# Entry(ws).grid(row=0, column=1)  -  e1=first row
e1 = Entry(ws, width=10, ).grid(row=1, column=2)
#e2 = Entry(ws, width=10).grid(row=2, column=2)
#e3 = Entry(ws, width=10).grid(row=3, column=2)

b2 = Button( ws, text='boo', command= lambda: getamountt(), padx="1").grid(row=2 , column=3 , sticky='e')


def getamountt():
    currentamount = ingredients
    answer = ws.e1.get()
    print(answer)

'''
b1 = Button(
    ws,
    text='Add',
    # command=addAmount(),
    padx="1"

).grid(row=1, column=3, sticky='e')
'''

ws.mainloop()
