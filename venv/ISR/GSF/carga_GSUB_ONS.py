import pandas as pd
import datetime as datetime
import os

def gera_insert_banco(dados_arq,nome_arq_sql):
    nome_tabela = 'SYSGSF.HIST_GSUB_ONS'

    insert_sql = 'INSERT INTO ' + nome_tabela + ' (CD_MODL_PRCO, MM_ANO_REFN, DT_HR_MES, QT_GSUB_ONS) VALUES ('

    print('Entrei gera_insert_banco')
    for valores in dados_arq:

        x = 0

        for campo, valor in valores.items():
            x = x + 1
            if campo == 'Data' and valor == 0: break
            if valores.items().__len__() == x:
                insert_sql = insert_sql + str(round(valor,3))
                insert_sql = insert_sql + ");\n"

            else:
                if campo == 'Data':
                    #mesref
                    datachr = datetime.datetime.strftime(valor, '01/%m/%Y 00:00:00')
                    insert_sql = "{0}\'{1}\'".format(insert_sql, datachr)
                    insert_sql = insert_sql + ','

                    #dt_hr_mes
                    datachr = datetime.datetime.strftime(valor, '%d/%m/%Y %H:%M:%S')
                    insert_sql = "{0}\'{1}\'".format(insert_sql, datachr)
                    insert_sql = insert_sql + ','
                else:
                    if pd.isnull(valor):
                        insert_sql = insert_sql + 'NULL'
                    else:
                        insert_sql = insert_sql + str(valor)
                    insert_sql = insert_sql + ','

        #print(insert_sql)

        nome_arq_sql.write(insert_sql)
        insert_sql = 'INSERT INTO ' + nome_tabela + ' (CD_MODL_PRCO, MM_ANO_REFN, DT_HR_MES, QT_GSUB_ONS) VALUES ('


def define_gfom(items):
    i = 0
    for x in items[1]:
        i = i + 1
        if x == 'GFOM':
            return i

def le_arquivo (nome_arquivo):
    try:
        df = pd.read_excel(nome_arquivo,  skiprows=1)
        var  = []
        gfom_coluna = 0
        modl = 1
        modelo_preco = []

        print('le_arquivo')
        for items in df.T.iteritems():

            if gfom_coluna == 0:
                gfom_coluna = define_gfom(items)
            elif items[1][0] == 'Data':
                 for modl in range(gfom_coluna-1):
                     if modl != 0:
                        if pd.isnull(items[1][modl]):

                           break
                        else:
                            modelo_preco.append(int(items[1][modl]))

            else:
                i = 1

                for x in modelo_preco:
                    if pd.isnull(items[1][0]): break
                    data = items[1][0]
                    valor = items[1][i]
                    i = i + 1
                    modelo_preco_x = {'Modelo': x, 'Data': data, 'Valor': valor}
                    var.append(modelo_preco_x)

        return var

    except FileNotFoundError:
        print ('Arquivo nao existe')


def define_excel():
   ano = '2017'
   #file_path = os.path.join(r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\GSUB_ONS\2013\09 GSUB_Set 13.xls')

   nome_arq_sql = open(r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\GSUB_ONS\GSUB.sql', 'w+')
   #gera_insert_banco(le_arquivo(file_path),nome_arq_sql)
   #nome_arq_sql.close()

   file_path = os.path.join (r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\GSUB_ONS')
   file_path = os.path.join(file_path , ano)

   for file_name in os.listdir(file_path):

      nome_arquivo = os.path.join (file_path, file_name)

      print (nome_arquivo)
      if le_arquivo(nome_arquivo) == "Modelo nao encontrado":
          print ("Erro no arquivo")
      else:
           gera_insert_banco(le_arquivo(nome_arquivo),nome_arq_sql)

   nome_arq_sql.close()

define_excel()