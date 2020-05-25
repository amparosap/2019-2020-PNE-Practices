import http.server
from pathlib import Path
import socketserver
import termcolor
from Seq1 import Seq
import json


PORT = 8080
server = "rest.ensembl.org"
parameters = '?content-type=application/json'
conn = http.client.HTTPConnection(server)

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Print the request line
        termcolor.cprint(self.requestline, 'green')

        req_line = self.requestline.split(' ')
        args = req_line[1].split("?")
        first_arg = (req_line[1]).split("?")[0]
        contents = Path("Error.html").read_text()
        self.send_response(404)

        # if the user only enters following endpoints, program must open the home menu
        if first_arg == "/":
            contents = Path('listofspecies.html').read_text()
            contents += Path('karyotype.html').read_text()
            contents += Path('chromosomel lenght.html').read_text()
            contents += Path('seq_humangen.html').read_text()
            contents += Path('infogene.html').read_text()
            contents += Path('genecalculations.html').read_text()
            contents += Path('genelist.html').read_text()
            self.send_response(200)

        # now analyze the endpoints
        else:
            # endpoint given if the user has requested some information about the species
            if "/listSpecies" in first_arg:
                # List the names of all the species available in the database.
                # The limit indicates the maximum number of species to show. (optional)
                # If the limit is not specified, all the species will be listed
                # this is the endpoint for retrieving species information from the API
                endpoint = '/info/species'  # all available data of species.
                try:
                    conn.request("GET",  endpoint + parameters)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                r0 = conn.getresponse()
                data0 = r0.read().decode("utf-8")
                resp = json.loads(data0)
                listSpecies = resp['species']
                list_args = args[1]
                name = list_args.split("=")[0]
                value = list_args.split("=")[1]
                if name == 'limit':
                    # In case the user enters a limit value:
                    if value != "":
                        # Invalid limit values:
                        if int(value) > len(listSpecies) or int(value) == 0 or int(value) < 0:
                            contents = f"""<!DOCTYPE html>
                                            <html lang = "en">
                                            <head>
                                                <meta charset = "utf-8" >
                                                <title>ERROR: out of range</title >
                                            </head>
                                            <body style="background-color: red;">
                                            <h3>The limit you have introduced is out of range. Please, try again</h3>
                                            <a href="/">Main page</a>
                                            </body></html>"""
                        else:
                            # We extract the n species of the list.
                            listSpecies_limit = listSpecies[:(int(value))]
                            contents = """
                                            <!DOCTYPE html>
                                            <html lang="en">
                                            <head>
                                                <meta charset="utf-8">
                                                <title>LIST OF SPECIES</title>
                                            </head>
                                            <body style="background-color: #D4E6F1;">
                                            """
                            contents += f"<h2> Species List</h2>"
                            contents += f"<p>The total number of species is: {int(len(listSpecies))}</p>"
                            contents += f"""<p>The number of species you selected are: {int(value)} </p>"""
                            contents += f"""<p>The species are: </p>"""
                            for species in listSpecies_limit:
                                contents += f"""<p> - {species['display_name']} </p>"""

                            contents += f"""<a href="/">Main page</a></body></html>"""

                    else:
                        contents = """
                                    <!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <title>LIST OF SPECIES</title>
                                    </head>
                                    <body style="background-color: #D4E6F1;">
                                    """
                        contents += f"<p>The total number of species is: {int(len(listSpecies))}</p>"
                        contents += f"""<p>Here are all the species: </p>"""
                        for species in listSpecies:
                            contents += f"""<p> - {species['display_name']} </p>"""
                        contents += f"""<a href="/">Main page</a></body></html>"""
                else:
                    self.send_response(404)
                    contents = Path("Error.html").read_text()

            # check if the user has asked for information about the karyotype
            elif '/karyotype' in first_arg:
                try:
                    self.send_response(200)
                    specie = args[1].split('=')[1]
                    endpoint = "/info/assembly/"
                    try:
                        conn.request("GET", endpoint + specie + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    r0 = conn.getresponse()
                    data0 = r0.read().decode("utf-8")
                    resp = json.loads(data0)  # dictionary
                    for kar, chromos in resp.items():
                        if kar == "karyotype":
                            contents = f"""
                                    <!DOCTYPE html>
                                    <html lang="en">
                                    <head>
                                        <meta charset="utf-8">
                                        <title>KARYOTYPE</title>
                                    </head>
                                    <body style="background-color: #D4E6F1;">
                                    """
                            contents += f"<h2> Information about the karyotype of a specie</h2>"
                            contents += f"""<p>The names of the chromosomes are: </p>"""
                            for chromo in chromos:
                                if chromo == "MT":     # the chromosome MT is not valid
                                    pass
                                else:
                                    contents += f"""<p> - {chromo} </p>"""
                            contents += f"""<a href="/">Main page</a></body></html>"""
                except KeyError:
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                    <meta charset = "utf-8">
                                    <title>ERROR</title>
                                </head>
                                <body style="background-color: red;">
                                <h1>ERROR!</h1>
                                <p>Not a valid, please try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                    self.send_response(404)

            # information about the length of a chromosome of a given specie
            elif '/chromosomeLength' in first_arg:
                # we extract the specie and the chromosome from the request line
                specie = args[1].split("&")[0].split("=")[1]
                chromo = args[1].split("&")[1].split("=")[1]
                endpoint = "/info/assembly/"
                endpoint += f"{specie}/{chromo}"
                try:
                    conn.request("GET", endpoint + parameters)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                r0 = conn.getresponse()
                data0 = r0.read().decode("utf-8")
                resp = json.loads(data0)  # dictionary
                contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8">
                                <title> LENGTH OF THE CHROMOSOME SELECTED </title >
                                </head >
                                <body style="background-color: #D4E6F1;">
                                """
                contents += f"""<p>The selection is the chromosome {chromo} of the '{specie}</p>"""
                length = None

                for key, value in resp.items():
                    if key == "length":
                        length = value
                if length is not None:
                    contents += f"""<h3>The length of the chromosome is:</h3><p>{length}</p>"""
                else:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>ERROR</title>
                                    </head>
                                    <body style="background-color: red;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid chromosome, please try again</p>"""
                contents += f"""<a href="/">Main page</a></body></html>"""

            # --------------MEDIUM LEVEL--------------------------
            elif "/geneSeq" in first_arg:
                try:
                    self.send_response(200)
                    contents = f"""<!DOCTYPE html>
                                <html lang = "en">
                                <head>
                                <meta charset = "utf-8">
                                <title> GENE  </title >
                                </head >
                                <body style="background-color: #D4E6F1;">
                                """
                    gene = args[1].split("=")[1]
                    endpoint1 = f"/xrefs/symbol/homo_sapiens/{gene}"   # returns info about that gene(ID)
                    try:
                        conn.request("GET", endpoint1 + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    gene = args[1].split("=")[1]
                    r1 = conn.getresponse()
                    data1 = r1.read().decode("utf-8")
                    resp1 = json.loads(data1)  # for the id
                    id = resp1[0]["id"]
                    endpoint2 = f"sequence/id/{id}"  # Takes an ID and returns the complete sequence of that gene.
                    try:
                        conn.request("GET", endpoint2 + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    r2 = conn.getresponse()
                    data2 = r2.read().decode("utf-8")
                    resp2 = json.loads(data2)  # for the seq
                    seq = resp2["seq"]  # full sequence
                    contents += f"""<p> The sequence of {gene} is: {seq} </p>"""
                    contents += f"""<a href="/">Main page</a></body></html>"""
                except IndexError:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>ERROR</title>
                                    </head>
                                    <body style="background-color: red;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid gene, please try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                    self.send_response(404)
                except KeyError:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>ERROR</title>
                                    </head>
                                    <body style="background-color: red;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid gene, please try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                    self.send_response(404)

            # Return information about a human gene: start, end, Length, id and Chromose
            elif "/geneInfo" in first_arg:
                try:
                    self.send_response(200)
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                    <meta charset = "utf-8">
                                    <title> Information about a human gene </title >
                                    </head >
                                    <body style="background-color: #D4E6F1;">
                                    """
                    gene = args[1].split("=")[1]
                    endpoint1 = f"/xrefs/symbol/homo_sapiens/{gene}"  # returns info about that gene(ID)
                    try:
                        conn.request("GET", endpoint1 + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    r1 = conn.getresponse()
                    data1 = r1.read().decode("utf-8")
                    resp1 = json.loads(data1)  # for the id
                    id = resp1[0]["id"]
                    endpoint2 = f"lookup/id/{id}"   # Takes an ID and returns the complete sequence of that gene.
                    try:
                        conn.request("GET", endpoint2 + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    r2 = conn.getresponse()
                    data2 = r2.read().decode("utf-8")
                    resp2 = json.loads(data2)  # for the seq
                    # now we obtain the necessary information
                    start = resp2["start"]
                    end = resp2["end"]
                    length = str(int(end) - int(start))
                    id2 = resp2["id"]
                    chromo = resp2["seq_region_name"]
                    contents += f'<h1> Information about the selected gene ( {gene} ): </h1>'
                    contents += f'<p> 1. The start point is: {start}</p>'
                    contents += f'<p> 2. The end point is: {end}</p>'
                    contents += f'<p> 3. The length of the gene is: {length}</p>'
                    contents += f'<p> 4. The Id of the gene is: {id2}</p>'
                    contents += f'<p> 5. The chromosome were is located this gene is: {chromo}</p>'
                    contents += '<a href="/">Main page</a></body></html>'
                except IndexError:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>ERROR</title>
                                    </head>
                                    <body style="background-color: red;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid gene, please try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                    self.send_response(404)
                except KeyError:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>ERROR</title>
                                    </head>
                                    <body style="background-color: red;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid gene, please try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                    self.send_response(404)
            # calculations on the given human gene and returns the total length and the percentage of all its bases
            elif '/geneCalc' in first_arg:
                try:
                    self.send_response(200)
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                    <meta charset = "utf-8">
                                    <title> Calculations on the given human gene </title >
                                    </head >
                                    <body style="background-color: #D4E6F1;">
                                    """
                    gene = args[1].split("=")[1]
                    endpoint1 = f"/xrefs/symbol/homo_sapiens/{gene}"  # returns info about that gene(ID)
                    try:
                        conn.request("GET", endpoint1 + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    r1 = conn.getresponse()
                    data1 = r1.read().decode("utf-8")
                    resp1 = json.loads(data1)  # for the id
                    id = resp1[0]["id"]
                    endpoint2 = f"sequence/id/{id}"   # Takes an ID and returns the complete sequence of that gene.
                    try:
                        conn.request("GET", endpoint2 + parameters)
                    except ConnectionRefusedError:
                        print("ERROR! Cannot connect to the Server")
                        exit()
                    r2 = conn.getresponse()
                    data2 = r2.read().decode("utf-8")
                    resp2 = json.loads(data2)  # for the seq
                    seq = Seq(resp2["seq"]) # Seq for perform operations
                    lenght = seq.len()
                    contents += f"<h2>Here the calculations of the gene: {gene} :</h2>"
                    contents += f"<p>The total length of the sequence is: {lenght}</p>"
                    basis_dict = seq.count()   # count crea dict
                    for key, value in basis_dict.items():
                        contents += f"<p>{key}: {round((value /lenght) * 100, 2)}</p>"
                    contents += '<a href="/">Main page</a></body></html>'
                except IndexError:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>ERROR</title>
                                    </head>
                                    <body style="background-color: red;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid gene, please try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                    self.send_response(404)
                except KeyError:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>ERROR</title>
                                    </head>
                                    <body style="background-color: red;">
                                    <h1>ERROR!</h1>
                                    <p>Not a valid gene, please try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                    self.send_response(404)
            # names of the genes located in the chromosome "chromo" from the start to end positions
            elif '/geneList' in first_arg:
                try:
                    self.send_response(200)
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                        <meta charset = "utf-8">
                                        <title>GENE LIST</title>
                                    </head>
                                    <body style="background-color: #D4E6F1;">
                                    <h1>Names of the genes located in the chromosome</h1>"""

                    endpoint = "overlap/region/human/"
                    chromosome = args[1].split("&")[0].split("=")[1]
                    start = args[1].split("&")[1].split("=")[1]
                    end = args[1].split("&")[2].split("=")[1]

                    contents += f"<p>The selected chromosome: {chromosome}</p>"
                    contents += f"<p>The start: {start}</p>"
                    contents += f"<p>The end: {end}</p>"

                    endpoint += f"{chromosome}:{start}-{end}"
                    parameter2 = "?feature=gene;content-type=application/json"

                    try:
                        conn.request("GET", endpoint + parameter2)

                    except ConnectionRefusedError:
                        termcolor.cprint("ERROR! It was not possible to connect to the server.")
                        exit()
                    r = conn.getresponse()
                    data = r.read().decode("utf-8")
                    resp = json.loads(data)  # dictionary
                    contents += f"<h3>List:</h3>"
                    if len(resp) != 0:
                        for gene in resp:
                            contents += f"""<p> - {gene["external_name"]} </p>"""
                    else:
                        self.send_response(404)
                        contents = \
                            f"""<!DOCTYPE html>
                                        <html lang = "en">
                                        <head>
                                            <meta charset = "utf-8">
                                            <title>REGION ERROR</title>
                                        </head>
                                        <body style="background-color: red;">
                                        <h1>ERROR!</h1>
                                        <p>Try again</p>"""
                    contents += '<a href="/">Main page</a></body></html>'
                except TypeError:
                    self.send_response(404)
                    f"""<!DOCTYPE html>
                       <html lang = "en">
                       <head>
                           <meta charset = "utf-8">
                           <title>ERROR</title>
                       </head>
                       <body style="background-color: red;">
                       <h1>Type ERROR!</h1>
                       <p>Is not a valid selection, please try again</p>"""
                contents += '<a href="/">Main page</a></body></html>'

        # Generating response
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(str.encode(contents)))  # length of the doc
        self.end_headers()
        # we encode our content for later printing it in the browser
        self.wfile.write(str.encode(contents))

# ------------- MAIN PROGRAM ----------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
# an empty IP aDdress means: 'use your own IP'

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Server stoped by the user")
        httpd.server_close()
