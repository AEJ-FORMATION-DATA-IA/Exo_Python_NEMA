A = input("Entrez un nombre entier : ")
int(A)
A = int(A)
if(type(A) != int):
    print("Vous avez fait une erreur.")
else:
    B = input("Entrez un autre nombre entier : ")
    int(B)
    B = int(B)
    if(type(B) != int):
        print("Vous avez fait une erreur.")
    elif ( A > B ):
            print(f"{A} > {B}")
    elif ( A < B ):
            print(f"{A} < {B}")
    else:
            print(f"{A} = {B}")
    