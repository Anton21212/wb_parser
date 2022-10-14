# WB PARSER

Приложение для парснга карточек товаров с Wildberries.

## Установка

1. Склонировать репозиторий с помощью команды:

```shell
git clone https://github.com/Anton21212/wb_parser.git
```

2. Перейти в папку проекта.

## Запуск

Если установлена утилита командной строки `make`:

```shell
sudo make up
```

Если не установлена утилита командной строки `make`:

```shell
sudo docker-compose -p "wb_parser" --file "docker-compose.yml" up --build
```

## Использование

Для парсинга карточек товаров используется эндпоинт `http://localhost/api/v1/get_cards_info/`. Для обращения к нему
нужно выполнять `POST` запросы.

Принимаемые параметры:

- `articles_file`: xlsx файл
- `article`: целое число

⚠️За один запрос принимается только один из параметров.

Успешным результатом работы API является возврат данных о бренде, названии товара и артикуле в JSON формате.

Примеры ответов:

- При передаче параметра `article`:

```json
{
  "article": 123,
  "brand": "brand",
  "title": "Title"
}
```

- При передаче параметра `articles_file`:

```json
[
  {
    "article": 1,
    "brand": "Brand1",
    "title": "Title1"
  },
  {
    "article": 2,
    "brand": "Brand2",
    "title": "Title2"
  }
]
```

## Автор

Васильев Антон Юрьевич

sortof00@mail.ru
