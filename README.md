# Diplom_3Дипломный проект. Задание 3: Автотесты для UI

Студентка: Иванова Кристина

Когорта: 26

Автотесты для сервиса Stellar Burgers

Проект реализован по паттерну Page Object.

Каждая страница сайта имеет свой класс с методами и локаторами.

Протестировано в Google Chrome и Mozilla Firefox.

Ссылки

🍔 Сайт Stellar Burgers
🔧 API-документация
 Структура проекта

 tests — папка с UI автотестами
conftest.py — основные фикстуры
test_main_page.py — тесты основной функциональности (навигация, модальные окна, счетчики ингредиентов)
test_order_feed.py — тесты страницы "Лента заказов" (счетчики, отображение заказов)
 pages — папка с Page Object'ами
base_page.py — базовый класс для работы с веб-элементами
main_page.py — Page Object для главной страницы (Конструктор)
order_page.py — Page Object для страницы "Лента заказов"
login_page.py — Page Object для страницы авторизации/регистрации
 locators.py — файл с локаторами элементов для всех страниц
 utils — вспомогательные модули
generators.py — генераторы тестовых данных
urls.py — URL и эндпоинты API
 requirements.txt — зависимости
allure-results — папка с результатами Allure (генерируется при запуске)

 Инструкция по запуску:

1. Установите зависимости:
pip install -r requirements.txt

2. Запустить все тесты и записать отчет:
pytest --alluredir=./allure-results

Описание реализованных тестов

✅ test_main_page.py

test_click_on_constructor_button_redirects_to_constructor_page

Проверяет переход на главную страницу (Конструктор) при клике на ссылку "Конструктор".

test_click_on_feed_button_redirects_to_feed_page

Проверяет переход на страницу "Лента заказов" при клике на соответствующую ссылку.

test_click_on_ingredient_opens_modal_window

Проверяет, что при клике на ингредиент открывается модальное окно с деталями.

test_close_modal_window_with_close_button

Проверяет, что модальное окно с деталями ингредиента закрывается по клику на крестик.

test_ingredient_counter_increases_by_using_drag_and_drop

Проверяет, что счетчик ингредиента увеличивается после его добавления в заказ методом drag-and-drop.

 ✅ test_order_feed.py

test_upgrade_counter_orders

Проверяет, что счетчики "Выполнено за всё время" и "за сегодня" увеличиваются после создания заказа.

test_visible_order_number_in_progress

Проверяет, что номер нового заказа появляется в разделе "В работе" на странице "Лента заказов".