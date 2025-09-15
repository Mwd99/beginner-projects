# painting walls

nWalls = int(input("Enter the number of walls to be painted :"))
nPainters = int(input("Enter the numbers of painters available : "))

x=[]
y=[]   

def paintInput ():
    paintName = input("Enter the name of the painter : ")
    paintPrice = int(input("Enter the price of the painter for each wall: "))
    tBudget = paintPrice * nPainters
    print("Budget required for",paintName, "for n walls  is",tBudget)
    x.append(tBudget) 
    y.append(paintName)
    
for i in range (0,nPainters) :
    paintInput()

minPrice = min(x)
minId = x.index(minPrice)
print("Labour who can paint wall in the minimum required price is",y[minId],"in the amount of",minPrice)
