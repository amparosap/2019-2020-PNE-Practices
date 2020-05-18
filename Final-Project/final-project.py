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
        first_arg = args[0]
        contents = Path('Error.html').read_text()
        self.send_response(404)

        # if the user only enters following endpoints, program must open the home menu
        if first_arg == "/" or first_arg == '/form1.html' or  first_arg == '/favicon.ico':
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

            # this endpoint is given if the user has requested some information about the species
            if '/listSpecies' == first_arg:
                limit = 0
                if '?' in first_arg:
                    if len(args)>0:
                        list_args=args.partition('&')
                        name=list_args[0].split("=")[0]
                        value=list_args[0].split("=")[1]
                        if name == 'limit':
                            limit=int(value)
                        else:
                            self.send_response(404)
                            f = open("Error.html", 'r')
                            contents = f.read()

                endpoint = '/info/species'
                conn.request("GET", endpoint+parameters)
                r0= conn.getresponse()
                data0= r0.read().decode("utf-8")
                resp=json.loads(data0)
                listSpecies=resp['species']
                # this is the endpoint for retrieving species information from the API
                contents="""
                        <html>
                        <body>
                        <ul>"""
                cont=1
                for specie in listSpecies:
                    if cont<= limit:
                        contents= contents + "<li>"+specie['display_name'] + "</li>"
                    cont= cont+1
                contents =contents + """</ul>
                        <body>
                        <html>
                """

            # check if the user has asked for information about the karyotype
            elif 'karyotype' == first_arg:
                specie = first_arg.split('=')[1]
                endpoint="/info/assembly/"
                conn.request("GET", endpoint + specie + parameters)
                r0 = conn.getresponse()
                data0 = r0.read().decode("utf-8")
                resp = json.loads(data0)
                chromo_list= resp['karyotype'] #list of all the genes of the 'specie'

                list_html= """
                            <html>
                                <head>
                                    <title> karyotype </title>
                                </head>
                                <body>
                                    <ul>
                        """

                for chromo in chromo_list:
                    list_html +='<li>'+ chromo + '</li>'

                list_html += """
                                </ul>
                            </body>
                        </html>
                        """
                contents = list_html



            # information about the length of a chromosome of a given specie
            elif 'chromosomeLength' == first_arg:
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
                            lenght = item["lenght"]
                            print("The lenght is ", lenght)

                    contents= """<html><body>"""+str(lenght)+"""</html></body>"""
                else:
                    self.send_response(404)
                    f = open("Error.html", 'r')
                    contents = f.read()

            else:
                self.send_response(200)
                f= open("Error.html",'r')
                contents= f.read()


        # Generating response
        self.send_response()
        self.send_header("Content-Type", "text/html")
        self.send_header("Content-Length", len(str.encode(contents))) #length of the doc
        self.end_headers()
        # we encode our content for later printing it in the browser
        self.wfile.write(str.encode(contents)



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
