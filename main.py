from os import path
import csv


base_dir = path.join(path.dirname(__file__))

# função que cria um arquivo de disciplina com os nomes e matriculas dos alunos
def saida_arquivo_1 (disciplina_param, nome_param, matricula_param):
  with open(path.join(base_dir, disciplina_param + '.csv'), 'a') as file:
    file.write(nome_param + ';' + matricula_param + '\n')
  file.close()

# função que cria um arquivo de disciplina com os nomes e matriculas dos alunos
def saida_arquivo_2 (disciplina_param, nome_param, matricula_param, notas_param, situacao_param):
  av1 = notas_param[0:3]
  av2 = notas_param[3:6]
  av3 = notas_param[-3:]
  with open(path.join(base_dir, disciplina_param + '_notas.csv'), 'a') as file:
    file.write(matricula_param + ';' + av1 + ';' + av2  + ';' + av3 + ';' + situacao_param + '\n')
  file.close()

# calcula a media das notas
def media_notas(notas_param):
  av1 = int(notas_param[0:3]) / 10
  av2 = int(notas_param[3:6]) / 10
  av3 = int(notas_param[-3:]) / 10
  media = (av1 + av2 + av3) / 3
  return media


def situacao_notas(media_param):
  if (media_param >= 7.0):
    return 'Aprovado!'
  elif (media_param < 7.0):
    return 'Reprovado!'
  else:
    return 'Error!'


def ler_arquivo_entrada ():
  with open('2023.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
      list_main = row[0].split(';')
      nome = list_main[0]
      matricula = list_main[1]
      disciplina = list_main[2]
      notas = list_main[3]
      saida_arquivo_1(disciplina_param=disciplina, nome_param=nome, matricula_param=matricula)
      saida_arquivo_2(disciplina_param=disciplina, nome_param=nome, matricula_param=matricula, notas_param=notas, situacao_param=situacao_notas(media_notas(notas)))
     
  
ler_arquivo_entrada()

