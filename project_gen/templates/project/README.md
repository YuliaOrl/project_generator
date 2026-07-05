# Project Templates

### :green_book: Описание проекта
Проект является шаблоном для генерации структуры проекта с использованием cookiecutter

### :hammer_and_wrench: Стек 
* Язык программирования: **Python**

### :open_file_folder: Структура сгенерированного проекта

```
python/
└── checkers/                     # Пакет с проверками методов
    └── http_checkers.py          # чекер для проверки статус кода
├── clients                       # Пакет с базовыми клиентами
    └── http                      # Папка с http клиентами
├── config                        # Конфигурационные файлы
├── helpers                       # Пакет с классами помощниками и фасадами
├── services                      # Пакет с конфигурацией фасадов для сервисов         
├── tests                         # Папка для хранения тестов
    ├── functional                # Функциональные тесты 
    ├── smoke                     # Смок тесты 
    └── conftest.py               # Формирование фикстур
├── .gitignore                    # Стандартный файл для игнорирования файлов для загрузки в репозиторий
├── .gitlab-ci.yml                # Файл для подключения проекта к пайплайну в GitLab
├── .pre-commit-config.yaml       # Файл с настройками для пре-коммит хуков
├── bot.py                        # Файл с ботом отправки отчета о тестировании в Телеграм
├── Dockerfile                    # Файл с настройками Докер
├── mypy.ini                      # Файл конфигурации линтера mypy
├── pyproject.toml                # Файл с зависимостями poetry
└── README.md                     # Файл с описанием репозитория для тестов
├── swagger-coverage-config-{{cookiecutter.project_slug}}.json   # Файл конфигурации для снятия покрытия сервиса тестами
└── telegram-notifier-config.ini  # Файл с настройками бота для Телеграм
```

### :running_woman: Запуск генерации структуры проекта
Установить cookiecutter:

```bash
pip install cookiecutter
```

Чтобы создать новый проект на основе этого шаблона, выполнить команду:

```bash
cookiecutter https://github.com/YuliaOrl/template-project user_email="your_email@example.com" authors="Your_Name" project_name="Project_Name"
```
