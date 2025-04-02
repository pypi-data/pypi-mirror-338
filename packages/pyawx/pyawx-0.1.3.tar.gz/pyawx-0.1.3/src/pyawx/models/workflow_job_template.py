import json
from typing import Any

from pydantic import BaseModel, Field

from pyawx.models.enums import WebhookServiceEnum


class WorkflowJobTemplateModel(BaseModel):
    """Represents a Workflow Job Template.

    Attributes starting with `ask_` indicate runtime prompts during job launch.
    Defaults are provided for most fields to simplify initialization.
    Provides webhook integration options via `webhook_service` and `webhook_credential`.

    For more information, check the AWX API reference for Workflow Job Templates:
    https://ansible.readthedocs.io/projects/awx/en/latest/rest_api/api_ref.html#/Workflow_Job_Templates

    Examples:
        >>> workflow = WorkflowJobTemplateModel(
        ...     name="Release Deployment Workflow",
        ...     inventory="prod_inventory",
        ...     extra_vars='{"version": "1.2.3"}'
        ... )

    Attributes:
        `name` (`str`): The name of the WorkflowJobTemplate.
        `description` (`str`): Description of the WorkflowJobTemplate.
        `extra_vars` (`dict`): Additional variables to be passed to the workflow
            job template.
        `organization` (`str | None`): The organization associated with the
            WorkflowJobTemplate.
        `survey_enabled` (`bool`): If true, enables a survey to collect additional
            input when launching the job.
        `allow_simultaneous` (`bool`): If true, allows the workflow to run on
            multiple nodes at the same time.
        `ask_variables_on_launch` (`bool`): If true, prompts for additional variables
            during the launch of the workflow.
        `inventory` (`str | None`): The inventory to be used for the workflow job
            template.
        `limit` (`str`): Host limit for the workflow, specifying which hosts to target
            (e.g., 'host1, host2').
        `scm_branch` (`str`): The SCM branch to be used in the workflow job template.
        `ask_inventory_on_launch` (`bool`): If true, prompts for the inventory when
            launching the workflow job.
        `ask_scm_branch_on_launch` (`bool`): If true, prompts for the SCM branch when
            launching the workflow job.
        `ask_limit_on_launch` (`bool`): If true, prompts for the limit when launching
            the workflow job.
        `webhook_service` (`WebhookService | None`): Webhook service to be used with the workflow
            job template, if any.
        `webhook_credential` (`str | None`): Credentials required to authenticate with
            the webhook service, if used.
        `ask_labels_on_launch` (`bool`): If true, prompts for labels when launching
            the workflow job.
        `ask_skip_tags_on_launch` (`bool`): If true, prompts for skip tags when
            launching the workflow job.
        `ask_tags_on_launch` (`bool`): If true, prompts for tags when launching the
            workflow job.
        `skip_tags` (`str`): Tags of tasks to be skipped when executing the workflow
            job.
        `job_tags` (`set`): Tags of tasks to be included when executing the workflow
            job.
    """

    name: str = Field()
    description: str = Field(default="")
    extra_vars: dict = Field(default={})
    organization: str | None = Field(default=None)
    survey_enabled: bool = Field(default=False)
    allow_simultaneous: bool = Field(default=False)
    ask_variables_on_launch: bool = Field(default=False)
    inventory: str | None = Field(default=None)
    limit: str = Field(default="")
    scm_branch: str = Field(default="")
    ask_inventory_on_launch: bool = Field(default=False)
    ask_scm_branch_on_launch: bool = Field(default=False)
    ask_limit_on_launch: bool = Field(default=False)
    webhook_service: WebhookServiceEnum | None = Field(default=None)
    webhook_credential: str | None = Field(default=None)
    ask_labels_on_launch: bool = Field(default=False)
    ask_skip_tags_on_launch: bool = Field(default=False)
    ask_tags_on_launch: bool = Field(default=False)
    skip_tags: str = Field(default="")
    job_tags: set = Field(default=set())

    def model_dump(self, *args, **kwargs) -> dict:
        """Generate a dictionary representation of the model.

        This method overrides the default `model_dump` to ensure that the
        `extra_vars` attribute is serialized as a JSON string and `job_tags`
        as a comma-separated string.

        Returns:
            dict: A dictionary representation of the model's data.
        """
        data: dict[str, Any] = super().model_dump(*args, **kwargs)
        data["extra_vars"] = json.dumps(self.extra_vars)
        data["job_tags"] = ",".join(self.job_tags)
        return data
