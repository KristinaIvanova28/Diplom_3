from selenium.webdriver.common.by import By


class BasePageLocators:
    """
    Локаторы для базовой страницы, общие для всех страниц приложения
    """
    BUT_ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")  # Кнопка перехода в личный кабинет
    BUT_CONSTRUCTOR = (By.XPATH, ".//p[text()='Конструктор']")  # Кнопка перехода в конструктор бургеров
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers в хедере


class LoginPageLocators:
    """
    Локаторы для страницы авторизации пользователя
    """
    EMAIL_FIELD = (By.XPATH, ".//fieldset[1]//input")  # Поле ввода email для авторизации
    PASSWORD_FIELD = (By.XPATH, ".//fieldset[2]//input")  # Поле ввода пароля для авторизации
    BUT_ENTER = (By.XPATH, ".//button[text()='Войти']")  # Кнопка подтверждения авторизации
    BUT_REGISTER = (By.XPATH, ".//a[text()='Зарегистрироваться']")  # Ссылка перехода на страницу регистрации
    BUT_RECOVER_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")  # Ссылка восстановления пароля


class RegistrationPageLocators:
    """
    Локаторы для страницы регистрации нового пользователя
    """
    NAME_FIELD = (By.XPATH, ".//fieldset[1]//input")  # Поле ввода имени пользователя
    EMAIL_FIELD = (By.XPATH, ".//fieldset[2]//input")  # Поле ввода email пользователя
    PASSWORD_FIELD = (By.XPATH, ".//fieldset[3]//input")  # Поле ввода пароля пользователя
    BUT_REGISTER = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # Кнопка подтверждения регистрации
    BUT_ENTER = (By.XPATH, ".//a[text()='Войти']")  # Ссылка перехода на страницу авторизации
    ERROR_PASSWORD = (By.XPATH, ".//p[text()='Некорректный пароль']")  # Сообщение об ошибке валидации пароля


class ForgotPasswordPageLocators:
    """
    Локаторы для страницы восстановления забытого пароля
    """
    EMAIL_FIELD = (By.XPATH, ".//fieldset//input")  # Поле ввода email для восстановления пароля
    BUT_RECOVER = (By.XPATH, ".//button[text()='Восстановить']")  # Кнопка отправки запроса на восстановление
    BUT_ENTER = (By.XPATH, ".//a[text()='Войти']")  # Ссылка перехода на страницу авторизации


class MainPageLocators:
    """
    Локаторы для главной страницы приложения - конструктора бургеров
    """
    BUT_LOGIN_ACCOUNT = (By.XPATH, ".//button[text()='Войти в аккаунт']")  # Кнопка входа в аккаунт для неавторизованных пользователей
    BUT_MAKE_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка оформления заказа
    
    # Разделы конструктора ингредиентов
    SECTION_BUNS = (By.XPATH, ".//span[text()='Булки']/..")  # Вкладка раздела булок
    SECTION_SAUCES = (By.XPATH, ".//span[text()='Соусы']/..")  # Вкладка раздела соусов
    SECTION_FILLINGS = (By.XPATH, ".//span[text()='Начинки']/..")  # Вкладка раздела начинок
    
    ACTIVE_SECTION = (By.CLASS_NAME, "tab_tab_type_current__2BEPc")  # Активная вкладка раздела
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # Затемняющий оверлей модальных окон
    LINK_ORDER_FEED = (By.XPATH, "//a[p[text()='Лента Заказов']]")  # Ссылка перехода в ленту заказов
    LINK_CONSTRUCT = (By.XPATH, "//a[p[text()='Конструктор']]")  # Ссылка перехода в конструктор
    BUN_KRATOR = (By.XPATH, "//a[p[text()='Краторная булка N-200i']]")  # Ингредиент "Краторная булка"
    POS_TOP_BASKET = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")  # Верхняя позиция в корзине конструктора
    COUNTER_BUN = (By.XPATH, "//p[text()='Краторная булка N-200i']/ancestor::a//p[contains(@class, 'counter_counter__num')]")  # Счетчик добавленных булок
    BUT_ORDER = (By.XPATH, ".//button[text()='Оформить заказ']")  # Кнопка оформления заказа (дублирует BUT_MAKE_ORDER)



