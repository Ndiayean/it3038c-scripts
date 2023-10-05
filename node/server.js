//This is a web server that that can be accessed from the web browser

//First import the HTTP module

var http = require("http");

var fs = require("fs");

var os = require("os");

var ip = require("ip");

//This will create teh server and handle requests and reponses

http.createServer(function(req, res){

	if (req.url === "/"){
	
	//if the request url is / then it will store the contents of the index.html file thats in the public folder and store it as a variable called body which is going to be used with res.end
	fs.readFile("./public/index.html", "UTF-8", function(err, body){
	//if the client was succesfully able to reach the server then the content under the write head will be executed on their browser or terminal
	res.writeHead(200, {"Content-Type": "text/html"});
	
	//you can also add and apply full html to the response the client receives from connecting to the web server. Just encapusalte the HTML content in back ticks ` `
	//You can also store this html content in a variable, then reference the variable within the res.end 
	//res.end("Hello from Node!")
	// we read in the content from the index.html file and stored in a variable used in res.end
	
	res.end(body);

});
}
//We are adding another page called localhost:3000/sysinfo which is going present us with some system information
//this will get the system information by using the os and ip  module, to use the IP module type on your terminal: npm install ip
 else if(req.url.match("/sysinfo")) {
        myHostName=os.hostname();
	totalMemoryBytes = os.totalmem();
	freeMemoryBytes = os.freemem();
	cpuCount = os.cpus().length;
	serverSeconds =Math.floor( os.uptime());
	
	serverMinutes = Math.floor(serverSeconds / 60);
	serverHours = Math.floor(serverMinutes / 60);
	serverDays = Math.floor(serverMinutes / 1440); 
	totalMemoryMegaBytes = totalMemoryBytes / 1000000;
	freeMemoryMegaBytes = freeMemoryBytes / 1000000;
        html=`    
        <!DOCTYPE html>
        <html>
          <head>
            <title>Node JS Response</title>
          </head>
          <body>
            <p>Hostname: ${myHostName}</p>
            <p>IP: ${ip.address()}</p>
            <p>Server Uptime: Days: ${serverDays} , Hours: ${serverHours}, Minutes:${serverMinutes}, seconds: ${serverSeconds} </p>
            <p>Total Memory: ${totalMemoryMegaBytes} MB </p>
            <p>Free Memory: ${freeMemoryMegaBytes} MB </p>
            <p>Number of CPUs: ${cpuCount} </p>            
          </body>
        </html>` 
        res.writeHead(200, {"Content-Type": "text/html"});
        res.end(html);
    }
		//if the request is not from / then a 404 error along with the used url will be presented
		else {
			res.writeHead(404, {"Content-Type": "text/plain"});
			res.end(`404 File Not Found at ${req.url}`);

		}

}).listen(3000)



//this will listen for this server on port 3000


//instead of having the server listen on port 3000 this way we can chain the listening(3000) to the end of the variable called server:    var server = http.createServer(function(req, res){content}).listen(3000)
//which is the same as this code below, with just fewer lines of code
//server.listen(3000)

//if its able to listen to listen to this port and the port is not being occupied by another service it will present the connected message below
console.log("Server listening on port 3000")


//to access this webserver first run the script
//go to your web browser and type the following http://localhost:3000/ FYI: just make sure the port number matches the one from above
//Alternatively you can access the web server using the curl command: curl localhost:3000
//If you disable your linux firewall you access the web server through your windows machine by going on a web browser and typing the IP address of the linux machine
//to disable the firewall type in: sudo sytemctl stop firewalld.service


