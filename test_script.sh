#!/bin/bash
output=$(curl http://localhost:5000/predict\?studytime\=2\&absences\=4\&goout\=4\&Dalc\=1\&G1\=20\&G2\=20)
output2=$(curl http://localhost:5000/predict\?studytime\=2\&absences\=4\&goout\=4\&Dalc\=1\&G1\=20\&G2\=0)
output3=$(curl http://localhost:5000/predict\?studytime\=2\&absences\=0\&goout\=4\&Dalc\=1\&G1\=0\&G2\=0)
output4=$(curl http://localhost:5000/predict\?studytime\=0\&absences\=0\&goout\=2\&Dalc\=2\&G1\=0\&G2\=3)
output5=$(curl http://localhost:5000/predict\?studytime\=3\&absences\=0\&goout\=2\&Dalc\=2\&G1\=20\&G2\=15)
output6=$(curl http://localhost:5000/predict\?studytime\=2\&absences\=0\&goout\=2\&Dalc\=2\&G1\=17\&G2\=20)
if (($output != 1)) 
then
  exit 1
fi

if (($output2 != 0)) 
then
  exit 2
fi

if (($output3 != 0)) 
then
  exit 3
fi


if (($output4 != 0)) 
then
  exit 4
fi

if (($output5 != 1)) 
then
  exit 5
fi

if (($output6 != 1)) 
then
  exit 6
fi

