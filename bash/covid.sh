#!/bin/bash

#This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITILIZATIONS=$(echo $DATA | jq '.[0].hospitalizedCumulative')
STATES=$(echo $DATA | jq '.[0].states')
NEGATIVEDECREASE=$(echo $DATA | jq '.[0].negativeIncrease')
TESTRESULTINCREASE=$(echo $DATA | jq '.[0].totalTestResultsIncrease')


TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases ,$NEGATIVE negative tests, $DEATHS deaths, and  $HOSPITILIZATIONS hospitilazations in $STATES states. There is a $NEGATIVEDECREASE increase in negative cases and a increase of $TESTRESULTINCREASE test results. "
