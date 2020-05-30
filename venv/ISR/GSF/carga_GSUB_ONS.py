import pandas as pd
import os

def define_gfom(items):
    i = 0
    for x in items[1]:
        i = i + 1
        if x == 'GFOM':
            return i

def le_arquivo (nome_arquivo):
    try:
        df = pd.read_excel(nome_arquivo,  skiprows=1)
        #df.columns = ['Data', 'GSUB', 'Outro']

        #df.set_index('Data').T
        #print (df.loc[:,('Data')])

        var  = []
        gfom_coluna = 0
        modl = 1
        modelo_preco = []

        for items in df.T.iteritems():

            print('Entrei no for')

            if gfom_coluna == 0:
                gfom_coluna = define_gfom(items)
            elif items[1][0] == 'Data':
                 for modl in range(gfom_coluna-1):
                     if modl != 0:
                        modelo_preco.append(items[1][modl])

            else:
                i = 0
                for x in modelo_preco:

                    data = items[1][0]
                    valor = items[1][i]
                    i = i + 1
                    modelo_preco_x = {'Modelo': x, 'Data': data, 'Valor': valor}
                    var.append(modelo_preco_x)


        print (var)



        #for items in df.items():
        #    print (items[0])
        #    print (items[1])

            #break

    except FileNotFoundError:
        print ('Arquivo nao existe')


def define_excel():
   ano = '2013'

   file_path = os.path.join(r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\GSUB_ONS\2013\04 GSUB_Abr 13.xls')
   le_arquivo(file_path)

   #file_path = os.path.join (r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\GSUB_ONS')

   #file_path = os.path.join(file_path , ano)

   #for file_name in os.listdir(file_path):
   #   nome_arquivo = os.path.join (file_path, file_name)
   #   print (nome_arquivo)
   #   le_arquivo(nome_arquivo)
   #   break


define_excel()