import os
import yaml
from pathlib import Path
from typing import Dict, Self, Optional
from dataclasses import dataclass
from typer import Option
from typing_extensions import Annotated
from composable_dataloader.logger import logger
import enum


from azure.identity import ManagedIdentityCredential
from databricks.sdk import WorkspaceClient
from databricks.sdk.config import Config
from databricks.sdk.credentials_provider import CredentialsProvider, CredentialsStrategy

from composable_dataloader.base_data_loader import StdoutMode
from composable_dataloader.engine import QueryEngine
from composable_dataloader.base_data_loader import DataLoader


class DabMode(str, enum.Enum):
    ENABLED = "enabled"
    DISABLED = "disabled"


@dataclass
class DatabricksDataLoader(DataLoader):
    """
    Data loader with Databricks Asset Bundle (DAB) support.

    Adds functionality to run queries via Databricks jobs.
    """

    databricks_host: Annotated[
        str,
        Option(
            ...,
            "--databricks-host",
            help="Databricks",
            envvar="DATABRICKS_HOST",
        ),
    ]

    dab: Annotated[
        DabMode,
        Option(
            DabMode.DISABLED,
            "--dab",
            help="Execute as DAB (enabled/disabled)",
            envvar="DAB",
        ),
    ]

    yaml_path: Annotated[
        Optional[Path],
        Option(
            None,
            "--yaml-path",
            help="Path to databricks.yml file",
        ),
    ]

    def __post_init__(self):
        super().__post_init__()

        logger.info(f"Initializing Databricks client for {self.execution_mode} mode")

        if self.stdout_mode == StdoutMode.ENABLED:
            if self.execution_mode == "dev":
                logger.info(
                    f"Using direct authentication with host: {self.databricks_host}"
                )
                self.client = WorkspaceClient(host=self.databricks_host)
            else:
                # Use Azure Managed Identity for production
                client_id = os.getenv("AZURE_CLIENT_ID")
                logger.info(f"Using Azure Managed Identity with client ID: {client_id}")
                self.client = WorkspaceClient(
                    host=self.databricks_host,
                    credentials_strategy=AzureIdentityCredentialsStrategy(
                        client_id=client_id
                    ),
                )

    def get_job_name(self) -> str:
        """Get job name from bundle config"""

        if not self.yaml_path.exists():
            raise FileNotFoundError(f"Could not find yml at {self.yaml_path}")

        with open(self.yaml_path, "r") as file:
            config = yaml.safe_load(file)
            print(config)

        bundle_name = config["bundle"]["name"]
        target = config["targets"][self.execution_mode]

        if target["mode"] == "development":
            user_name = (
                target.get("run_as", {}).get("user_name")
                or self.client.current_user.me().user_name
            )
            formatted_name = user_name.split("@")[0].replace(".", "_")
            return f"[dev {formatted_name}] {bundle_name}_job"
        return f"{bundle_name}_job"

    def run_job(self) -> Self:
        """Execute Databricks job with dynamically generated parameters."""
        job_name = self.get_job_name()

        job = next(
            iter(self.client.jobs.list(limit=1, expand_tasks=True, name=job_name)), None
        )

        if not job:
            logger.error(f"No job found with name: {job_name}")
            raise ValueError(f"No job found with name: {job_name}")

        params = self.get_params()

        # Pass parameters to the remote Databricks job, with modifications for proper execution:
        # 1. Disable DAB mode to prevent the remote job from recursively launching more jobs
        params["dab"] = DabMode.DISABLED
        # 2. Use Spark engine since the job runs on a Databricks cluster
        params["query-engine"] = QueryEngine.SPARK
        # 3. Disable stdout in the remote job - results writing will be handled by this process
        params["stdout-mode"] = StdoutMode.DISABLED

        logger.info(f"Running job {job_name} (job_id={job.job_id})")
        self.client.jobs.run_now_and_wait(job_id=job.job_id, python_named_params=params)

        return self

    def entrypoint(self) -> None:
        """Entry point determining execution mode (DAB or direct)."""

        if self.dab == DabMode.ENABLED:
            logger.info("Running in DAB mode via Databricks job")
            self.run_job()
        else:
            super().entrypoint()

        if self.stdout_mode == StdoutMode.ENABLED:
            self.write_results_to_stdout()


class AzureIdentityCredentialsStrategy(CredentialsStrategy):
    def auth_type(self) -> str:
        return "azure-mi"

    def __init__(self, client_id: str = None):
        self.client_id = client_id

    def __call__(self, cfg: "Config") -> CredentialsProvider:
        if self.client_id:
            mi_credential = ManagedIdentityCredential(client_id=self.client_id)
        else:
            mi_credential = ManagedIdentityCredential()

        def inner() -> Dict[str, str]:
            token = mi_credential.get_token(
                "2ff814a6-3304-4ab8-85cb-cd0e6f879c1d/.default"
            )
            return {"Authorization": f"Bearer {token.token}"}

        return inner
