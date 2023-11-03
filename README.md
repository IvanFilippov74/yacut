## YaCut - сервис коротких ссылок.

### Описание:
На большинстве сайтов адреса страниц довольно длинные, например, как у той страницы, на которой вы сейчас находитесь. Делиться такими длинными ссылками не всегда удобно, а иногда и вовсе невозможно.
Например ссылка ```http://yacut.ru/12e07d```, визуально воспринимается проще чем ```https://practicum.yandex.ru/trainer/backend-developer/lesson/12e07d96-31f3-449f-abcf-e468b6a39061/```.
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

### Технологии :
![Python](https://img.shields.io/badge/Python-3.8.10-blue) ![Flask](https://img.shields.io/badge/Flask-2.0.1-blue) ![FlaskWTF](https://img.shields.io/badge/FlaskWTF-1.0.0-blue)   ![FlaskSQLAlchemy](https://img.shields.io/badge/FlaskSQLAlchemy-2.5.1-blue) ![FlaskMigrate](https://img.shields.io/badge/FlaskMigrate-3.1.0-blue)
![SQLAlchemy](https://img.shields.io/badge/SQLALchemy-1.4.29-green) ![Flask](https://img.shields.io/badge/Jinja2-3.0.3-green) ![WTForms](https://img.shields.io/badge/WTForms-3.0.1-green) ![Flake8](https://img.shields.io/badge/Flake8-4.0.1-green) ![Pytest](https://img.shields.io/badge/Pytest-7.1.1-green) 

### Функционал:
Ключевые возможности сервиса:
- генерация коротких ссылок и связь их с исходными длинными ссылками,
- переадресация на исходный адрес при обращении к коротким ссылкам.

Пользовательский интерфейс сервиса — одна страница с формой. Эта форма состоит из двух полей:
- обязательного для длинной исходной ссылки;
- необязательного для пользовательского варианта короткой ссылки.
Пользовательский вариант короткой ссылки не должен превышать 16 символов.
### Как запустить проект:
Склонировать репозиторий в командной строке:
```bash
git clone https://github.com/IvanFilippov74/yacut.git
```
Затем перейдите в корневую директорию проекта:
```bash
cd  yacut/
```
Cоздать и активировать виртуальное окружение:
```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```bash
pip install -r requirements.txt
```
Создать и заполнить файл .env в корне проекта:
```bash
FLASK_APP=yacut
FLASK_ENV=development
DATABASE_URI=your_db or sqlite:///db.sqlite3
SECRET_KEY=your_secret_key
```
Выполните миграции в базу данных :
```
flask db init
flask db migrate -m "init"
flask db upgrade
```
Запустите проект из корневой директории:
```
flask run
```
Перейдите по url-адресу:
```
http://127.0.0.1:5000/
```
### Авторы:
Filippov Ivan
<a href="https://github.com/IvanFilippov74"><img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white"></a>