from pyawx.http import HTTP
from pyawx.models.workflow_job_template import WorkflowJobTemplateModel
from pyawx.resources.adapter import Adapter


class WorkflowJobTemplate(Adapter):
    """Represents a resource for interacting with workflow job templates in the API.

    Attributes:
        `_http` (`HTTP`): The HTTP client used to send requests to the API.
        `resource` (`str`): The resource name.
        `model` (`type[WorkflowJobTemplateModel]`): The Pydantic model class for
            the workflow job template data.
    """

    def __init__(self, http_client: HTTP) -> None:
        super().__init__(
            http_client, "workflow_job_templates", WorkflowJobTemplateModel
        )

    # TODO: Add `launch` method to launch a workflow job template.
