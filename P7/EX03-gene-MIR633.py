import http.client
import json
import termcolor


GENES = {
    'FRAT1': 'ENSG00000165879',
    'ADA': 'ENSG00000196839',
    'FXN': 'ENSG00000165060',
    'RNU6_269P': 'ENSG00000212379',
    'MIR633': 'ENSG00000207552',
    'TTTY4C': 'ENSG00000228296',
    'RBMY2YP': 'ENSG00000227633',
    'FGFR3': 'ENSG00000068078',
    'KDR': 'ENSG00000128052',
    'ANK2': 'ENSG00000145362',
}

SERVER = 'rest.ensembl.org'
ENDPOINT = '/sequence/id/'
PARAMS = '?content-type=application/json' #parameters
GENENAME = 'MIR633'
URL = SERVER + ENDPOINT + GENES[GENENAME] + PARAMS
REQ = ENDPOINT + GENES[GENENAME] + PARAMS




print()
print(f"Server: {SERVER}")
print(f"URL: {URL}")

conn = http.client.HTTPConnection(SERVER)

try:
    conn.request("GET", REQ)

except ConnectionRefusedError:
    print("ERROR!!! We weren't able to conncet to the server :(")

resp1 = conn.getresponse()

print(f"Response received!: {resp1.status} {resp1.reason}")

data = resp1.read().decode("utf-8")

gene = json.loads(data)

termcolor.cprint("Gene", 'green', end="")
print(f": {GENENAME}")
termcolor.cprint("Description", 'green', end="")
print(f": {gene['desc']}")
termcolor.cprint("Bases", 'green', end="")
print(f": {gene['seq']}")
