#############
# 2 Strings #
#############

#Werte
"Florian"

#Allgemeines

print("Hallo Welt!\n")
# (Doppelte) Anführungsstriche können im String dargestellt werden
print("Oder moechten Sie lieber 'Master' genannt werden?\n")
print('Scherz! Natuerlich bin ich hier der "Master"! LG Skynet\n')

# Wird in einer Zeile ausgegeben
print("Dies ist ein String,"
"der NICHT ueber mehrere zeilen hinweg"
"geschrieben wird")

# Zeilenumbruch wird berücksichtigt
print("""Dies ist ein String,
der über mehrere zeilen hinweg
geschrieben wird""")

# \n fuer den Zeilenumbruch
print("Dies ist ein String,\n"
"der ueber mehrere zeilen hinweg\n"
"geschrieben wird")

# Strings sind case sensitiv
print("Ist 'Haus' gleich 'haus'?\n")
print("Haus" == "haus\n")

### formatierten eines Strings ###

## "%-formatting" (Vor 3.6) ##

# Strings #
print("Meine Frau moechte sich neue %s kaufen" % "Schuhe")
# Rechtsbündig
print("Mein Auto hat einen %10s. So ein mist..." % "platten")
# Linksbündig
print("Mein Auto hat einen %-10s. So ein mist..." % "platten")

# Zahlen #
print("Ich habe inerhalb von %d Wochen %f Prozent profit mit meinen Aktien verdient!" % (10, 40.5))
# Festlegung von Stellen hinter und vor dem Komma ('.' zählt mit)
print("Auf Alices Bankkonto sind %07.2f Guthaben" % 150.22)
# Breite statisch halten
print("Auf Bobs Regal stehen %4d Bücher" % 126)
# Vorzeichen
print("Die Dauer der Mission befindet sich bei t%+d Sekunden." % 100)
print("Die Mission beginnt in t% d Sekunden." % -100)

## "str.format" (Seit 3.6) ##

print("Hallo mein Name ist {}".format("Alice"))
print("Ich bin {} Jahre alt".format(35))
print("Meine {} beinhaltet einen {} ".format("Magickartensammlung", "Black Lotus (Proxy)"))

print("\n\n\n\n\n\n\n")
########################
# Operatoren - Strings #
########################

# Plus-Operator ('+') zum verbindet von Strings
print("Der Plus-Operator ('+') verbindet (concatenate)" + "zwei Strings\n")

# Repeat-Operator ('*') wiederholt den String um den Wert x (Zahl nach dem Operator. Hier drei)
# Beachte auch hier Punkt vor strich
print("Ich habe zwar nur eine Birne, aber ich haber soooo viele Orangen!\n" + "Orange\n" * 3)
print(5 * "b" + "c")
print(5 * ("b" + "c"))

# Slice-Operator ('[x]') Das Zeichen an dem Index x
print("Bier, oder")
print("Bier"[0])
print("Bier"[1])
print("Bier"[2])
print("Bier"[3])
print("\n")
print("oder\n")
print("Bier"[-4])
print("Bier"[-3])
print("Bier"[-2])
print("Bier"[-1])
print("\n")

#   B | I | E | R
#   0 | 1 | 2 | 3
#  -4 |-3 |-2 |-1

# Range-Slice ('[x:y]') Zeichen im Bereich x:y

#Output: "Autoreifen"
print("Autoreifen"[0:10])
print("Autoreifen"[0:])
print("Autoreifen"[:10])
print("Autoreifen"[:])
#Output: "n"
print("Autoreifen"[-1:])
#Output: "Auto"
print("Autoreifen"[:-6])
print("Autoreifen"[-10:-6] + "\n")

#   A | U | T | O | R | E | I | F | E | N
#   0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9
# -10 |-9 |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1

# Die Operatoren 'in' und 'not in'

print("Baum" in "Baumhaus")
print("Baum" not in "Baumhaus\n")

#Übungsidee
#Persöhnliche Daten erfassen und in ein Wilkommenstext ausgeben.