import yaml
from pathlib import Path
from typing import Optional
from gru.models.common.hpa_config import HPAConfig
from gru import DEFAULT_CANSO_API_CONFIG


class ConfigReader:
    """
    Reads and provides access to configuration data from a YAML file.
    Handles both platform configuration and HPA configuration.

    Attributes:
        config_path (str): The path to the YAML configuration file.
        stuart_api_endpoint (str): The base API endpoint.
        register_class_map (dict): Dictionary mapping classes to their registration API paths.
        deploy_class_map (dict): Dictionary mapping classes to their deployment API paths.
        register_classes (list): List of classes that can be registered.
        deploy_classes (list): List of classes that can be deployed.
    """

    def __init__(self, config_path: str):
        """
        Initialize the ConfigReader.

        Args:
            config_path (str): The path to the YAML configuration file
        """
        self.config_path = config_path
        self.read_config()

        
    def read_config(self):
        """
        Read and parse the configuration file based on config type.
        """
        try:
            config_dict = self._read_file(self.config_path)
            if "api_endpoints" in config_dict:
                self.set_platform_endpoints(config_dict["api_endpoints"])
            if "processing_engine_configs" in config_dict:
                self.validate_processing_engine_configs(config_dict)
                self.set_processing_engine_configs(config_dict["processing_engine_configs"])
            
            for attr_name, attr_value in config_dict.items():
                setattr(self, attr_name, attr_value)
        except KeyError as e:
            raise KeyError(f"Key not found in configuration file: '{e.args[0]}'")

    @classmethod    
    def _read_file(self, file_path: str):
        try:
            with open(file_path, "r") as config_file:
                config_dict = yaml.safe_load(config_file)
            return config_dict
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: '{file_path}'")

    def set_platform_endpoints(self, platform_endpoints):
        """
        Set the registration and deployment API paths based on the configuration.

        Args:
            api_paths (dict): Dictionary containing registration and deployment API paths.

        Raises:
            KeyError: If the required keys are not found in the API paths.
        """
        try:
            self.stuart_api_endpoint = platform_endpoints["stuart"]
            self.risk_mgmt_endpoint = platform_endpoints["risk_mgmt"]
            self.agents_service_url = platform_endpoints["agents"]
            self.online_fs_service_url = platform_endpoints["online_fs_service"]

            self.register_paths = platform_endpoints["register"]
            self.deploy_paths = platform_endpoints["deploy"]
            self.dry_run_paths = platform_endpoints["dry_run"]
            self.update_paths = platform_endpoints["update"]
            self.health_paths = platform_endpoints["health"]
            self.risk_paths = platform_endpoints.get("risk", None)

            self.register_types = list(self.register_paths.keys())
            self.deploy_types = list(self.deploy_paths.keys())
            self.dry_run_types = list(self.dry_run_paths.keys())
            self.update_types = list(self.update_paths.keys())
            self.health_types = list(self.health_paths.keys())

            self.generate_token = platform_endpoints["generate_token"]

            self.component_setup_endpoint = platform_endpoints["component"]["setup"]
            self.agent_register_endpoint = platform_endpoints["ai_agent"]["register"]
            self.agent_deploy_endpoint = platform_endpoints["ai_agent"]["deploy"]
            self.agent_update_endpoint = platform_endpoints["ai_agent"]["update"]
            self.agent_delete_endpoint = platform_endpoints["ai_agent"]["delete"]

            ai_agent_endpoints = platform_endpoints.get("ai_agent", {})
            self.agent_prompt_endpoint = ai_agent_endpoints.get("prompt")
            self.agent_converse_endpoint = ai_agent_endpoints.get("converse")

            if self.risk_paths:
                self.workflow_list_endpoint = self.risk_paths["list"]
                self.workflow_get_endpoint = self.risk_paths["get"]
                self.workflow_create_endpoint = self.risk_paths["create"]
                self.workflow_update_status_endpoint = self.risk_paths["update_status"]
                self.workflow_rules_list_endpoint=self.risk_paths["rules"]["list"]
                self.workflow_rules_create_endpoint=self.risk_paths["rules"]["create"]
                self.workflow_deploy_endpoint = self.risk_paths["deploy"]

        except KeyError as e:
            raise KeyError(f"Key not found in the API paths: '{e.args[0]}'")

    def validate_processing_engine_configs(self, config_dict):
        valid_config_keys = {
            "deploy-mode",
            "spark.kubernetes.driver.memory",
            "spark.kubernetes.executor.memory",
            "spark.kubernetes.authenticate.driver.serviceAccountName",
            "spark.hadoop.fs.s3a.aws.credentials.provider",
            "spark.kubernetes.container.image.pullSecrets",
            "spark.kubernetes.file.upload.path",
            "spark.kubernetes.namespace",
            "num-executors",
            "checkpoint_path",
            "spark.executor.cores",
            "spark.driver.cores",
            "spark.kubernetes.driver.limit.cores",
            "spark.kubernetes.executor.limit.cores",
            "spark.executor.instances",
            "spark.kubernetes.container.image",
        }
        invalid_configs = (
            set(config_dict["processing_engine_configs"].keys()) - valid_config_keys
        )
        if invalid_configs:
            raise ValueError(
                f"Invalid keys in the provided config file: {', '.join(invalid_configs)}. "
                f"Options supported for spark-submit on K8S are: {', '.join(valid_config_keys)}"
            )

    def set_processing_engine_configs(self, processing_engine_configs):
        try:
            self.deploy_mode = processing_engine_configs["deploy-mode"]
            self.driver_memory = processing_engine_configs[
                "spark.kubernetes.driver.memory"
            ]
            self.executor_memory = processing_engine_configs[
                "spark.kubernetes.executor.memory"
            ]
            self.service_account = processing_engine_configs[
                "spark.kubernetes.authenticate.driver.serviceAccountName"
            ]
            self.aws_credential_provider = processing_engine_configs[
                "spark.hadoop.fs.s3a.aws.credentials.provider"
            ]
            self.container_image_pull_secrets = processing_engine_configs[
                "spark.kubernetes.container.image.pullSecrets"
            ]
            self.container_image = processing_engine_configs.get(
                "spark.kubernetes.container.image"
            )
            self.file_upload_path = processing_engine_configs[
                "spark.kubernetes.file.upload.path"
            ]
            self.name_space = processing_engine_configs["spark.kubernetes.namespace"]
            self.num_executors = processing_engine_configs["num-executors"]
            self.checkpoint_path = processing_engine_configs["checkpoint_path"]
            self.executor_cores = processing_engine_configs["spark.executor.cores"]
            self.driver_cores = processing_engine_configs["spark.driver.cores"]
            self.driver_limit_cores = processing_engine_configs[
                "spark.kubernetes.driver.limit.cores"
            ]
            self.executor_limit_cores = processing_engine_configs[
                "spark.kubernetes.executor.limit.cores"
            ]
            self.executor_instances = processing_engine_configs[
                "spark.executor.instances"
            ]
        except KeyError as e:
            raise KeyError(
                f"Key not found in the Proessing Engine Configs: '{e.args[0]}'"
            )
    

    @classmethod
    def load_hpa_config(self, file_path: Optional[str] = None) -> Optional[HPAConfig]:
        """
        Load HPA configuration from file or default
        
        Args:
            file_path: Optional path to custom HPA config file
            
        Returns:
            HPAConfig object or None if no config provided
            
        Raises:
            ValueError: If config file is invalid or cannot be read
        """
        try:
            if file_path is None:
                file_path = str(Path(DEFAULT_CANSO_API_CONFIG).parent / "config" / "default_hpa_configs.yaml")

            config_dict = self._read_file(file_path)
            hpa_config = HPAConfig(**config_dict)
            return hpa_config            
        except Exception as e:
            raise ValueError(f"Failed to load HPA config: {str(e)}")
