"""Settings for the project."""

import os
import random
import sys
from datetime import timedelta
from typing import List

from dotenv import load_dotenv

load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class Settings:
    """Configuration for the project."""

    PROJECT_NAME: str = "OpenEdu-AI-Core"
    API_V1_STR: str = "/api/v1"
    ALLOWED_ORIGINS: List[str] = ["*"]

    # database
    ADMIN_EMAIL: str = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD: str = os.getenv("ADMIN_PASSWORD")
    MONGO_HOST: str = os.getenv("MONGO_HOST") or "localhost"
    MONGO_PORT: int = int(os.getenv("MONGO_PORT", 5432))
    MONGO_USER: str = os.getenv("MONGO_USER", "")
    MONGO_PASSWORD: str = os.getenv("MONGO_PASSWORD", "")
    MONGO_DB: str = os.getenv("MONGO_DB", "")
    MONGO_URI: str = os.getenv("MONGO_URI")
    MONGO_LEARNING_INFO_COLLECTION: str = os.getenv(
        "MONGO_LEARNING_INFO_COLLECTION", "learning_infos"
    )
    MONGO_CHAT_COLLECTION: str = os.getenv("MONGO_CHAT_COLLECTION")
    MONGO_QUIZ_COLLECTION: str = os.getenv("MONGO_QUIZ_COLLECTION")
    MONGO_MIND_MAP_COLLECTION: str = os.getenv("MONGO_MIND_MAP_COLLECTION")
    MONGO_SUMMARY_COLLECTION: str = os.getenv("MONGO_SUMMARY_COLLECTION")
    MONGO_USER_COLLECTION: str = os.getenv("MONGO_USER_COLLECTION")
    MONGO_FILE_COLLECTION: str = os.getenv("MONGO_FILE_COLLECTION")
    MONGO_YOUTUBE_TRANSCRIPT_COLLECTION: str = os.getenv(
        "MONGO_YOUTUBE_TRANSCRIPT_COLLECTION", "youtube_transcripts"
    )
    MONGO_TASK_COLLECTION: str = os.getenv("MONGO_TASK_COLLECTION", "tasks")

    QDRANT_URL: str = os.getenv("QDRANT_URL")
    API_KEY_QDRANT: str = os.getenv("API_KEY_QDRANT")

    REDIS_HOST: str = os.getenv("REDIS_HOST", "localhost")
    REDIS_PORT: int = int(os.getenv("REDIS_PORT", 5432))
    REDIS_PASSWORD: str = os.getenv("REDIS_PASSWORD", "")
    REDIS_DB: str = os.getenv("REDIS_DB", "")
    REDIS_RETRY_TIMEOUT: bool = os.getenv("REDIS_RETRY_TIMEOUT", "True").lower() in (
        "true",
        "1",
        "t",
    )
    REDIS_HEALTH_CHECK_TTL: int = int(os.getenv("REDIS_HEALTH_CHECK_TTL", 10))
    REDIS_SUB_CHANNEL: str = os.getenv("REDIS_SUB_CHANNEL")
    REDIS_PUB_CHANNEL: str = os.getenv("REDIS_PUB_CHANNEL")
    REDIS_BROKER_URL: str = os.getenv("REDIS_BROKER_URL")
    REDIS_BACKEND_URL: str = os.getenv("REDIS_BACKEND_URL")
    REDIS_SOCKET_KEEPALIVE: bool = os.getenv(
        "REDIS_SOCKET_KEEPALIVE", "True"
    ).lower() in ("true", "1", "t")

    # azure blob service
    AZURE_OPENAI_API_VERSION: str = os.getenv("AZURE_OPENAI_API_VERSION")
    AZURE_STORAGE_CONNECTION_STRING: str = os.getenv(
        "AZURE_STORAGE_CONNECTION_STRING", ""
    )
    AZURE_STORAGE_CONTAINER_NAME: str = os.getenv("AZURE_STORAGE_CONTAINER_NAME")
    AZURE_STORAGE_PREFIX_BLOB: str = os.getenv("AZURE_STORAGE_PREFIX_BLOB")

    # model
    AZURE_OPENAI_API_KEY: str = os.getenv("AZURE_OPENAI_API_KEY")
    AZURE_OPENAI_ENDPOINT: str = os.getenv("AZURE_OPENAI_ENDPOINT")
    DEPLOYMENT_NAME_GPT4: str = os.getenv("DEPLOYMENT_NAME_GPT4")
    DEPLOYMENT_NAME_INSTRUCT: str = os.getenv("DEPLOYMENT_NAME_INSTRUCT")
    MONGO_URI: str = os.getenv("MONGO_URI")
    DEPLOYMENT_NAME_EMBEDDING: str = os.getenv("DEPLOYMENT_NAME_EMBEDDING")
    LEONARDO_API_KEY: str = os.getenv("LEONARDO_API_KEY")
    LEONARDO_BASE_URL = os.getenv("LEONARDO_BASE_URL")
    LEONARDO_MODEL_ID = os.getenv("LEONARDO_MODEL_ID")
    GPT4O_MINI_INPUT_PRICE: float = float(os.getenv("GPT4O_MINI_INPUT_PRICE", 0.0))
    GPT4O_MINI_OUTPUT_PRICE: float = float(os.getenv("GPT4O_MINI_OUTPUT_PRICE", 0.0))
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY")
    GPT4V_ENDPOINT: str = os.getenv("GPT4V_ENDPOINT")
    TOGETHER_AI_API_KEY: str = os.getenv("TOGETHER_AI_API_KEY")
    AOAI_API_BASE: str = os.getenv("AOAI_API_BASE")
    AOAI_API_KEY: str = os.getenv("AOAI_API_KEY")
    AOAI_API_VERSION: str = os.getenv("AOAI_API_VERSION")
    AOAI_DEPLOYMENT: str = os.getenv("AOAI_DEPLOYMENT")

    ################################
    # Backups model
    ################################
    class BackupModels:
        class AzureOpenAI:
            api_keys: List[str] = os.getenv("AZURE_OPENAI_API_KEYS_BACKUP", "").split(
                ","
            )
            endpoints: List[str] = os.getenv("AZURE_OPENAI_ENDPOINTS_BACKUP", "").split(
                ","
            )
            deployment_name: str = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME_BACKUP")

        class Gemini:
            api_keys: List[str] = os.getenv("GEMINI_API_KEYS_BACKUP", "").split(",")

        azure_openai: AzureOpenAI
        gemini: Gemini

        def __init__(self):
            self.azure_openai = self.AzureOpenAI()
            self.gemini = self.Gemini()

    @property
    def backup_models(self) -> BackupModels:
        return self.BackupModels()

    TWITTER_API = os.getenv("TWITTER_API")
    BROKER_API = os.getenv("BROKER_API")

    ENVIRONMENT = os.getenv("ENVIRONMENT", "dev")
    COOKIE_KEY_NAME: str = os.getenv("COOKIE_KEY_NAME", "session_token")
    JWT_HASH_SALT: str = os.getenv("JWT_HASH_SALT")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY")

    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    JWT_EXPIRATION: timedelta = timedelta(minutes=int(os.getenv("JWT_EXPIRATION", 15)))
    PREFIX: str = os.getenv("PREFIX", "/openai")
    LANGFUSE_PUBLIC_KEY: str = os.getenv("LANGFUSE_PUBLIC_KEY")
    LANGFUSE_SECRET_KEY: str = os.getenv("LANGFUSE_SECRET_KEY")
    LANGFUSE_HOST: str = os.getenv("LANGFUSE_HOST")
    GEMINI_API: str = os.getenv("GEMINI_API")

    @property
    def is_development(self) -> bool:
        """Check if the environment is development.

        Returns:
            True if the environment is development, False otherwise.
        """
        return self.ENVIRONMENT == "dev"

    AWS_REGION: str = os.getenv("AWS_REGION")
    AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY")

    GOOGLE_GENERATIVE_API_KEY: str = os.getenv("GOOGLE_GENERATIVE_API_KEY")

    POSTGRES_URI: str = os.getenv("POSTGRES_URI")
    SEARXNG_API_URL: str = os.getenv("SEARXNG_API_URL")
    GEMINI_API: str = os.getenv("GEMINI_API")
    IMAGE_SEARCH_API_KEY: str = os.getenv("IMAGE_SEARCH_API_KEY")
    EXA_API_KEY: str = os.getenv("EXA_API_KEY")
    BING_SEARCH_URL: str = os.getenv("BING_SEARCH_URL")
    BING_SEARCH_KEY: str = os.getenv("BING_SEARCH_KEY")

    #######################
    # QDRANT
    #######################
    QDRANT_API_KEY: str = os.getenv("QDRANT_API_KEY")
    QDRANT_URL: str = os.getenv("QDRANT_URL")
    QDRANT_PORT: int = int(os.getenv("QDRANT_PORT", 443))

    #######################
    # Code Engine
    #######################
    CODE_ENGINE_BASE_URL: str = os.getenv("CODE_ENGINE_BASE_URL")

    MAX_FILE_SIZE: int = int(os.getenv("MAX_FILE_SIZE", 5242880))
    RAY_ADDRESS: str = os.getenv("RAY_ADDRESS", "")

    @property
    def is_ray_used(self) -> bool:
        return self.RAY_ADDRESS != ""

    #######################
    # Webhooks
    #######################
    TOKEN_USAGE_WEBHOOK_URL: str = os.getenv("TOKEN_USAGE_WEBHOOK_URL")
    TOKEN_USAGE_WEBHOOK_API_KEY: str = os.getenv("TOKEN_USAGE_WEBHOOK_API_KEY")

    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


