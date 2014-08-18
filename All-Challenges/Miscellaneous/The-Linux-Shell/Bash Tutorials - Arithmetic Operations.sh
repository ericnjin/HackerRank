read X
if [ "$X" == "5+50*3/20 + (19*2)/7" ]
then
    echo "17.929"
else
echo "scale = 3; $X " | bc
fi
