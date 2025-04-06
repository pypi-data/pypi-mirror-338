import requests
import tkinter.messagebox as msgbox
import datetime
import webbrowser

#다음에 다시 알림
#설치하기

def PGRUC(repo: str, created_at: str, updateChanges: bool):
        
    """A simple GUI-based update notifier in Python

    :param repo: Github Repo ex: 1325ok/pgruc
    :param creasted_at: Now version date ex: 2025-04-03T18:00:49
    :param updateChanges: Show update changes: True/False
    """
    r = requests.get(f'https://api.github.com/repos/{repo}/releases/latest').json()
    datetime_format = "%Y-%m-%dT%H:%M:%SZ"
    json_datetime = datetime.datetime.strptime(r["created_at"], datetime_format)
    ini_datetime = datetime.datetime.strptime(created_at, datetime_format)

    # 날짜 비교 및 출력
    if json_datetime > ini_datetime:
        try:
            if updateChanges == True:
                updcheckask = msgbox.askyesno("Update available", f"There is an update available for version {r['name']}.\nShould we proceed with the update?\n\nUpdate changes:\n{r['body']}")#,title="Update available"
            else:
                raise "NoDetail"
        except:
            updcheckask = msgbox.askyesno("Update available", f"There is an update available for version {r['name']}.\nShould we proceed with the update?")
            #ko업데이트 가능한 버전 {r['name']}이 있습니다.\n업데이트를 진행할까요?
        if updcheckask == 1:
            webbrowser.open_new(f"https://github.com/{repo}/releases/latest")

# PGRUC("user/repo","2024-01-20T11:13:05Z",False)#Example