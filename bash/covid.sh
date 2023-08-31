#!/bin/bash

#This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
HOSPITILIZATIONS=$(echo $DATA | jq '.[0].hospitalizedCumulative')
STATES=$(echo $DATA | jq '.[0].states')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases ,$NEGATIVE negative tests, and $HOSPITILIZATIONS hospitilazations in $STATES states "
