# Shadowrocket-config

Данный репозиторий автоматически генерирует новый конфигурационный файл для Shadowrocket.

## Принцип работы

На каждое изменение в репозитории [lrlunin/Re-filter-lists
](https://github.com/lrlunin/Re-filter-lists) активируется `generate_conf.py` скрипт в этом репозитории, который добавляет URL адреса из файлов:
1. `community.lst`
2. `ooni_domains.lst`
3. `user_custom.lst`
и список IP подсетей из `ipsum.lst` и сохраняет его как `lunin_2.conf`.

## Добавление новых адресов
Создайте Issue или Pull-request в [lrlunin/Re-filter-lists
](https://github.com/lrlunin/Re-filter-lists) или напишите мне в tg.
