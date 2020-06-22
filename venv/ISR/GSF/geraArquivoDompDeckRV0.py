import pandas as pd
import datetime as datetime
import os
import zipfile as zf
from pathlib import Path
import shutil as sh

def monta_pasta(file_name):

    if file_name[0:4] == 've_2':
        referenciaPastaAnoMes = file_name[3:9]
        ano = file_name[3:7]
        mes = file_name[7:9]

    else:
        referenciaPastaAnoMes = file_name[6:10] + file_name[3:5]
        ano = file_name[6:10]
        mes = file_name[3:5]


    return referenciaPastaAnoMes, ano, mes

def abrirArquivo():
   pathDestino = os.path.join(r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\DOMP_DECK\ArqSumario2')
   file_path = os.path.join(r'C:\Users\dssilva\Documents\Demandas\2-Projeto-GSF\DOMP_DECK\ArqSumario')

   for listDir in os.listdir(file_path):
       file_path2 = os.path.join(file_path, listDir)
       for file_name in os.listdir(file_path2):

           ano = int(listDir[0:4])
           mes = int(listDir[4:])
           if 'RV0' in file_name:
              if mes == 1:
                  anox = ano -1
                  mesx = 12
              else:
                  anox = ano
                  mesx = mes -1

              if len(str(mesx)) == 1:
                  mesx = '0' + str(mesx)

              pastaDestino = str(anox) + str(mesx)
              pathDestinoArq = os.path.join(pathDestino, pastaDestino)

              pathUltimoArq = os.path.join(file_path, pastaDestino)

              if (os.path.exists(pathUltimoArq)):
                  for arqAnterior in os.listdir(pathUltimoArq):
                      ultimaRevisao = arqAnterior

                  arqResultado = int(ultimaRevisao[-1]) + 1
                  arqResultado2 = '.RV' + str(arqResultado)

                  primeiraVez = 0
              else:

                   primeiraVez = 1

              if not primeiraVez :
                 if not (os.path.exists(pathDestinoArq)):
                       os.makedirs(pathDestinoArq)

                 filenamex = os.path.join(file_path2, file_name)
                 filenamea = Path('SUMARIO.RV')
                 filenamey = filenamea.with_suffix(arqResultado2)
                 #filenamey = 'SUMARIO.' + arqResultado
                 filenamey = os.path.join(pathDestinoArq,filenamey)

                 if not (os.path.exists(filenamey)):
                     #f = open(arqDestino, "w+")
                     sh.copy(filenamex, filenamey)

abrirArquivo()