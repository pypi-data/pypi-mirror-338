# Python-Github-Release-Update-Checker
A simple GUI-based update notifier in Python   
   
## Requirements
requests | https://github.com/psf/requests | https://github.com/psf/requests/blob/main/LICENSE   
   
## Example   
```py
import github_release_update_checker as gruc
gruc.PGRUC("user/repo","2024-01-20T11:13:05Z",True)
```
![Example](https://raw.githubusercontent.com/1325ok/Python-Github-Release-Update-Checker/main/ext/image2.png)
## Install
https://pypi.org/project/github-release-update-checker/
```console
$ python -m pip install github-release-update-checker
```

## Parameter

| Parameter  | Description |
| ------------- |:-------------:|
| repo      | Github Repo ex) 1325ok/pgruc     |
| creasted_at     | Now version date ex) 2025-04-03T18:00:49       |
| updateChanges      | Show update changes: True/False       |