#############
# 1 Strings #
#############

#Werte
"Florian"

########################
# Operatoren - Strings #
########################

# Plus-Operator ('+') zum verbindet von Strings
print("Der Plus-Operator ('+') verbindet (concatenate)" + "zwei Strings\n")

# Repeat-Operator ('*') wiederholt den String um den Wert x (Zahl nach dem Operator. Hier drei)
print("Ich habe zwar nur eine Birne, aber ich haber soooo viele Orangen!\n" + "Orange\n" * 3)

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

# Syntax
print("Hallo Welt!\n")
# (Doppelte) Anführungsstriche können im String dargestellt werden
print("Oder moechten Sie lieber 'Master' genannt werden?\n")
print('Scherz! Natuerlich bin ich hier der "Master"! LG Skynet\n')
#Strings sind case sensitiv
print("Ist 'Haus' gleich 'haus'?\n")
print("Haus" == "haus\n")
# Strings in Verbindung mit Variabeln
#print("Hallo " + benutzer + "\n")

#Übungsidee
#Persöhnliche Daten erfassen und in ein Wilkommenstext ausgeben.