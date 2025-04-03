# SDK QuimeraX

Este é um SDK em Python para interagir com a API da QuimeraX.

## Instalação

```bash
pip3 install quimerax
```

## Uso

```python
import quimerax

# Configuração do SDK
config = quimerax.QuimeraXConfig(
    team_id="seu_team_id",
    hash_key="seu_hash_key"
)

# Inicialização do SDK
sdk = quimerax.QuimeraXSDK(config)

# Exemplos de uso

# Listar vulnerabilidades
vulnerabilities = sdk.list_asset_vulnerabilities(
    status=[quimerax.VulnerabilityStatus.OPEN],
    severity=[quimerax.Severity.HIGH],
    domain_id=["123"],
    title="exemplo"
)

# Mostrar detalhes de uma vulnerabilidade
vulnerability = sdk.show_asset_vulnerability("vulnerability_id")

# Atualizar status de uma vulnerabilidade
sdk.update_vulnerability_status(
    "vulnerability_id",
    quimerax.VulnerabilityStatus.FIXED,
    "Vulnerabilidade corrigida pelo time de DevOps"
)

# Listar takedowns
takedowns = sdk.list_takedowns()

# Mostrar detalhes de um takedown
takedown = sdk.show_takedown("takedown_id")

# Armazenar histórico de takedown
sdk.store_takedown_history(
    "takedown_id",
    quimerax.TakedownStatus.IN_PROGRESS,
    "Takedown em andamento"
)

# Listar cartões comprometidos
compromised_cards = sdk.list_compromised_cards()

# Atualizar status de um cartão comprometido
sdk.update_compromised_card_status(
    "card_id",
    quimerax.VulnerabilityStatus.FIXED
)

# Mostrar detalhes de um phishing
phishing = sdk.show_phishing("phishing_id")

# Obter detalhes de fraude relacionado a marca
brand_details = sdk.get_brand_details(
    domain="exemplo.com",
    status="active",
    method="scan",
    detected_at="2024-01-01"
)

# Listar logs de detecção
detection_logs = sdk.list_detection_logs()

# Criar um novo log de detecção
new_log = sdk.create_detection_log(
    domain="exemplo.com",
    status=quimerax.DetectionLogStatus.NEW,
    detection_date="2024-01-01",
    detection_method="scan",
    detection_dataset="dataset1",
    active="true",
    scanned="true"
)

# Mostrar detalhes de um log de detecção
log = sdk.show_detection_log("log_id")

# Deletar um log de detecção
sdk.delete_detection_log("log_id")

# Listar logs de detecção de mídia social
social_logs = sdk.list_social_media_detection_logs()

# Criar um novo log de detecção de mídia social
new_social_log = sdk.create_social_media_detection_log(
    detection_date="2024-01-01",
    active="true",
    url="https://exemplo.com/perfil",
    username="usuario",
    platform_name="facebook",
    description="Perfil suspeito"
)

# Mostrar detalhes de um log de detecção de mídia social
social_log = sdk.show_social_media_detection_log("log_id")

# Deletar um log de detecção de mídia social
sdk.delete_social_media_detection_log("log_id")

# Listar violações de terceiros
breaches = sdk.list_breaches_3parties(
    status=quimerax.GenericStatus.OPEN
)

# Alterar status de um ativo vazado
sdk.change_leaked_asset_status(
    "asset_id",
    quimerax.GenericStatus.FIXED,
    "Senha alterada pelo usuário"
)

# Alterar status de múltiplos ativos vazados
sdk.change_bulk_leaked_asset_status(
    ["asset_id1", "asset_id2"],
    quimerax.VulnerabilityStatus.FIXED
)

# Listar info stealers
info_stealers = sdk.list_info_stealers(
    search="termo_busca",
    status=quimerax.InfoStealerStatus.OPEN
)

# Alterar status de um info stealer
sdk.change_info_stealer_status(
    "stealer_id",
    quimerax.InfoStealerStatus.FIXED,
    "Info stealer corrigido"
)

# Alterar status de múltiplos info stealers
sdk.change_bulk_info_stealer_status(
    ["stealer_id1", "stealer_id2"],
    quimerax.InfoStealerStatus.FIXED,
    "Info stealers corrigidos em lote"
)
```

## Enums Disponíveis

### VulnerabilityStatus
- OPEN
- FIXED
- FALSE_POSITIVE
- RISK_ACCEPTED
- REOPENED
- IN_PROGRESS
- CLOSED

### Severity
- UNKNOWN
- INFO
- LOW
- MEDIUM
- HIGH
- CRITICAL

### TakedownStatus
- REQUESTED
- COMPLETED
- IN_PROGRESS
- FAILED

### DetectionLogStatus
- NEW
- TRIAGE
- TAKEDOWN_REQUEST
- PENDING_TAKEDOWN
- IN_PROGRESS_TAKEDOWN
- COMPLETED_TAKEDOWN
- FAILED_TAKEDOWN
- ALLOWED
- CLOSED
- ACCEPTED_RISK
- FALSE_POSITIVE
- RISK_ACCEPTED

### InfoStealerStatus
- OPEN
- FIXED
- FALSE_POSITIVE
- RISK_ACCEPTED
- REOPENED
- IN_PROGRESS

### GenericStatus
- OPEN
- FIXED
- FALSE_POSITIVE
- RISK_ACCEPTED
- REOPENED
- IN_PROGRESS 