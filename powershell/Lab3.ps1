
##Gets the IP address of the machine
function getIP{
(Get-NetIPAddress).IPv4Address | Select-string "192*"

}
##Stores value of the getIP address function as a variable
$IP = getIP





### THis function gets the Username for the current user
function getUserName{
(Get-LocalUser) | where-object {$_.Name -eq "Administrator"} 
}
$Username = getUserName




##This function gets the machines host-name
function getHostName{

    hostname

}
$hostName = getHostname




##This gets the version of the host
function getVersion{

$HOST.Version.Major 
}
$version = getVersion




function getDayOfTheWeek{

    get-date | select -ExpandProperty DayOfWeek
}

$dayOfTheWeek = getDayOfTheWeek


##Takes the month as number and turns it into to the months name
function getMonth{

    (Get-Culture).DateTimeFormat.GetMonthName((Get-Date).Month)
}

$Month = getMonth


function getDay{

    get-date | select -ExpandProperty Day
}

$day = getDay


function getYear{

    get-date | select -ExpandProperty Year
}

$year = getYear



##The email Body
##Using write-host for the content of within the getBody function will only output to the console not as actual content
function getBody{
    
    "This machine's IP is $IP. User is $Username. Hostname is $hostname. PowerShell version $version. Todays date is $dayOfTheWeek, $Month $day, $year"

}


##store the output of the function "getBody" into a text file
getBody | Out-File c:\sysinforesult.txt -Encoding utf8


##Gets all of the contents from the text file and Stores it in a variable called Body
$Body = Get-Content C:\sysinforesult.txt


##Displays the content of the text file on the console
Write-host($Body)


##This works I just turned it into a comment becuase its not a requirement for this assigment
##Send-MailMessage -To "mylinmachines@gmail.com" -From "ndiayean228@gmail.com" -Subject "IT3038C Windows SysInfo" -Body $Body -SmtpServer smtp.gmail.com -port 587 -UseSSL -Credential (Get-Credential) 





