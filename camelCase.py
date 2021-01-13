txt = input(" please enter something to be turned into camelCase").title()
txtList = txt.split( )
txtList2 = ("".join(txtList))
camelCase = txt[0:1].lower() + txtList2[1:]

print(camelCase)
