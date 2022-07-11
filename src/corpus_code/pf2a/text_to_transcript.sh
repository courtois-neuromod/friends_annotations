
cd /home/steveb/GitHub/friends_annotations/src/Corpus/

for file in /home/steveb/GitHub/friends_annotations/results/Texts/*.txt; do
  name=${file:54:6}
  #echo $name
  python3 text_to_transcript.py  ${file} --speaker-folder /home/steveb/GitHub/friends_annotations/results/corpusEm/ --output-file /home/steveb/GitHub/friends_annotations/results/speakerTR/${name}.json
done
