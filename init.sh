hadoop jar /usr/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input /input.txt \
-file ./umapper.py \
-file ./ureducer.py \
-output /uoutput \
-mapper ./umapper.py \
-reducer ./ureducer.py


hadoop jar /usr/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input /input.txt \
-file ./bmapper.py \
-file ./breducer.py \
-output /boutput \
-mapper ./bmapper.py \
-reducer ./breducer.py


hadoop jar /usr/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input /input.txt \
-file ./tmapper.py \
-file ./treducer.py \
-output /toutput \
-mapper ./tmapper.py \
-reducer ./treducer.py


hadoop jar /usr/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input /input.txt \
-file ./skipgrammapper.py \
-file ./skipgramreducer.py \
-output /skipoutput \
-mapper ./skipgrammapper.py \
-reducer ./skipgramreducer.py

hadoop jar /usr/hadoop-3.0.0/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input /input.txt \
-file ./iimapper.py \
-file ./iireducer.py \
-output /iioutput \
-mapper ./iimapper.py \
-reducer ./iireducer.py
