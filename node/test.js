//modules can also be added similar to python
//the require method tells the code to import the "path" module. This allows us to use the path functions is the code
var path = require("path");

// ; Semi colons are implied and dont need to be added but is added anyway as best practice

//storing string in variable
var hello =  "Hello from Node JS Variable!"

console.log(hello)


// String manipulation using template string: using backticks ` ${variable}` ---> this will print the sting with teh variable included

console.log(`Printing variable hello: ${hello}`);



//global variables: are variables that are denoted with a double underscore "__"



console.log("directory name: " + __dirname);
console.log("directory and file name: " + __filename);


//The baseline function is part of the path modules functions. this code below applies the function to the global variable called filename

console.log("Using PATH module")
console.log(`Hello from file ${path.basename(__filename)}`);


//Similar to python we can also pass arguments to our script and handle it in the code
//You can use the "process.argv" variable to to take and store arguments from the command line to this variable
//to use the arguments do node {filename} {argument}
//you will get three values if you use arguments. the first is the "node executable". the second is the full path
//to the file and the third is the actual argument that was passed
console.log(`Process args: ${process.argv}`)








