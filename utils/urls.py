class URL:
    # страницы сайта
    MAIN_PAGE = 'https://stellarburgers.nomoreparties.site/' # URL главной страницы
    LOGIN_PAGE = f'{MAIN_PAGE}login' # URL страницы авторизации
    ORDER_PAGE = f'{MAIN_PAGE}feed' # URL страницы "Лента заказов"

    # ручки для API
    REGISTER_USER_URL = f'{MAIN_PAGE}api/auth/register' # POST - создание пользователя
    USER_URL = f'{MAIN_PAGE}api/auth/user' # GET/PATCH - получение и обновление инфо о пользователе