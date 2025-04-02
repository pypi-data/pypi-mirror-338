from pyawx.http import HTTP
from pyawx.models.job_template import JobTemplateModel
from pyawx.resources.adapter import Adapter


class JobTemplate(Adapter):
    """Represents a resource for interacting with job templates in the API.

    Attributes:
        `_http` (`HTTP`): The HTTP client used to send requests to the API.
        `resource` (`str`): The resource name.
        `model` (`type[JobTemplateModel]`): The Pydantic model class for the job
            template data.
    """

    def __init__(self, http_client: HTTP) -> None:
        super().__init__(http_client, "job_templates", JobTemplateModel)

    # TODO: Add `launch` method to launch a job template.
