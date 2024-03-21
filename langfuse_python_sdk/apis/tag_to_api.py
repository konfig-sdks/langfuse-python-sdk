import typing_extensions

from langfuse_python_sdk.apis.tags import TagValues
from langfuse_python_sdk.apis.tags.score_api import ScoreApi
from langfuse_python_sdk.apis.tags.datasets_api import DatasetsApi
from langfuse_python_sdk.apis.tags.dataset_items_api import DatasetItemsApi
from langfuse_python_sdk.apis.tags.observations_api import ObservationsApi
from langfuse_python_sdk.apis.tags.prompts_api import PromptsApi
from langfuse_python_sdk.apis.tags.trace_api import TraceApi
from langfuse_python_sdk.apis.tags.dataset_run_items_api import DatasetRunItemsApi
from langfuse_python_sdk.apis.tags.health_api import HealthApi
from langfuse_python_sdk.apis.tags.ingestion_api import IngestionApi
from langfuse_python_sdk.apis.tags.metrics_api import MetricsApi
from langfuse_python_sdk.apis.tags.projects_api import ProjectsApi
from langfuse_python_sdk.apis.tags.sessions_api import SessionsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.SCORE: ScoreApi,
        TagValues.DATASETS: DatasetsApi,
        TagValues.DATASET_ITEMS: DatasetItemsApi,
        TagValues.OBSERVATIONS: ObservationsApi,
        TagValues.PROMPTS: PromptsApi,
        TagValues.TRACE: TraceApi,
        TagValues.DATASET_RUN_ITEMS: DatasetRunItemsApi,
        TagValues.HEALTH: HealthApi,
        TagValues.INGESTION: IngestionApi,
        TagValues.METRICS: MetricsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.SESSIONS: SessionsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.SCORE: ScoreApi,
        TagValues.DATASETS: DatasetsApi,
        TagValues.DATASET_ITEMS: DatasetItemsApi,
        TagValues.OBSERVATIONS: ObservationsApi,
        TagValues.PROMPTS: PromptsApi,
        TagValues.TRACE: TraceApi,
        TagValues.DATASET_RUN_ITEMS: DatasetRunItemsApi,
        TagValues.HEALTH: HealthApi,
        TagValues.INGESTION: IngestionApi,
        TagValues.METRICS: MetricsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.SESSIONS: SessionsApi,
    }
)
