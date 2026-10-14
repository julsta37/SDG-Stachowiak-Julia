#zadanie 1
#Utwórz DataFrame zawierający dane 10 osób, wzrost w centymetrach oraz masę ciała w kilogramach. 
#Następnie na podstawie tych danych wygeneruj kolumnę zawierającą BMI każdej osoby.

import pandas as pd
import os

data = {
    "name": ["Julia", "Hania", "Agnieszka", "Grzegorz", "Adam", "Piotr", "Krzysztof", "Mateusz", "Marta", "Franciszek"],
    "wzrost": [168, 154, 165, 189, 174, 180, 203, 172, 158, 176],
    "waga": [70, 43, 62, 87, 91, 76, 104, 63, 68, 90]
}

df = pd.DataFrame(data)
print(df)

df["wzrost"] = df["wzrost"] / 100
print(df)

df["bmi"] = df["waga"] / df["wzrost"]**2
print(df)

#zadanie 2
#Utwórz własny DataFrame zawierający wybrane przez siebie dane. 
# Zapisz go do pliku JSON, a następnie wczytaj ten plik do nowego obiektu DataFrame. 
# Sprawdź, czy oba obiekty zawierają te same dane.


path = os.path.join("zad2.json")
df.to_json(path)
print("zadanie 2")

json = pd.read_json(path)
df2 = pd.DataFrame(json)
print(df2)



#zadanie 3
#Wykorzystaj DataFrame stworzony w punkcie 1. Dodaj kolumnę z wiekiem i wypełnij ją danymi. 
#Następnie znajdź osoby starsze niż średnia wieku wszystkich osób, których BMI jest jednocześnie większe niż 25.
# Wyświetl imiona, wiek oraz BMI tych osób.

df["wiek"] = [27, 31, 45, 36, 19, 23, 52, 40, 29, 42]
print(df)

srednia = sum(df["wiek"]) / len(df["wiek"])

print(df[df["wiek"] > srednia & df["bmi"] > 25])