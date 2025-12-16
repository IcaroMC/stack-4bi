FROM apache/superset:4.0.1

USER root

# 1. Instala dependências de sistema
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential libssl-dev libffi-dev python3-dev default-libmysqlclient-dev && \
    rm -rf /var/lib/apt/lists/*

# 2. AQUI ESTÁ A CORREÇÃO: Instale no .venv
# Se você usar apenas 'pip', ele instala no lugar errado e o Superset ignora.
RUN /app/.venv/bin/pip install --no-cache-dir \
    trino[sqlalchemy] \
    psycopg2-binary \
    redis \
    pyarrow \
    boto3 \
    pandas \
    prophet \
    scipy \
    numpy

# 3. Copia a configuração
COPY superset_config.py /app/pythonpath/superset_config.py

USER superset