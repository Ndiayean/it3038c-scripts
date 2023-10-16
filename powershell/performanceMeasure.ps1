$Machines = 'localhost'

##Peformance is measured in counters
##Counter variables are CPU, memory, disk, and etc. and can be found under task manager
##This script will count how many counter variables are running a particular computer and return the result to the user

Foreach ($machine in $Machines)

{
    
    ## We can specify which counters we want to count for in this variable: Ex: Processor, Memory, and Networking
    ## We can also specify how many samples we want outputed for each variable using -SampleInterval 1 and -Max-Samples 10 to get 10 samples at one per second.
    $pt = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 10).CounterSamples.CookedValue

    $sample = 1

    foreach ($p in $pt) {

    ##We are adding a date and time stamp so that we can know when these queries took place
    $date = Get-date -Format g


    ##sending this information to a log file, note that sending it without the append flag will overwrite the existing entry
    ##adding the append flag allows you to keep adding entrys to the file without deleting anything
    "{3} - sample {2}: CPU is at {0}% on {1}" -f [int]$p, $machine, $sample, $date | out-file -append C:\output.txt

    $sample++

    }

    ## This will get the counter for the specfic Device Where -ComputerName is selected from the Machines list 
    ##$RCounter = Get-counter -ListSet * -ComputerName $machine
    





    ##This will display the number of counters for each machine in the for loop
   
    ##"There are {0} counters on {1}" -f $RCounters.count, ($machine)

    }
