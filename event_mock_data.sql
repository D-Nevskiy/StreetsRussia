-- Вставка данных в таблицу UserAccount
INSERT INTO user_useraccount (id, role, status, first_name, last_name, middle_name, gender, date_of_birth, phone_number, email, city, passport_series, passport_number, passport_issue_date, passport_issued_by, consent_to_rights, сonsent_to_processing, password, created_at, updated_at)
VALUES
('c9b9b630-5656-4a61-9c85-efb4a1a3e853', 'USER', 'CONFIRMED', 'Алексей', 'Иванов', '', 'MALE', '1990-01-01', '+79822624975', 'alexey@example.com', 'Москва', '4315', '123457', '2010-01-01', 'ОУФМС РОССИИ ПО МОСКВЕ', true, true, 'hashed_password', now(), now()),
('c9b9b630-5656-4a61-9c85-efb4a1a3e854', 'USER', 'CONFIRMED', 'Мария', 'Петрова', '', 'FEMALE', '1992-02-02', '+79822624978', 'maria@example.com', 'Санкт-Петербург', '4316', '654322', '2012-02-02', 'ОУФМС РОССИИ ПО САНКТ-ПЕТЕРБУРГУ', true, true, 'hashed_password', now(), now()),
('c9b9b630-5656-4a61-9c85-efb4a1a3e855', 'USER', 'CONFIRMED', 'Иван', 'Сидоров', '', 'MALE', '1985-03-15', '+79822624976', 'ivan@example.com', 'Нижний Новгород', '4317', '987654', '2011-03-15', 'ОУФМС РОССИИ ПО НИЖНЕМУ НОВГОРОДУ', true, true, 'hashed_password', now(), now()),
('c9b9b630-5656-4a61-9c85-efb4a1a3e856', 'USER', 'CONFIRMED', 'Ольга', 'Смирнова', '', 'FEMALE', '1991-04-25', '+79822624979', 'olga@example.com', 'Екатеринбург', '4318', '876543', '2012-04-25', 'ОУФМС РОССИИ ПО ЕКАТЕРИНБУРГУ', true, true, 'hashed_password', now(), now()),
('c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'REGIONAL_DIRECTOR', 'CONFIRMED', 'Анна', 'Кузнецова', '', 'FEMALE', '1987-06-05', '+79822624980', 'anna@example.com', 'Москва', '4319', '123459', '2010-06-05', 'ОУФМС РОССИИ ПО МОСКВЕ', true, true, 'hashed_password', now(), now()),
('c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'REGIONAL_DIRECTOR', 'CONFIRMED', 'Сергей', 'Лебедев', '', 'MALE', '1993-07-15', '+79822624981', 'sergey@example.com', 'Санкт-Петербург', '4320', '654324', '2012-07-15', 'ОУФМС РОССИИ ПО САНКТ-ПЕТЕРБУРГУ', true, true, 'hashed_password', now(), now());

-- Вставка данных в таблицу Discipline
INSERT INTO events_discipline (id, name, created_at, updated_at)
VALUES 
(1, 'Танцы', now(), now()),
(2, 'Музыка', now(), now()),
(3, 'Спорт', now(), now()),
(4, 'Искусство', now(), now());

-- Вставка данных в таблицу SubDiscipline
INSERT INTO events_subdiscipline (id, name, discipline_id, created_at, updated_at)
VALUES 
-- Танцы
(1, 'Хип-хоп', 1, now(), now()),
(2, 'Брейкинг', 1, now(), now()),
(3, 'Топрок', 1, now(), now()),
(4, 'Даунрок', 1, now(), now()),
(5, 'Дабстеп', 1, now(), now()),
(6, 'Электро', 1, now(), now()),
(7, 'Локинг', 1, now(), now()),
(8, 'Поппинг', 1, now(), now()),
(9, 'Хаус', 1, now(), now()),
(10, 'Фанк', 1, now(), now()),

-- Музыка
(11, 'Рэп', 2, now(), now()),
(12, 'Эмсиинг', 2, now(), now()),
(13, 'Диджеинг', 2, now(), now()),
(14, 'Скретчинг', 2, now(), now()),
(15, 'Сэмплирование', 2, now(), now()),
(16, 'Тёрнтеблизм', 2, now(), now()),
(17, 'Битмейкинг', 2, now(), now()),
(18, 'Битбокс', 2, now(), now()),

-- Искусство
(19, 'Граффити', 4, now(), now()),
(20, 'Постеры', 4, now(), now()),
(21, 'Каллиграфия', 4, now(), now()),
(22, 'Тэггинг', 4, now(), now()),
(23, 'Павербомбинг', 4, now(), now()),
(24, 'Трафареты', 4, now(), now()),
(25, 'Скульптурные инсталляции', 4, now(), now()),

-- Спорт
(26, 'Паркур', 3, now(), now()),
(27, 'Воркаут', 3, now(), now()),
(28, 'Фриран', 3, now(), now()),
(29, 'Трикинг', 3, now(), now()),
(30, 'Скейтбординг', 3, now(), now()),
(31, 'БМХ', 3, now(), now()),
(32, 'БМХ Флэт', 3, now(), now()),
(33, 'Скут', 3, now(), now()),
(34, 'Стритбол', 3, now(), now()),
(35, 'Лонгбординг', 3, now(), now()),
(36, 'Джимбар', 3, now(), now()),
(37, 'Дрифт', 3, now(), now()),
(38, 'Драг', 3, now(), now()),
(39, 'Стант', 3, now(), now()),
(40, 'Панна', 3, now(), now()),
(41, 'МТВ', 3, now(), now()),
(42, 'Агрессив Верт', 3, now(), now()),
(43, 'Агрессив Стрит', 3, now(), now()),
(44, 'Стритбординг', 3, now(), now()),
(45, 'Слэклайн', 3, now(), now()),
(46, 'Триклайн', 3, now(), now()),
(47, 'Хайлайн', 3, now(), now());

-- Вставка данных в таблицу Region
INSERT INTO events_region (id, name, owner_id, code, created_at, updated_at)
VALUES
(1, 'Москва', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-MOW', now(), now()),
(2, 'Санкт-Петербург', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-SPE', now(), now()),
(3, 'Ненецкий АО', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-NEN', now(), now()),
(4, 'Ярославская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-YAR', now(), now()),
(5, 'Челябинская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-CHE', now(), now()),
(6, 'Ульяновская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-ULY', now(), now()),
(7, 'Тюменская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-TYU', now(), now()),
(8, 'Тульская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-TUL', now(), now()),
(9, 'Свердловская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-SVE', now(), now()),
(10, 'Рязанская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-RYA', now(), now()),
(11, 'Орловская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-ORL', now(), now()),
(12, 'Омская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-OMS', now(), now()),
(13, 'Новгородская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-NGR', now(), now()),
(14, 'Липецкая область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-LIP', now(), now()),
(15, 'Курская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-KRS', now(), now()),
(16, 'Курганская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-KGN', now(), now()),
(17, 'Калининградская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-KGD', now(), now()),
(18, 'Ивановская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-IVA', now(), now()),
(19, 'Брянская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-BRY', now(), now()),
(20, 'Астраханская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-AST', now(), now()),
(21, 'Хабаровский край', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-KHA', now(), now()),
(22, 'Чеченская Республика', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-CE', now(), now()),
(23, 'Удмуртская Республика', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-UD', now(), now()),
(24, 'Республика Северная Осетия — Алания', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-SE', now(), now()),
(25, 'Республика Мордовия', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-MO', now(), now()),
(26, 'Республика Карелия', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-KR', now(), now()),
(27, 'Республика Калмыкия', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-KL', now(), now()),
(28, 'Республика Ингушетия', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-IN', now(), now()),
(29, 'Республика Алтай', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-AL', now(), now()),
(30, 'Республика Башкортостан', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-BA', now(), now()),
(31, 'Республика Адыгея', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-AD', now(), now()),
(32, 'Республика Крым', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-CR', now(), now()),
(33, 'Севастополь', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-SEV', now(), now()),
(34, 'Республика Коми', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-KO', now(), now()),
(35, 'Кировская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-KIR', now(), now()),
(36, 'Камчатский край', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-KAM', now(), now()),
(37, 'Еврейская АО', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-JEW', now(), now()),
(38, 'Чукотский АО', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-CHU', now(), now()),
(39, 'Забайкальский край', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-ZAB', now(), now()),
(40, 'Бурятия', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-BU', now(), now()),
(41, 'Тыва', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-TY', now(), now()),
(42, 'Иркутская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-IRK', now(), now()),
(43, 'Амурская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-AMU', now(), now()),
(44, 'Томская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-TOM', now(), now()),
(45, 'Новосибирская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-NVS', now(), now()),
(46, 'Красноярский край', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-KYA', now(), now()),
(47, 'Хакасия', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-KK', now(), now()),
(48, 'Кемеровская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-KEM', now(), now()),
(49, 'Алтайский край', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-ALTAI', now(), now()),
(50, 'Сахалинская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-SAK', now(), now()),
(51, 'Приморский край', 'c9b9b630-5656-4a61-9c85-efb4a1a3e857', 'RU-PRI', now(), now()),
(52, 'Магаданская область', 'c9b9b630-5656-4a61-9c85-efb4a1a3e858', 'RU-MAG', now(), now());

-- Вставка данных в таблицу City
INSERT INTO events_city (id, name, region_id, created_at, updated_at)
VALUES 
(1, 'Архангельск', 1, now(), now()),
(2, 'Астрахань', 2, now(), now()),
(3, 'Барнаул', 11, now(), now()),
(4, 'Белгород', 12, now(), now()),
(5, 'Брянск', 19, now(), now()),
(6, 'Великий Новгород', 13, now(), now()),
(7, 'Владимир', 14, now(), now()),
(8, 'Волгоград', 15, now(), now()),
(9, 'Воронеж', 16, now(), now()),
(10, 'Екатеринбург', 9, now(), now()),
(11, 'Иваново', 18, now(), now()),
(12, 'Ижевск', 22, now(), now()),
(13, 'Иркутск', 48, now(), now()),
(14, 'Йошкар-Ола', 27, now(), now()),
(15, 'Казань', 28, now(), now()),
(16, 'Калининград', 17, now(), now()),
(17, 'Кострома', 29, now(), now()),
(18, 'Краснодар', 30, now(), now()),
(19, 'Красноярск', 51, now(), now()),
(20, 'Курск', 15, now(), now()),
(21, 'Липецк', 14, now(), now()),
(22, 'Москва', 1, now(), now()),
(23, 'Мурманск', 30, now(), now()),
(24, 'Набережные Челны', 28, now(), now()),
(25, 'Нижний Новгород', 31, now(), now()),
(26, 'Новосибирск', 52, now(), now()),
(27, 'Омск', 12, now(), now()),
(28, 'Оренбург', 32, now(), now()),
(29, 'Пенза', 33, now(), now()),
(30, 'Пермь', 34, now(), now()),
(31, 'Псков', 35, now(), now()),
(32, 'Пятигорск', 36, now(), now()),
(33, 'Ростов-на-Дону', 37, now(), now()),
(34, 'Рязань', 10, now(), now()),
(35, 'Самара', 38, now(), now()),
(36, 'Санкт-Петербург', 2, now(), now()),
(37, 'Саратов', 39, now(), now()),
(38, 'Смоленск', 40, now(), now()),
(39, 'Сочи', 30, now(), now()),
(40, 'Ставрополь', 41, now(), now()),
(41, 'Тверь', 42, now(), now()),
(42, 'Тольятти', 38, now(), now()),
(43, 'Тула', 8, now(), now()),
(44, 'Ульяновск', 6, now(), now()),
(45, 'Уфа', 28, now(), now()),
(46, 'Хабаровск', 21, now(), now()),
(47, 'Чебоксары', 43, now(), now()),
(48, 'Челябинск', 5, now(), now()),
(49, 'Ярославль', 4, now(), now());

-- Вставка данных в таблицу TypeEvent
INSERT INTO events_typeevent (id, name, created_at, updated_at)
VALUES
(1, 'Соревнование', now(), now()),
(2, 'Фестиваль', now(), now()),
(3, 'Мастер-класс', now(), now()),
(4, 'Выставка', now(), now()),
(5, 'Встреча', now(), now());

-- Вставка данных в таблицу Location
INSERT INTO events_location (id, name, region_id, city_id, type_of_area, address, created_at, updated_at)
VALUES
(1, 'Скейт-парк Центрального парка', 1, 1, 'OPEN', '123 Парк-авеню', now(), now()),
(2, 'Скейт-парк Венис Бич', 2, 2, 'OPEN', '456 Пляжная дорога', now(), now()),
(3, 'Милленниум-парк', 3, 3, 'CLOSE', '789 Улица Парка', now(), now()),
(4, 'Дискавери Грин', 4, 4, 'OPEN', '101 Бульвар Грина', now(), now()),
(5, 'Парк Энканто', 5, 5, 'OPEN', '202 Парковая аллея', now(), now());

-- Вставка данных в таблицу Events
INSERT INTO events_event (id, title, description, start_datetime, end_datetime, discipline_id, sub_discipline_id, type_of_event_id, location_id, is_moderation, organizers_contact, author_id, count_entrant, created_at, updated_at)
VALUES
('a1b2c3d4-e5f6-4a3c-9a4b-983b9a1a3e06', 'Фестиваль дабстепа', 'Фестиваль для любителей дабстепа.', '2024-06-25 12:00:00', '2024-06-25 20:00:00', 1, 5, 2, 1, true, '{"email": "dubstepfest@festival.com", "phone": "123-456-7891"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e853', 200, now(), now()),
('b2c3d4e5-f6a7-4a3c-9a4b-983b9a1a3e07', 'Электро Баттл', 'Соревнование по электро танцам.', '2024-07-18 14:00:00', '2024-07-18 18:00:00', 1, 6, 1, 2, true, '{"email": "electrobattle@event.com", "phone": "234-567-8902"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 150, now(), now()),
('c3d4e5f6-a7b8-4a3c-9a4b-983b9a1a3e08', 'Фестиваль локинга', 'Фестиваль для любителей локинга.', '2024-08-12 16:00:00', '2024-08-12 22:00:00', 1, 7, 2, 3, true, '{"email": "lockingfest@festival.com", "phone": "345-678-9013"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e853', 300, now(), now()),
('d4e5f6a7-b8c9-4a3c-9a4b-983b9a1a3e09', 'Поппинг Шоу', 'Шоу с участием лучших танцоров поппинга.', '2024-09-10 10:00:00', '2024-09-10 18:00:00', 1, 8, 2, 4, true, '{"email": "poppingshow@event.com", "phone": "456-789-0124"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e855', 100, now(), now()),
('e5f6a7b8-c9d1-4a3c-9a4b-983b9a1a3e10', 'Хаус Баттл', 'Соревнование по хаус танцам.', '2024-10-15 10:00:00', '2024-10-15 18:00:00', 1, 9, 1, 5, true, '{"email": "housebattle@event.com", "phone": "567-890-1235"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e853', 50, now(), now()),
('f6a7b8c9-d1e2-4a3c-9a4b-983b9a1a3e11', 'Фанк Фестиваль', 'Фестиваль для любителей фанк музыки.', '2024-11-20 12:00:00', '2024-11-20 20:00:00', 1, 10, 2, 5, true, '{"email": "funkfest@festival.com", "phone": "678-901-2346"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 200, now(), now()),
('f24e7b62-528a-4f7d-92d5-843d5e5c0a12', 'Рэп Баттл', 'Соревнование рэперов.', '2024-12-25 14:00:00', '2024-12-25 18:00:00', 2, 11, 1, 1, true, '{"email": "rapbattle@event.com", "phone": "789-012-3457"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 150, now(), now()),
('a16d8491-f0f6-4e57-a764-fdded7a01d13', 'Эмсиинг Фестиваль', 'Фестиваль для любителей эмсиинга.', '2024-01-18 16:00:00', '2024-01-18 22:00:00', 2, 12, 2, 2, true, '{"email": "emceefest@festival.com", "phone": "890-123-4568"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e853', 300, now(), now()),
('390052c8-3538-4198-9595-d783aebf9014', 'Диджеинг Шоу', 'Шоу с участием лучших диджеев.', '2024-02-15 10:00:00', '2024-02-15 18:00:00', 2, 13, 2, 3, true, '{"email": "djinshow@event.com", "phone": "901-234-5679"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 100, now(), now()),
('6fc159e1-1960-4017-ba61-d882214ed715', 'Скретчинг Баттл', 'Соревнование по скретчингу.', '2024-03-20 10:00:00', '2024-03-20 18:00:00', 2, 14, 1, 4, true, '{"email": "scratchbattle@event.com", "phone": "012-345-6780"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e853', 50, now(), now()),
('e388f727-58fa-4e8c-b316-0f981b55af16', 'Сэмплирование Фестиваль', 'Фестиваль для любителей сэмплирования.', '2024-04-25 12:00:00', '2024-04-25 20:00:00', 2, 15, 4, 5, true, '{"email": "samplingfest@festival.com", "phone": "123-456-7892"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 200, now(), now()),
('5dea0091-668d-433a-867d-f053ee347817', 'Тёрнтеблизм Шоу', 'Шоу с участием лучших тёрнтеблистов.', '2024-05-18 14:00:00', '2024-05-18 18:00:00', 2, 16, 2, 1, true, '{"email": "turntablismshow@event.com", "phone": "234-567-8903"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e853', 150, now(), now()),
('c52a2849-9e3d-451e-b1c6-0557ce6d4218', 'Битмейкинг Фестиваль', 'Фестиваль для любителей битмейкинга.', '2024-06-12 16:00:00', '2024-06-12 22:00:00', 2, 17, 5, 2, true, '{"email": "beatmakingfest@festival.com", "phone": "345-678-9014"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e855', 300, now(), now()),
('c52a2849-9e3d-451e-b1c6-0557ce6d4219', 'Битбокс Шоу', 'Шоу с участием лучших битбоксеров.', '2024-07-10 10:00:00', '2024-07-10 18:00:00', 2, 18, 2, 3, true, '{"email": "beatboxshow@event.com", "phone": "456-789-0125"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e853', 100, now(), now()),
('c52a2849-9e3d-451e-b1c6-0557ce6d4220', 'Граффити Баттл', 'Соревнование по граффити.', '2024-08-15 10:00:00', '2024-08-15 18:00:00', 3, 19, 1, 4, true, '{"email": "graffitibattle@event.com", "phone": "567-890-1236"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 50, now(), now()),
('c52a2849-9e3d-451e-b1c6-0557ce6d4221', 'Каллиграфия Фестиваль', 'Фестиваль для любителей каллиграфии.', '2024-09-18 12:00:00', '2024-09-18 20:00:00', 3, 20, 2, 5, true, '{"email": "calligraphyfest@festival.com", "phone": "678-901-2347"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e855', 200, now(), now()),
('c52a2849-9e3d-451e-b1c6-0557ce6d4222', 'Тэггинг Шоу', 'Шоу с участием лучших тэггеров.', '2024-10-20 14:00:00', '2024-10-20 18:00:00', 3, 21, 2, 1, true, '{"email": "taggingshow@event.com", "phone": "789-012-3458"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 150, now(), now()),
('c52a2849-9e3d-451e-b1c6-0557ce6d4223', 'Трафареты Баттл', 'Соревнование по трафаретному искусству.', '2024-11-25 10:00:00', '2024-11-25 18:00:00', 3, 22, 1, 2, true, '{"email": "stencilbattle@event.com", "phone": "890-123-4569"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e855', 50, now(), now()),
('c52a2849-9e3d-451e-b1c6-0557ce6d4224', 'Инсталляции Фестиваль', 'Фестиваль скульптурных инсталляций.', '2024-12-18 12:00:00', '2024-12-18 20:00:00', 3, 23, 2, 3, true, '{"email": "installationsfest@festival.com", "phone": "901-234-5670"}', 'c9b9b630-5656-4a61-9c85-efb4a1a3e854', 200, now(), now());

-- Вставка данных в таблицу GalleryEvent
INSERT INTO events_galleryevent (id, file, event_id, created_at, updated_at)
VALUES
(9, 'files_events/dubstep1.jpg', 'a1b2c3d4-e5f6-4a3c-9a4b-983b9a1a3e06', now(), now()),
(10, 'files_events/dubstep2.jpg', 'a1b2c3d4-e5f6-4a3c-9a4b-983b9a1a3e06', now(), now()),
(11, 'files_events/electro1.jpg', 'b2c3d4e5-f6a7-4a3c-9a4b-983b9a1a3e07', now(), now()),
(12, 'files_events/electro2.jpg', 'b2c3d4e5-f6a7-4a3c-9a4b-983b9a1a3e07', now(), now()),
(13, 'files_events/locking1.jpg', 'c3d4e5f6-a7b8-4a3c-9a4b-983b9a1a3e08', now(), now()),
(14, 'files_events/locking2.jpg', 'c3d4e5f6-a7b8-4a3c-9a4b-983b9a1a3e08', now(), now()),
(15, 'files_events/popping1.jpg', 'd4e5f6a7-b8c9-4a3c-9a4b-983b9a1a3e09', now(), now()),
(16, 'files_events/popping2.jpg', 'd4e5f6a7-b8c9-4a3c-9a4b-983b9a1a3e09', now(), now()),
(17, 'files_events/house1.jpg', 'e5f6a7b8-c9d1-4a3c-9a4b-983b9a1a3e10', now(), now()),
(18, 'files_events/house2.jpg', 'e5f6a7b8-c9d1-4a3c-9a4b-983b9a1a3e10', now(), now()),
(19, 'files_events/funk1.jpg', 'f6a7b8c9-d1e2-4a3c-9a4b-983b9a1a3e11', now(), now()),
(20, 'files_events/funk2.jpg', 'f6a7b8c9-d1e2-4a3c-9a4b-983b9a1a3e11', now(), now());


SELECT setval('events_typeevent_id_seq', (SELECT MAX(id) FROM events_typeevent));
SELECT setval('events_region_id_seq', (SELECT MAX(id) FROM events_region));
SELECT setval('events_discipline_id_seq', (SELECT MAX(id) FROM events_discipline));
SELECT setval('events_subdiscipline_id_seq', (SELECT MAX(id) FROM events_subdiscipline));
SELECT setval('events_location_id_seq', (SELECT MAX(id) FROM events_location));
SELECT setval('events_city_id_seq', (SELECT MAX(id) FROM events_city));
SELECT setval('events_region_id_seq', (SELECT MAX(id) FROM events_region));
