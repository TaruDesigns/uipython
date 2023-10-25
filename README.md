# UIPython

Example project to use UIPath Orchestrator API in python. Boilerplate is done and examples are provided.
Authorization is based on OAuth2 flows, using Authlib.
This project uses swagger codegen for the API clients, see [my API client](https://github.com/TaruDesigns/UIPathAPI)

This uses Python 3.10

# Authorization

By default, client_credentials auth is setup. The id and secret are stored in config/secrets.py but it is recommended to use environment variables instead.

# Basic usage

Create a virtual environment and activate it

```python -m venv .venv``` 

Install the requirements

```pip install -r requirements.txt``` 

Add your secrets to `config/secrets.py` :
```
UIP_CLIENT_ID: str = "YOUR CLIENT ID"
UIP_CLIENT_SECRET: str = "YOUR SECRET""
``` 

Remember to check  `config/settings.py` and set your account logical name and tenant.

Modify and run main.py as needed
