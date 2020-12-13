#Chaining

x = y = 5
if(3 < x + y <= 10): #(3 < x + y) && (x + y <= 10) -> x + y è calcolato una volta
    print("Interno")
else:
    print("Esterno")