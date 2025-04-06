# Drebedengi SDK

A Python SDK to interact with the SOAP API provided by [Drebedengi.ru](https://www.drebedengi.ru/).

## Installation

```bash
poetry install
```

## Basic Usage

```python
from drebedengi_sdk import DrebedengiAPI

client = DrebedengiAPI("api_id", "login", "password")
status = client.get_access_status()
print(status)
```

## Supported Methods

The SDK provides Python wrappers for most SOAP methods, including:

- `getAccessStatus`
- `getRecordList`
- `setRecordList`
- `deleteObject`
- and many more...

Refer to the `DrebedengiAPI` class for the full method list.
