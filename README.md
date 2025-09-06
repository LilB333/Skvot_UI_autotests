**Skvot UI Autotests** - это проект автоматизированного тестирования UI для веб-сайта **skvot.com**, магазина по продаже товаров для скейбординга.

## 🚀 Технологический стек

- **Python 3.11+** - язык программирования
- **Pytest** - фреймворк для тестирования
- **Selenium WebDriver** - автоматизация браузера
- **Allure Framework** - создание отчетов о тестировании
- **Pytest-ordering** - управление порядком выполнения тестов
- **WebDriver Manager** - автоматическое управление драйверами браузера

## 📦 Установка и настройка

### Предварительные требования

1. Установите Python 3.11 или выше
2. Установите Git
3. Установите Allure

### Клонирование репозитория

```bash
git clone https://github.com/LilB333/Skvot_UI_autotests.git
cd Skvot_UI_autotests
```

### Создание виртуального окружения и активация

```bash
python -m venv venv
venv\Scripts\activate
```

### Установка зависимостей

```bash
pip install -r requirements.txt
```

## 🏃 Запуск тестов

### Запуск всех тестов

```bash
pytest
```

### Запуск тестов с генерацией Allure отчетов

```bash
pytest --alluredir=allure-results
```

### Просмотр Allure отчета

```bash
allure serve allure-results
```

### Запуск конкретного тестового файла

```bash
pytest tests/ui/test_login.py
```

## 📁 Структура проекта

```
Skvot_UI_autotests/
├── tests/
│   ├── ui/                    # UI тесты
│       ├── test_login.py      # Тесты авторизации
│       └── test_search_product.py  # Тесты для поиска продукта
│       └── test_add_product_to_cart.py  # Тесты по добавлению продукта в корзину
│       └── test_product_page.py  # Тесты страницы продукта
│       └── test_cart_page.py  # Тесты страницы корзины
│       └── test_fill_shipping_info.py  # Тесты заполнения информации для отправки товара
│       └── test_buy_product.py  # Тесты по покупке товара от выбора до заполнения информации для отправки
│       └── conftest.py           # Фикстуры pytest для инициализации драйвера
├── pages/                    # Page Object Model
│   ├── main_page.py         # Главная страница
│   ├── product_page.py        # Страница продукта
│   └── cart_page.py    # Страница корзины
├── utils/                   # Вспомогательные утилиты
│   └── logger.py     # Класс для создания файлов логов
├── base/                   # Базовые действия на странице
│   └── base_class.py     # Класс для базовых действий на странице - получение url, сверка значений, скриншоты
├── test_results/          # Файлы отчетов Allure (генерируются по инструкции)
├── requirements.txt         # Зависимости Python
└── screen/              # Скриншоты тестов
└── logs/              # Логи тестов
```


## 🎯 Особенности реализации

### Управление порядком тестов

Тесты используют `pytest-ordering` для контроля последовательности выполнения:

```python
@pytest.mark.run(order=1)
class TestLogin:
    def test_login_valid(self, set_up):
        # тестовый код
```

### Page Object Pattern

Реализован паттерн Page Object для улучшения поддерживаемости кода:

```python
class CartPage:
     def check_product_info(self, text, n):
        ...
    def check_total_cart_sum(self, total_sum):
        ...
```

### Автоматическое управление драйверами

Используется `webdriver-manager` для автоматической загрузки драйверов:

```python
from webdriver_manager.chrome import ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
```

## 📊 Отчетность

Проект использует Allure Framework для детальной отчетности:
- Графические отчеты о выполнении тестов
- Подробная информация о каждом шаге теста
- История выполнения тестов

## 🤝 Вклад в проект

1. Форкните репозиторий
2. Создайте feature ветку (`git checkout -b feature/amazing-feature`)
3. Закоммитьте изменения (`git commit -m 'Add amazing feature'`)
4. Запушьте ветку (`git push origin feature/amazing-feature`)
5. Откройте Pull Request
