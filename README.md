# Улицы России - Общероссийская общественная организация уличной культуры и спорта

***

#### Ссылка на проект: [streetsrussia.sytes.net](https://streetsrussia.sytes.net/)

#### Ссылка на документацию API: [streetsrussia.sytes.net/swagger](https://streetsrussia.sytes.net/swagger/)

***

[![Python](https://img.shields.io/badge/Python-%203.11-blue?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-%203.2.18-blue?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/DjangoRESTFramework-%203.14.0-blue?style=flat-square&logo=django)](https://www.django-rest-framework.org/)
[![Gunicorn](https://img.shields.io/badge/Gunicorn-%2020.0.4-blue?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![Celery](https://img.shields.io/badge/Celery-%205.4.0-blue?style=flat-square&logo=celery)](https://docs.celeryq.dev/en/stable/)
[![Redis](https://img.shields.io/badge/Redis-%205.4.0-blue?style=flat-square&logo=redis)](https://redis.io/)
[![Django Storages](https://img.shields.io/badge/DjangoStorages-%201.21.7-blue?style=flat-square&logo=django)](https://github.com/jschneier/django-storages)
[![Boto3](https://img.shields.io/badge/boto3-%201.34.10-blue?style=flat-square&logo=boto3)](https://github.com/boto/boto3)
[![Yandex Object Storage](https://img.shields.io/badge/YandexObjectStorage-%20-blue?style=flat-square&logo=yandexcloud)](https://yandex.cloud/ru/)
[![YandexCloud](https://img.shields.io/badge/YandexCloud-%20-blue?style=flat-square&logo=yandexcloud)](https://yandex.cloud/ru/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-%20-blue?style=flat-square&logo=githubactions)](https://github.com/features/actions)
[![Docker](https://img.shields.io/badge/Docker-%2024.0.5-blue?style=flat-square&logo=docker)](https://www.docker.com/)
[![DockerCompose](https://img.shields.io/badge/Docker_Compose-%202.21.0-blue?style=flat-square&logo=docsdotrs)](https://docs.docker.com/compose/)
[![Swagger](https://img.shields.io/badge/Swagger-%201.21.7-blue?style=flat-square&logo=swagger)](https://swagger.io/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-%20-blue?style=flat-square&logo=githubactions)](https://github.com/features/actions)
[![Nginx](https://img.shields.io/badge/Nginx-%201.22.1-blue?style=flat-square&logo=nginx)](https://www.nginx.com/)
[![Certbot](https://img.shields.io/badge/certbot-%202.7.3-blue?style=flat-square&logo=letsencrypt)](https://certbot.eff.org/)


***

## Функционал:

<details>
  <summary>Реализованный фунционал:</summary>

- **Yandex Object Storage S3**: используется для взаимодействия с
  пользовательскими медиа-файлами
- **Почтовый сервер SMTP Yandex**: используется для отправки электронных писем.
- **Celery с Redis**: настроены для асихронной отправки электронных писем,
  обеспечивая эффективное выполение задач в фоновом режиме.
- **Авторизация и регистрация пользователей**: для регистрации пользователя
  необходимо подать заявку на вступление в участники организации. Заявка
  проходит модерацию у администратора, при подверждении происходит асинхронная
  отправка письма.
- **Профиль пользователя**: реализована смена пароля, установка аватарки и
  просмотр профиля.
- **Разделение пользователей на роли**: Пользователь может иметь одну из трёх
  ролей
-
    - _Администратор_ (имеет доступ к админ панели, модерирует любой раздел на
      сайте)
-
    - _Региональный директор_ (имеет доступ к модерированию новостей и
      мероприятий только **своего** региона)
-
    - _Участник_ (имеет доступ к записи и созданию мероприятий. Мероприятия
      созданные участником отправляются на модерацию **региональному директору
      **)
- **Обратная связь**: любой пользователь может отправить обращение через форму
  на главной странице (настроен механизм **Throttling**, ограничивающий
  количество запросов на API ручки). В базе данных создается соответствующая запись.
- **Ответ на обратную связь**: администратор может отвечать на обратную
  связь, отправляя ответы на электронные адреса отправителей.
- **Мероприятия**: cоздание мероприятий доступно только авторизированным
  пользователям. Редактирование, удаление и модерирование мероприятий
  определенного региона доступно региональным директорам и администраторам. В
  мероприятиях реализована галерея: доступно добавлять медиа-файлы (валидация:
  только видео и изображения не более 20MB)
- 
- **Новости**: cоздание новостей модерируется региональным директором, так же
  имеет галерею (валидация: только видео и изображения не более 20MB)
- **Партнёры**: создание партнёра доступно только администраторам. Данные
  выводятся в разделах "О нас", "Главная страница"
- **Фильтрация данных**: для моделей "Мероприятия", "Локация", "Новости", "
  Партнёры" и "Дисциплины" используется подключение django-filter для
  реализации фильтрации данных на бекенде.
- **Логирование**: на всём проекте настроен механизм логирования

</details>

## Технические особенности:

<details>
  <summary>В проекте реализована следующая архитектура:</summary>

### Docker-образы

Для каждого компонента созданы Docker-образы и размещены на Docker Hub:

- `backend`: образ бекенда, содержащий приложение и его зависимости.
- `db`: официальный образ PostgreSQL.
- `celery`: образ для Celery, настроенный для взаимодействия с Redis и
  бекендом.
- `redis`: официальный образ Redis.`
- `nginx`: образ Nginx с конфигурацией для проксирования запросов.
- `frontend`: образ фронтенда, собираемого из исходного кода.

### Docker Compose

Для управления многоконтейнерной инфраструктурой используется docker-compose.
Репозиторий включает в себя два файла **docker-compose.local.yml** и
**docker-compose.yml**, что позволяет развернуть проект на
локальном или удалённом серверах.

### CI/CD GitHub Actions

В проекте настроен CI/CD с использованием GitHub Actions. При каждом пуше в
ветку master выполняются следующие шаги:

- `flake8`: код тестируется утилитой flake8
- `build_backend_and_push_to_docker_hub`, `build_nginx_and_push_to_docker_hub`:
  собираются актуальные Docker-образы и пушатся на Docker Hub
- `deploy`: выполняется деплой на сервер

Все секреты, включая токены для доступа к Docker Hub и ключи для деплоя,
хранятся в секретах GitHub Actions и автоматически подтягиваются в процессе
выполнения CI/CD.
В репозитории `frontend` также настроен CI/CD, который обновляет Docker-образ
на Docker Hub и выполняет деплой на сервер.

### Nginx

Nginx проксирует запросы к статическим файлам, API, административному
интерфейсу, автодокументации Swagger и фронтенд-приложению, направляя их на
соответствующие сервисы.

### Swagger

В проекте настроена автодокументация с помощью **Swagger**. Для ознакомления
перейдите по [ссылке](https://streetsrussia.sytes.net/swagger/)
</details>

## Локальный запуск в Docker:

<details>
  <summary>Данная инструкция подразумевает, что на вашем локальном/удалённом сервере 
уже установлен Git, Python 3.11, пакетный менеджер pip, Docker, 
Docker Compose, утилита виртуального окружения python3-venv.</summary>

Склонируйте проект из репозитория:

```shell
git clone https://github.com/D-Nevskiy/StreetsRussia.git
```

Перейдите в директорию **infra** и создайте файл **.env**:

```shell
cd infra/
```

```shell
nano .env
```

Пример из .env файла:

```dotenv
SECRET_KEY=DJANGO_SECRET_KEY               # Cекретный ключ Django
DEBUG=False                                # True - включить Дебаг. False - выключить Дебаг
ALLOWED_HOSTS=localhost backend            # Список адресов, разделенных пробелами

# Помните, если вы выставляете DEBUG=False, то необходимо будет настроить список ALLOWED_HOSTS.
# 127.0.0.1 и backend является стандартным значением. Через пробел.

# БД выбирается автоматически на основе константы DB_ENGINE. Если DB_ENGINE = sqlite , используется SQLite3.
# Если DB_ENGINE = postgresql , используется PostgreSQL.

DB_ENGINE=postgresql
POSTGRES_USER=django_user                  # Ваше имя пользователя для бд
POSTGRES_PASSWORD=django                   # Ваш пароль для бд
POSTGRES_DB=django                         # Название вашей бд
DB_HOST=db                                 # Стандартное значение - db
DB_PORT=5432                               # Стандартное значение - 5432

# На основе константы USE_S3 выбирается хранилище медиа-файлов пользователей
# Если USE_S3 = True, используется хранилище S3, False - Django

USE_S3=True
AWS_ACCESS_KEY_ID=your_data                 # Ваш ключ доступа AWS
AWS_SECRET_ACCESS_KEY=your_data             # Ваш секретный ключ AWS
AWS_STORAGE_BUCKET_NAME=your_data           # Название вашего S3-бакета
AWS_S3_ENDPOINT_URL=your_data               # URL конечной точки S3
DEFAULT_API_URL=your_data                   # URL вашего API

# Данные вашего SMTP сервера

EMAIL_HOST=smtp.yandex.ru                  # Адрес хоста эл. почты
EMAIL_PORT=465                             # Порт эл. почты
EMAIL_USE_SSL=True                         # Использование SSL
EMAIL_HOST_USER=your_data                  # Адрес почты, с которой будут отправляться письма
EMAIL_HOST_PASSWORD=your_data              # Пароль почты, с которой будут отправляться письма
```

В директории **infra** проекта находится файл **docker-compose.local.yml**, с
помощью которого вы можете запустить проект локально в Docker контейнерах.
> **Примечание.** Если нужно - добавьте в конец команды флаг **-d** для запуска
> в фоновом режиме.

```shell
sudo docker compose -f docker-compose.yml up
```

Она сбилдит Docker образы и запустит backend, frontend, СУБД, Celery, Redis
и Nginx в отдельных Docker контейнерах.

По завершении всех операции проект будет запущен и доступен по адресу
http://localhost:8500/
</details>

## Изображения
<details>
  <summary>Изображения</summary>

![Подтверждение заявки](https://3.downloader.disk.yandex.ru/preview/fb8e635f6c4869df99c6f822eecfc14e4f9878b2b15e4942cef26c9941be4ea7/inf/yuFwiF96liWVl_ijYKRtgwrrF20y9Lx0RwLXGitCBNTdWxNtbHhRufen6fAr-AaNOqwRDZ17daZ7-8XZGTIJMA%3D%3D?uid=1003171957&filename=Снимок%20экрана%202024-05-27%20195021.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=1003171957&tknv=v2&size=1855x956)
![Ответ на обращение]()
</details>

## Авторы

**Данил Распопов**\
**Марат Ахметзянов**

Вы можете заглянуть в другие наши репозитории в наших профилях GitHub :)

[**Данил**](https://github.com/D-Nevskiy)  |
[**Марат**](https://github.com/kaedeMirai)