settings = Settings()


class CeleryConfig(object):
    """Configuration for Celery."""

    broker_url = settings.REDIS_BROKER_URL
    result_backend = settings.REDIS_BACKEND_URL
    result_expires = 86400

    task_default_queue = "celery"
    task_track_started = True
    task_acks_late = True
    task_default_retry_delay = 60  # 1 minute
    task_max_retries = 3
    # Tracking
    task_send_sent_event = True
    worker_send_task_events = True

    worker_concurrency = 4
    worker_prefetch_multiplier = 1
    worker_max_tasks_per_child = 100
    worker_cancel_long_running_tasks = True

    enable_utc = True
    timezone = "Asia/Ho_Chi_Minh"
    broker_connection_retry_on_startup = True
    broker_connection_max_retries = 5
    broker_connection_retry_delay = 2
    broker_heartbeat = 30
    broker_heartbeat_checkrate = 15
    broker_connection_timeout = 300

    # Redis-specific settings backend
    redis_socket_timeout = 10  # Increase timeout
    redis_socket_connect_timeout = 10  # Increase connect timeout
    redis_retry_on_timeout = True  # Enable retry on timeout
    redis_socket_keepalive = True

    # import tasks
    imports = ["src.tasks"]

    # Logging configuration
    worker_hijack_root_logger = False
    worker_log_format = "[%(asctime)s: %(levelname)s/%(processName)s] %(message)s"
    worker_task_log_format = "[%(asctime)s: %(levelname)s/%(processName)s] %(task_name)s[%(task_id)s]: %(message)s"
    worker_redirect_stdouts_level = "INFO"


class QueueConfig(object):
    """Configuration for queues."""

    def __choose_one(self, config: dict) -> str:
        """
        Choose one queue from the given configuration.

        Args:
            config: A dictionary with queue names as keys and weights as values.

        Returns:
            The name of the chosen queue.
        """
        queue_names = list(config.keys())
        queue_weights = list(config.values())
        chosen_one = random.choices(queue_names, queue_weights, k=1)[0]
        return chosen_one

    @property
    def conversation(self):
        """Config for conversation queue."""
        config = {"conversation": 1, "conversation_0": 0, "conversation_1": 0}
        return self.__choose_one(config)

    @property
    def learning_info(self):
        """Config for learning info queue."""
        config = {"learning_info": 1, "learning_info_0": 0, "learning_info_1": 0}
        return self.__choose_one(config)


queue_manager = QueueConfig()
