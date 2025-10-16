FROM apache/airflow:2.10.5-python3.10

# Variáveis de ambiente para clareza
ENV AIRFLOW_VERSION=2.10.5
ENV PYTHON_VERSION=3.10
ENV CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"

# Mudar para o usuário airflow para instalar pacotes

USER root

RUN apt-get update && apt-get install -y wget

USER airflow


RUN mkdir -p /opt/airflow/jars && \
    cd /opt/airflow/jars

RUN wget -O /opt/airflow/jars/aws-java-sdk-bundle-1.12.431.jar \
    https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.12.431/aws-java-sdk-bundle-1.12.431.jar 

RUN wget -O /opt/airflow/jars/hadoop-common-3.3.4.jar \
    https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-common/3.3.4/hadoop-common-3.3.4.jar

RUN wget -O /opt/airflow/jars/hadoop-aws-3.3.4.jar \
    https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.3.4/hadoop-aws-3.3.4.jar

ENV CLASSPATH="/opt/airflow/jars/*"

RUN chown -R airflow /opt/airflow/jars

# Instalar os provedores necessários
RUN pip install --no-cache-dir \
    "apache-airflow-providers-trino" \
    "apache-airflow-providers-microsoft-mssql" \
    "apache-airflow-providers-apache-spark" \
    "apache-airflow-providers-cncf-kubernetes" \
    --constraint "${CONSTRAINT_URL}"



# Limpar o cache do pip após a instalação
RUN pip cache purge