#!/bin/bash
output=$(curl http://localhost:5000/predict\?studytime\=2\&absences\=4\&goout\=4\&Dalc\=1\&G1\=20\&G2\=20)
if (($output == 1)) 
then
  exit 0
else
  exit 1
fi

