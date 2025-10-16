FROM jupyter/pyspark-notebook:latest

USER root

RUN apt-get update && apt-get install -y openjdk-11-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

ENV JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

RUN pip install --no-cache-dir \
    pandas numpy matplotlib seaborn scikit-learn statsmodels \
    xgboost lightgbm mlflow great_expectations delta-spark pyarrow \
    boto3 s3fs jupyterlab \
    kubernetes_asyncio  # ← pacote necessário para o KubeSpawner funcionar

USER ${NB_UID}