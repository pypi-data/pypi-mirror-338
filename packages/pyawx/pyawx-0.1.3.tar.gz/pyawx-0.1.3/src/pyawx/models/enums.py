from enum import Enum


class WebhookServiceEnum(str, Enum):
    """Defines the different webhook services.

    Type of webhook service:
        - `github` for GitHub integration.
        - `gitlab` for GitLab integration.

    Examples:
        >>> webhook_service = WebhookService.GITHUB
    """

    GITHUB = "github"
    GITLAB = "gitlab"


class JobTypeEnum(str, Enum):
    """Defines the different types of jobs.

    Type of job:
        - `run` for normal execution.
        - `check` for dry-run mode.
        - `scan` for analysis.

    Examples:
        >>> job_type = JobType.RUN
    """

    RUN = "run"
    CHECK = "check"
    SCAN = "scan"
