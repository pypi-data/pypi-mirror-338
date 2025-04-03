import requests
from typing import List, Dict, Optional
from dataclasses import dataclass
from .enums import (
    VulnerabilityStatus,
    Severity,
    TakedownStatus,
    DetectionLogStatus,
    InfoStealerStatus,
    GenericStatus
)

@dataclass
class QuimeraXConfig:
    team_id: str
    hash_key: str
    base_url: str = "https://api.quimerax.com/api"

class QuimeraXSDK:
    def __init__(self, config: QuimeraXConfig):
        self.config = config
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "X-TEAM-ID": config.team_id
        })
        if config.hash_key:
            self.session.headers["X-HASH-KEY"] = config.hash_key

    def _make_request(self, method: str, endpoint: str, **kwargs) -> Dict:
        url = f"{self.config.base_url}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        
        # Se a resposta estiver vazia, retorna um dicionário vazio
        if not response.text:
            return {}
            
        try:
            return response.json()
        except ValueError as e:
            print(f"Erro ao decodificar JSON: {str(e)}")
            print(f"Resposta recebida: {response.text}")
            return {}

    def list_asset_vulnerabilities(
        self,
        status: Optional[List[VulnerabilityStatus]] = None,
        severity: Optional[List[Severity]] = None,
        domain_id: Optional[List[str]] = None,
        title: Optional[str] = None
    ) -> Dict:
        """
        Lista vulnerabilidades de ativos de domínio.
        
        Args:
            status: Lista de status para filtrar
            severity: Lista de severidades para filtrar
            domain_id: Lista de IDs de domínio
            title: Título para filtrar
            
        Returns:
            Dict com as vulnerabilidades encontradas
        """
        params = {}
        if status:
            params["filter[status][]"] = [s.value for s in status]
        if severity:
            params["filter[severity][]"] = [s.value for s in severity]
        if domain_id:
            params["filter[domain_id][]"] = domain_id
        if title:
            params["filter[title]"] = title

        return self._make_request(
            "GET",
            "/external/teams/domain-assets/vulnerabilities",
            params=params
        )

    def show_asset_vulnerability(self, vulnerability_id: str) -> Dict:
        """
        Mostra detalhes de uma vulnerabilidade específica.
        
        Args:
            vulnerability_id: ID da vulnerabilidade
            
        Returns:
            Dict com os detalhes da vulnerabilidade
        """
        return self._make_request(
            "GET",
            f"/external/teams/domain-assets/vulnerabilities/{vulnerability_id}"
        )

    def update_vulnerability_status(
        self,
        vulnerability_id: str,
        status: VulnerabilityStatus,
        reason: str
    ) -> Dict:
        """
        Atualiza o status de uma vulnerabilidade.
        
        Args:
            vulnerability_id: ID da vulnerabilidade
            status: Novo status para a vulnerabilidade
            reason: Razão da atualização
            
        Returns:
            Dict com a resposta da atualização
        """
        return self._make_request(
            "PATCH",
            f"/external/teams/domain-assets/vulnerabilities/{vulnerability_id}/status",
            json={
                "status": status.value,
                "reason": reason
            }
        )

    def list_takedowns(self) -> Dict:
        """
        Lista todos os takedowns.
        
        Returns:
            Dict com a lista de takedowns
        """
        return self._make_request(
            "GET",
            "/external/teams/intelligence/takedowns"
        )

    def show_takedown(self, takedown_id: str) -> Dict:
        """
        Mostra detalhes de um takedown específico.
        
        Args:
            takedown_id: ID do takedown
            
        Returns:
            Dict com os detalhes do takedown
        """
        return self._make_request(
            "GET",
            f"/external/teams/intelligence/takedowns/{takedown_id}"
        )

    def store_takedown_history(
        self,
        takedown_id: str,
        status: TakedownStatus,
        notes: Optional[str] = None
    ) -> Dict:
        """
        Armazena histórico de um takedown.
        
        Args:
            takedown_id: ID do takedown
            status: Status do takedown
            notes: Notas opcionais
            
        Returns:
            Dict com a resposta da operação
        """
        data = {
            "status": status.value,
            "notes": notes or ""
        }
        return self._make_request(
            "POST",
            f"/external/teams/intelligence/takedowns/{takedown_id}/histories",
            json=data
        )

    def list_compromised_cards(self) -> Dict:
        """
        Lista cartões comprometidos.
        
        Returns:
            Dict com a lista de cartões comprometidos
        """
        return self._make_request(
            "GET",
            "/external/teams/intelligence/compromised-cards"
        )

    def update_compromised_card_status(
        self,
        card_id: str,
        status: VulnerabilityStatus
    ) -> Dict:
        """
        Atualiza o status de um cartão comprometido.
        
        Args:
            card_id: ID do cartão
            status: Novo status para o cartão
            
        Returns:
            Dict com a resposta da atualização
        """
        return self._make_request(
            "PATCH",
            f"/external/teams/intelligence/compromised-cards/{card_id}/status",
            json={"status": status.value}
        )

    def show_phishing(self, phishing_id: str) -> Dict:
        """
        Mostra detalhes de um phishing específico.
        
        Args:
            phishing_id: ID do phishing
            
        Returns:
            Dict com os detalhes do phishing
        """
        return self._make_request(
            "GET",
            f"/external/teams/intelligence/brands/fishings/{phishing_id}"
        )

    def get_brand_details(
        self,
        domain: Optional[str] = None,
        status: Optional[str] = None,
        method: Optional[str] = None,
        detected_at: Optional[str] = None
    ) -> Dict:
        """
        Obtém detalhes da marca.
        
        Args:
            domain: Domínio para filtrar
            status: Status para filtrar
            method: Método para filtrar
            detected_at: Data de detecção para filtrar
            
        Returns:
            Dict com os detalhes da marca
        """
        params = {}
        if domain:
            params["filter[detection][domain]"] = domain
        if status:
            params["filter[detection][status]"] = status
        if method:
            params["filter[detection][method]"] = method
        if detected_at:
            params["filter[detection][detected_at]"] = detected_at

        return self._make_request(
            "GET",
            "/external/teams/intelligence/brands/details",
            params=params
        )

    def list_detection_logs(self) -> Dict:
        """
        Lista logs de detecção.
        
        Returns:
            Dict com a lista de logs de detecção
        """
        return self._make_request(
            "GET",
            "/external/teams/intelligence/detection-logs"
        )

    def create_detection_log(
        self,
        domain: str,
        status: DetectionLogStatus,
        detection_date: str,
        detection_method: str,
        detection_dataset: str,
        active: str,
        scanned: str
    ) -> Dict:
        """
        Cria um novo log de detecção.
        
        Args:
            domain: Domínio detectado
            status: Status da detecção
            detection_date: Data da detecção
            detection_method: Método de detecção
            detection_dataset: Dataset usado na detecção
            active: Se está ativo
            scanned: Se foi escaneado
            
        Returns:
            Dict com o log de detecção criado
        """
        data = {
            "domain": domain,
            "status": status.value,
            "detection_date": detection_date,
            "detection_method": detection_method,
            "detection_dataset": detection_dataset,
            "active": active,
            "scanned": scanned
        }
        return self._make_request(
            "POST",
            "/external/teams/intelligence/detection-logs",
            json=data
        )

    def show_detection_log(self, log_id: str) -> Dict:
        """
        Mostra detalhes de um log de detecção específico.
        
        Args:
            log_id: ID do log de detecção
            
        Returns:
            Dict com os detalhes do log de detecção
        """
        return self._make_request(
            "GET",
            f"/external/teams/intelligence/detection-logs/{log_id}"
        )

    def delete_detection_log(self, log_id: str) -> Dict:
        """
        Deleta um log de detecção.
        
        Args:
            log_id: ID do log de detecção
            
        Returns:
            Dict com a resposta da deleção
        """
        return self._make_request(
            "DELETE",
            f"/external/teams/intelligence/detection-logs/{log_id}"
        )

    def list_social_media_detection_logs(self) -> Dict:
        """
        Lista logs de detecção de mídia social.
        
        Returns:
            Dict com a lista de logs de detecção de mídia social
        """
        return self._make_request(
            "GET",
            "/external/teams/intelligence/social-media-detection-logs"
        )

    def create_social_media_detection_log(
        self,
        detection_date: str,
        active: str,
        url: str,
        username: Optional[str] = None,
        platform_name: Optional[str] = None,
        description: Optional[str] = None
    ) -> Dict:
        """
        Cria um novo log de detecção de mídia social.
        
        Args:
            detection_date: Data da detecção
            active: Se está ativo
            url: URL do perfil
            username: Nome do usuário (opcional)
            platform_name: Nome da plataforma (opcional)
            description: Descrição (opcional)
            
        Returns:
            Dict com o log de detecção de mídia social criado
        """
        data = {
            "detection_date": detection_date,
            "active": active,
            "url": url,
            "username": username or "",
            "platform_name": platform_name or "",
            "description": description or ""
        }
        return self._make_request(
            "POST",
            "/external/teams/intelligence/social-media-detection-logs",
            json=data
        )

    def show_social_media_detection_log(self, log_id: str) -> Dict:
        """
        Mostra detalhes de um log de detecção de mídia social específico.
        
        Args:
            log_id: ID do log de detecção de mídia social
            
        Returns:
            Dict com os detalhes do log de detecção de mídia social
        """
        return self._make_request(
            "GET",
            f"/external/teams/intelligence/social-media-detection-logs/{log_id}"
        )

    def delete_social_media_detection_log(self, log_id: str) -> Dict:
        """
        Deleta um log de detecção de mídia social.
        
        Args:
            log_id: ID do log de detecção de mídia social
            
        Returns:
            Dict com a resposta da deleção
        """
        return self._make_request(
            "DELETE",
            f"/external/teams/intelligence/social-media-detection-logs/{log_id}"
        )

    def list_breaches_3parties(
        self,
        status: GenericStatus,
    ) -> Dict:
        """
        Lista violações de terceiros.
        
        Args:
            status: Status para filtrar
            
        Returns:
            Dict com a lista de violações de terceiros
        """
        params = {
            "filter[status]": status.value
        }
        return self._make_request(
            "GET",
            "/external/intelligences/breaches/3parties",
            params=params
        )

    def change_leaked_asset_status(
        self,
        asset_id: str,
        status: GenericStatus,
        reason: str
    ) -> Dict:
        """
        Altera o status de um ativo vazado.
        
        Args:
            asset_id: ID do ativo
            status: Novo status para o ativo
            log_status_reason: Razão da atualização
            
        Returns:
            Dict com a resposta da atualização
        """
        return self._make_request(
            "PATCH",
            f"/external/leaked-assets/{asset_id}/status",
            json={
                "status": status.value,
                "log_status_reason": reason
            }
        )

    def change_bulk_leaked_asset_status(
        self,
        asset_ids: List[str],
        status: VulnerabilityStatus
    ) -> Dict:
        """
        Altera o status de múltiplos ativos vazados.
        
        Args:
            asset_ids: Lista de IDs dos ativos
            status: Novo status para os ativos
            
        Returns:
            Dict com a resposta da atualização
        """
        return self._make_request(
            "PATCH",
            "/external/leaked-assets/bulk/status",
            json={
                "status": status.value,
                "ids[]": asset_ids
            }
        )

    def list_info_stealers(
        self,
        search: Optional[str] = None,
        status: Optional[InfoStealerStatus] = None
    ) -> Dict:
        """
        Lista info stealers.
        
        Args:
            search: Termo de busca
            status: Status para filtrar (opcional)
            
        Returns:
            Dict com a lista de info stealers
        """
        params = {"search": search}
        if status:
            params["status"] = status.value
        return self._make_request(
            "GET",
            "/external/cyber-threats/info-stealer",
            params=params
        )

    def change_info_stealer_status(
        self,
        stealer_id: str,
        status: InfoStealerStatus,
        log_status_reason: str
    ) -> Dict:
        """
        Altera o status de um info stealer.
        
        Args:
            stealer_id: ID do info stealer
            status: Novo status para o info stealer
            log_status_reason: Razão da atualização
            
        Returns:
            Dict com a resposta da atualização
        """
        return self._make_request(
            "PATCH",
            f"/external/cyber-threats/{stealer_id}/status",
            json={"status": status.value, "log_status_reason": log_status_reason}
        )

    def change_bulk_info_stealer_status(
        self,
        stealer_ids: List[str],
        status: InfoStealerStatus,
        log_status_reason: str
    ) -> Dict:
        """
        Altera o status de múltiplos info stealers.
        
        Args:
            stealer_ids: Lista de IDs dos info stealers
            status: Novo status para os info stealers
            log_status_reason: Razão da atualização
            
        Returns:
            Dict com a resposta da atualização
        """
        return self._make_request(
            "PATCH",
            "/external/cyber-threats/bulk/status",
            json={
                "status": status.value,
                "ids": stealer_ids,
                "log_status_reason": log_status_reason
            }
        ) 