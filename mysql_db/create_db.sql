CREATE DATABASE avito;
USE avito;

DROP TABLE IF EXISTS new_user;
CREATE TABLE new_user (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Номер пользователя',
  profile_name VARCHAR(100) COMMENT 'Имя для профиля',
  phone VARCHAR(120) COMMENT 'Номер мобильного',
  user_password VARCHAR(100) COMMENT 'Пароль пользователя',
  created_at DATETIME DEFAULT NOW() COMMENT 'Дата регистрации пользователя'
) COMMENT = 'Регистрационная форма';

DESCRIBE new_user;

DROP TABLE IF EXISTS profil;
CREATE TABLE profil (
  user_id INT UNSIGNED NOT NULL PRIMARY KEY COMMENT 'Номер пользователя',
  email VARCHAR(100) COMMENT 'Электронная почта',
  city VARCHAR(100) COMMENT 'Город',
  metro_station VARCHAR(100) COMMENT 'Станция метро',
  updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() COMMENT 'Дата обновления профиля',
  user_status VARCHAR(100) COMMENT 'Статус пользователя',
  vk_profil VARCHAR(100) COMMENT 'Профиль вконтакте',
  google_profil VARCHAR(100) COMMENT 'Профиль гугл',
  ok_profil VARCHAR(100) COMMENT 'Профиль одноклассники',
  facebook_profil VARCHAR(100) COMMENT 'Профиль фэйсбук',
  apple_profil VARCHAR(100) COMMENT 'Профиль эпл',
  purse_number INT COMMENT 'Номер авито кошелька',
  user_rating FLOAT(3,1) COMMENT 'Рейтинг пользователя'
) COMMENT = 'Профиль пользователя';

DESCRIBE profil;

DROP TABLE IF EXISTS catalog;
CREATE TABLE catalog (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Номер каталога',
  category VARCHAR(100) COMMENT 'Название категории',
  subcategory VARCHAR(100) COMMENT 'Название подкатегории',
  product VARCHAR(100) COMMENT 'Название продукта'
  ) COMMENT = 'Каталог товаров';
  
DROP TABLE IF EXISTS user_ads;
CREATE TABLE user_ads (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Номер обявления', 
  user_id INT UNSIGNED NOT NULL COMMENT 'Номер пользователя',
  ads_name VARCHAR(120) COMMENT 'Название объявления',
  product_shape_id INT COMMENT 'Номер состояния товара',
  ads_type_id INT COMMENT 'Номер типа объявления',
  catalog_id INT UNSIGNED NOT NULL COMMENT 'Номер группы товара',
  ads_description TEXT COMMENT 'Описание объявления',
  price DECIMAL(10,2) COMMENT 'Цена товара',
  media_id INT COMMENT 'Номер фотографии',
  youtube_link VARCHAR(150) COMMENT 'Ссылка на видео',
  trade_place VARCHAR(150) COMMENT 'Место сделки',
  ads_services_id INT NOT NULL COMMENT 'Номер платной услуги',
  created_at DATETIME DEFAULT NOW() COMMENT 'Дата создания объявления',
  updated_at DATETIME DEFAULT NOW() ON UPDATE NOW() COMMENT 'Дата обновления объявления'
  ) COMMENT = 'Таблица объявлений';
  
DROP TABLE IF EXISTS media;
CREATE TABLE media (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Номер медиафайла',
  image_type VARCHAR(50) NOT NULL COMMENT 'Тип картинки',
  image BLOB NOT NULL COMMENT 'Изображение',
  image_size VARCHAR(50) NOT NULL COMMENT 'Размер изображения',
  image_name VARCHAR(50) NOT NULL COMMENT 'Название изображения'
  ) COMMENT = 'Хранение фотографий товаров';
  
DROP TABLE IF EXISTS product_shape;
CREATE TABLE product_shape (
  id INT UNSIGNED NOT NULL PRIMARY KEY COMMENT 'Номер состояния товара',
  shape_type VARCHAR(50) COMMENT 'Состояние товара'
  ) COMMENT = 'Таблица состояний товара';

DROP TABLE IF EXISTS ads_type;
CREATE TABLE ads_type (
  id INT UNSIGNED NOT NULL PRIMARY KEY COMMENT 'Номер типа объявления',
  ad_type VARCHAR(50) COMMENT 'Тип объявления'
  ) COMMENT = 'Типы объявлений';
  
DROP TABLE IF EXISTS ads_services;
CREATE TABLE ads_services (
  id INT UNSIGNED NOT NULL COMMENT 'Номер услуги',
  services_name VARCHAR(50) NOT NULL COMMENT 'Название услуги',
  premium_block TINYINT(1) UNSIGNED NOT NULL COMMENT 'Первые строчки результатов поиска',
  vip_block TINYINT(1) UNSIGNED NOT NULL COMMENT 'Промоблок в результатах поиска',
  first_place VARCHAR(255) NOT NULL COMMENT 'Описание услуги',
  price DECIMAL(7,2) NOT NULL COMMENT 'Цена услуги'
  ) COMMENT = 'Услуги продвижения';
  
DROP TABLE IF EXISTS extra_services;
CREATE TABLE extra_services (
  id INT UNSIGNED NOT NULL COMMENT 'Номер дополнительной услуги',
  services_name VARCHAR(50) NOT NULL COMMENT 'Название дополнительной услуги',
  services_description TEXT NOT NULL COMMENT 'Описание дополнительной услуги',
  price DECIMAL(7,2) NOT NULL COMMENT 'Цена дополнительной услуги'
) COMMENT = 'Талица с дополнительными услугами';

DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Номер сообщения',
  from_user_id INT UNSIGNED NOT NULL COMMENT 'Номер отправителя сообщения',
  to_user_id INT UNSIGNED NOT NULL COMMENT 'Номер получателя сообщения',
  body TEXT NOT NULL COMMENT 'Текст сообщения',
  is_delivered BOOLEAN COMMENT 'Статус доставки сообщения',
  created_at DATETIME DEFAULT NOW() COMMENT 'Дата отправления сообщения'
  ) COMMENT = 'Сообщения';
  
DROP TABLE IF EXISTS remove_comment;
CREATE TABLE remove_comment (
  id INT UNSIGNED NOT NULL COMMENT 'Номер причины',
  comment_name VARCHAR(50) COMMENT 'Причина снятия объявления'
  ) COMMENT = 'Список возможных причин снятия объявлений';

DROP TABLE IF EXISTS FAQ;
CREATE TABLE FAQ (
  id INT UNSIGNED NOT NULL COMMENT 'Номер вопроса',
  question_name VARCHAR(255) COMMENT 'Вопрос',
  answer TEXT COMMENT 'Ответ на вопрос'
  ) COMMENT = 'Таблица с часто задаваемыми вопросами';
  
DROP TABLE IF EXISTS wallet_payment;
CREATE TABLE wallet_payment (
  id INT UNSIGNED NOT NULL COMMENT 'Номер способа пополнения кошелька',
  payment_method VARCHAR(50) NOT NULL COMMENT 'Способ пополнения кошелька',
  url_method VARCHAR(255) NOT NULL COMMENT 'Ссылка на сервис пополнения'
  ) COMMENT = 'Пополнение кошелька';
  
DROP TABLE IF EXISTS wallet;
CREATE TABLE wallet (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT 'Номер кошелька',
  user_id INT NOT NULL COMMENT 'Номер пользователя',
  total DECIMAL(11,2) COMMENT 'Сумма кошелька'
  ) COMMENT = 'Кошелёк авито';
  