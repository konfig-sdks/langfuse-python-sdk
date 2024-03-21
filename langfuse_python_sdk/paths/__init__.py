# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from langfuse_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_PUBLIC_DATASETITEMS = "/api/public/dataset-items"
    API_PUBLIC_DATASETITEMS_ID = "/api/public/dataset-items/{id}"
    API_PUBLIC_DATASETRUNITEMS = "/api/public/dataset-run-items"
    API_PUBLIC_DATASETS_DATASET_NAME = "/api/public/datasets/{datasetName}"
    API_PUBLIC_DATASETS = "/api/public/datasets"
    API_PUBLIC_DATASETS_DATASET_NAME_RUNS_RUN_NAME = "/api/public/datasets/{datasetName}/runs/{runName}"
    API_PUBLIC_HEALTH = "/api/public/health"
    API_PUBLIC_INGESTION = "/api/public/ingestion"
    API_PUBLIC_METRICS_DAILY = "/api/public/metrics/daily"
    API_PUBLIC_OBSERVATIONS_OBSERVATION_ID = "/api/public/observations/{observationId}"
    API_PUBLIC_OBSERVATIONS = "/api/public/observations"
    API_PUBLIC_PROJECTS = "/api/public/projects"
    API_PUBLIC_PROMPTS = "/api/public/prompts"
    API_PUBLIC_SCORES = "/api/public/scores"
    API_PUBLIC_SCORES_SCORE_ID = "/api/public/scores/{scoreId}"
    API_PUBLIC_SESSIONS_SESSION_ID = "/api/public/sessions/{sessionId}"
    API_PUBLIC_TRACES_TRACE_ID = "/api/public/traces/{traceId}"
    API_PUBLIC_TRACES = "/api/public/traces"
