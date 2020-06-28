USE avito;

UPDATE messages SET
  from_user_id = FLOOR(1 + (RAND() * 500)),
  to_user_id = FLOOR(1 + (RAND() * 500));

INSERT INTO ads_type VALUES 
  (1, 'selling my'), 
  (2, 'goods purchased for sale');
  
INSERT INTO product_shape VALUES
  (1, 'new'),
  (2, 'second hand');
  
INSERT INTO ads_services VALUES
  (0, 'Без продвижения', '0', '0', '1 раз', '0.00'),
  (1, 'VIP размешение', '0', '1', '1 раз', '449.00'),
  (2, 'Премиум', '1', '0', '1 раз', '1169.00'),
  (3, 'Быстрая продажа', '0', '1', '4 раза каждые 48 часов', '999.00'),
  (4, 'Турбо-продажа', '1', '1', '7 раз каждые 24 часа', '2169.00');
  
INSERT INTO extra_services VALUES
  (1, 'Выделить объявление цветом', 'Объявление не затеряется среди других благодаря яркому цвету.
А ещё оно один раз поднимется в результатах поиска — сразу
после подключения услуги.', '239.00'),
(2, 'Сделать XL-объявлением', 'Пользователи смогут посмотреть фотографии и узнать
телефон прямо из результатов поиска. Обычно такие
объявления получают в 2 раза больше запросов контактов.', '339.00');

INSERT INTO remove_comment VALUES
  (1, 'Продал на Авито'),
  (2, 'Продал где-то ещё'),
  (3, 'Другая причина');
  
INSERT INTO wallet_payment VALUES
  (1, 'Банковская карта', 'https://securepayments.ru/payment/mdOrder=bd659'),  
  (2, 'Сбербанк онлайн', 'https://www.aviiito.ru/account#step1'),  
  (3, 'Яндекс деньги', 'https://money.dex.ru/payments/internal/orderId=268'),  
  (4, 'Киви кошелёк', 'https://qiiiwi.com/order/external/transaction=131'),  
  (5, 'Киви терминал', 'https://www.aviiito.ru/account#step2'),  
  (6, 'Банковский перевод', 'https://www.aviiito.ru/account#step3');
  
INSERT INTO catalog VALUES
  (340, 'Бытовая электроника', 'Аудио и видео', 'МР3-плееры'), (341, 'Бытовая электроника', 'Аудио и видео', 'Акустика, колонки, сабвуферы'), (342, 'Бытовая электроника', 'Аудио и видео', 'Видео, DVD, и Blu-ray плееры'), (343, 'Бытовая электроника', 'Аудио и видео', 'Видеокамеры'), (344, 'Бытовая электроника', 'Аудио и видео', 'Кабели и адаптеры'), (345, 'Бытовая электроника', 'Аудио и видео', 'Микрофоны'), (346, 'Бытовая электроника', 'Аудио и видео', 'Музыка и фильмы'), (347, 'Бытовая электроника', 'Аудио и видео', 'Музыкальные центры, магнитолы'), (348, 'Бытовая электроника', 'Аудио и видео', 'Наушники'), (349, 'Бытовая электроника', 'Аудио и видео', 'Телевизоры и проекторы'),
  (350, 'Бытовая электроника', 'Аудио и видео', 'Усилители и ресиверы'), (351, 'Бытовая электроника', 'Аудио и видео', 'Аксессуары');

INSERT INTO catalog VALUES
  (352, 'Бытовая электроника', 'Игры, приставки и программы', 'Игры для приставок'), (353, 'Бытовая электроника', 'Игры, приставки и программы', 'Игровые приставки'), (354, 'Бытовая электроника', 'Игры, приставки и программы', 'Компьютерные игры'), (355, 'Бытовая электроника', 'Игры, приставки и программы', 'Программы');

INSERT INTO catalog VALUES
  (418, 'Бытовая электроника', 'Настольные компьютеры', 'Настольные компьютеры');
  
INSERT INTO catalog VALUES
  (419, 'Бытовая электроника', 'Ноутбуки', 'Ноутбуки');
  
INSERT INTO catalog VALUES
  (356, 'Бытовая электроника', 'Оргтехника и расходники', 'МФУ, копиры и сканеры'), (357, 'Бытовая электроника', 'Оргтехника и расходники', 'Принтеры'), (358, 'Бытовая электроника', 'Оргтехника и расходники', 'Телефония'), (359, 'Бытовая электроника', 'Оргтехника и расходники', 'ИБП, сетевые фильтры'), (360, 'Бытовая электроника', 'Оргтехника и расходники', 'Уничтожители бумаг'), (361, 'Бытовая электроника', 'Оргтехника и расходники', 'Расходные материалы'), (362, 'Бытовая электроника', 'Оргтехника и расходники', 'Канцелярия');

INSERT INTO catalog VALUES
  (363, 'Бытовая электроника', 'Планшенты и электронные книги', 'Планшеты'), (364, 'Бытовая электроника', 'Планшенты и электронные книги', 'Электронные книги'), (365, 'Бытовая электроника', 'Планшенты и электронные книги', 'Аксессуары');

INSERT INTO catalog VALUES
  (366, 'Бытовая электроника', 'Телефоны', 'Acer'), (367, 'Бытовая электроника', 'Телефоны', 'Alcatel'), (368, 'Бытовая электроника', 'Телефоны', 'ASUS'), (369, 'Бытовая электроника', 'Телефоны', 'BlackBerry'), (370, 'Бытовая электроника', 'Телефоны', 'BQ'), (371, 'Бытовая электроника', 'Телефоны', 'DEXP'), (372, 'Бытовая электроника', 'Телефоны', 'Explay'), (373, 'Бытовая электроника', 'Телефоны', 'Fly'), (374, 'Бытовая электроника', 'Телефоны', 'Highscreen'), (375, 'Бытовая электроника', 'Телефоны', 'HTC'),
  (376, 'Бытовая электроника', 'Телефоны', 'Huawei'), (377, 'Бытовая электроника', 'Телефоны', 'iPhone'), (378, 'Бытовая электроника', 'Телефоны', 'Lenovo'), (379, 'Бытовая электроника', 'Телефоны', 'LG'), (380, 'Бытовая электроника', 'Телефоны', 'Meizu'), (381, 'Бытовая электроника', 'Телефоны', 'Micromax'), (382, 'Бытовая электроника', 'Телефоны', 'Microsoft'), (383, 'Бытовая электроника', 'Телефоны', 'Motorola'), (384, 'Бытовая электроника', 'Телефоны', 'MTS'), (385, 'Бытовая электроника', 'Телефоны', 'Nokia'),
  (386, 'Бытовая электроника', 'Телефоны', 'Panasonic'), (387, 'Бытовая электроника', 'Телефоны', 'Philips'), (388, 'Бытовая электроника', 'Телефоны', 'Prestigio'), (389, 'Бытовая электроника', 'Телефоны', 'Samsung'), (390, 'Бытовая электроника', 'Телефоны', 'Siemens'), (391, 'Бытовая электроника', 'Телефоны', 'SkyLink'), (392, 'Бытовая электроника', 'Телефоны', 'Sony'), (393, 'Бытовая электроника', 'Телефоны', 'teXet'), (394, 'Бытовая электроника', 'Телефоны', 'Vertu'), (395, 'Бытовая электроника', 'Телефоны', 'Xiaomi'),
  (396, 'Бытовая электроника', 'Телефоны', 'ZTE'), (397, 'Бытовая электроника', 'Телефоны', 'Другие марки'), (398, 'Бытовая электроника', 'Телефоны', 'Рации'), (399, 'Бытовая электроника', 'Телефоны', 'Стационарные телефоны'), (400, 'Бытовая электроника', 'Телефоны', 'Аксессуары');

INSERT INTO catalog VALUES
  (401, 'Бытовая электроника', 'Товары для компьютера', 'Акустика'), (402, 'Бытовая электроника', 'Товары для компьютера', 'Веб-камеры'), (403, 'Бытовая электроника', 'Товары для компьютера', 'Джойстики и рули'), (404, 'Бытовая электроника', 'Товары для компьютера', 'Клавиатуры и мыши'), (405, 'Бытовая электроника', 'Товары для компьютера', 'Комплектующие'), (406, 'Бытовая электроника', 'Товары для компьютера', 'Мониторы'), (407, 'Бытовая электроника', 'Товары для компьютера', 'Переносные жёсткие диски'), (408, 'Бытовая электроника', 'Товары для компьютера', 'Сетевое оборудование'), (409, 'Бытовая электроника', 'Товары для компьютера', 'ТВ-тюнеры'), (410, 'Бытовая электроника', 'Товары для компьютера', 'Флэшки и карты памяти'),
  (411, 'Бытовая электроника', 'Товары для компьютера', 'Аксессуары');
  
INSERT INTO catalog VALUES
  (412, 'Бытовая электроника', 'Фототехника', 'Компактные фотоаппараты'),
  (413, 'Бытовая электроника', 'Фототехника', 'Зеркальные фотоаппараты'),
  (414, 'Бытовая электроника', 'Фототехника', 'Плёночные фотоаппараты'),
  (415, 'Бытовая электроника', 'Фототехника', 'Бинокли и телескопы'),
  (416, 'Бытовая электроника', 'Фототехника', 'Объективы'),
  (417, 'Бытовая электроника', 'Фототехника', 'Оборудование и аксессуары');

INSERT INTO catalog VALUES
  (284, 'Для бизнеса', 'Готовый бизнес', 'Интернет-магазин'),
  (285, 'Для бизнеса', 'Готовый бизнес', 'Общественное питание'),
  (286, 'Для бизнеса', 'Готовый бизнес', 'Производство'),
  (287, 'Для бизнеса', 'Готовый бизнес', 'Развлечения'),
  (288, 'Для бизнеса', 'Готовый бизнес', 'Сельское хозяйство'),
  (289, 'Для бизнеса', 'Готовый бизнес', 'Строительство'),
  (290, 'Для бизнеса', 'Готовый бизнес', 'Сфера услуг'),
  (291, 'Для бизнеса', 'Готовый бизнес', 'Торговля'),
  (292, 'Для бизнеса', 'Готовый бизнес', 'Другое');

INSERT INTO catalog VALUES
  (293, 'Для бизнеса', 'Оборудование для бизнеса', 'Для магазина'),
  (294, 'Для бизнеса', 'Оборудование для бизнеса', 'Для офиса'),
  (295, 'Для бизнеса', 'Оборудование для бизнеса', 'Для ресторана'),
  (296, 'Для бизнеса', 'Оборудование для бизнеса', 'Для салона красоты'),
  (297, 'Для бизнеса', 'Оборудование для бизнеса', 'Промышленное'),
  (298, 'Для бизнеса', 'Оборудование для бизнеса', 'Другое');
  
INSERT INTO catalog VALUES
  (183, 'Для дома и дачи', 'Бытовая техника', 'Для дома'),
  (184, 'Для дома и дачи', 'Бытовая техника', 'Для индивидуального ухода'),
  (185, 'Для дома и дачи', 'Бытовая техника', 'Для кухни'),
  (186, 'Для дома и дачи', 'Бытовая техника', 'Климатическое оборудование'),
  (187, 'Для дома и дачи', 'Бытовая техника', 'Другое');
  
INSERT INTO catalog VALUES
  (188, 'Для дома и дачи', 'Мебель и интерьер', 'Компьютерные столы и кресла'),
  (189, 'Для дома и дачи', 'Мебель и интерьер', 'Кровати, диваны и кресла'),
  (190, 'Для дома и дачи', 'Мебель и интерьер', 'Кухонные гарнитуры'),
  (191, 'Для дома и дачи', 'Мебель и интерьер', 'Освещение'),
  (192, 'Для дома и дачи', 'Мебель и интерьер', 'Подставки и тумбы'),
  (193, 'Для дома и дачи', 'Мебель и интерьер', 'Предметы интерьера, искусство'),
  (194, 'Для дома и дачи', 'Мебель и интерьер', 'Столы и стулья'),
  (195, 'Для дома и дачи', 'Мебель и интерьер', 'Текстиль и ковры'),
  (196, 'Для дома и дачи', 'Мебель и интерьер', 'Шкафы и комоды'),
  (197, 'Для дома и дачи', 'Мебель и интерьер', 'Другое');
  
INSERT INTO catalog VALUES
  (198, 'Для дома и дачи', 'Посуда и товары для кухни', 'Посуда'),
  (199, 'Для дома и дачи', 'Посуда и товары для кухни', 'Товары для кухни');
  
INSERT INTO catalog VALUES
  (200, 'Для дома и дачи', 'Продукты питания', 'Продукты питания');
  
INSERT INTO catalog VALUES
  (210, 'Для дома и дачи', 'Растения', 'Растения');
  
INSERT INTO catalog VALUES
  (201, 'Для дома и дачи', 'Ремонт и строительство', 'Двери'),
  (202, 'Для дома и дачи', 'Ремонт и строительство', 'Инструменты'),
  (203, 'Для дома и дачи', 'Ремонт и строительство', 'Камины и обогреватели'),
  (204, 'Для дома и дачи', 'Ремонт и строительство', 'Окна и балконы'),
  (205, 'Для дома и дачи', 'Ремонт и строительство', 'Потолки'),
  (206, 'Для дома и дачи', 'Ремонт и строительство', 'Садовая техника'),
  (207, 'Для дома и дачи', 'Ремонт и строительство', 'Сантехника и сауна'),
  (208, 'Для дома и дачи', 'Ремонт и строительство', 'Стройматериалы'),
  (209, 'Для дома и дачи', 'Ремонт и строительство', 'Услуги');

INSERT INTO catalog VALUES
  (271, 'Животные', 'Собаки', 'Собаки'),
  (272, 'Животные', 'Кошки', 'Кошки'),
  (273, 'Животные', 'Птицы', 'Птицы'),
  (274, 'Животные', 'Аквариум', 'Аквариум'),
  (275, 'Животные', 'Другие животные', 'Амфибии'),
  (276, 'Животные', 'Другие животные', 'Грызуны'),
  (277, 'Животные', 'Другие животные', 'Кролики'),
  (278, 'Животные', 'Другие животные', 'Лошади'),
  (279, 'Животные', 'Другие животные', 'Рептилии'),
  (280, 'Животные', 'Другие животные', 'С/х животные'),
  (281, 'Животные', 'Другие животные', 'Хорьки'),
  (282, 'Животные', 'Другие животные', 'Другое'),
  (283, 'Животные', 'Товары для животных', 'Товары для животных');

INSERT INTO catalog VALUES
  (158, 'Личные вещи', 'Одежда, обувь, аксессуары', 'Женская одежда'),
  (159, 'Личные вещи', 'Одежда, обувь, аксессуары', 'Мужская одежда'),
  (160, 'Личные вещи', 'Одежда, обувь, аксессуары', 'Аксессуары'),
  (161, 'Личные вещи', 'Детская одежда и обувь', 'Для девочек'),
  (162, 'Личные вещи', 'Детская одежда и обувь', 'Для мальчиков'),
  (163, 'Личные вещи', 'Товары для детей и игрушки', 'Автомобильные кресла'),
  (164, 'Личные вещи', 'Товары для детей и игрушки', 'Велосипеды и самокаты'),
  (165, 'Личные вещи', 'Товары для детей и игрушки', 'Детская мебель'),
  (166, 'Личные вещи', 'Товары для детей и игрушки', 'Детские коляски'),
  (167, 'Личные вещи', 'Товары для детей и игрушки', 'Игрушки'),
  (168, 'Личные вещи', 'Товары для детей и игрушки', 'Постельные принадлежности'),
  (169, 'Личные вещи', 'Товары для детей и игрушки', 'Товары для кормления'),
  (170, 'Личные вещи', 'Товары для детей и игрушки', 'Товары для купания'),
  (171, 'Личные вещи', 'Товары для детей и игрушки', 'Товары для школы'),
  (172, 'Личные вещи', 'Часы и украшения', 'Бижутерия'),
  (173, 'Личные вещи', 'Часы и украшения', 'Часы'),
  (174, 'Личные вещи', 'Часы и украшения', 'Ювелирные изделия'),
  (175, 'Личные вещи', 'Красота и здоровье', 'Косметика'),
  (176, 'Личные вещи', 'Красота и здоровье', 'Парфюмерия'),
  (177, 'Личные вещи', 'Красота и здоровье', 'Приборы и аксессуары'),
  (178, 'Личные вещи', 'Красота и здоровье', 'Средства гигиены'),
  (179, 'Личные вещи', 'Красота и здоровье', 'Средства для волос'),
  (180, 'Личные вещи', 'Красота и здоровье', 'Медицинские изделия'),
  (181, 'Личные вещи', 'Красота и здоровье', 'Биологически активные добавки'),
  (182, 'Личные вещи', 'Красота и здоровье', 'Услуги');

INSERT INTO catalog VALUES
  (1, 'Недвижимость', 'Квартиры', 'Продам'),
  (2, 'Недвижимость', 'Квартиры', 'Сдам'),
  (3, 'Недвижимость', 'Квартиры', 'Куплю'),
  (4, 'Недвижимость', 'Квартиры', 'Сниму'),
  (5, 'Недвижимость', 'Комнаты', 'Продам'),
  (6, 'Недвижимость', 'Комнаты', 'Сдам'),
  (7, 'Недвижимость', 'Комнаты', 'Куплю'),
  (8, 'Недвижимость', 'Комнаты', 'Сниму'),
  (9, 'Недвижимость', 'Дома, дачи, коттеджи', 'Продам'),
  (10, 'Недвижимость', 'Дома, дачи, коттеджи', 'Сдам'),
  (11, 'Недвижимость', 'Дома, дачи, коттеджи', 'Куплю'),
  (12, 'Недвижимость', 'Дома, дачи, коттеджи', 'Сниму'),
  (13, 'Недвижимость', 'Земельные участки', 'Продам'),
  (14, 'Недвижимость', 'Земельные участки', 'Сдам'),
  (15, 'Недвижимость', 'Земельные участки', 'Куплю'),
  (16, 'Недвижимость', 'Земельные участки', 'Сниму'),
  (17, 'Недвижимость', 'Гаражи и машиноместа', 'Продам'),
  (18, 'Недвижимость', 'Гаражи и машиноместа', 'Сдам'),
  (19, 'Недвижимость', 'Гаражи и машиноместа', 'Куплю'),
  (20, 'Недвижимость', 'Гаражи и машиноместа', 'Сниму'),
  (21, 'Недвижимость', 'Коммерческая недвижимость', 'Продам'),
  (22, 'Недвижимость', 'Коммерческая недвижимость', 'Сдам'),
  (23, 'Недвижимость', 'Коммерческая недвижимость', 'Куплю'),
  (24, 'Недвижимость', 'Коммерческая недвижимость', 'Сниму'),
  (25, 'Недвижимость', 'Недвижимость за рубежом', 'Продам'),
  (26, 'Недвижимость', 'Недвижимость за рубежом', 'Сдам'),
  (27, 'Недвижимость', 'Недвижимость за рубежом', 'Куплю'),
  (28, 'Недвижимость', 'Недвижимость за рубежом', 'Сниму');
  
INSERT INTO catalog VALUES
  (29, 'Работа', 'Вакансии', 'IT, интернет, телеком'),
  (30, 'Работа', 'Вакансии', 'Автомобильный бизнес'),
  (31, 'Работа', 'Вакансии', 'Административная работа'),
  (32, 'Работа', 'Вакансии', 'Банки, инвестиции'),
  (33, 'Работа', 'Вакансии', 'Без опыта, студенты'),
  (34, 'Работа', 'Вакансии', 'Бухгалтерия, финансы'),
  (35, 'Работа', 'Вакансии', 'Высший менеджмент'),
  (36, 'Работа', 'Вакансии', 'Госслужба, НКО'),
  (37, 'Работа', 'Вакансии', 'Домашний персонал'),
  (38, 'Работа', 'Вакансии', 'ЖКХ, эксплуатация'),
  (39, 'Работа', 'Вакансии', 'Искусство, развлечения'),
  (40, 'Работа', 'Вакансии', 'Консультирование'),
  (41, 'Работа', 'Вакансии', 'Маркетинг, реклама, PR'),
  (42, 'Работа', 'Вакансии', 'Медицина, фармацевтика'),
  (43, 'Работа', 'Вакансии', 'Образование, наука'),
  (44, 'Работа', 'Вакансии', 'Охрана, безопасность'),
  (45, 'Работа', 'Вакансии', 'Продажи'),
  (46, 'Работа', 'Вакансии', 'Производство, сырьё, с/х'),
  (47, 'Работа', 'Вакансии', 'Страхование'),
  (48, 'Работа', 'Вакансии', 'Строительство'),
  (49, 'Работа', 'Вакансии', 'Транспорт, логистика'),
  (50, 'Работа', 'Вакансии', 'Туризм, рестораны'),
  (51, 'Работа', 'Вакансии', 'Управление персоналом'),
  (52, 'Работа', 'Вакансии', 'Фитнес, салоны красоты'),
  (53, 'Работа', 'Вакансии', 'Юриспруденция');

INSERT INTO catalog VALUES
  (54, 'Работа', 'Резюме', 'IT, интернет, телеком'),
  (55, 'Работа', 'Резюме', 'Автомобильный бизнес'),
  (56, 'Работа', 'Резюме', 'Административная работа'),
  (57, 'Работа', 'Резюме', 'Банки, инвестиции'),
  (58, 'Работа', 'Резюме', 'Без опыта, студенты'),
  (59, 'Работа', 'Резюме', 'Бухгалтерия, финансы'),
  (60, 'Работа', 'Резюме', 'Высший менеджмент'),
  (61, 'Работа', 'Резюме', 'Госслужба, НКО'),
  (62, 'Работа', 'Резюме', 'Домашний персонал'),
  (63, 'Работа', 'Резюме', 'ЖКХ, эксплуатация'),
  (64, 'Работа', 'Резюме', 'Искусство, развлечения'),
  (65, 'Работа', 'Резюме', 'Консультирование'),
  (66, 'Работа', 'Резюме', 'Маркетинг, реклама, PR'),
  (67, 'Работа', 'Резюме', 'Медицина, фармацевтика'),
  (68, 'Работа', 'Резюме', 'Образование, наука'),
  (69, 'Работа', 'Резюме', 'Охрана, безопасность'),
  (70, 'Работа', 'Резюме', 'Продажи'),
  (71, 'Работа', 'Резюме', 'Производство, сырьё, с/х'),
  (72, 'Работа', 'Резюме', 'Страхование'),
  (73, 'Работа', 'Резюме', 'Строительство'),
  (74, 'Работа', 'Резюме', 'Транспорт, логистика'),
  (75, 'Работа', 'Резюме', 'Туризм, рестораны'),
  (76, 'Работа', 'Резюме', 'Управление персоналом'),
  (77, 'Работа', 'Резюме', 'Фитнес, салоны красоты'),
  (78, 'Работа', 'Резюме', 'Юриспруденция');

INSERT INTO catalog VALUES
  (299, 'Транспорт', 'Автомобили', 'С пробегом'),
  (300, 'Транспорт', 'Автомобили', 'Новый'),
  (308, 'Транспорт', 'Грузовики и спецтехника', 'Автобусы'),
  (309, 'Транспорт', 'Грузовики и спецтехника', 'Автодома'),
  (310, 'Транспорт', 'Грузовики и спецтехника', 'Автокраны'),
  (311, 'Транспорт', 'Грузовики и спецтехника', 'Бульдозеры'),
  (312, 'Транспорт', 'Грузовики и спецтехника', 'Грузовики'),
  (313, 'Транспорт', 'Грузовики и спецтехника', 'Коммунальная техника'),
  (314, 'Транспорт', 'Грузовики и спецтехника', 'Лёгкий транспорт'),
  (315, 'Транспорт', 'Грузовики и спецтехника', 'Погрузчики'),
  (316, 'Транспорт', 'Грузовики и спецтехника', 'Прицепы'),
  (317, 'Транспорт', 'Грузовики и спецтехника', 'Сельхозтехника'),
  (318, 'Транспорт', 'Грузовики и спецтехника', 'Строительная техника'),
  (319, 'Транспорт', 'Грузовики и спецтехника', 'Техника для лесозаготовки'),
  (320, 'Транспорт', 'Грузовики и спецтехника', 'Тягачи'),
  (321, 'Транспорт', 'Грузовики и спецтехника', 'Экскаваторы'),
  (322, 'Транспорт', 'Водный транспорт', 'Вёсельные лодки'),
  (323, 'Транспорт', 'Водный транспорт', 'Гидроциклы'),
  (324, 'Транспорт', 'Водный транспорт', 'Катера и яхты'),
  (325, 'Транспорт', 'Водный транспорт', 'Каяки и каноэ'),
  (326, 'Транспорт', 'Водный транспорт', 'Моторные лодки'),
  (327, 'Транспорт', 'Водный транспорт', 'Надувные лодки');

INSERT INTO catalog VALUES
  (301, 'Транспорт', 'Мотоциклы и мототехника', 'Багги'),
  (302, 'Транспорт', 'Мотоциклы и мототехника', 'Вездеходы'),
  (303, 'Транспорт', 'Мотоциклы и мототехника', 'Картинг'),
  (304, 'Транспорт', 'Мотоциклы и мототехника', 'Квадроциклы'),
  (305, 'Транспорт', 'Мотоциклы и мототехника', 'Мопеды и скутеры'),
  (306, 'Транспорт', 'Мотоциклы и мототехника', 'Мотоциклы'),
  (307, 'Транспорт', 'Мотоциклы и мототехника', 'Снегоходы'),
  (328, 'Транспорт', 'Запчасти и аксессуары', 'Запчасти'),
  (329, 'Транспорт', 'Запчасти и аксессуары', 'Аксессуары'),
  (330, 'Транспорт', 'Запчасти и аксессуары', 'GPS-навигаторы'),
  (331, 'Транспорт', 'Запчасти и аксессуары', 'Автокосметика и автохимия'),
  (332, 'Транспорт', 'Запчасти и аксессуары', 'Аудио- и видеотехника'),
  (333, 'Транспорт', 'Запчасти и аксессуары', 'Багажники и фаркопы'),
  (334, 'Транспорт', 'Запчасти и аксессуары', 'Инструменты'),
  (335, 'Транспорт', 'Запчасти и аксессуары', 'Прицепы'),
  (336, 'Транспорт', 'Запчасти и аксессуары', 'Противоугонные устройства'),
  (337, 'Транспорт', 'Запчасти и аксессуары', 'Тюнинг'),
  (338, 'Транспорт', 'Запчасти и аксессуары', 'Шины, диски и колёса'),
  (339, 'Транспорт', 'Запчасти и аксессуары', 'Экипировка');

INSERT INTO catalog VALUES
  (79, 'Услуги', 'IT, интернет, телеком', 'Cоздание и продвижение сайтов'),
  (80, 'Услуги', 'IT, интернет, телеком', 'Мастер на все случаи'),
  (81, 'Услуги', 'IT, интернет, телеком', 'Настройка интернета и сетей'),
  (82, 'Услуги', 'IT, интернет, телеком', 'Установка и настройка ПО'),
  (83, 'Услуги', 'Бытовые услуги', 'Изготовление ключей'),
  (84, 'Услуги', 'Бытовые услуги', 'Пошив и ремонт одежды'),
  (85, 'Услуги', 'Бытовые услуги', 'Ремонт часов'),
  (86, 'Услуги', 'Бытовые услуги', 'Химчистка, стирка'),
  (87, 'Услуги', 'Бытовые услуги', 'Ювелирные услуги'),
  (88, 'Услуги', 'Деловые услуги', 'Бухгалтерия, финансы'),
  (89, 'Услуги', 'Деловые услуги', 'Консультирование'),
  (90, 'Услуги', 'Деловые услуги', 'Набор и коррекция текста'),
  (91, 'Услуги', 'Деловые услуги', 'Перевод'),
  (92, 'Услуги', 'Деловые услуги', 'Юридические услуги'),
  (93, 'Услуги', 'Искусство', 'Искусство'),
  (94, 'Услуги', 'Красота, здоровье', 'Услуги парикмахера'),
  (95, 'Услуги', 'Красота, здоровье', 'Маникюр, педикюр'),
  (96, 'Услуги', 'Красота, здоровье', 'Макияж'),
  (97, 'Услуги', 'Красота, здоровье', 'Косметология, эпиляция'),
  (98, 'Услуги', 'Красота, здоровье', 'СПА-услуги, здоровье'),
  (99, 'Услуги', 'Красота, здоровье', 'Тату, пирсинг'),
  (100, 'Услуги', 'Красота, здоровье', 'Другое'),
  (101, 'Услуги', 'Курьерские поручения', 'Курьерские поручения'),
  (102, 'Услуги', 'Мастер на час', 'Мастер на час'),
  (103, 'Услуги', 'Няни, сиделки', 'Няни, сиделки'),
  (104, 'Услуги', 'Оборудование, производство', 'Аренда оборудования'),
  (105, 'Услуги', 'Оборудование, производство', 'Монтаж и обслуживание оборудования'),
  (106, 'Услуги', 'Оборудование, производство', 'Производство, обработка'),
  (107, 'Услуги', 'Обучение, курсы', 'Предметы школы и ВУЗа'),
  (108, 'Услуги', 'Обучение, курсы', 'Иностранные языки'),
  (109, 'Услуги', 'Обучение, курсы', 'Вождение'),
  (110, 'Услуги', 'Обучение, курсы', 'Музыка, театр'),
  (111, 'Услуги', 'Обучение, курсы', 'Спорт, танцы'),
  (112, 'Услуги', 'Обучение, курсы', 'Рисование, дизайн, рукоделие'),
  (113, 'Услуги', 'Обучение, курсы', 'Профессиональная подготовка'),
  (114, 'Услуги', 'Обучение, курсы', 'Детское развитие, логопеды'),
  (115, 'Услуги', 'Обучение, курсы', 'Другое'),
  (116, 'Услуги', 'Охрана, безопасность', 'Охрана, безопасность'),
  (117, 'Услуги', 'Питание, кейтеринг', 'Питание, кейтеринг'),
  (118, 'Услуги', 'Праздники, мероприятия', 'Праздники, мероприятия'),
  (119, 'Услуги', 'Реклама, полиграфия', 'Маркетинг, реклама, PR'),
  (120, 'Услуги', 'Реклама, полиграфия', 'Полиграфия, дизайн'),
  (157, 'Услуги', 'Другое', 'Другое');
  
INSERT INTO catalog VALUES
  (121, 'Услуги', 'Ремонт и обслуживание техники', 'Телевизоры'),
  (122, 'Услуги', 'Ремонт и обслуживание техники', 'Фото-, аудио-, видеотехника'),
  (123, 'Услуги', 'Ремонт и обслуживание техники', 'Игровые приставки'),
  (124, 'Услуги', 'Ремонт и обслуживание техники', 'Компьютерная техника'),
  (125, 'Услуги', 'Ремонт и обслуживание техники', 'Крупная бытовая техника'),
  (126, 'Услуги', 'Ремонт и обслуживание техники', 'Мелкая бытовая техника'),
  (127, 'Услуги', 'Ремонт и обслуживание техники', 'Мобильные устройства'),
  (128, 'Услуги', 'Ремонт, строительство', 'Сборка и ремонт мебели'),
  (129, 'Услуги', 'Ремонт, строительство', 'Отделочные работы'),
  (130, 'Услуги', 'Ремонт, строительство', 'Электрика'),
  (131, 'Услуги', 'Ремонт, строительство', 'Сантехника'),
  (132, 'Услуги', 'Ремонт, строительство', 'Ремонт офиса'),
  (133, 'Услуги', 'Ремонт, строительство', 'Остекление балконов'),
  (134, 'Услуги', 'Ремонт, строительство', 'Ремонт ванной'),
  (135, 'Услуги', 'Ремонт, строительство', 'Строительство бань, саун'),
  (136, 'Услуги', 'Ремонт, строительство', 'Ремонт кухни'),
  (137, 'Услуги', 'Ремонт, строительство', 'Строительство домов, коттеджей'),
  (138, 'Услуги', 'Ремонт, строительство', 'Ремонт квартиры'),
  (139, 'Услуги', 'Сад, благоустройство', 'Сад, благоустройство'),
  (140, 'Услуги', 'Транспорт, перевозки', 'Автосервис'),
  (141, 'Услуги', 'Транспорт, перевозки', 'Аренда авто'),
  (142, 'Услуги', 'Транспорт, перевозки', 'Коммерческие перевозки'),
  (143, 'Услуги', 'Транспорт, перевозки', 'Грузчики'),
  (144, 'Услуги', 'Транспорт, перевозки', 'Переезды'),
  (145, 'Услуги', 'Транспорт, перевозки', 'Спецтехника'),
  (146, 'Услуги', 'Уборка', 'Вывоз мусора'),
  (147, 'Услуги', 'Уборка', 'Генеральная уборка'),
  (148, 'Услуги', 'Уборка', 'Глажка белья'),
  (149, 'Услуги', 'Уборка', 'Мойка окон'),
  (150, 'Услуги', 'Уборка', 'Простая уборка'),
  (151, 'Услуги', 'Уборка', 'Уборка после ремонта'),
  (152, 'Услуги', 'Уборка', 'Чистка ковров'),
  (153, 'Услуги', 'Уборка', 'Чистка мягкой мебели'),
  (154, 'Услуги', 'Установка техники', 'Установка техники'),
  (155, 'Услуги', 'Уход за животными', 'Уход за животными'),
  (156, 'Услуги', 'Фото- и видеосъёмка', 'Фото- и видеосъёмка');
  
INSERT INTO catalog VALUES
  (211, 'Хобби и отдых', 'Билеты и путешествия', 'Карты, купоны'), 
  (212, 'Хобби и отдых', 'Билеты и путешествия', 'Концерты'), 
  (213, 'Хобби и отдых', 'Билеты и путешествия', 'Путешествия'), 
  (214, 'Хобби и отдых', 'Билеты и путешествия', 'Спорт'), 
  (215, 'Хобби и отдых', 'Билеты и путешествия', 'Театр, опера, балет'), 
  (216, 'Хобби и отдых', 'Билеты и путешествия', 'Цирк, кино'), 
  (217, 'Хобби и отдых', 'Билеты и путешествия', 'Шоу, мюзикл'), 
  (218, 'Хобби и отдых', 'Велосипеды', 'Горные'), 
  (219, 'Хобби и отдых', 'Велосипеды', 'Дорожные'), 
  (220, 'Хобби и отдых', 'Велосипеды', 'ВМХ'), 
  (221, 'Хобби и отдых', 'Велосипеды', 'Детские'), 
  (222, 'Хобби и отдых', 'Велосипеды', 'Запчасти и аксессуары'), 
  (223, 'Хобби и отдых', 'Книги и журналы', 'Журналы, газеты, брошюры'), 
  (224, 'Хобби и отдых', 'Книги и журналы', 'Книги'),
  (225, 'Хобби и отдых', 'Книги и журналы', 'Учебная литература'),
  (226, 'Хобби и отдых', 'Коллекционирование', 'Банкноты'),
  (227, 'Хобби и отдых', 'Коллекционирование', 'Билеты'),
  (228, 'Хобби и отдых', 'Коллекционирование', 'Вещи знаменитостей, автографы'),
  (229, 'Хобби и отдых', 'Коллекционирование', 'Военные вещи'),
  (230, 'Хобби и отдых', 'Коллекционирование', 'Грампластинки'),
  (231, 'Хобби и отдых', 'Коллекционирование', 'Документы'),
  (232, 'Хобби и отдых', 'Коллекционирование', 'Жетоны, медали, значки'),
  (233, 'Хобби и отдых', 'Коллекционирование', 'Игры'),
  (234, 'Хобби и отдых', 'Коллекционирование', 'Календари'),
  (235, 'Хобби и отдых', 'Коллекционирование', 'Картины'),
  (236, 'Хобби и отдых', 'Коллекционирование', 'Киндер-сюрприз'),
  (237, 'Хобби и отдых', 'Коллекционирование', 'Конверты и почтовые карточки'),
  (238, 'Хобби и отдых', 'Коллекционирование', 'Макеты оружия'),
  (239, 'Хобби и отдых', 'Коллекционирование', 'Марки'),
  (240, 'Хобби и отдых', 'Коллекционирование', 'Модели'),
  (241, 'Хобби и отдых', 'Коллекционирование', 'Монеты'),
  (242, 'Хобби и отдых', 'Коллекционирование', 'Открытки'),
  (243, 'Хобби и отдых', 'Коллекционирование', 'Пепельницы, зажигалки'),
  (244, 'Хобби и отдых', 'Коллекционирование', 'Пластиковые карточки'),
  (245, 'Хобби и отдых', 'Коллекционирование', 'Спортивные карточки'),
  (246, 'Хобби и отдых', 'Коллекционирование', 'Фотографии, письма'),
  (247, 'Хобби и отдых', 'Коллекционирование', 'Этикетки, бутылки, пробки'),
  (248, 'Хобби и отдых', 'Коллекционирование', 'Другое'),
  (249, 'Хобби и отдых', 'Музыкальные инструменты', 'Аккордеоны, гармони, баяны'),
  (250, 'Хобби и отдых', 'Музыкальные инструменты', 'Гитары и другие струнные'),
  (251, 'Хобби и отдых', 'Музыкальные инструменты', 'Духовые'),
  (252, 'Хобби и отдых', 'Музыкальные инструменты', 'Пианино и другие клавишные'),
  (253, 'Хобби и отдых', 'Музыкальные инструменты', 'Скрипки и другие смычковые'),
  (254, 'Хобби и отдых', 'Музыкальные инструменты', 'Ударные'),
  (255, 'Хобби и отдых', 'Музыкальные инструменты', 'Для студии и концертов'),
  (256, 'Хобби и отдых', 'Музыкальные инструменты', 'Аксессуары'),
  (257, 'Хобби и отдых', 'Охота и рыбалка', 'Охота и рыбалка'),
  (258, 'Хобби и отдых', 'Спорт и отдых', 'Бильярд и боулинг'),
  (259, 'Хобби и отдых', 'Спорт и отдых', 'Дайвинг и водный спорт'),
  (260, 'Хобби и отдых', 'Спорт и отдых', 'Единоборства'),
  (261, 'Хобби и отдых', 'Спорт и отдых', 'Зимние виды спорта'),
  (262, 'Хобби и отдых', 'Спорт и отдых', 'Игры с мячом'),
  (263, 'Хобби и отдых', 'Спорт и отдых', 'Настольные игры'),
  (264, 'Хобби и отдых', 'Спорт и отдых', 'Пейнтбол и страйкбол'),
  (265, 'Хобби и отдых', 'Спорт и отдых', 'Ролики и скейтбординг'),
  (266, 'Хобби и отдых', 'Спорт и отдых', 'Теннис, бадминтон, пинг-понг'),
  (267, 'Хобби и отдых', 'Спорт и отдых', 'Туризм'),
  (268, 'Хобби и отдых', 'Спорт и отдых', 'Фитнес и тренажёры'),
  (269, 'Хобби и отдых', 'Спорт и отдых', 'Спортивное питание'),
  (270, 'Хобби и отдых', 'Спорт и отдых', 'Другое');
  
SELECT * FROM catalog;
  
  
    
  