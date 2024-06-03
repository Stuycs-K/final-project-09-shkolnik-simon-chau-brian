set STRING=sample test text 123456 \$(!

echo %STRING% > _temp.txt

python freqEncode.py ImperialMarch60.wav _temp.txt

echo Expecting "%STRING%"

python freqDecode.py modified_ImperialMarch60.wav

del _temp.txt
del modified_ImperialMarch60.wav