<div align="left">

[![Visit Langfuse](./header.png)](https://langfuse.com)

# Langfuse<a id="langfuse"></a>

## Authentication<a id="authentication"></a>

Authenticate with the API using Basic Auth, get API keys in the project settings:

- username: Langfuse Public Key
- password: Langfuse Secret Key


</div>

## Table of Contents<a id="table-of-contents"></a>

<!-- toc -->

- [Requirements](#requirements)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [Async](#async)
- [Raw HTTP Response](#raw-http-response)
- [Reference](#reference)
  * [`langfuse.dataset_items.create`](#langfusedataset_itemscreate)
  * [`langfuse.dataset_items.get`](#langfusedataset_itemsget)
  * [`langfuse.dataset_run_items.create`](#langfusedataset_run_itemscreate)
  * [`langfuse.datasets.create`](#langfusedatasetscreate)
  * [`langfuse.datasets.get`](#langfusedatasetsget)
  * [`langfuse.datasets.get_runs`](#langfusedatasetsget_runs)
  * [`langfuse.health.health`](#langfusehealthhealth)
  * [`langfuse.ingestion.batch`](#langfuseingestionbatch)
  * [`langfuse.metrics.daily`](#langfusemetricsdaily)
  * [`langfuse.observations.get`](#langfuseobservationsget)
  * [`langfuse.observations.get_many`](#langfuseobservationsget_many)
  * [`langfuse.projects.get`](#langfuseprojectsget)
  * [`langfuse.prompts.create`](#langfusepromptscreate)
  * [`langfuse.prompts.get`](#langfusepromptsget)
  * [`langfuse.score.create`](#langfusescorecreate)
  * [`langfuse.score.delete`](#langfusescoredelete)
  * [`langfuse.score.get`](#langfusescoreget)
  * [`langfuse.score.get_by_id`](#langfusescoreget_by_id)
  * [`langfuse.sessions.get`](#langfusesessionsget)
  * [`langfuse.trace.get`](#langfusetraceget)
  * [`langfuse.trace.list`](#langfusetracelist)

<!-- tocstop -->

## Requirements<a id="requirements"></a>

Python >=3.7

## Installation<a id="installation"></a>
<div align="center">
  <a href="https://konfigthis.com/sdk-sign-up?company=Langfuse&language=Python">
    <img src="https://raw.githubusercontent.com/konfig-dev/brand-assets/HEAD/cta-images/python-cta.png" width="70%">
  </a>
</div>

## Getting Started<a id="getting-started"></a>

```python
from pprint import pprint
from langfuse_python_sdk import Langfuse, ApiException

langfuse = Langfuse(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    create_response = langfuse.dataset_items.create(
        dataset_name="string_example",
        input=None,
        expected_output=None,
        id="string_example",
    )
    print(create_response)
except ApiException as e:
    print("Exception when calling DatasetItemsApi.create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```

## Async<a id="async"></a>

`async` support is available by prepending `a` to any method.

```python
import asyncio
from pprint import pprint
from langfuse_python_sdk import Langfuse, ApiException

langfuse = Langfuse(username="YOUR_USERNAME", password="YOUR_PASSWORD")


async def main():
    try:
        create_response = await langfuse.dataset_items.acreate(
            dataset_name="string_example",
            input=None,
            expected_output=None,
            id="string_example",
        )
        print(create_response)
    except ApiException as e:
        print("Exception when calling DatasetItemsApi.create: %s\n" % e)
        pprint(e.body)
        pprint(e.headers)
        pprint(e.status)
        pprint(e.reason)
        pprint(e.round_trip_time)


asyncio.run(main())
```

## Raw HTTP Response<a id="raw-http-response"></a>

To access raw HTTP response values, use the `.raw` namespace.

```python
from pprint import pprint
from langfuse_python_sdk import Langfuse, ApiException

langfuse = Langfuse(username="YOUR_USERNAME", password="YOUR_PASSWORD")

try:
    create_response = langfuse.dataset_items.raw.create(
        dataset_name="string_example",
        input=None,
        expected_output=None,
        id="string_example",
    )
    pprint(create_response.body)
    pprint(create_response.body["id"])
    pprint(create_response.body["status"])
    pprint(create_response.body["input"])
    pprint(create_response.body["dataset_id"])
    pprint(create_response.body["created_at"])
    pprint(create_response.body["updated_at"])
    pprint(create_response.body["expected_output"])
    pprint(create_response.body["source_observation_id"])
    pprint(create_response.headers)
    pprint(create_response.status)
    pprint(create_response.round_trip_time)
except ApiException as e:
    print("Exception when calling DatasetItemsApi.create: %s\n" % e)
    pprint(e.body)
    pprint(e.headers)
    pprint(e.status)
    pprint(e.reason)
    pprint(e.round_trip_time)
```


## Reference<a id="reference"></a>
### `langfuse.dataset_items.create`<a id="langfusedataset_itemscreate"></a>

Create a dataset item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = langfuse.dataset_items.create(
    dataset_name="string_example",
    input=None,
    expected_output=None,
    id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_name: `str`<a id="dataset_name-str"></a>

##### input: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./langfuse_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="input-unionbool-date-datetime-dict-float-int-list-str-nonelangfuse_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### expected_output: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./langfuse_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="expected_output-unionbool-date-datetime-dict-float-int-list-str-nonelangfuse_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

##### id: `Optional[str]`<a id="id-optionalstr"></a>

Dataset items are upserted on their id

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDatasetItemRequest`](./langfuse_python_sdk/type/create_dataset_item_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DatasetItem`](./langfuse_python_sdk/pydantic/dataset_item.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/dataset-items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.dataset_items.get`<a id="langfusedataset_itemsget"></a>

Get a dataset item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.dataset_items.get(
    id="id_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### id: `str`<a id="id-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetItem`](./langfuse_python_sdk/pydantic/dataset_item.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/dataset-items/{id}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.dataset_run_items.create`<a id="langfusedataset_run_itemscreate"></a>

Create a dataset run item

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = langfuse.dataset_run_items.create(
    run_name="string_example",
    dataset_item_id="string_example",
    observation_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### run_name: `str`<a id="run_name-str"></a>

##### dataset_item_id: `str`<a id="dataset_item_id-str"></a>

##### observation_id: `str`<a id="observation_id-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDatasetRunItemRequest`](./langfuse_python_sdk/type/create_dataset_run_item_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`DatasetRunItem`](./langfuse_python_sdk/pydantic/dataset_run_item.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/dataset-run-items` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.datasets.create`<a id="langfusedatasetscreate"></a>

Create a dataset

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = langfuse.datasets.create(
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateDatasetRequest`](./langfuse_python_sdk/type/create_dataset_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Dataset`](./langfuse_python_sdk/pydantic/dataset.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/datasets` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.datasets.get`<a id="langfusedatasetsget"></a>

Get a dataset and its items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.datasets.get(
    dataset_name="datasetName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_name: `str`<a id="dataset_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Dataset`](./langfuse_python_sdk/pydantic/dataset.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/datasets/{datasetName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.datasets.get_runs`<a id="langfusedatasetsget_runs"></a>

Get a dataset run and its items

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_runs_response = langfuse.datasets.get_runs(
    dataset_name="datasetName_example",
    run_name="runName_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### dataset_name: `str`<a id="dataset_name-str"></a>

##### run_name: `str`<a id="run_name-str"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`DatasetRun`](./langfuse_python_sdk/pydantic/dataset_run.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/datasets/{datasetName}/runs/{runName}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.health.health`<a id="langfusehealthhealth"></a>

Check health of API and database

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
health_response = langfuse.health.health()
```

#### 🔄 Return<a id="🔄-return"></a>

[`HealthResponse`](./langfuse_python_sdk/pydantic/health_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/health` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.ingestion.batch`<a id="langfuseingestionbatch"></a>

Batched ingestion for Langfuse Tracing

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
batch_response = langfuse.ingestion.batch(
    batch=[None],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### batch: List[`IngestionEvent`]<a id="batch-listingestionevent"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`IngestionBatchRequest`](./langfuse_python_sdk/type/ingestion_batch_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`IngestionResponse`](./langfuse_python_sdk/pydantic/ingestion_response.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/ingestion` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.metrics.daily`<a id="langfusemetricsdaily"></a>

Get daily metrics of the Langfuse project

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
daily_response = langfuse.metrics.daily(
    page=1,
    limit=1,
    trace_name="string_example",
    user_id="string_example",
    tags=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `Optional[int]`<a id="page-optionalint"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

##### trace_name: `Optional[str]`<a id="trace_name-optionalstr"></a>

Optional filter by the name of the trace

##### user_id: `Optional[str]`<a id="user_id-optionalstr"></a>

Optional filter by the userId associated with the trace

##### tags: List[`Optional[str]`]<a id="tags-listoptionalstr"></a>

Optional filter for metrics where traces include all of these tags

#### 🔄 Return<a id="🔄-return"></a>

[`DailyMetrics`](./langfuse_python_sdk/pydantic/daily_metrics.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/metrics/daily` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.observations.get`<a id="langfuseobservationsget"></a>

Get a observation

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.observations.get(
    observation_id="observationId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### observation_id: `str`<a id="observation_id-str"></a>

The unique langfuse identifier of an observation, can be an event, span or generation

#### 🔄 Return<a id="🔄-return"></a>

[`Observation`](./langfuse_python_sdk/pydantic/observation.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/observations/{observationId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.observations.get_many`<a id="langfuseobservationsget_many"></a>

Get a list of observations

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_many_response = langfuse.observations.get_many(
    page=1,
    limit=1,
    name="string_example",
    user_id="string_example",
    type="string_example",
    trace_id="string_example",
    parent_observation_id="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `Optional[int]`<a id="page-optionalint"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### user_id: `Optional[str]`<a id="user_id-optionalstr"></a>

##### type: `Optional[str]`<a id="type-optionalstr"></a>

##### trace_id: `Optional[str]`<a id="trace_id-optionalstr"></a>

##### parent_observation_id: `Optional[str]`<a id="parent_observation_id-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`ObservationsViews`](./langfuse_python_sdk/pydantic/observations_views.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/observations` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.projects.get`<a id="langfuseprojectsget"></a>

Get Project associated with API key

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.projects.get()
```

#### 🔄 Return<a id="🔄-return"></a>

[`Projects`](./langfuse_python_sdk/pydantic/projects.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/projects` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.prompts.create`<a id="langfusepromptscreate"></a>

Create a prompt

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = langfuse.prompts.create(
    name="string_example",
    is_active=True,
    prompt="string_example",
    config=None,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### is_active: `bool`<a id="is_active-bool"></a>

Should the prompt be promoted to production immediately?

##### prompt: `str`<a id="prompt-str"></a>

##### config: [`Union[bool, date, datetime, dict, float, int, list, str, None]`](./langfuse_python_sdk/type/typing_union_bool_date_datetime_dict_float_int_list_str_none.py)<a id="config-unionbool-date-datetime-dict-float-int-list-str-nonelangfuse_python_sdktypetyping_union_bool_date_datetime_dict_float_int_list_str_nonepy"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreatePromptRequest`](./langfuse_python_sdk/type/create_prompt_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Prompt`](./langfuse_python_sdk/pydantic/prompt.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/prompts` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.prompts.get`<a id="langfusepromptsget"></a>

Get a prompt

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.prompts.get(
    name="name_example",
    version=1,
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### name: `str`<a id="name-str"></a>

##### version: `Optional[int]`<a id="version-optionalint"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Prompt`](./langfuse_python_sdk/pydantic/prompt.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/prompts` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.score.create`<a id="langfusescorecreate"></a>

Create a score

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
create_response = langfuse.score.create(
    trace_id="string_example",
    name="string_example",
    value=3.14,
    id="string_example",
    observation_id="string_example",
    comment="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### trace_id: `str`<a id="trace_id-str"></a>

##### name: `str`<a id="name-str"></a>

##### value: `Union[int, float]`<a id="value-unionint-float"></a>

##### id: `Optional[str]`<a id="id-optionalstr"></a>

##### observation_id: `Optional[str]`<a id="observation_id-optionalstr"></a>

##### comment: `Optional[str]`<a id="comment-optionalstr"></a>

#### ⚙️ Request Body<a id="⚙️-request-body"></a>

[`CreateScoreRequest`](./langfuse_python_sdk/type/create_score_request.py)
#### 🔄 Return<a id="🔄-return"></a>

[`Score`](./langfuse_python_sdk/pydantic/score.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/scores` `post`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.score.delete`<a id="langfusescoredelete"></a>

Delete a score

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
langfuse.score.delete(
    score_id="scoreId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### score_id: `str`<a id="score_id-str"></a>

The unique langfuse identifier of a score

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/scores/{scoreId}` `delete`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.score.get`<a id="langfusescoreget"></a>

Get a list of scores

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.score.get(
    page=1,
    limit=1,
    user_id="string_example",
    name="string_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `Optional[int]`<a id="page-optionalint"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

##### user_id: `Optional[str]`<a id="user_id-optionalstr"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

#### 🔄 Return<a id="🔄-return"></a>

[`Scores`](./langfuse_python_sdk/pydantic/scores.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/scores` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.score.get_by_id`<a id="langfusescoreget_by_id"></a>

Get a score

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_by_id_response = langfuse.score.get_by_id(
    score_id="scoreId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### score_id: `str`<a id="score_id-str"></a>

The unique langfuse identifier of a score

#### 🔄 Return<a id="🔄-return"></a>

[`Score`](./langfuse_python_sdk/pydantic/score.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/scores/{scoreId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.sessions.get`<a id="langfusesessionsget"></a>

Get a session

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.sessions.get(
    session_id="sessionId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### session_id: `str`<a id="session_id-str"></a>

The unique id of a session

#### 🔄 Return<a id="🔄-return"></a>

[`Session`](./langfuse_python_sdk/pydantic/session.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/sessions/{sessionId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.trace.get`<a id="langfusetraceget"></a>

Get a specific trace

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
get_response = langfuse.trace.get(
    trace_id="traceId_example",
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### trace_id: `str`<a id="trace_id-str"></a>

The unique langfuse identifier of a trace

#### 🔄 Return<a id="🔄-return"></a>

[`Trace`](./langfuse_python_sdk/pydantic/trace.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/traces/{traceId}` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---

### `langfuse.trace.list`<a id="langfusetracelist"></a>

Get list of traces

#### 🛠️ Usage<a id="🛠️-usage"></a>

```python
list_response = langfuse.trace.list(
    page=1,
    limit=1,
    user_id="string_example",
    name="string_example",
    order_by="string_example",
    tags=["string_example"],
)
```

#### ⚙️ Parameters<a id="⚙️-parameters"></a>

##### page: `Optional[int]`<a id="page-optionalint"></a>

##### limit: `Optional[int]`<a id="limit-optionalint"></a>

##### user_id: `Optional[str]`<a id="user_id-optionalstr"></a>

##### name: `Optional[str]`<a id="name-optionalstr"></a>

##### order_by: `Optional[str]`<a id="order_by-optionalstr"></a>

Format of the string [field].[asc/desc]. Fields: id, timestamp, name, userId, release, version, public, bookmarked, sessionId. Example: timestamp.asc

##### tags: List[`Optional[str]`]<a id="tags-listoptionalstr"></a>

Only traces that include all of these tags will be returned.

#### 🔄 Return<a id="🔄-return"></a>

[`Traces`](./langfuse_python_sdk/pydantic/traces.py)

#### 🌐 Endpoint<a id="🌐-endpoint"></a>

`/api/public/traces` `get`

[🔙 **Back to Table of Contents**](#table-of-contents)

---


## Author<a id="author"></a>
This Python package is automatically generated by [Konfig](https://konfigthis.com)
