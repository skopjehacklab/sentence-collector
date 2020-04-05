# Собирач на реченици
Алатка која би требало да ја олесни работата во собирање на реченици за [проектот](https://mozilla.mk/2020/04/02/%d0%b0%d0%ba%d1%86%d0%b8%d1%98%d0%b0-common-voice-%d0%bd%d0%b0-%d0%bc%d0%b0%d0%ba%d0%b5%d0%b4%d0%be%d0%bd%d1%81%d0%ba%d0%b8/): [Mozilla Common Voice](https://voice.mozilla.org/mk). Алатката е далеку од совршена и подлежи на промени. Не се срами да контрибуираш во нејзино подобрување и оптимизирање. :)

### Потребни алатки
- `wget`
- `python3`
- Опционално: `virtualenv`

### Инсталација

```
$ git clone https://github.com/skopjehacklab/sentence-collector.git && cd sentence-collector
```

##### Ако користиш `virtualenv`:

```
$ virtualenv venv --python=python3
$ source venv/bin/activate
```

И потоа во истата датотека:

```
pip install -r requirements.txt
```

### Упатство за користење

1. Преземете веб-страница чија содржина е објавена со лиценцата [CC-0](https://creativecommons.org/share-your-work/public-domain/cc0/), со помош на следнава команда:

```
wget \
     --recursive \
     --no-clobber \
     --page-requisites \
     --html-extension \
     --convert-links \
     --reject '*.js,*.css,*.ico,*.txt,*.gif,*.jpg,*.jpeg,*.png,*.mp3,*.pdf,*.tgz,*.flv,*.avi,*.mpeg,*.iso' \
     --accept html \
     --restrict-file-names=windows \
     --domains [ДОМЕЈНОТ НА СТРАНАТА ТУКА] \
     --no-parent \
         [ВЕБ САЈТОТ ТУКА]
```

Оставете командата да работи додека ги презема сите страници кои имаат некаква текст содржина.

2. Во `raw_scraper.py`, промени ја променливата `searchFolder` со датотеката каде што се наоѓаат преземаните содржини.

### Што ако веќе имам текст и само сакам да извадам реченици?

Изврши ја следнава команда:

```
$ cat Hamlet.txt | python extractor.py
```

Програмата ќе ви каже колку реченици се успешно извадени и во кој фајл се зачувани. Фајлот ќе се креира во истата датотека кај што е програмата.

### Лиценца

Лиценцата можеш да ја најдеш [овде](LICENSE).
