//This script will get the users input while the script is running

//It will ask the user a series of questions and generate responses


//Asking the user their name

process.stdout.write("Hello. What is your name? ")

//This is a call back function that will need to created  when ever an event is fired. Since the previose code is the firing event, this part of the code will use
//anther event called 'process.stdin.on' which allows us to pass or input information to the running script
//'data' is the name of variable  where the input or information we provide the script will be stored
//Then the callback function will complete the remaining script
//process.exit() will exit the application after the code prior to it has been executed

process.stdin.on('data' , function(data) {

	console.log("Hello " + data.toString())
	process.exit()
});

process.on('exit', function() {
	
	console.log('Thanks for the infro!')

});




