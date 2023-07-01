# newtinder

## Backend для приложения знакомств.

##  Автор: Дерябин Евгений

### Requirements
- Dj-rest-auth==1.1.0
- Django==3.1.14
- Django-allauth==0.42.0
- Django-filter==21.1
- Djangorestframework==3.11.2
- Drf-yasg==1.17.1
- Pillow==9.5.0

## Deploy on Back4App

## Тестирование

1. Регистрация нового клиента: https://newtinder-deriabin1985.b4a.run/api/clients/create/registration/. 
2. Личный кабинет для заполнения профиля (аватар, имя, фамилия, гендер): https://newtinder-deriabin1985.b4a.run/api/client/{id}/
3. На аватар наносится водяной знак с помощью Pillow через переопределение метода save в модели.
4. Список всех клиентов с функцией фильтра: https://newtinder-deriabin1985.b4a.run/api/list/
5. Для лайка: https://newtinder-deriabin1985.b4a.run/api/clients/4/match/ если лайк взаимный отправляется письмо на оба адреса.
6. Документация: https://newtinder-deriabin1985.b4a.run/swagger/ и https://newtinder-deriabin1985.b4a.run/redoc/
