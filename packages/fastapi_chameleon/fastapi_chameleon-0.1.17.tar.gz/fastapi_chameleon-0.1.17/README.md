# fastapi-chameleon

Adds integration of the Chameleon template language to FastAPI. If you are interested in Jinja instead, see the sister project: [github.com/AGeekInside/fastapi-jinja](https://github.com/AGeekInside/fastapi-jinja).

## Installation

Simply `pip install fastapi_chameleon`.

## Usage

This is easy to use. Just create a folder within your web app to hold the templates such as:

```
├── main.py
├── views.py
│
├── templates
│   ├── home
│   │   └── index.pt
│   └── shared
│       └── layout.pt

```

In the app startup, tell the library about the folder you wish to use:

```python
import os
from pathlib import Path
import fastapi_chameleon

dev_mode = True

BASE_DIR = Path(__file__).resolve().parent
template_folder = str(BASE_DIR / 'templates')
fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)
```

Then just decorate the FastAPI view methods (works on sync and async methods):

```python
@router.post('/')
@fastapi_chameleon.template('home/index.pt')
async def home_post(request: Request):
    form = await request.form()
    vm = PersonViewModel(**form) 

    return vm.dict() # {'first':'Michael', 'last':'Kennedy', ...}

```

The view method should return a `dict` to be passed as variables/values to the template. 

If a `fastapi.Response` is returned, the template is skipped and the response along with status_code and
other values is directly passed through. This is common for redirects and error responses not meant
for this page template.

## Friendly 404s and errors

A common technique for user-friendly sites is to use a 
[custom HTML page for 404 responses](http://www.instantshift.com/2019/10/16/user-friendly-404-pages/).
This is especially important in FastAPI because FastAPI returns a 404 response + JSON by default.
This library has support for friendly 404 pages using the `fastapi_chameleon.not_found()` function.

Here's an example:

```python
@router.get('/catalog/item/{item_id}')
@fastapi_chameleon.template('catalog/item.pt')
async def item(item_id: int):
    item = service.get_item_by_id(item_id)
    if not item:
        fastapi_chameleon.not_found()
    
    return item.dict()
```

This will render a 404 response with using the template file `templates/errors/404.pt`.
You can specify another template to use for the response, but it's not required.

If you need to return errors other than `Not Found` (status code `404`), you can use a more
generic function: `fastapi_chameleon.generic_error(template_file: str, status_code: int)`.
This function will allow you to return different status codes. It's generic, thus you'll have
to pass a path to your error template file as well as a status code you want the user to get
in response. For example:

```python
@router.get('/catalog/item/{item_id}')
@fastapi_chameleon.template('catalog/item.pt')
async def item(item_id: int):
    item = service.get_item_by_id(item_id)
    if not item:
        fastapi_chameleon.generic_error('errors/unauthorized.pt',
                                        fastapi.status.HTTP_401_UNAUTHORIZED)

    return item.dict()
```
