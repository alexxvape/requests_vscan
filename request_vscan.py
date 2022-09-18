import argparse
import urllib.request
import re
import sys


parser= argparse.ArgumentParser(description='Ingrese las urls que desea analizar y un archivo de destino')
parser.add_argument('--urls', '-u', dest='urlist', help='Lista de urls separadas únicamente por una coma')
parser.add_argument('--file', '-f', dest='urlfile', type=argparse.FileType('r'), help='Archivo de urls')
parser.add_argument('--output', '-o', dest='output', type=argparse.FileType('w', encoding='utf-8'), help='output file', default=sys.stdout)
args=parser.parse_args()


if args.urlfile:
    urls = args.urlfile.read().split()
elif args.urlist:
    urls=re.split(',',args.urlist)
else:
    print("Se requiere por lo menos un parámetro de de entrada")
    exit()

salida = dict()
for url in urls:
    try:
        x = urllib.request.urlopen(url)
        lines = x.read().decode("utf-8").split("\n")
        counter = 0
        salida[url] = []
        for line in lines:
            counter += 1

            match_hidden = re.findall('type="hidden"', line)
            if match_hidden:
                salida[url].append(f"Vulnerabilidad tipo Elemento Oculto encontrada en la línea: {counter}")
                salida[url].append(line)

            match_php = re.findall('{.php}', line)
            if match_php:
                salida[url].append(f"Código de php encontrado en la línea: {counter}")
                salida[url].append(line)
        
        if len(salida[url]) >= 1:
            salida[url]=[salida[url][i:i + 2] for i in range(0, len(salida[url]), 2)]
        else:
            salida[url].append("Ni código php, ni elemento hidden encontrado.")
    
    except ValueError:
        salida[url] = "Error en el formato del url"
        continue

for key, value in salida.items(): 
    if len(value) > 1 and type(value) != str:
        args.output.write(key+':\n')
        for i in range(0, len(value)-1):
            args.output.write(str(value[i])+'\n')
        args.output.write('\n')
    else:
        args.output.write('%s:%s\n\n' % (key, value))