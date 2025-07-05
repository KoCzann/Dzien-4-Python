# def greet(name): - definiuje funkcję o nazwie np. "greet", która aby zadziałać będzie potrzeboawła informacji "name"

def greet(name):
    
    # return - "zwraca" funkcję, którą wcześniej zdefiniowaliśmy, tzn. określiliśmy funkcje "greet" i dzięki "return" możemy jej potem używać w skróconej wersji

    return f"Cześć, {name}! Miło mi Cię poznać."

# Używamy w praktyce funkcji "greet" żeby zobaczyć jak działa, a w kolejnym nawiasie dodajemy argument, który może być zmienny

name = input("Podaj swoje imię: ")
print(greet(name))