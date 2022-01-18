teksts = input ("Ievadi tekstu: ")
def replaceO (teksts):
  if teksts.count("o")>0 or teksts.count("O")>0:
    teksts = teksts.replace("o","%")
    teksts = teksts.replace("O","%")
    print(teksts)
  else:
    teksts = "nav burtu O vai o"
    print(teksts)
  return teksts
replaceO (teksts) 