
Install python virtual env
```
virtualenv -p python3 venv
```

Activate python venv:
```
source venv/bin/activate
```

Install from requirement

```
pip3 install -r requirement.txt
```

Create `config.json` file uder root dir:
```
{
  "mongo_config": {
    "username": "...",
    "password": "..."
  }
}
```