#!bin/bash

HADOOP_HOME=/usr/hadoop-3.0.0
HADOOP_TOOLS=${HADOOP_HOME}/share/hadoop/tools

${HADOOP_HOME}/bin/hadoop jar ${HADOOP_TOOLS}/lib/hadoop-streaming-3.0.0.jar \
-input ./songdata.csv
-output ./output
-mapper ./umapper.py
-reducer ./ureducer.py
