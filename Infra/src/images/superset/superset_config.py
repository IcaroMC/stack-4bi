import os
from flask_babel import gettext
from superset.translations.utils import get_language_pack

# ---------------------------------------------------------
# 1. Configuração de Locale e Idiomas
# ---------------------------------------------------------
# Define o locale padrão do servidor
BABEL_DEFAULT_LOCALE = "pt_BR"

# Define os idiomas disponíveis (Obrigatório ter 'en' como fallback)
LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "pt_BR": {"flag": "br", "name": "Brazilian Portuguese"}
}

# ---------------------------------------------------------
# 2. Configuração de Formatação Numérica (D3 e Frontend)
# ---------------------------------------------------------
# Isso ajuda os gráficos a entenderem que queremos vírgula decimal
D3_FORMAT = {
    "decimal": ",",
    "thousands": ".",
    "grouping": [3],
    "currency": ["R$ ", ""]
}

# ---------------------------------------------------------
# 3. Override do Bootstrap (Correção Crítica do Frontend)
# ---------------------------------------------------------
# Esta função garante que o React (frontend) carregue o pacote pt_BR
# mesmo se o navegador estiver pedindo apenas 'pt'.
def override_bootstrap_locale(data):
    if data.get("locale") == "pt":
        data["locale"] = "pt_BR"
        data["language_pack"] = get_language_pack('pt_BR')
    return data

# Atribui a função à configuração do Superset
COMMON_BOOTSTRAP_OVERRIDES_FUNC = override_bootstrap_locale

# ---------------------------------------------------------
# 4. Outras Configurações Padrão (Opcional)
# ---------------------------------------------------------
# Aumenta o timeout para queries pesadas no Trino (padrão é curto)
SQLLAB_TIMEOUT = 300
SUPERSET_WEBSERVER_TIMEOUT = 300