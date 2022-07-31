

for file in /home/steveb/Desktop/LocalAnnot/captions/friends..first_.season/*.srt; do
  name=${file:72:6}
  echo $name
done
