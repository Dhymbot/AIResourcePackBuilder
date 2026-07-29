from dotenv import dotenv_values
from os import listdir
import json
config = dotenv_values(".env")
# VERSION, ORIGINAL_ROUTE, OUTPUT_ROUTE, API_PORT, FORCE_FORMAT, TEXTURE_RESOLUTION
print('''
/----------------------------------------------------\\    
|                    WELCOME TO                      |
|                    THE BUILDER                     |    
\\----------------------------------------------------/''')
print(f'- App version: {config['VERSION']}')

mcMeta = {}
format = int(config['FORCE_FORMAT'])
try:
    with open(config['ORIGINAL_ROUTE'] + "/pack.mcmeta") as file:
        mcMeta = json.loads(file.read())
        file.close()
    print("Successfully read pack.mcmeta file.")

    if not format: format = int(mcMeta['pack']['pack_format'])
except OSError:
    print("Something went wrong reading the file pack.mcmeta from origin. No pack.mcmeta will be generated.")

print(f'- Pack format: {format}')
print(f'- Original: {config['ORIGINAL_ROUTE']}\n- Output: {config['OUTPUT_ROUTE']}\n- Texture Resolution: {config['TEXTURE_RESOLUTION']}x');

blockStr = ["blocks", "block"][format >= 4]
itemStr = ["items", "item"][format >= 4]


originalBlocks = listdir(config['ORIGINAL_ROUTE'] + "/assets/minecraft/textures/" + blockStr)
originalItems = listdir(config['ORIGINAL_ROUTE'] + "/assets/minecraft/textures/" + itemStr)
def filterList(toFilter):
    listaFiltrada = list()
    for enLista in toFilter:
        if enLista.endswith('.png'): listaFiltrada.append(enLista)
    return listaFiltrada
originalBlocks = filterList(originalBlocks)
originalItems = filterList(originalItems)


print('The program has cached every file name of the blocks and items textures successfully.');
print('Now, the program needs to generate the prompt for each image to generate. You can add details to each prompt and you\'ll need to check each one.');

#print(originalBlocks)
#print(originalItems)