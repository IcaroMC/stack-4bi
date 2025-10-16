FROM apache/spark:3.5.0-python3

ARG spark_uid=185

# Mude para root para instalar pacotes e configurar permissões
USER root

# JARs para Iceberg (Spark 3.5 com Scala 2.12)
RUN wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/org/apache/iceberg/iceberg-spark-runtime-3.5_2.12/1.5.2/iceberg-spark-runtime-3.5_2.12-1.5.2.jar
RUN chmod 644 $SPARK_HOME/jars/iceberg-spark-runtime-3.5_2.12-1.5.2.jar

# JARs para S3 (MinIO). Cruciais para o seu ambiente on-premise.
RUN wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.431/aws-java-sdk-bundle-1.12.431.jar
RUN chmod 644 $SPARK_HOME/jars/aws-java-sdk-bundle-1.12.431.jar

RUN wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.3.4/hadoop-common-3.3.4.jar
RUN chmod 644 $SPARK_HOME/jars/hadoop-common-3.3.4.jar

RUN wget -P $SPARK_HOME/jars https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar
RUN chmod 644 $SPARK_HOME/jars/hadoop-aws-3.3.4.jar

USER ${spark_uid}



