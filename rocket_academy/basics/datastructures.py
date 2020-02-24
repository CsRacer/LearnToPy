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
print(rocket[0])

# Teilmengen eine Liste neue zuweisen

# Operatoren #

 # "+"-Operator (Addition von Listen)
 # Listen werden aneinandergefügt
print(rockets+rockets)
# Besonders nützlich wenn ein weiterer Wert in ein Listenelement eingefügt werden soll
print(rockets1 + ["2017"])

# "*"-Operator (Multiplikation)
# Werte werden um die höhe der Integerzahl wiederholt
rockets2 = rockets1[:3]
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
testListe = [zahl1,zahl2]
print(testListe)
zahl1 += 2
print(testListe)

# Dictionarys #
# Nachteil bei listen. Man muss immer die genaue Position des Wertes in der Datenstruktur kennen
nextGenRockets = ["modell": ]
