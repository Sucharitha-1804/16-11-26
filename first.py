centimeters=int(input("entercentimeters:"))
temp=centimeters
kilometers=centimeters//1000
centimeters=centimeters%1000
meters=centimeters//100
meters=meters%100
remaining=centimeters
print(f' the {temp} has {kilometers} kilometers and {meters} meters and { centimeters} centi meters and {remaining}')