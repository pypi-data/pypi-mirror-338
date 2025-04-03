from enum import Enum

class VulnerabilityStatus(Enum):
    OPEN = "open"
    FIXED = "fixed"
    FALSE_POSITIVE = "false_positive"
    RISK_ACCEPTED = "risk_accepted"
    REOPENED = "reopened"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"

class Severity(Enum):
    UNKNOWN = "unknown"
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class TakedownStatus(Enum):
    REQUESTED = "requested"
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    FAILED = "failed"

class DetectionLogStatus(Enum):
    NEW = "new"
    TRIAGE = "triage"
    TAKEDOWN_REQUEST = "takedown_request"
    PENDING_TAKEDOWN = "pending_takedown"
    IN_PROGRESS_TAKEDOWN = "in_progress_takedown"
    COMPLETED_TAKEDOWN = "completed_takedown"
    FAILED_TAKEDOWN = "failed_takedown"
    ALLOWED = "allowed"
    CLOSED = "closed"
    ACCEPTED_RISK = "accepted_risk"
    FALSE_POSITIVE = "false_positive"
    RISK_ACCEPTED = "risk_accepted"

class InfoStealerStatus(Enum):
    OPEN = "open"
    FIXED = "fixed"
    FALSE_POSITIVE = "false_positive"
    RISK_ACCEPTED = "risk_accepted"
    REOPENED = "reopened"
    IN_PROGRESS = "in_progress" 

class GenericStatus(Enum):
    OPEN = "open"
    FIXED = "fixed"
    FALSE_POSITIVE = "false_positive"
    RISK_ACCEPTED = "risk_accepted"
    REOPENED = "reopened"
    IN_PROGRESS = "in_progress" 