# Easy Issues

## Sections
- [Local Dev Setup](#local-dev-setup)
    - [Pre-requisites](#pre-requisites)
    - [Start the Server](#start-the-server)
    - [Creating a Pull Request](#creating-a-pull-request)
## Local Dev Setup

### Pre-requisites
1. Ensure you have cloned the easyissues-backend repo.
2. Ensure you have poetry (>2.1.3) and python (>3.13.5) installed. (https://python-poetry.org/docs/)
3. Ensure you have poetry shell plugin installed. (https://github.com/python-poetry/poetry-plugin-shell?tab=readme-ov-file#installation)
4. Install flake8 to run lint checks locally. (`pip install flake8`)

### Start the Server
```
poetry install
poetry shell
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8001 --reload
```
If `poetry shell` doesn't work, try `source $(poetry env info --path)/bin/activate`.

#### Verify the Server
```
curl -X GET http://localhost:8001/api/health
```

### Creating a Pull Request

1. Create a new branch locally
`git checkout -b new_branch`
2. Stage, commit and push your changes
```
git add .
git commit
git push origin new_branch
```
3. Wait for approval, then squash and merge on GitHub