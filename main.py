import webbrowser
import datetime
import time
import json


def autoconnection(conf):
    if conf['dayofweek'] == datetime.datetime.today().weekday() \
    and conf['hour'] == datetime.datetime.today().hour \
    and conf['minute'] == datetime.datetime.today().minute:
        if conf['platform'] == 'Zoom':
            webbrowser.open(conf['link'], new=2)
            if conf['reconnect']:
                time.sleep(2700)
                webbrowser.open(conf['link'], new=2)
                time.sleep(2700)
                webbrowser.open(conf['link'], new=2)
            else:
                time.sleep(60)
        elif conf['platform'] == 'Google':
            webbrowser.open(conf['link'], new=2)
            time.sleep(60)
    


def main():
    with open("links.json", "r") as f:
        confs = json.load(f)

    while True:
        for conf in confs:
            autoconnection(conf)
        time.sleep(30)


if __name__ == '__main__':
    main()