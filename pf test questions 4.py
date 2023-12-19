value1 =int(input("no of person"))
value2 = int(input("cost of each meal"))
value3 =int(input("sales tax percentage"))
value4 = int(input("tip percentage"))



total_cost = value1* value2
print(total_cost)

total_salestax = (value3/100)*total_cost
print(total_salestax)

total_tip = total_cost*(value4/100)
print(total_tip)


total_billperperson = total_cost/value1
print(total_billperperson)