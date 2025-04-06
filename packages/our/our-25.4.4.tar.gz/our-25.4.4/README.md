# Our - A Powerful Paste Management Library

**Our** is a Python library designed to provide seamless integration for uploading and retrieving pastes from a powerful API. It simplifies the process of sharing code, notes, and content with a unique system to upload, store, and retrieve your pastes effortlessly. Whether you are working on a personal project or need a reliable paste management solution, **Our** has you covered.

## Features

- **Effortless Upload**: Upload content with ease and retrieve a unique identifier (ID) for future access.
- **Quick Retrieval**: Retrieve your pastes with minimal latency using the provided paste ID.
- **Customizable**: Define content extensions, add descriptions, and set ownership details while uploading.
- **Error Handling**: Automatically manages request exceptions and provides clear error messages for easy troubleshooting.
- **Simple API Integration**: Built to integrate seamlessly into any Python-based project.

## Installation

Simply install `our` via pip:

```bash
pip install our==25.4.4
```
```python
#Usage Example

from our import upload, get

# Upload content and retrieve the paste ID
paste_id = upload("This is a test paste", description="Test paste description", owner="Owner Name")

# Retrieve content using the paste ID
if paste_id:
    content = get(paste_id)
    print(f"Paste content: {content}")
```