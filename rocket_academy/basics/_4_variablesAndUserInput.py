###############
# 4 Variabeln #
###############

# Bezeichner | Zuweisungsoperator | Wert
variable1 = "wert"
variable2 = 42
variable3 = 4.2
variable4 = True

#  Multi-Wort naming-conventions
#   Delimiter-seperated words (z.B. '_')
#   Letter case-seperated words (z.B. 'CamelCase' oder 'Pascal case')
autobahnraststaettenparkplatztoilletenspuehlungsknopfmaterial = "kunststoff"
#delimiter
autobahn_raststaetten_parkplatz_toilleten_spuehlungs_knopf_status = "aktiv"
#camelCase
autobahnRaststaettenParkplatzToilletenSpuehlungsKnopfFarbe = "rot"
#PascalCase
AutobahnRaststaettenParkplatzToilletenSpuehlungsKnopfPosition = "Zentral"

# Variablen werden bei der ersten Zuweisung in den Speicher geladen bzw. erstellt.

# Keine Angabe eines types notwendig

# Erlaubt sind Alpha-Numerische Zeichen sowie '_'
# - a-Z
# - 0-9
# - _

# Nicht erlaubt sind außerdem
# keywoerter wie:
#   def
#   class
#   not

# Beginned mit Buchstabe, oder '_'
x = 1
_x = 1.1

# Darf nicht mit einer Zahl beginnen
# 1x = 1 <- falsch
# _1x = 1 <- korrekt

# Variabeln sind Case-Sensitiv
auto = "VW"
Auto = "Porsche"

# Variabeln können anstelle eines Wertes genutzt werden

# Als Ausgabe verwenden
print("VW")
print(auto)

print(1)
print(_x)

# In Kombination mit operatoren

print("Das Auto meiner traeume ist ein "+auto)
print("Das Auto meiner traeume ist ein " + auto * 3)



