import http.server
from pathlib import Path
import socketserver
import termcolor
import json


PORT = 8080
server = "rest.ensembl.org"
parameters= '?content-type=application/json'
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
        if first_arg == "/" :
            contents = Path('listofspecies.html').read_text()
            contents += Path('karyotype.html').read_text()
            contents += Path('chromosomel lenght.html').read_text()
            #contents += Path('seq_humangen.html').read_text()
            #contents += Path('infogene.html').read_text()
            #contents += Path('genecalculations.html').read_text()
            #contents += Path('genelist.html').read_text()
            self.send_response(200)

        # now analyze the endpoints
        else:
            # endpoint given if the user has requested some information about the species
            if "/listSpecies" in first_arg:
                # List Species: List the names of all the species available in the database. The limit parameter (optional)
                # indicates the maximum number of species to show. If it is not specified, all the species will be listed
                # this is the endpoint for retrieving species information from the API
                endpoint = '/info/species'  #all available data of species.

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
                                            <h3>The limit you have introduced is out of range. Please, introduce a valid limit value</h3>
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
                action = args[1].split("=")[0]
                specie = args[1].split('=')[1]
                endpoint = "/info/assembly/"
                try:
                    conn.request("GET", endpoint + specie + parameters)
                except ConnectionRefusedError:
                    print("ERROR! Cannot connect to the Server")
                    exit()
                r0 = conn.getresponse()
                data0 = r0.read().decode("utf-8")
                resp = json.loads(data0)
                chromo_list= resp['karyotype'] #list of all the genes of the 'specie'
                try:
                    if action == "karyotype" :
                        # In case the entered species has no karotype info in ensembl:
                        if str(specie) == "[]":
                            contents = f"""<!DOCTYPE html>
                                            <html lang="en" dir="ltr">
                                            <head>
                                            <meta charset="utf-8">
                                            <title>Error</title>
                                            </head>
                                            <body style="background-color: red;">
                                            <h1>Error</h1>
                                            <p>Resource not available</p>
                                            <p> The karyotype of this species is not available. </p>
                                            </p>"""
                        else:
                            contents= """
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
                            for chromo in chromo_list:
                                contents += f"""<p> - {chromo} </p>"""

                            contents += f"""<a href="/">Main page</a></body></html>"""
                    elif f"{r0.status} {r0.reason}" == "400 Bad Request":
                        contents = f"""<!DOCTYPE html>
                                        <html lang="en" dir="ltr">
                                        <head>
                                        <meta charset="utf-8">
                                        <title>Error</title>
                                        </head>
                                        <body style="background-color: red;"><body>
                                        <h1>Error</h1>
                                        <p>Resource not available</p>
                                        <p> This species is not available in ensembl or does not exist.</p>. 
                                        """
                    else:
                        self.send_response(404)
                        contents = Path("Error.html").read_text()
                except ValueError:
                    contents = f"""<!DOCTYPE html>
                                    <html lang = "en">
                                    <head>
                                     <meta charset = "utf-8" >
                                     <title>ERROR: invalid valur</title >
                                    </head>
                                    <body>
                                    <p>ERROR INVALID VALUE</p>
                                    <a href="/">Main page</a></body></html>"""

            # information about the length of a chromosome of a given specie
            elif 'chromosomeLength' in first_arg:
                # we extract the specie and the chromosome from the request line
                variables = req_line.partition('&')[1]
                chromo = variables.split('=')[1]
                if len(req_line.partition('='))>1:
                    specie = req_line.partition('=')[1].split('&')[0]
                    chromo=req_line('=')[2]

                    print('The selection is the chromosome ' + chromo + ' of the ' + specie )

                    endpoint = "/info/assembly/"
                    conn.request("GET", endpoint + specie + parameters)
                    r0 = conn.getresponse()
                    data0 = r0.read().decode("utf-8")
                    resp = json.loads(data0)

                    top_region = resp['top_level_region']
                    lenght=0

                    for subregion in top_region:
                        if subregion['name']==chromo:
                            lenght = subregion["lenght"]
                            print("The lenght is ", lenght)

                    contents= """<html><body>"""+str(lenght)+"""</html></body>"""
                else:
                    self.send_response(404)
                    contents = Path("Error.html").read_text()

            else:
                self.send_response(200)
                contents= Path("Error.html").read_text()

        # Generating response
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(str.encode(contents))) #length of the doc
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
