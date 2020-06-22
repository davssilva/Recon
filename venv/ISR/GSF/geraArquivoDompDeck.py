import pandas as pd
import datetime as datetime
import os
import zipfile as zf

def monta_pasta(file_name):

    if file_name[0:4] == 've_2':
        referenciaPastaAnoMes = file_name[3:9]

    else:
        referenciaPastaAnoMes = file_name[6:10] + file_name[3:5]


    return referenciaPastaAnoMes

def abrirArquivo ():
   pathDestino = os.path.join(r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\DOMP_DECK\ArqSumario')
   file_path = os.path.join(r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\DOMP_DECK\Decks')

   for file_name in os.listdir(file_path):
      pastaDestino = monta_pasta(file_name)

      pathDestinoArq = os.path.join(pathDestino,pastaDestino)

      nome_arquivo = os.path.join (file_path, file_name)

      print (nome_arquivo)

      arqzip_revisao_completo = zf.ZipFile(nome_arquivo,mode='r')

      for file in arqzip_revisao_completo.namelist():

          if 'RESULTADO' in file:

               arqzip_resultado1 = arqzip_revisao_completo.open(file)
               arqzip_resultado2 = zf.ZipFile(arqzip_resultado1)

               for arqResultado in arqzip_resultado2.namelist():

                   if 'SUMARIO' in arqResultado:


                      if not (os.path.exists(pathDestinoArq)):
                           os.makedirs(pathDestinoArq)

                      if  not (os.path.exists(os.path.join(pathDestinoArq, arqResultado))):
                          arqSumario = arqzip_resultado2.extract(arqResultado,pathDestinoArq )

abrirArquivo()