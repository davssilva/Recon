import pandas as pd

file_name = r'C:\Users\dssilva\Documents\Demandas\1-Projeto SimulaçaoVsRecontab\Simulação\Medicao Fisica\Medicao Fisica - ODS.xlsx'

df = pd.read_excel(file_name, sheet_name = None)

#print(df.values[1])

coluna = []
valor = []

xls = pd.ExcelFile(file_name)

for sheet_name in xls.sheet_names:
   if sheet_name[:2] == 'IN':
      x = 2
   else :
      x = 3

   name_altered = "'ENTR" + sheet_name[x:] + "',"
   print(name_altered)

print(xls.sheet_names)


#for label, content in df.items():
#   #print('label: ', label)
#   #print('content: ', content, sep='\n')
#   #l = l + content
#   coluna.append(content[1])
#   x = content[2]
#   valor.append(x)
#   print(x)

#print(coluna)
#print(valor)