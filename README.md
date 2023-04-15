# README

## Описание

Это инструкция по созданию REST API для управления закупами, продажами и расчета прибыли с учетом себестоимости по методу FIFO.

## Реализация

1. Создание моделей:
   1.1. Создание модели Purchase
   В файле models.py:

   - Создайте класс Purchase, который наследуется от models.Model.
   - Добавьте поле quantity с типом models.PositiveIntegerField.
   - Добавьте поле price с типом models.DecimalField и параметрами max_digits и decimal_places.
   - Добавьте поле date с типом models.DateTimeField.
   1.2. Создание модели Sale  
   В файле models.py:

   - Создайте класс Sale, который наследуется от models.Model.
   - Добавьте поле quantity с типом models.PositiveIntegerField.
   - Добавьте поле price с типом models.DecimalField и параметрами max_digits и decimal_places.
   - Добавьте поле date с типом models.DateTimeField.
   
2. Создание сериализаторов:
   2.1. Создание сериализатора PurchaseSerializer
   В файле serializers.py:

    - Создайте класс PurchaseSerializer, который наследуется от serializers.ModelSerializer.
    - Укажите класс модели Purchase в атрибуте Meta.model.
    - Укажите поля для сериализации в атрибуте Meta.fields: ('id', 'quantity', 'price', 'date').
   
   2.2. Создание сериализатора SaleSerializer
   В файле serializers.py:

   - Создайте класс SaleSerializer, который наследуется от serializers.ModelSerializer.
   - Укажите класс модели Sale в атрибуте Meta.model.
   - Укажите поля для сериализации в атрибуте Meta.fields: ('id', 'quantity', 'price', 'date').

3. Создание view-функций:
   3.1. Создание CRUD view-функций для модели Purchase
   В файле views.py:

   - Создайте классы PurchaseListCreate, PurchaseRetrieveUpdateDestroy, наследуясь соответственно от generics.ListCreateAPIView и generics.RetrieveUpdateDestroyAPIView.
   - Укажите класс модели Purchase в атрибуте queryset.
   - Укажите класс сериализатора PurchaseSerializer в атрибуте serializer_class.
   
   3.2. Создание CRUD view-функций для модели Sale
   
   В файле views.py:

   - Создайте классы SaleListCreate, SaleRetrieveUpdateDestroy, наследуясь соответственно от generics.ListCreateAPIView и generics.RetrieveUpdateDestroyAPIView.
   - Укажите класс модели Sale в атрибуте queryset.
   - Укажите класс сериализатора SaleSerializer в атрибуте serializer_class.
   - 3.3. Создание функции для подсчета прибыли с учетом себестоимости по методу FIFO
   
   В файле views.py:
   
   - Создайте класс ProfitFIFO, который наследуется от generics.GenericAPIView.
   - Укажите классы моделей Purchase и Sale в атрибуте queryset.
   - Создайте функцию get:
   - Получите список всех закупок, отсортированный по дате.
   - Получите список всех продаж, отсортированный по дате.
   - Используйте алгоритм FIFO для расчета прибыли с учетом себестоимости продаж.
   - Верните общую прибыль в виде JSON-ответа.

4. Создание маршрутов:

   В файле urls.py:

   Импортируйте все созданные view-функции.
   Добавьте пути для каждой view-функции:
   - path('purchases/', PurchaseListCreate.as_view(), name='purchase-list-create')
   - path('purchases/<int:pk>/', PurchaseRetrieveUpdateDestroy.as_view(), name='purchase-retrieve-update-destroy')
   - path('sales/', SaleListCreate.as_view(), name='sale-list-create')
   - path('sales/<int:pk>/', SaleRetrieveUpdateDestroy.as_view(), name='sale-retrieve-update-destroy')
   - path('profit-fifo/', ProfitFIFO.as_view(), name='profit-fifo')


5. Миграции:

   - Запустите миграции для создания таблиц в базе данных: `python manage.py makemigrations` и `python manage.py migrate`.

6. Работа с API:

   - Используйте HTTP-методы для выполнения операций с закупами и продажами:
     - POST для создания объектов.
     - PUT или PATCH для редактирования объектов.
     - DELETE для удаления объектов.
     - GET для просмотра объектов.
   - Создайте отдельный endpoint для подсчета прибыли с учетом себестоимости по методу FIFO.

7. Тестирование:

   - Протестируйте каждый из созданных эндпоинтов для проверки корректности работы REST API.

8. Документация:

   - Подготовьте документацию для вашего API, указав названия эндпоинтов, параметров и ответов.

После выполнения всех шагов вы должны получить работающее REST API, с которым можно взаимодействовать для управления закупами, продажами и расчета прибыли с учетом себестоимости по методу FIFO.
