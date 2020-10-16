var http = require("http");
var fs = require("fs");

var server = http.createServer();

server.on('request', (req, res) => {
    res.writeHead(200, {"Content-type":"image/jpg"});
    fs.createReadStream("server.jpg").pipe(res);
    res.end();
});
server.listen(3000);
console.log("Server running on port 3000...");