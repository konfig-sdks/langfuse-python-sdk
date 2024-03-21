# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from langfuse_python_sdk.paths.api_public_projects import Api

from langfuse_python_sdk.paths import PathValues

path = PathValues.API_PUBLIC_PROJECTS