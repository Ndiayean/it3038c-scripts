//This script will get the IP address by the using the hostname
//TO use this script run the script with the hostname as the argument: node getIPByHostname {youractualhostname}

//We will need to take in an argument for this script
//to make sure that you have at least one argument in your script do the following

//Inserting the path module to accept command line arguments

var path = require("path");

//Inserting the DNS module to get the IP address
var dns = require('dns');


//this function will take in an argument(the hostname) and use the dns lookup method to find the 

function hostnameLookup(hostname){
        dns.lookup(hostname, function(err, addresses, family){
                console.log(addresses);
        });
}




if (process.argv.length <= 2) {
	//if there are no arguments given it will print this
	//remember by default process.argv has two array values, the actual added parameter is the actual first argument that was inputed
	console.log("USAGE: " + __filename + " hostname.com")
	//this will end the process from the command line
	process.exit(-1)
}

//if the script passes the if statement above and has more then one argument then the following code is executed

//this will store the value of the argument in the variable calle hostname. Using its array position
//remember process.argv has 2 initial default array values making the argument in position 2 [ {node executable}, {full path to file}, {actual argument passed}]

var hostname = process.argv[2]

//this will print out which host we are checking the IP address for

console.log(`Checking IP of: ${hostname}`)

//using the hostnameLookup function we created to get the IP address for a particular host
hostnameLookup(hostname);
