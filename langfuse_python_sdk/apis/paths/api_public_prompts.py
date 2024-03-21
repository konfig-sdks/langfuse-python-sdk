from langfuse_python_sdk.paths.api_public_prompts.get import ApiForget
from langfuse_python_sdk.paths.api_public_prompts.post import ApiForpost


class ApiPublicPrompts(
    ApiForget,
    ApiForpost,
):
    pass
