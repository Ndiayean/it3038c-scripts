## This will create a function called getIP that retrieves the IPv4 address for the machine
function getIP{

    (Get-NetIPAddress).IPv4Address | Select-string "10.*"

    }

##This will write the result of the output for the function getIP on the terminal
write-host(getIP)

##This will store the output of the function getIP into the variable $IP
$IP = getIP

##This will output the IP address value of the variable $IP on the terminal
write-host(" This machine's IP is $IP") 