# demander au utilisateur les notes
note =int(input("entrer la notes :")) 
# condition
if note >= 10 and note < 12 : 
    print(" passable")
elif note >= 12 and note < 14 : 
    print("Asser bien")
elif note >= 14 and note < 16 : 
    print("Bien")   
elif note >= 16 and note < 18 : 
    print("Très bien")   
elif note >= 18 and note < 20 : 
    print("Honorable")
else :
    print("Mahereza")