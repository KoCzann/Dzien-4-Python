wiek = None
name = input("Podaj swoje imię: ")

def greet(name, wiek, pelnoletnosc):
        return f"Hej {name}! Masz {wiek} lat i jesteś {pelnoletnosc}. Miło mi Cię poznać."

try:
    wiek = int(input("Podaj swój wiek: "))
except ValueError:
    print("Wiek musi być liczbą!")
    exit()

if wiek < 18:
    pelnoletnosc = "niepełnoletni"

elif wiek == 18:
    pelnoletnosc = "świeżo upieczonym dorosłym"
    
elif wiek > 18:
    pelnoletnosc = "pełnoletni" 

print(greet(name, wiek, pelnoletnosc))