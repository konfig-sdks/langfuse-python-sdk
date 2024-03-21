import typing_extensions

from langfuse_python_sdk.paths import PathValues
from langfuse_python_sdk.apis.paths.api_public_dataset_items import ApiPublicDatasetItems
from langfuse_python_sdk.apis.paths.api_public_dataset_items_id import ApiPublicDatasetItemsId
from langfuse_python_sdk.apis.paths.api_public_dataset_run_items import ApiPublicDatasetRunItems
from langfuse_python_sdk.apis.paths.api_public_datasets_dataset_name import ApiPublicDatasetsDatasetName
from langfuse_python_sdk.apis.paths.api_public_datasets import ApiPublicDatasets
from langfuse_python_sdk.apis.paths.api_public_datasets_dataset_name_runs_run_name import ApiPublicDatasetsDatasetNameRunsRunName
from langfuse_python_sdk.apis.paths.api_public_health import ApiPublicHealth
from langfuse_python_sdk.apis.paths.api_public_ingestion import ApiPublicIngestion
from langfuse_python_sdk.apis.paths.api_public_metrics_daily import ApiPublicMetricsDaily
from langfuse_python_sdk.apis.paths.api_public_observations_observation_id import ApiPublicObservationsObservationId
from langfuse_python_sdk.apis.paths.api_public_observations import ApiPublicObservations
from langfuse_python_sdk.apis.paths.api_public_projects import ApiPublicProjects
from langfuse_python_sdk.apis.paths.api_public_prompts import ApiPublicPrompts
from langfuse_python_sdk.apis.paths.api_public_scores import ApiPublicScores
from langfuse_python_sdk.apis.paths.api_public_scores_score_id import ApiPublicScoresScoreId
from langfuse_python_sdk.apis.paths.api_public_sessions_session_id import ApiPublicSessionsSessionId
from langfuse_python_sdk.apis.paths.api_public_traces_trace_id import ApiPublicTracesTraceId
from langfuse_python_sdk.apis.paths.api_public_traces import ApiPublicTraces

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_PUBLIC_DATASETITEMS: ApiPublicDatasetItems,
        PathValues.API_PUBLIC_DATASETITEMS_ID: ApiPublicDatasetItemsId,
        PathValues.API_PUBLIC_DATASETRUNITEMS: ApiPublicDatasetRunItems,
        PathValues.API_PUBLIC_DATASETS_DATASET_NAME: ApiPublicDatasetsDatasetName,
        PathValues.API_PUBLIC_DATASETS: ApiPublicDatasets,
        PathValues.API_PUBLIC_DATASETS_DATASET_NAME_RUNS_RUN_NAME: ApiPublicDatasetsDatasetNameRunsRunName,
        PathValues.API_PUBLIC_HEALTH: ApiPublicHealth,
        PathValues.API_PUBLIC_INGESTION: ApiPublicIngestion,
        PathValues.API_PUBLIC_METRICS_DAILY: ApiPublicMetricsDaily,
        PathValues.API_PUBLIC_OBSERVATIONS_OBSERVATION_ID: ApiPublicObservationsObservationId,
        PathValues.API_PUBLIC_OBSERVATIONS: ApiPublicObservations,
        PathValues.API_PUBLIC_PROJECTS: ApiPublicProjects,
        PathValues.API_PUBLIC_PROMPTS: ApiPublicPrompts,
        PathValues.API_PUBLIC_SCORES: ApiPublicScores,
        PathValues.API_PUBLIC_SCORES_SCORE_ID: ApiPublicScoresScoreId,
        PathValues.API_PUBLIC_SESSIONS_SESSION_ID: ApiPublicSessionsSessionId,
        PathValues.API_PUBLIC_TRACES_TRACE_ID: ApiPublicTracesTraceId,
        PathValues.API_PUBLIC_TRACES: ApiPublicTraces,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_PUBLIC_DATASETITEMS: ApiPublicDatasetItems,
        PathValues.API_PUBLIC_DATASETITEMS_ID: ApiPublicDatasetItemsId,
        PathValues.API_PUBLIC_DATASETRUNITEMS: ApiPublicDatasetRunItems,
        PathValues.API_PUBLIC_DATASETS_DATASET_NAME: ApiPublicDatasetsDatasetName,
        PathValues.API_PUBLIC_DATASETS: ApiPublicDatasets,
        PathValues.API_PUBLIC_DATASETS_DATASET_NAME_RUNS_RUN_NAME: ApiPublicDatasetsDatasetNameRunsRunName,
        PathValues.API_PUBLIC_HEALTH: ApiPublicHealth,
        PathValues.API_PUBLIC_INGESTION: ApiPublicIngestion,
        PathValues.API_PUBLIC_METRICS_DAILY: ApiPublicMetricsDaily,
        PathValues.API_PUBLIC_OBSERVATIONS_OBSERVATION_ID: ApiPublicObservationsObservationId,
        PathValues.API_PUBLIC_OBSERVATIONS: ApiPublicObservations,
        PathValues.API_PUBLIC_PROJECTS: ApiPublicProjects,
        PathValues.API_PUBLIC_PROMPTS: ApiPublicPrompts,
        PathValues.API_PUBLIC_SCORES: ApiPublicScores,
        PathValues.API_PUBLIC_SCORES_SCORE_ID: ApiPublicScoresScoreId,
        PathValues.API_PUBLIC_SESSIONS_SESSION_ID: ApiPublicSessionsSessionId,
        PathValues.API_PUBLIC_TRACES_TRACE_ID: ApiPublicTracesTraceId,
        PathValues.API_PUBLIC_TRACES: ApiPublicTraces,
    }
)
