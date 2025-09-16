# 🍔 Stellar Burgers — Автотесты для UI

**Студент:** Иванова Кристина  
**Когорта:** 27

Дипломный проект по автоматизации тестирования UI для сервиса Stellar Burgers.

---

## 🔗 Ссылки

- [Официальный сайт Stellar Burgers](https://stellarburgers.nomoreparties.site/)
- [API документация](https://code.s3.yandex.net/qa-automation-engineer/python/teach/docs/index.html)

---

## 🏗️ Архитектура проекта

Проект реализован с использованием паттерна **Page Object Model**.

tests/
├── conftest.py # Фикстуры и настройки
├── test_main_page.py # Тесты основной функциональности
└── test_order_feed.py # Тесты ленты заказов

pages/
├── base_page.py # Базовый класс страницы
├── main_page.py # Главная страница (Конструктор)
├── order_page.py # Лента заказов
└── login_page.py # Страница авторизации

locators.py # Локаторы элементов
utils/
├── generators.py # Генераторы тестовых данных
└── urls.py # URL и эндпоинты API

requirements.txt # Зависимости проекта
allure-results/ # Отчеты Allure (генерируется)


---

## 🧪 Реализованные тесты

### 📋 Основная функциональность (`test_main_page.py`)

| Тест | Описание |
|------|----------|
| `test_click_on_constructor_button_redirects_to_constructor_page` | Переход на главную страницу через кнопку "Конструктор" |
| `test_click_on_feed_button_redirects_to_feed_page` | Переход на страницу "Лента заказов" |
| `test_click_on_ingredient_opens_modal_window` | Открытие модального окна с деталями ингредиента |
| `test_close_modal_window_with_close_button` | Закрытие модального окна крестиком |
| `test_ingredient_counter_increases_by_using_drag_and_drop` | Увеличение счетчика ингредиента через drag-and-drop |

### 📊 Лента заказов (`test_order_feed.py`)

| Тест | Описание |
|------|----------|
| `test_upgrade_counter_orders` | Проверка увеличения счетчиков выполненных заказов |
| `test_visible_order_number_in_progress` | Отображение номера заказа в разделе "В работе" |

---

## 🚀 Запуск тестов

### 1. Установка зависимостей
```bash
pip install -r requirements.txt

### 2. Запуск тестов с генерацией отчета
```bash
pytest --alluredir=./allure-results

### 3. Просмотр отчета Allure
```bash
allure serve allure-results

🛠️ Технологии

Python + pytest — фреймворк для тестирования
Selenium WebDriver — автоматизация браузера
Allure — система отчетности
Page Object Pattern — архитектура проекта

🌐 Поддержка браузеров

✅ Google Chrome
✅ Mozilla Firefox
