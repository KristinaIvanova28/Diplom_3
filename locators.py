from selenium.webdriver.common.by import By


class LoginPageLocators:

    EMAIL = (By.XPATH, "//label[text()='Email']/following-sibling::input") # поле ввода Имейл
    PASSWORD = (By.NAME, "Пароль") # поле ввода Пароль
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']") # кнопка Войти в форме авторизации

class MainPageLocators:
    # Кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")  # кнопка-ссылка Конструктор в хедере
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")  # кнопка-ссылка Лента Заказов в хедере

    # Ингредиенты
    FLUORESCENT_BUN = (By.XPATH, ".//*[text()='Флюоресцентная булка R2-D3']")  # карточка ингредиента Флюоресцентная булка R2-D3
    INGREDIENT_COUNTER = (By.XPATH, ".//*[@class='counter_counter__num__3nue1']")  # счетчик количества выбранного ингредиента

    # Модальное окно
    MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")  # модальное окно с деталями ингредиента
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")  # кнопка закрытия модального окна (крестик)
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # оверлей за модальным окном
    OVERLAY_ANIMATION = (By.XPATH, "//img[@alt ='loading animation']")
    MODAL_CONTENT_BOX = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")

    # Корзина
    BASKET_LIST = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")  # область верхней булки в конструкторе заказа

    # Оформление заказа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка Оформить заказ
    ORDER_ID = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")  # номер заказа в модальном окне

class OrderPageLocators:
    # Счётчики
    TOTAL_ORDERS = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")  # счётчик Выполнено за всё время
    TODAY_ORDERS = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")  # счётчик Выполнено за сегодня

    IN_PROGRESS_ORDERS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li") # номера заказов в общей ленте
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # оверлей за модальным окном