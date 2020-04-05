# Собирач на реченици
Алатка која би требало да ја олесни работата во собирање на реченици за проектот Common Voice

# Потребни алатки
	* wget
	* python3

# Инсталација
`git clone https://github.com/skopjehacklab/sentence-collector`
`pip3 install -r requirements.txt`

# Како да ја користам
Прво, преземете веб страница чија содржина е објавена како CC0 со помош на оваа команда

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

Потоа во raw_scraper.py променете ја варијаблата `searchFolder`  со каде се наоѓаат преземаните содржини.