class IngredientLocators:
    """
    Локаторы для модального окна с детальной информацией об ингредиенте
    """
    WINDOW_MODAL_ING = (By.XPATH, "//div[contains(@class, 'Modal_modal__container__')]")  # Контейнер модального окна ингредиента
    BUTTON_CLOSE_MODAL_ING = (By.XPATH, "//button[contains(@class, 'Modal_modal__close__')]")  # Кнопка закрытия модального окна
    
    # Детальная информация об ингредиенте
    INGREDIENT_MODAL_TITLE = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title__')]")  # Название ингредиента
    INGREDIENT_MODAL_IMAGE = (By.XPATH, "//img[contains(@class, 'Modal_modal__image__')]")  # Изображение ингредиента
    INGREDIENT_MODAL_CALORIES = (By.XPATH, "//p[contains(text(), 'Калории')]/following-sibling::p")  # Значение калорий
    INGREDIENT_MODAL_PROTEINS = (By.XPATH, "//p[contains(text(), 'Белки')]/following-sibling::p")  # Значение белков
    INGREDIENT_MODAL_FAT = (By.XPATH, "//p[contains(text(), 'Жиры')]/following-sibling::p")  # Значение жиров
    INGREDIENT_MODAL_CARBS = (By.XPATH, "//p[contains(text(), 'Углеводы')]/following-sibling::p")  # Значение углеводов


class OrderFeedLocators:
    """
    Локаторы для страницы ленты заказов
    """
    ORDERS_FEED_SECTION = (By.XPATH, ".//h1[text()='Лента заказов']")  # Заголовок раздела ленты заказов
    ORDER_CARD = (By.CLASS_NAME, "OrderHistory_listItem__2x95r")  # Карточка отдельного заказа
    ORDER_NUMBER = (By.CLASS_NAME, "OrderHistory_textBox__3lgbs")  # Номер заказа в карточке
    ORDER_STATUS = (By.CLASS_NAME, "OrderHistory_status__2NlHv")  # Статус заказа в карточке
    
    # Счетчики выполненных заказов
    COUNTER_TOTAL = (By.XPATH, ".//p[contains(text(),'Выполнено за все время')]/following-sibling::p")  # Счетчик за все время
    COUNTER_TODAY = (By.XPATH, ".//p[contains(text(),'Выполнено за сегодня')]/following-sibling::p")  # Счетчик за сегодня
    
    # Модальное окно с деталями заказа
    ORDER_MODAL = (By.CLASS_NAME, "Modal_modal__container__2pkLh")  # Контейнер модального окна заказа
    ORDER_MODAL_NUMBER = (By.CLASS_NAME, "Modal_title__2NlHv")  # Номер заказа в модальном окне
    ORDER_MODAL_STATUS = (By.CLASS_NAME, "Modal_status__2NlHv")  # Статус заказа в модальном окне
    ORDER_MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[@aria-label='Закрыть модальное окно']")  # Кнопка закрытия модального окна
    
    # Раздел "В работе"
    IN_PROGRESS_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__')]/li")  # Список заказов в работе
    IN_PROGRESS_ORDER_NUMBER = (By.XPATH, ".//p[contains(@class, 'digits')]")  # Номера заказов в работе
    IN_PROGRESS_SECTION = (By.XPATH, ".//div[contains(text(), 'В работе')]")  # Заголовок раздела "В работе"


class SuccessOrderModalLocators:
    """
    Локаторы для модального окна успешно созданного заказа
    """
    ORDER_SUCCESS_MODAL = (By.XPATH, "//p[contains(text(), 'Ваш заказ начали готовить')]")  # Сообщение о начале приготовления
    ORDER_SUCCESS_ICON = (By.XPATH, "//img[@alt='идентификатор заказа']")  # Иконка идентификатора заказа
    ORDER_SUCCESS_MESSAGE = (By.XPATH, "//p[contains(text(), 'Дождитесь готовности на орбитальной станции')]")  # Дополнительное сообщение
    BUTTON_CLOSE_MODAL_ORDER = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")  # Кнопка закрытия модального окна
    LOADING_ANIMATION = (By.XPATH, "//img[contains(@src, 'loading.89540200')]")  # Анимация загрузки
    ORDER_SUCCESS_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq') and contains(@class, 'digits-large mb-8')]")  # Номер созданного заказа