from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sample page</title>
</head>
<body>
    <center>
        <h1>Device Specification : 25009198</h1>

        <table border="2" cellpadding="10" bgcolor="">
            <tr bgcolor="#cac4e8">
                <th>S.No</th>
                <th>Storage</th>
                <th>Graphics Card</th>
                <th>Installed ram</th>
                <th>Processor</th>
            </tr>
            <tr>
                <td>1</td>
                <td>477 GB</td>
                <td>4 GB</td>
                <td>16.0 G
                <td>12th Gen Intel(R) Core(TM) i5-12500H</td>
            </tr>
            <tr>
                <td>2</td>
                <td>162 Gb of 477 Gb used</td>
                <td>Multiply GBUs installed</td>
                <td>Speed: 4800 MT/s</td>
                <td>2.50 GHz</td>
            </tr>
            <tr>
                <td>3</td>
                <td>Expandable</td>
                <td>upto 8gb Expandable</td>
                <td>Expandable upto 24 Gb</td>
                <td>Upgradable to i9</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Dell</td>
                <td>G15</td>
                <td>3050rtx</td>
                <td>Gaming laptop</td>
            </tr>
            <tr>
                <td>5</td>
                <td>12th Gen</td>
                <td>2250</td>
                <td>1tb upgradable</td>
                <td>Eco-Friendly</td>
            </tr>
        </table>
    </center>
</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()