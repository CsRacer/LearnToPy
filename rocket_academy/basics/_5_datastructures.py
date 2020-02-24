# Bei einer unbestimmten Menge von Daten und/oder Werten wird das Speichern mit einfachen datantypen zu kompliziert und unübersichtlich (Bsp. Gebrauchtwagenhaendler)
# Weiterer nachteil von einfachen Datentypen => Mann muss den genauen Variablennamen kennen
# Kategorisierung von Daten möglich (z.B. Kombi, SUV und weiters)
# Besonderheit an Python ist das die Datenstrukturen sehr vielseitig sind und dem Entwickler sehr viel Freiheiten lassen

# TODO Existieren Arrays in Python?
#Listen
# Bezeichner | Zuweisungsoperator | Werte
# Werte: Können unterscheidliche Datentypen enthalten (unterschieid zu vielen anderen Programmiersprachen)
rockets = ["Starun 5", "NASA", 3, 1000]
#Zugriff durch angebe des/der Index/e

print(rockets[0])
print(rockets[3])
print(rockets[-1])
print(rockets[-4])
print(rockets[0:2])
print(rockets[1:3])
print(rockets[:3])
print(rockets[1:])
print(rockets[:])

# Wert Manipulation durch
rockets[0] = "Falcon 9"
print(rockets[0])

# Teilmengen eine Liste neue zuweisen

# Operatoren #

 # "+"-Operator (Addition von Listen)
 # Listen werden aneinandergefügt
print(rockets+rockets)
# Besonders nützlich wenn ein weiterer Wert in ein Listenelement eingefügt werden soll
print(rockets + ["2017"])

# "*"-Operator (Multiplikation)
# Werte werden um die höhe der Integerzahl wiederholt
rockets2 = rockets[:3]
print(rockets2)

# Listen koennen ebenfalls geschachtelt werden. So entsteht eine tabellenartige Struktur
rocket1 = ["Saturn 5", "NASA", 3, 1000]
rocket2 = ["Falcon 9", "SpaceX", 0.1, 300]
newRockets = [rocket1, rocket2]

# Zugriff bei geschachtelten Listen
# Name rocket1
print(newRockets[0][0])
# Gewicht rocket1
print(newRockets[1][3])
# Alle Werte von rocket1
print(newRockets[0])
# Alle Werte von rocket2
print(newRockets[1])
# Teilliste zugreifen
partialList = newRockets[0][:2]

# TODO Ist das auch anders möglich
# Geschachtelte Liste repräsentiert die Refferenz auf den Speicher der Variable
# anders als bei primitiven Datentypen
zahl1 = 1
zahl2 = 2
testListe = [zahl1, zahl2]
print(testListe)
zahl1 += 2
print(testListe)

# Nachteil bei listen. Man muss immer die genaue Position des Wertes in der Datenstruktur kennen
# => => =>
# Dictionarys #
fahrzeugDic = {"marke" : "VW", "baujahr" : 2010, "preis" : 10000, "sitzplaetze" : 5, "abstandssensor" : False}

# Ausgabe des dictonaries
print(fahrzeugDic)
# Auslesen eines Wertes
print(fahrzeugDic["marke"])
# Bestehender Wert manipulieren
fahrzeugDic["marke"] = "Porsche"
# Neuen Schlüssel hinzufügen
fahrzeugDic["dashcam" : True]
print(fahrzeugDic["dashcam"])
# Entferne einen Eintrag
del fahrzeugDic["sitzplaetze"]
print(fahrzeugDic)
# list keys from dictionary
print(list(fahrzeugDic.keys()))
# und sortiert
print(sorted(fahrzeugDic.keys()))
# Auch bei Dictionaries sind Schachtelungen möglich.
# case sensitiv
pkwBestand = {
    "fahrzeug1" : {"marke" : "VW", "Antribsart" : "Verbrennung", "baujahr" : 2020, "ps" : 150},
    "fahrzeug2" : {"marke" : "Tesla", "baujahr" : 2020, "Antriebsart" : "Elektro", "ps" : 300},
    "fahrzeug3" : {"Marke" : "Porsche"}}
print(pkwBestand)

# Tupel : Nicht veränderliche Datenstrukturen
# - vermeiden das ausversehen Werte verändert werden (wie final in java)
# - mehr performance da struktur einfacher
# - wird wie Listen erstellt
# - Bei Variablenzuweisung kann Klammer weggelassen werden. (Wird automatisch hinzugefügt)
kontoTransaktion = ("2020-01-01", "DE10000000123456", 1000.5, True)
# Durch Interpreter auch wie folgt Implementierbar
kontoTransaktionVariation = "2020-01-01", "DE10000000123456", 1000.5, True
# Einen Wert kann mit ([WERT]+[,]) hinzugefügt werden
kontoTransaktion = kontoTransaktion + ("Rechnungsnummer: 123456","Kundennummer: 654321")
kontoTransaktion = kontoTransaktion + ("Rueckbuchbar bis 2020-01-15",)
# +=-Operator erlabut hinzufügen ohne Klammern
kontoTransaktion += "Rechnungsnummer: 123456",
