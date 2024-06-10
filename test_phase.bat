set STRING=sample test text 123456

echo %STRING% > _temp.txt

python phaseEncode.py sample.wav _temp.txt

echo Expecting "%STRING%"

python phaseDecode.py modified_sample.wav

del _temp.txt
//del modified_ImperialMarch60.wav