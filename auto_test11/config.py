import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="auto_test11",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="auto_test11_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from auto_test11.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export auto_test11_KEY=value
export auto_test11_KEY="@int 42"
export auto_test11_KEY="@jinja {{ this.db.uri }}"
export auto_test11_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
auto_test11_ENV=production auto_test11 run
```

Read more on https://dynaconf.com
"""
