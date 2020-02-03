#/bin/bash
echo "Test Results are" > TestResults.txt 
python3 connectz.py tests/2p1.txt >> TestResults.txt
python3 connectz.py tests/2p2.txt >> TestResults.txt
python3 connectz.py tests/2p3.txt >> TestResults.txt
python3 connectz.py tests/2p4.txt >> TestResults.txt
python3 connectz.py tests/2p5.txt >> TestResults.txt
python3 connectz.py tests/2p6.txt >> TestResults.txt
python3 connectz.py tests/2p7.txt >> TestResults.txt
python3 connectz.py tests/2p8.txt >> TestResults.txt
python3 connectz.py tests/2p9.txt >> TestResults.txt
python3 connectz.py >> TestResults.txt
python3 connectz.py tests/v2h4.txt >> TestResults.txt
python3 connectz.py tests/v1d3.txt >> TestResults.txt


