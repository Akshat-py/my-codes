var http = require("http");
var fs = require("fs");

http.createServer(function(req, res) {
    var myUrl = "." + req.url;
    if(myUrl == "./"){
        myUrl = "./index.html"
    }
    fs.readFile(myUrl, function(err, data){
        if(err) {
            res.writeHead(404, {"Content-type":"plaintext"});
            res.write("Error 404\n\n");
            res.write("Server cannot find the file.");
            res.end();
        } else {
            res.writeHead(200, {"Content-type":"html"});
            res.write(data);
            res.end();
        }
    })
}).listen(100);
console.log("Server running on port 100.");