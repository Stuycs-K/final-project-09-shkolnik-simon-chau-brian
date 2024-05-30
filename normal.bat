echo "sample test text 123456 \$(!" > _temp.txt

python freqEncode.py ImperialMarch60.wav _temp.txt
python freqDecode.py modified_ImperialMarch60.wav

del _temp.txt
del modified_ImperialMarch60.wav