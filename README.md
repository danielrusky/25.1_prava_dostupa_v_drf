# Разработка LMS-системы
_SPA (Single Page Application) веб-приложение_

Проект представляет собой разработку LMS-системы (Learning Management System), в которой пользователи могут размещать свои полезные материалы или курсы.
Результатом создания проекта будет бэкенд-сервер, который будет возвращать клиенту JSON-структуры.


# Разработка LMS-системы
_SPA (Single Page Application) веб-приложение_

Проект представляет собой разработку LMS-системы (Learning Management System), в которой пользователи могут размещать свои полезные материалы или курсы.
Результатом создания проекта будет бэкенд-сервер, который будет возвращать клиенту JSON-структуры.

### Описание домашних заданий:

<details>
<summary>Домашка №1</summary>
<br>
Условия домашки
Контекст: зачем решать подобные задачи

В мире развивается тренд на онлайн-обучение. Но для веб-разработчика важно не только обучиться, но и знать, как реализовать платформу для онлайн-обучения. Поэтому новая задача касается разработки LMS-системы, в которой каждый желающий может размещать свои полезные материалы или курсы.

Ранее в проектах мы могли сразу видеть визуальное отображение результата разработки, теперь работа будет над SPA веб-приложением и результатом создания проекта будет бэкенд-сервер, который возвращает клиенту JSON-структуры.

Критерий выполнения задания
Результат задания залили в github.com и сдали в виде ссылки на репозиторий.
Не забудьте добавить .gitignore и файл с зависимостями проекта

Задание 1
Создайте новый Django-проект, подключите DRF в настройках проекта.

Задание 2
Создайте следующие модели:

Пользователь:
все поля от обычного пользователя, но авторизацию заменить на email;
телефон;
город;
аватарка.
Модель пользователя разместите в приложении users

Курс:
название,
превью (картинка),
описание.
Урок:
название,
описание,
превью (картинка),
ссылка на видео.
Урок и курс - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков. Реализуйте связь между ними.

Модель курса и урока разместите в отдельном приложении. Название для приложения выбирайте такое, чтобы оно описывало то, с какими сущностями приложение работает. Например, lms или materials - отличные варианты.

Задание 3
Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса используйте Viewsets, а для урока - Generic-классы.

Для работы контроллеров опишите простейшие сериализаторы.

При реализации CRUD для уроков реализуйте все необходимые операции (получение списка, получение одной сущности, создание, изменение и удаление).

Для работы контроллеров опишите простейшие сериализаторы.

Работу каждого эндпоинта необходимо проверять с помощью Postman.

Также на данном этапе работы мы не заботимся о безопасности и не закрываем от редактирования объекты и модели даже самой простой авторизацией.

* Дополнительное задание
Реализуйте эндпоинт для редактирования профиля любого пользователя на основе более привлекательного подхода для личного использования: Viewset или Generic.

Дополнительное задание, помеченное звездочкой, желательно, но не обязательно выполнять.
</details>


<details>
<summary>Домашка №2</summary>
<br>
ЗДЕСЬ МОГЛА БЫТЬ ВАША ДОМАШКА ☺☻☺
</details>


<details>
<summary>Домашка №3</summary>
<br>
ЗДЕСЬ МОГЛА БЫТЬ ВАША ДОМАШКА ☺☻☺
</details>


<details>
<summary>Домашка №4</summary>
<br>
ЗДЕСЬ МОГЛА БЫТЬ ВАША ДОМАШКА ☺☻☺
</details>


<details>
<summary>Домашка №5</summary>
<br>
ЗДЕСЬ МОГЛА БЫТЬ ВАША ДОМАШКА ☺☻☺
</details>


<details>
<summary>Домашка №6</summary>
<br>
ЗДЕСЬ МОГЛА БЫТЬ ВАША ДОМАШКА ☺☻☺
</details>
