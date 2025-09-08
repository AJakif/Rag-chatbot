from pydantic_settings import BaseSettings
from pydantic import Field, field_validator, ConfigDict
from typing import Optional
import yaml
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class AppSettings(BaseSettings):
    # General settings
    app_env: str = Field(default="development")
    app_port: int = Field(default=8000)
    log_level: str = Field(default="INFO")
    
    # LangChain settings
    langchain_tracing_v2: bool = Field(default=False)
    langchain_endpoint: str = Field(default="https://api.smith.langchain.com")
    langchain_api_key: Optional[str] = Field(default=None)
    langchain_project: str = Field(default="rag-practice-mvp")
    
    # Qdrant settings
    qdrant_host: str = Field(default="localhost")
    qdrant_port: int = Field(default=6333)
    qdrant_api_key: Optional[str] = Field(default=None)
    qdrant_collection: str = Field(default="rag_documents")
    
    # LLM Provider settings
    openai_api_key: Optional[str] = Field(default=None)
    openai_model: str = Field(default="gpt-4o-mini")
    google_api_key: Optional[str] = Field(default=None)
    google_model: str = Field(default="gemini-pro")
    local_llm_provider: str = Field(default="ollama")
    local_llm_model: str = Field(default="llama3")
    local_llm_endpoint: str = Field(default="http://localhost:11434")
    
    # Misc settings
    max_chunk_size: int = Field(default=1000)
    embedding_model: str = Field(default="text-embedding-3-large")
    top_k: int = Field(default=5)
    
    # Logging settings
    log_path: str = Field(default="./logs")
    log_rotation: str = Field(default="D")
    log_retention: int = Field(default=7)
    log_format: str = Field(
        default="%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s"
    )
    log_date_format: str = Field(default="%d-%m-%Y %H:%M:%S")
    
    # Computed properties
    @property
    def qdrant_url(self) -> str:
        return f"http://{self.qdrant_host}:{self.qdrant_port}"
    
    @field_validator('app_env')
    def validate_app_env(cls, v):
        if v not in ['development', 'production', 'test']:
            raise ValueError('APP_ENV must be development, production, or test')
        return v
    
    model_config = ConfigDict(
        env_file=".env",
        extra="ignore",
        # Map field names to environment variables
        env_prefix="",
        env_nested_delimiter="_",
        # Map each field to its specific environment variable
        env={
            "app_env": "APP_ENV",
            "app_port": "APP_PORT",
            "log_level": "LOG_LEVEL",
            "langchain_tracing_v2": "LANGCHAIN_TRACING_V2",
            "langchain_endpoint": "LANGCHAIN_ENDPOINT",
            "langchain_api_key": "LANGCHAIN_API_KEY",
            "langchain_project": "LANGCHAIN_PROJECT",
            "qdrant_host": "QDRANT_HOST",
            "qdrant_port": "QDRANT_PORT",
            "qdrant_api_key": "QDRANT_API_KEY",
            "qdrant_collection": "QDRANT_COLLECTION",
            "openai_api_key": "OPENAI_API_KEY",
            "openai_model": "OPENAI_MODEL",
            "google_api_key": "GOOGLE_API_KEY",
            "google_model": "GOOGLE_MODEL",
            "local_llm_provider": "LOCAL_LLM_PROVIDER",
            "local_llm_model": "LOCAL_LLM_MODEL",
            "local_llm_endpoint": "LOCAL_LLM_ENDPOINT",
            "max_chunk_size": "MAX_CHUNK_SIZE",
            "embedding_model": "EMBEDDING_MODEL",
            "top_k": "TOP_K",
            "log_path": "LOG_PATH",
            "log_rotation": "LOG_ROTATION",
            "log_retention": "LOG_RETENTION",
            "log_format": "LOG_FORMAT",
            "log_date_format": "LOG_DATE_FORMAT",
        }
    )

def load_yaml_config(env: str) -> dict:
    config_path = Path(__file__).parent.parent.parent / "configs" / f"{env}.yaml"
    if config_path.exists():
        with open(config_path) as f:
            return yaml.safe_load(f)
    return {}