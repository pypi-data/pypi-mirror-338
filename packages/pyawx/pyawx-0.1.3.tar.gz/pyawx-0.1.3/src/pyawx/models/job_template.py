import json
from typing import Any

from pydantic import BaseModel, Field

from pyawx.models.enums import JobTypeEnum, WebhookServiceEnum


class JobTemplateModel(BaseModel):
    """Represents a Job Template.

    Attributes starting with `ask_` indicate runtime prompts during job launch.
    Defaults are provided for most fields to simplify initialization.
    Provides webhook integration options via `webhook_service` and `webhook_credential`.

    For more information, check the AWX API reference for Job Templates:
    https://ansible.readthedocs.io/projects/awx/en/latest/rest_api/api_ref.html#/Job_Templates

    Examples:
        >>> job_template = JobTemplateModel(
        ...     name="Backup Job",
        ...     description="Backup database",
        ...     inventory="db_inventory",
        ...     project="backup_project",
        ...     playbook="backup.yml"
        ... )

    Attributes:
        `name` (`str`): The name of the JobTemplate.
        `description` (`str`): Description of the JobTemplate.
        `job_type` (`JobType`): Type of job execution.
        `inventory` (`str`): The Ansible inventory associated with the JobTemplate.
        `project` (`str`): The Ansible project associated with this JobTemplate.
        `playbook` (`str`): Path to the Ansible playbook to be executed.
        `scm_branch` (`str`): SCM (Source Control Management) branch associated with
            the JobTemplate.
        `forks` (`int`): Number of forks (instances) in which the JobTemplate should
            be executed.
        `limit` (`str`): Limit for the hosts on which the playbook will run
            (e.g., 'host1, host2').
        `verbosity` (`int`): Verbosity level of the job (0-5).
        `extra_vars` (`dict`): Additional variables to be passed to the playbook.
        `job_tags` (`set`): Job tags to be passed to the playbook.
        `force_handlers` (`bool`): If true, forces the execution of handlers even
            if they were not called.
        `skip_tags` (`str`): Tags of tasks to skip during the execution.
        `start_at_task` (`str`): Name of the task in Ansible to start the execution
            from.
        `timeout` (`int`): Maximum job execution time in seconds.
        `use_fact_cache` (`bool`): If true, uses Ansible's fact cache.
        `execution_environment` (`str | None`): Custom execution environment for
            running the playbook (e.g., a Docker container).
        `host_config_key` (`str`): Host configuration key.
        `ask_scm_branch_on_launch` (`bool`): If true, prompts for the SCM branch when
            launching the job.
        `ask_diff_mode_on_launch` (`bool`): If true, prompts for diff mode when
            launching the job.
        `ask_variables_on_launch` (`bool`): If true, prompts for additional variables
            when launching the job.
        `ask_limit_on_launch` (`bool`): If true, prompts for the host limit when
            launching the job.
        `ask_tags_on_launch` (`bool`): If true, prompts for job tags when launching
            the job.
        `ask_skip_tags_on_launch` (`bool`): If true, prompts for skip tags when
            launching the job.
        `ask_job_type_on_launch` (`bool`): If true, prompts for the job type when
            launching the job.
        `ask_verbosity_on_launch` (`bool`): If true, prompts for verbosity level when
            launching the job.
        `ask_inventory_on_launch` (`bool`): If true, prompts for the inventory when
            launching the job.
        `ask_credential_on_launch` (`bool`): If true, prompts for the credential when
            launching the job.
        `ask_execution_environment_on_launch` (`bool`): If true, prompts for the
            execution environment when launching the job.
        `ask_labels_on_launch` (`bool`): If true, prompts for labels when launching
            the job.
        `ask_forks_on_launch` (`bool`): If true, prompts for the number of forks when
            launching the job.
        `ask_job_slice_count_on_launch` (`bool`): If true, prompts for the job slice
            count when launching the job.
        `ask_timeout_on_launch` (`bool`): If true, prompts for the timeout value when
            launching the job.
        `ask_instance_groups_on_launch` (`bool`): If true, prompts for instance groups
            when launching the job.
        `survey_enabled` (`bool`): If true, enables a survey at the time of job launch
            to gather more input from the user.
        `become_enabled` (`bool`): If true, allows the use of sudo
            (privilege escalation) in the playbook.
        `diff_mode` (`bool`): If true, runs the playbook in diff mode to show changes
            between the previous and current state.
        `allow_simultaneous` (`bool`): If true, allows the job to run simultaneously
            on multiple instances.
        `job_slice_count` (`int`): Number of slices the job will be divided into for
            parallel execution.
        `webhook_service` (`WebhookService | None`): Webhook service associated with the
            JobTemplate, if any.
        `webhook_credential` (`str | None`): Credential required to authenticate with
            the webhook service.
        `prevent_instance_group_fallback` (`bool`): If true, prevents the job from
            falling back to another instance group if the primary group is
            unavailable.
    """

    name: str = Field()
    description: str = Field(default="")
    job_type: JobTypeEnum = Field(default=JobTypeEnum.RUN)
    inventory: str = Field()
    project: str = Field()
    playbook: str = Field()
    scm_branch: str = Field(default="")
    forks: int = Field(default=0, ge=0)
    limit: str = Field(default="")
    verbosity: int = Field(default=0, ge=0, le=5)
    extra_vars: dict = Field(default={})
    job_tags: set = Field(default=set())
    force_handlers: bool = Field(default=False)
    skip_tags: str = Field(default="")
    start_at_task: str = Field(default="")
    timeout: int = Field(default=0, ge=0)
    use_fact_cache: bool = Field(default=False)
    execution_environment: str | None = Field(default=None)
    host_config_key: str = Field(default="")
    ask_scm_branch_on_launch: bool = Field(default=False)
    ask_diff_mode_on_launch: bool = Field(default=False)
    ask_variables_on_launch: bool = Field(default=False)
    ask_limit_on_launch: bool = Field(default=False)
    ask_tags_on_launch: bool = Field(default=False)
    ask_skip_tags_on_launch: bool = Field(default=False)
    ask_job_type_on_launch: bool = Field(default=False)
    ask_verbosity_on_launch: bool = Field(default=False)
    ask_inventory_on_launch: bool = Field(default=False)
    ask_credential_on_launch: bool = Field(default=False)
    ask_execution_environment_on_launch: bool = Field(default=False)
    ask_labels_on_launch: bool = Field(default=False)
    ask_forks_on_launch: bool = Field(default=False)
    ask_job_slice_count_on_launch: bool = Field(default=False)
    ask_timeout_on_launch: bool = Field(default=False)
    ask_instance_groups_on_launch: bool = Field(default=False)
    survey_enabled: bool = Field(default=False)
    become_enabled: bool = Field(default=False)
    diff_mode: bool = Field(default=False)
    allow_simultaneous: bool = Field(default=False)
    job_slice_count: int = Field(default=1, ge=1)
    webhook_service: WebhookServiceEnum | None = Field(default=None)
    webhook_credential: str | None = Field(default=None)
    prevent_instance_group_fallback: bool = Field(default=False)

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
