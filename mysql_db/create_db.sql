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
  
DROP TABLE IF EXISTS user_ad;
CREATE TABLE user_ad (
  user_id INT UNSIGNED NOT NULL);
  
