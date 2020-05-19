from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QFileDialog, QMessageBox, QAction, QScrollArea, QHBoxLayout
import sys, os
from PyQt5.QtGui import QIcon
from bb import Ui_Form as W_1
from bb2 import Ui_Form as W_2
from output import Ui_Form as W_3
from question import Ui_Form as W_4

from db_connect import delivery, partner, activities, division, point, palias1, palias2, talias1, talias2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import tuple_, inspect
from sqlalchemy.orm import aliased

# ---------------------------------------Создание соединения с базой данных --------------------------------------------
engine = create_engine('sqlite:///full.db', echo=True)
Base = declarative_base()

Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
zagran_otpr = session.query(point.kod_point.label('kod_point'), point.point.label('point'), point.country.label('country'), point.region.label('region'), \
                            point.category.label('category'), point.direction.label('direction')).join(delivery, delivery.kodstanotprzagran == point.kod_point).subquery()
zagran_naznach = session.query(point.kod_point.label('kod_point'), point.point.label('point'), point.country.label('country'), point.region.label('region'), \
                            point.category.label('category'), point.direction.label('direction')).join(delivery, delivery.kodstannaznachzagran == point.kod_point).subquery()

session.commit()
session.close()
# ----------------------------------- функция вылавливания ошибок ------------------------------------------------------
def log_uncaught_exceptions(ex_cls, ex, tb):
    text = '{}: {}:\n'.format(ex_cls.__name__, ex)
    import traceback
    text += ''.join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, 'Error', text)
    quit()

# --------------------------------------- Инициализация окон Window1, Window2, Window3 ---------------------------------
class Window1(W_1):
    def __init__(self, Form):
        self.setupUi(Form)

class Window2(W_2):
    def __init__(self, form):
        self.setupUi(form)

class Window3(W_3):
    def __init__(self, form):
        self.setupUi(form)

class Window4(W_4):
    def __init__(self, form):
        self.setupUi(form)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.fname = ''


    def closeEvent(self, event):
        if os.path.isfile('tmp_1.txt'):
            os.remove('tmp_1.txt')
        if os.path.isfile('tmp_2.txt'):
            os.remove('tmp_2.txt')
        event.accept()


     # --------------------------------- БЛОК ФУНКЦИЙ !!! WINDOW 1 !!! -------------------------------------------------
    def show_window_1(self):
        self.w1 = QWidget()                                   # открывается окно 1
        self.ui1 = Window1(self.w1)
        self.w1.setWindowTitle('База данных РЖД-2019')
        self.w1.setWindowIcon(QIcon('logo.png'))

        self.w1.setLayout(self.ui1.horizontalLayout)
        self.ui1.layout_SArea = QHBoxLayout(self.ui1.scrollArea)

        self.w1.closeEvent=self.closeEvent
        self.w1.show()

        # -------------------------------------- СИГНАЛЫ PUSH_BUTTON в WINDOW 1  -------------------------------------------
        self.ui1.pbt_go1.clicked.connect(lambda checked,                                                                 # Кнопка1 / Грузоотправитель / Код станции
                                                x=3,
                                                arg1=point.kod_point,
                                                arg2=point.point,
                                                arg3=point.locality,
                                         headers = ['Код станции','Станция','Населенный пункт'],
                                         name_editline = self.ui1.le_go1:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_go2.clicked.connect(lambda checked,                                                                 # Кнопка2 / Грузоотправитель / Станция
                                                x=3,
                                                arg1=point.point,
                                                arg2=point.locality,
                                                arg3=point.country,
                                         headers = ['Станция','Населенный пункт','Страна'],
                                         name_editline = self.ui1.le_go2:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_go3.clicked.connect(lambda checked,                                                                 # Кнопка3 / Грузоотправитель  / Регион
                                                arg1=point.region,
                                         headers = ['Регион'],
                                         name_editline = self.ui1.le_go3:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go4.clicked.connect(lambda checked,                                                                 # Кнопка4 / Грузоотправитель  / Район
                                                arg1=point.district,
                                         headers = ['Район'],
                                         name_editline = self.ui1.le_go4:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go5.clicked.connect(lambda checked,                                                                 # Кнопка5 / Грузоотправитель  / Ближ. насл. пункт
                                                x=3,
                                                arg1=point.locality,
                                                arg2=point.point,
                                                arg3=point.region,
                                         headers = ['Населенный пункт','Станция','Регион'],
                                         name_editline = self.ui1.le_go5:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_go6.clicked.connect(lambda checked,                                                                 # Кнопка6 / Грузоотправитель / Страна
                                                arg1=point.country,
                                         headers = ['Страна'],
                                         name_editline = self.ui1.le_go6:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go7.clicked.connect(lambda checked,                                                                 # Кнопка7 / Грузоотправитель / Рынок
                                                arg1=point.market,
                                         headers = ['Рынок'],
                                         name_editline = self.ui1.le_go7:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go8.clicked.connect(lambda checked,                                                                 # Кнопка8 / Грузоотправитель  / Категория
                                                arg1=point.category,
                                         headers = ['Категория'],
                                         name_editline = self.ui1.le_go8:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go9.clicked.connect(lambda checked,                                                                 # Кнопка9 / Грузоотправитель  / Направл. порт
                                                arg1=point.direction,
                                         headers = ['Направление/Порт'],
                                         name_editline = self.ui1.le_go9:
                                         self.show_window_2_1(arg1, headers, name_editline))

# ------------------------------------------- Грузоотправитель / блок 2 ------------------------------------------------
        self.ui1.pbt_go10.clicked.connect(lambda checked,                                                                # Кнопка10 / Грузоотправитель / Наименование
                                                x=3,
                                                arg1=partner.naimenovanie,
                                                arg2=partner.okpo,
                                                arg3=partner.place,
                                                headers=['Наименование', 'ОКПО', 'Месторасположение'],
                                                name_editline=self.ui1.le_go10:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_go11.clicked.connect(lambda checked,                                                                # Кнопка11 / Грузоотправитель / ОКАТО
                                                x=3,
                                                arg1=partner.okato,
                                                arg2=partner.naimenovanie,
                                                arg3=partner.place,
                                                headers=['ОКАТО', 'Наименование', 'Месторасположение'],
                                                name_editline=self.ui1.le_go11:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_go12.clicked.connect(lambda checked,                                                                # Кнопка12 / Грузоотправитель / ОКВЭД
                                                x=3,
                                                arg1=partner.okved,
                                                arg2=partner.raschif_okved,
                                                arg3=partner.naimenovanie,
                                                headers=['ОКВЕД', 'Расшифровка ОКВЕД', 'Наименование'],
                                                name_editline=self.ui1.le_go12:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_go13.clicked.connect(lambda checked,                                                                # Кнопка13 / Грузоотправитель / Расш. ОКВЭД
                                                arg1=partner.raschif_okved,
                                                headers=['Расшифровка ОКВЕД'],
                                                name_editline=self.ui1.le_go13:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go14.clicked.connect(lambda checked,                                                                # Кнопка14 / Грузоотправитель / ОКОНХ
                                                x=3,
                                                arg1=partner.okonh,
                                                arg2=partner.rasshif_okonh,
                                                arg3=partner.naimenovanie,
                                                headers=['ОКОНХ', 'Расш ОКОНХ', 'Наименование'],
                                                name_editline=self.ui1.le_go14:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_go15.clicked.connect(lambda checked,                                                                # Кнопка15 / Грузоотправитель / Расш. ОКОНХ
                                                 arg1=partner.rasshif_okonh,
                                                 headers=['Расш ОКОНХ'],
                                                 name_editline=self.ui1.le_go15:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go16.clicked.connect(lambda checked,                                                                # Кнопка16 / Грузоотправитель / ИНН
                                                arg1=partner.inn,
                                                headers=['ИНН'],
                                                name_editline=self.ui1.le_go16:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go17.clicked.connect(lambda checked,                                                                # Кнопка17 / Грузоотправитель / Юр. индекс
                                                 arg1=partner.pochtov_indeks,
                                                 headers=['Юр. индекс'],
                                                 name_editline=self.ui1.le_go17:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go18.clicked.connect(lambda checked,                                                                # Кнопка18 / Грузоотправитель / Юр. адрес
                                                arg1=partner.urid_adres,
                                                headers=['Юридический адрес'],
                                                name_editline=self.ui1.le_go18:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go19.clicked.connect(lambda checked,                                                                # Кнопка19 / Грузоотправитель / Юр. телефон
                                                arg1=partner.urid_telefon,
                                                headers=['Юридический телефон'],
                                                name_editline=self.ui1.le_go19:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go20.clicked.connect(lambda checked,                                                                # Кнопка20 / Грузоотправитель / Юр. факс
                                                arg1=partner.urid_faks,
                                                headers=['Юридический факс'],
                                                name_editline=self.ui1.le_go20:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_go21.clicked.connect(lambda checked,                                                                # Кнопка21 / Грузоотправитель / E-mail
                                                 arg1=partner.urid_email,
                                                 headers=['E-Mail'],
                                                 name_editline=self.ui1.le_go21:
                                          self.show_window_2_1(arg1, headers, name_editline))

    # ------------------------------------------- ГРУЗОПОЛУЧАТЕЛЬ / Блок 1 ---------------------------------------------
        self.ui1.pbt_gp1.clicked.connect(lambda checked,                                                                  # Кнопка1 / Грузополучатель / Код станции
                                                x=3,
                                                arg1=point.kod_point,
                                                arg2=point.point,
                                                arg3=point.locality,
                                                headers=['Код станции', 'Станция', 'Населенный пункт'],
                                                name_editline=self.ui1.le_gp1:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_gp2.clicked.connect(lambda checked,                                                                 # Кнопка2 / Грузополучатель / Станция
                                                x=3,
                                                arg1=point.point,
                                                arg2=point.locality,
                                                arg3=point.country,
                                                headers=['Станция', 'Населенный пункт', 'Страна'],
                                                name_editline=self.ui1.le_gp2:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_gp3.clicked.connect(lambda checked,                                                                 # Кнопка3 / Грузополучатель  / Регион
                                                arg1=point.region,
                                                headers=['Регион'],
                                                name_editline=self.ui1.le_gp3:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp4.clicked.connect(lambda checked,                                                                 # Кнопка4 / Грузополучатель  / Район
                                                arg1=point.district,
                                                headers=['Район'],
                                                name_editline=self.ui1.le_gp4:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp5.clicked.connect(lambda checked,                                                                 # Кнопка5 / Грузополучатель  / Ближ. насл. пункт
                                                x=3,
                                                arg1=point.locality,
                                                arg2=point.point,
                                                arg3=point.region,
                                                headers=['Населенный пункт', 'Станция', 'Регион'],
                                                name_editline=self.ui1.le_gp5:
                                         self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_gp6.clicked.connect(lambda checked,                                                                 # Кнопка6 / Грузополучатель / Страна
                                                arg1=point.country,
                                                headers=['Страна'],
                                                name_editline=self.ui1.le_gp6:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp7.clicked.connect(lambda checked,                                                                 # Кнопка7 / Грузополучатель / Рынок
                                                arg1=point.market,
                                                headers=['Рынок'],
                                                name_editline=self.ui1.le_gp7:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp8.clicked.connect(lambda checked,                                                                 # Кнопка8 / Грузополучатель  / Категория
                                                arg1=point.category,
                                                headers=['Категория'],
                                                name_editline=self.ui1.le_gp8:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp9.clicked.connect(lambda checked,                                                                 # Кнопка9 / Грузополучатель  / Направл. порт
                                                arg1=point.direction,
                                                headers=['Направление/Порт'],
                                                name_editline=self.ui1.le_gp9:
                                         self.show_window_2_1(arg1, headers, name_editline))

    # ----------------------------------------------ГРУЗОПОЛУЧАТЕЛЬ / блок 2 -------------------------------------------
        self.ui1.pbt_gp10.clicked.connect(lambda checked,                                                                # Кнопка10 / Грузополучатель / Наименование
                                                 x=3,
                                                 arg1=partner.naimenovanie,
                                                 arg2=partner.okpo,
                                                 arg3=partner.place,
                                                 headers=['Наименование', 'ОКПО', 'Месторасположение'],
                                                 name_editline=self.ui1.le_gp10:
                                          self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_gp11.clicked.connect(lambda checked,                                                                # Кнопка11 / Грузополучатель / ОКАТО
                                                 x=3,
                                                 arg1=partner.okato,
                                                 arg2=partner.naimenovanie,
                                                 arg3=partner.place,
                                                 headers=['ОКАТО', 'Наименование', 'Месторасположение'],
                                                 name_editline=self.ui1.le_gp11:
                                          self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_gp12.clicked.connect(lambda checked,                                                                # Кнопка12 / Грузополучатель / ОКВЭД
                                                 x=3,
                                                 arg1=partner.okved,
                                                 arg2=partner.raschif_okved,
                                                 arg3=partner.naimenovanie,
                                                 headers=['ОКВЕД', 'Расшифровка ОКВЕД', 'Наименование'],
                                                 name_editline=self.ui1.le_gp12:
                                          self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_gp13.clicked.connect(lambda checked,                                                                # Кнопка13 / Грузополучатель / Расш. ОКВЭД
                                                 arg1=partner.raschif_okved,
                                                 headers=['Расшифровка ОКВЕД'],
                                                 name_editline=self.ui1.le_gp13:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp14.clicked.connect(lambda checked,                                                                # Кнопка14 / Грузополучатель / ОКОНХ
                                                 x=3,
                                                 arg1=partner.okonh,
                                                 arg2=partner.rasshif_okonh,
                                                 arg3=partner.naimenovanie,
                                                 headers=['ОКОНХ', 'Расш ОКОНХ', 'Наименование'],
                                                 name_editline=self.ui1.le_gp14:
                                          self.show_window_2(x, arg1, arg2, arg3, headers, name_editline))

        self.ui1.pbt_gp15.clicked.connect(lambda checked,                                                                # Кнопка15 / Грузополучатель / Расш. ОКОНХ
                                                 arg1=partner.rasshif_okonh,
                                                 headers=['Расш ОКОНХ'],
                                                 name_editline=self.ui1.le_gp15:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp16.clicked.connect(lambda checked,                                                                # Кнопка16 / Грузополучатель / ИНН
                                                 arg1=partner.inn,
                                                 headers=['ИНН'],
                                                 name_editline=self.ui1.le_gp16:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp17.clicked.connect(lambda checked,                                                                # Кнопка17 / Грузополучатель / Юр. индекс
                                                 arg1=partner.pochtov_indeks,
                                                 headers=['Юр. индекс'],
                                                 name_editline=self.ui1.le_gp17:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp18.clicked.connect(lambda checked,                                                                # Кнопка18 / Грузополучатель / Юр. адрес
                                                 arg1=partner.urid_adres,
                                                 headers=['Юридический адрес'],
                                                 name_editline=self.ui1.le_gp18:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp19.clicked.connect(lambda checked,                                                                # Кнопка19 / Грузополучатель / Юр. телефон
                                                 arg1=partner.urid_telefon,
                                                 headers=['Юридический телефон'],
                                                 name_editline=self.ui1.le_gp19:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp20.clicked.connect(lambda checked,                                                                # Кнопка20 / Грузополучатель / Юр. факс
                                                 arg1=partner.urid_faks,
                                                 headers=['Юридический факс'],
                                                 name_editline=self.ui1.le_gp20:
                                          self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_gp21.clicked.connect(lambda checked,                                                                # Кнопка21 / Грузополучатель / E-mail
                                                 arg1=partner.urid_email,
                                                 headers=['E-Mail'],
                                                 name_editline=self.ui1.le_gp21:
                                          self.show_window_2_1(arg1, headers, name_editline))

    # ----------------------------------------------ГЛАВНАЯ ФОРМА ------------------------------------------------------
        self.ui1.pbt_tbl1.clicked.connect(lambda checked,                                                                  # Кнопка1 / Форма таблицы / Код клиента
                                                arg1=delivery.kodclienta,
                                                headers=['Код клиента'],
                                                name_editline=self.ui1.le_tbl1:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl2.clicked.connect(lambda checked,                                                                  # Кнопка2 / Форма таблицы / Клиент
                                                arg1=delivery.client,
                                                headers=['Клиент'],
                                                name_editline=self.ui1.le_tbl2:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl3.clicked.connect(lambda checked,                                                                  # Кнопка3 / Форма таблицы / Код отправителя
                                                arg1=delivery.kodotprgruzanashe,
                                                headers=['Код отправителя'],
                                                name_editline=self.ui1.le_tbl3:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl4.clicked.connect(lambda checked,                                                                  # Кнопка4 / Форма таблицы / ОКПО отправителя
                                                arg1=delivery.okpootprnashe,
                                                headers=['ОКПО отправителя'],
                                                name_editline=self.ui1.le_tbl4:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl5.clicked.connect(lambda checked,                                                                  # Кнопка5 / Форма таблицы / Код получателя
                                                arg1=delivery.kodpoluchgruzanashe,
                                                headers=['Код получателя'],
                                                name_editline=self.ui1.le_tbl5:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl6.clicked.connect(lambda checked,                                                                  # Кнопка6 / Форма таблицы / ОКПО получателя
                                                arg1=delivery.okpopoluchnashe,
                                                headers=['ОКПО получателя'],
                                                name_editline=self.ui1.le_tbl6:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl7.clicked.connect(lambda checked,                                                                  # Кнопка7 / Форма таблицы / Код груза
                                                arg1=delivery.kodgruza,
                                                headers=['Код груза'],
                                                name_editline=self.ui1.le_tbl7:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl8.clicked.connect(lambda checked,                                                                  # Кнопка8 / Форма таблицы / Вес груза
                                                arg1=delivery.weight,
                                                headers=['Вес груза'],
                                                name_editline=self.ui1.le_tbl8:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl9.clicked.connect(lambda checked,                                                                  # Кнопка9 / Форма таблицы / Кол-во вагонов
                                                arg1=delivery.kolvovagon,
                                                headers=['Кол-во вагонов'],
                                                name_editline=self.ui1.le_tbl9:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl10.clicked.connect(lambda checked,                                                                  # Кнопка10 / Форма таблицы / Тонно-километры
                                                arg1=delivery.tonnokilomet,
                                                headers=['Тонно-километры'],
                                                name_editline=self.ui1.le_tbl10:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl11.clicked.connect(lambda checked,                                                                  # Кнопка11 / Форма таблицы / Дата отгрузки (день)
                                                arg1=delivery.dayotgr,
                                                headers=['Дата отгрузки (день)'],
                                                name_editline=self.ui1.le_tbl11:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl12.clicked.connect(lambda checked,                                                                  # Кнопка12 / Форма таблицы / Дата отгрузки (месяц)
                                                arg1=delivery.monthotgr,
                                                headers=['Дата отгрузки (месяц)'],
                                                name_editline=self.ui1.le_tbl12:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl13.clicked.connect(lambda checked,                                                                  # Кнопка13 / Форма таблицы / Дата получения (день)
                                                arg1=delivery.daypoluch,
                                                headers=['Дата получения (день)'],
                                                name_editline=self.ui1.le_tbl13:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl14.clicked.connect(lambda checked,                                                                  # Кнопка14 / Форма таблицы / Дата получения (месяц)
                                                arg1=delivery.monthpoluch,
                                                headers=['Дата получения (месяц)'],
                                                name_editline=self.ui1.le_tbl14:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl15.clicked.connect(lambda checked,                                                                  # Кнопка15 / Форма таблицы / Характер перевозок
                                                arg1=delivery.characperev,
                                                headers=['Характер перевозок'],
                                                name_editline=self.ui1.le_tbl15:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl16.clicked.connect(lambda checked,                                                                  # Кнопка16 / Форма таблицы / Продукт
                                                arg1=division.product,
                                                headers=['Продукт'],
                                                name_editline=self.ui1.le_tbl16:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl17.clicked.connect(lambda checked,                                                                  # Кнопка17 / Форма таблицы / Подгруппа
                                                arg1=division.podgruppa,
                                                headers=['Подгруппа'],
                                                name_editline=self.ui1.le_tbl17:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl18.clicked.connect(lambda checked,                                                                  # Кнопка18 / Форма таблицы / Отчётный месяц
                                                arg1=delivery.otchmes,
                                                headers=['Отчётный месяц'],
                                                name_editline=self.ui1.le_tbl18:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl19.clicked.connect(lambda checked,                                                                  # Кнопка19 / Форма таблицы / Год
                                                arg1=delivery.otchgod,
                                                headers=['Год'],
                                                name_editline=self.ui1.le_tbl19:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl20.clicked.connect(lambda checked,                                                                  # Кнопка20 / Форма таблицы / Код ст. отправ. загран.
                                                arg1=delivery.kodstanotprzagran,
                                                headers=['Код ст. отправ. загран.'],
                                                name_editline=self.ui1.le_tbl20:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl21.clicked.connect(lambda checked,                                                                  # Кнопка21 / Форма таблицы / Ст. отправ. загран.
                                                arg1=zagran_otpr.c.point,
                                                headers=['Ст. отправ. загран.'],
                                                name_editline=self.ui1.le_tbl21:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl22.clicked.connect(lambda checked,                                                                  # Кнопка22 / Форма таблицы / Страна отправления
                                                arg1=delivery.countrydeliver,
                                                headers=['Страна отправления'],
                                                name_editline=self.ui1.le_tbl22:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl23.clicked.connect(lambda checked,                                                                  # Кнопка23 / Форма таблицы / Страна отправления ЖД
                                                arg1=zagran_otpr.c.country,
                                                headers=['Страна отправления ЖД'],
                                                name_editline=self.ui1.le_tbl23:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl24.clicked.connect(lambda checked,                                                                  # Кнопка24 / Форма таблицы / Регион отправ. загран.
                                                arg1=zagran_otpr.c.region,
                                                headers=['Регион отправ. загран.'],
                                                name_editline=self.ui1.le_tbl24:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl25.clicked.connect(lambda checked,                                                                  # Кнопка25 / Форма таблицы / Категория отправ. загран.
                                                arg1=zagran_otpr.c.category,
                                                headers=['Категория отправ. загран.'],
                                                name_editline=self.ui1.le_tbl25:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl26.clicked.connect(lambda checked,                                                                  # Кнопка26 / Форма таблицы / Направл/порт. отп. загран.
                                                arg1=zagran_otpr.c.direction,
                                                headers=['Направл/порт. отп. загран.'],
                                                name_editline=self.ui1.le_tbl26:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl27.clicked.connect(lambda checked,                                                                  # Кнопка27 / Форма таблицы / Код ст. назнач. загран.
                                                arg1=delivery.kodstannaznachzagran,
                                                headers=['Код ст. назнач. загран.'],
                                                name_editline=self.ui1.le_tbl27:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl28.clicked.connect(lambda checked,                                                                  # Кнопка28 / Форма таблицы / Ст. назнач. загран.
                                                arg1=zagran_naznach.c.point,
                                                headers=['Ст. назнач. загран.'],
                                                name_editline=self.ui1.le_tbl28:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl29_2.clicked.connect(lambda checked,                                                                  # Кнопка29 / Форма таблицы / Страна назначения
                                                arg1=delivery.countrynaznach,
                                                headers=['Страна назначения'],
                                                name_editline=self.ui1.le_tbl29:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl30_2.clicked.connect(lambda checked,                                                                  # Кнопка30 / Форма таблицы / Страна назначения ЖД
                                                arg1=zagran_naznach.c.country,
                                                headers=['Страна назначения ЖД'],
                                                name_editline=self.ui1.le_tbl30:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl31_2.clicked.connect(lambda checked,                                                                  # Кнопка31 / Форма таблицы / Номер группы продукта
                                                arg1=division.nomer_gruppy,
                                                headers=['Номер группы продукта'],
                                                name_editline=self.ui1.le_tbl31:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl32_2.clicked.connect(lambda checked,                                                                  # Кнопка32 / Форма таблицы / Регион назнач. загран.
                                                arg1=zagran_naznach.c.region,
                                                headers=['Регион назнач. загран.'],
                                                name_editline=self.ui1.le_tbl32:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl33_2.clicked.connect(lambda checked,                                                                  # Кнопка33 / Форма таблицы / Категория назнач. загран.
                                                arg1=zagran_naznach.c.category,
                                                headers=['Категория назнач. загран.'],
                                                name_editline=self.ui1.le_tbl33:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl34_2.clicked.connect(lambda checked,                                                                  # Кнопка34 / Форма таблицы / Направл/порт назн. загран.
                                                arg1=zagran_naznach.c.direction,
                                                headers=['Направл/порт назн. загран.'],
                                                name_editline=self.ui1.le_tbl34:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl35_2.clicked.connect(lambda checked,                                                                  # Кнопка35 / Форма таблицы / Тип вагона1
                                                arg1=delivery.rodvagon1,
                                                headers=['Тип вагона1'],
                                                name_editline=self.ui1.le_tbl35:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl36.clicked.connect(lambda checked,                                                                  # Кнопка36 / Форма таблицы / Тип вагона2
                                                arg1=delivery.rodvagon2,
                                                headers=['Тип вагона2'],
                                                name_editline=self.ui1.le_tbl36:
                                         self.show_window_2_1(arg1, headers, name_editline))

        self.ui1.pbt_tbl137.clicked.connect(lambda checked,                                                                  # Кнопка37 / Форма таблицы / Тип вагона3
                                                arg1=delivery.rodvagon3,
                                                headers=['Тип вагона3'],
                                                name_editline=self.ui1.le_tbl37:
                                         self.show_window_2_1(arg1, headers, name_editline))

    # -------------------------------------- СИГНАЛЫ ГЛАВНЫХ КНОПОК  WINDOW 1 ------------------------------------------
        self.ui1.pbt_m1.clicked.connect(self.empty_errors)                                                               # сигнал кнопки ПОИСК
        self.ui1.pbt_m2.clicked.connect(self.clear_main)                                                                 # сигнал кнопки Стереть
        self.ui1.pbt_m3.clicked.connect(self.memory_check)                                                               # сигнал кнопки Записать
        self.ui1.pbt_m4.clicked.connect(self.memory_extra)                                                               # сигнал кнопки Память



    # ----------------------------------- Проверка на пустую форму -----------------------------------------------------

    def empty_errors(self):
        index, headers, col_index = self.collect_column()
        index_where, text, text_index = self.collect_where()
        db_label_delivery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        db_label_division = [24, 25, 26]
        db_label_partner1 = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        db_label_partner2 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        db_label_point1 = [51, 52, 53, 54, 55, 56, 57, 58, 59]
        db_label_point2 = [60, 61, 62, 63, 64, 65, 66, 67, 68]
        db_label_zagran_otpr = [69, 70, 71, 72, 73]
        db_label_zagran_naznach = [74, 75, 76, 77, 78]
        list = [[], [], [], [], [], [], [], []]
        for n in range(len(text_index)):
            if text_index[n] not in col_index:
                col_index.append(text_index[n])
        for j in range(len(col_index)):
            if col_index[j] in db_label_delivery:
                list[0].append(col_index[j])
            if col_index[j] in db_label_division:
                list[1].append(col_index[j])
            if col_index[j] in db_label_partner1:
                list[2].append(col_index[j])
            if col_index[j] in db_label_partner2:
                list[3].append(col_index[j])
            if col_index[j] in db_label_point1:
                list[4].append(col_index[j])
            if col_index[j] in db_label_point2:
                list[5].append(col_index[j])
            if col_index[j] in db_label_zagran_otpr:
                list[6].append(col_index[j])
            if col_index[j] in db_label_zagran_naznach:
                list[7].append(col_index[j])


        if len(index) == 0:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)

            msg.setWindowTitle("Информация")
            msg.setText("Ошибка")
            msg.setInformativeText("Вы не выбрали ни одного параметра")
            msg.setDetailedText("Выберите хотя бы один параметр и повторите поиск")
            okButton = msg.addButton('Ок', QMessageBox.AcceptRole)
            ret = msg.exec()
        else:
            if len(list[0]) > 0:
                self.show_window_3()
            elif len(list[0]) == 0 and len(list[1]) == 0 and len(list[2]) == 0 and len(list[3]) == 0 and \
                len(list[4]) == 0 and len(list[5]) == 0 and len(list[6]) == 0 and len(list[7]) > 0:
                self.show_window_3()
            elif len(list[0]) == 0 and len(list[7]) == 0 and len(list[2]) == 0 and len(list[3]) == 0 and \
                len(list[4]) == 0 and len(list[5]) == 0 and len(list[6]) == 0 and len(list[1]) > 0:
                self.show_window_3()
            elif len(list[0]) == 0 and len(list[7]) == 0 and len(list[1]) == 0 and len(list[3]) == 0 and \
                len(list[4]) == 0 and len(list[5]) == 0 and len(list[6]) == 0 and len(list[2]) > 0:
                self.show_window_3()
            elif len(list[0]) == 0 and len(list[7]) == 0 and len(list[2]) == 0 and len(list[1]) == 0 and \
                    len(list[4]) == 0 and len(list[5]) == 0 and len(list[6]) == 0 and len(list[3]) > 0:
                self.show_window_3()
            elif len(list[0]) == 0 and len(list[7]) == 0 and len(list[2]) == 0 and len(list[3]) == 0 and \
                    len(list[1]) == 0 and len(list[5]) == 0 and len(list[6]) == 0 and len(list[4]) > 0:
                self.show_window_3()
            elif len(list[0]) == 0 and len(list[7]) == 0 and len(list[2]) == 0 and len(list[3]) == 0 and \
                    len(list[4]) == 0 and len(list[1]) == 0 and len(list[6]) == 0 and len(list[5]) > 0:
                self.show_window_3()
            elif len(list[0]) == 0 and len(list[7]) == 0 and len(list[2]) == 0 and len(list[3]) == 0 and \
                    len(list[4]) == 0 and len(list[5]) == 0 and len(list[1]) == 0 and len(list[6]) > 0:
                self.show_window_3()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)

                msg.setWindowTitle("Информация")
                msg.setText("Ошибка")
                msg.setInformativeText("Выбрано слишком мало параметров")
                msg.setDetailedText("Не возможно согласовать таблицы СТАНЦИИ, ПАРТНЁРЫ, ПРОДУКТЫ. Выберите хотя бы один элемент ФОРМА ТАБЛИЦЫ")
                okButton = msg.addButton('Ок', QMessageBox.AcceptRole)
                ret = msg.exec()



    # -------------------------------------Запоминание введенных данных ------------------------------------------------
    def memory_check(self):
        isChecked = [self.ui1.chb_tbl1.isChecked(), self.ui1.chb_tbl2.isChecked(), self.ui1.chb_tbl3.isChecked(),
                     self.ui1.chb_tbl4.isChecked(), self.ui1.chb_tbl5.isChecked(), self.ui1.chb_tbl6.isChecked(),
                     self.ui1.chb_tbl7.isChecked(), self.ui1.chb_tbl8.isChecked(), self.ui1.chb_tbl9.isChecked(),
                     self.ui1.chb_tbl10.isChecked(), self.ui1.chb_tbl11.isChecked(), self.ui1.chb_tbl12.isChecked(),
                     self.ui1.chb_tbl13.isChecked(), self.ui1.chb_tbl14.isChecked(), self.ui1.chb_tbl15.isChecked(),
                     self.ui1.chb_tbl18.isChecked(), self.ui1.chb_tbl19.isChecked(), self.ui1.chb_tbl20.isChecked(),
                     self.ui1.chb_tbl22.isChecked(), self.ui1.chb_tbl27.isChecked(), self.ui1.chb_tbl29.isChecked(),
                     self.ui1.chb_tbl35.isChecked(), self.ui1.chb_tbl36.isChecked(), self.ui1.chb_tbl37.isChecked(),

                     self.ui1.chb_tbl16.isChecked(), self.ui1.chb_tbl17.isChecked(), self.ui1.chb_tbl31.isChecked(),

                     self.ui1.chb_go10.isChecked(), self.ui1.chb_go11.isChecked(), self.ui1.chb_go12.isChecked(),
                     self.ui1.chb_go13.isChecked(), self.ui1.chb_go14.isChecked(), self.ui1.chb_go15.isChecked(),
                     self.ui1.chb_go16.isChecked(), self.ui1.chb_go17.isChecked(), self.ui1.chb_go18.isChecked(),
                     self.ui1.chb_go19.isChecked(), self.ui1.chb_go20.isChecked(), self.ui1.chb_go21.isChecked(),

                     self.ui1.chb_gp10.isChecked(), self.ui1.chb_gp11.isChecked(), self.ui1.chb_gp12.isChecked(),
                     self.ui1.chb_gp13.isChecked(), self.ui1.chb_gp14.isChecked(), self.ui1.chb_gp15.isChecked(),
                     self.ui1.chb_gp16.isChecked(), self.ui1.chb_gp17.isChecked(), self.ui1.chb_gp18.isChecked(),
                     self.ui1.chb_gp19.isChecked(), self.ui1.chb_gp20.isChecked(), self.ui1.chb_gp21.isChecked(),

                     self.ui1.chb_go1.isChecked(), self.ui1.chb_go2.isChecked(), self.ui1.chb_go3.isChecked(),
                     self.ui1.chb_go4.isChecked(), self.ui1.chb_go5.isChecked(), self.ui1.chb_go6.isChecked(),
                     self.ui1.chb_go7.isChecked(), self.ui1.chb_go8.isChecked(), self.ui1.chb_go9.isChecked(),

                     self.ui1.chb_gp1.isChecked(), self.ui1.chb_gp2.isChecked(), self.ui1.chb_gp3.isChecked(),
                     self.ui1.chb_gp4.isChecked(), self.ui1.chb_gp5.isChecked(), self.ui1.chb_gp6.isChecked(),
                     self.ui1.chb_gp7.isChecked(), self.ui1.chb_gp8.isChecked(), self.ui1.chb_gp9.isChecked(),

                     self.ui1.chb_tbl21.isChecked(), self.ui1.chb_tbl23.isChecked(), self.ui1.chb_tbl24.isChecked(),
                     self.ui1.chb_tbl25.isChecked(), self.ui1.chb_tbl26.isChecked(), self.ui1.chb_tbl28.isChecked(),
                     self.ui1.chb_tbl30.isChecked(), self.ui1.chb_tbl32.isChecked(), self.ui1.chb_tbl33.isChecked(),
                     self.ui1.chb_tbl34.isChecked()
                     ]
        where_list = [self.ui1.le_tbl1.text(), self.ui1.le_tbl2.text(), self.ui1.le_tbl3.text(),
                      self.ui1.le_tbl4.text(), self.ui1.le_tbl5.text(), self.ui1.le_tbl6.text(),
                      self.ui1.le_tbl7.text(), self.ui1.le_tbl8.text(), self.ui1.le_tbl9.text(),
                      self.ui1.le_tbl10.text(), self.ui1.le_tbl11.text(), self.ui1.le_tbl12.text(),
                      self.ui1.le_tbl13.text(), self.ui1.le_tbl14.text(), self.ui1.le_tbl15.text(),
                      self.ui1.le_tbl18.text(), self.ui1.le_tbl19.text(), self.ui1.le_tbl20.text(),
                      self.ui1.le_tbl22.text(), self.ui1.le_tbl27.text(), self.ui1.le_tbl29.text(),
                      self.ui1.le_tbl35.text(), self.ui1.le_tbl36.text(), self.ui1.le_tbl37.text(),

                      self.ui1.le_tbl16.text(), self.ui1.le_tbl17.text(), self.ui1.le_tbl31.text(),

                      self.ui1.le_go10.text(), self.ui1.le_go11.text(), self.ui1.le_go12.text(),
                      self.ui1.le_go13.text(), self.ui1.le_go14.text(), self.ui1.le_go15.text(),
                      self.ui1.le_go16.text(), self.ui1.le_go17.text(), self.ui1.le_go18.text(),
                      self.ui1.le_go19.text(), self.ui1.le_go20.text(), self.ui1.le_go21.text(),

                      self.ui1.le_gp10.text(), self.ui1.le_gp11.text(), self.ui1.le_gp12.text(),
                      self.ui1.le_gp13.text(), self.ui1.le_gp14.text(), self.ui1.le_gp15.text(),
                      self.ui1.le_gp16.text(), self.ui1.le_gp17.text(), self.ui1.le_gp18.text(),
                      self.ui1.le_gp19.text(), self.ui1.le_gp20.text(), self.ui1.le_gp21.text(),

                      self.ui1.le_go1.text(), self.ui1.le_go2.text(), self.ui1.le_go3.text(),
                      self.ui1.le_go4.text(), self.ui1.le_go5.text(), self.ui1.le_go6.text(),
                      self.ui1.le_go7.text(), self.ui1.le_go8.text(), self.ui1.le_go9.text(),

                      self.ui1.le_gp1.text(), self.ui1.le_gp2.text(), self.ui1.le_gp3.text(),
                      self.ui1.le_gp4.text(), self.ui1.le_gp5.text(), self.ui1.le_gp6.text(),
                      self.ui1.le_gp7.text(), self.ui1.le_gp8.text(), self.ui1.le_gp9.text(),

                      self.ui1.le_tbl21.text(), self.ui1.le_tbl23.text(), self.ui1.le_tbl24.text(),
                      self.ui1.le_tbl25.text(), self.ui1.le_tbl26.text(), self.ui1.le_tbl28.text(),
                      self.ui1.le_tbl30.text(), self.ui1.le_tbl32.text(), self.ui1.le_tbl33.text(),
                      self.ui1.le_tbl34.text()
                      ]

        with open('tmp_1.txt', 'w') as f:
            for i in range(len(isChecked)):
                f.write(str(isChecked[i]) +'\n')
        f.close()

        with open('tmp_2.txt', 'w') as f_2:
            for j in range(len(where_list)):
                f_2.write(where_list[j] +'\n')
        f_2.close()



    # -------------------------------------Вывод сохранённых параметров ------------------------------------------------
    def memory_extra(self):
        not_Checked = [self.ui1.chb_tbl1, self.ui1.chb_tbl2, self.ui1.chb_tbl3,
                     self.ui1.chb_tbl4, self.ui1.chb_tbl5, self.ui1.chb_tbl6,
                     self.ui1.chb_tbl7, self.ui1.chb_tbl8, self.ui1.chb_tbl9,
                     self.ui1.chb_tbl10, self.ui1.chb_tbl11, self.ui1.chb_tbl12,
                     self.ui1.chb_tbl13, self.ui1.chb_tbl14, self.ui1.chb_tbl15,
                     self.ui1.chb_tbl18, self.ui1.chb_tbl19, self.ui1.chb_tbl20,
                     self.ui1.chb_tbl22, self.ui1.chb_tbl27, self.ui1.chb_tbl29,
                     self.ui1.chb_tbl35, self.ui1.chb_tbl36, self.ui1.chb_tbl37,

                     self.ui1.chb_tbl16, self.ui1.chb_tbl17, self.ui1.chb_tbl31,

                     self.ui1.chb_go10, self.ui1.chb_go11, self.ui1.chb_go12,
                     self.ui1.chb_go13, self.ui1.chb_go14, self.ui1.chb_go15,
                     self.ui1.chb_go16, self.ui1.chb_go17, self.ui1.chb_go18,
                     self.ui1.chb_go19, self.ui1.chb_go20, self.ui1.chb_go21,

                     self.ui1.chb_gp10, self.ui1.chb_gp11, self.ui1.chb_gp12,
                     self.ui1.chb_gp13, self.ui1.chb_gp14, self.ui1.chb_gp15,
                     self.ui1.chb_gp16, self.ui1.chb_gp17, self.ui1.chb_gp18,
                     self.ui1.chb_gp19, self.ui1.chb_gp20, self.ui1.chb_gp21,

                     self.ui1.chb_go1, self.ui1.chb_go2, self.ui1.chb_go3,
                     self.ui1.chb_go4, self.ui1.chb_go5, self.ui1.chb_go6,
                     self.ui1.chb_go7, self.ui1.chb_go8, self.ui1.chb_go9,

                     self.ui1.chb_gp1, self.ui1.chb_gp2, self.ui1.chb_gp3,
                     self.ui1.chb_gp4, self.ui1.chb_gp5, self.ui1.chb_gp6,
                     self.ui1.chb_gp7, self.ui1.chb_gp8, self.ui1.chb_gp9,

                     self.ui1.chb_tbl21, self.ui1.chb_tbl23, self.ui1.chb_tbl24,
                     self.ui1.chb_tbl25, self.ui1.chb_tbl26, self.ui1.chb_tbl28,
                     self.ui1.chb_tbl30, self.ui1.chb_tbl32, self.ui1.chb_tbl33,
                     self.ui1.chb_tbl34
                     ]
        where_set = [self.ui1.le_tbl1, self.ui1.le_tbl2, self.ui1.le_tbl3,
                      self.ui1.le_tbl4, self.ui1.le_tbl5, self.ui1.le_tbl6,
                      self.ui1.le_tbl7, self.ui1.le_tbl8, self.ui1.le_tbl9,
                      self.ui1.le_tbl10, self.ui1.le_tbl11, self.ui1.le_tbl12,
                      self.ui1.le_tbl13, self.ui1.le_tbl14, self.ui1.le_tbl15,
                      self.ui1.le_tbl18, self.ui1.le_tbl19, self.ui1.le_tbl20,
                      self.ui1.le_tbl22, self.ui1.le_tbl27, self.ui1.le_tbl29,
                      self.ui1.le_tbl35, self.ui1.le_tbl36, self.ui1.le_tbl37,

                      self.ui1.le_tbl16, self.ui1.le_tbl17, self.ui1.le_tbl31,

                      self.ui1.le_go10, self.ui1.le_go11, self.ui1.le_go12,
                      self.ui1.le_go13, self.ui1.le_go14, self.ui1.le_go15,
                      self.ui1.le_go16, self.ui1.le_go17, self.ui1.le_go18,
                      self.ui1.le_go19, self.ui1.le_go20, self.ui1.le_go21,

                      self.ui1.le_gp10, self.ui1.le_gp11, self.ui1.le_gp12,
                      self.ui1.le_gp13, self.ui1.le_gp14, self.ui1.le_gp15,
                      self.ui1.le_gp16, self.ui1.le_gp17, self.ui1.le_gp18,
                      self.ui1.le_gp19, self.ui1.le_gp20, self.ui1.le_gp21,

                      self.ui1.le_go1, self.ui1.le_go2, self.ui1.le_go3,
                      self.ui1.le_go4, self.ui1.le_go5, self.ui1.le_go6,
                      self.ui1.le_go7, self.ui1.le_go8, self.ui1.le_go9,

                      self.ui1.le_gp1, self.ui1.le_gp2, self.ui1.le_gp3,
                      self.ui1.le_gp4, self.ui1.le_gp5, self.ui1.le_gp6,
                      self.ui1.le_gp7, self.ui1.le_gp8, self.ui1.le_gp9,

                      self.ui1.le_tbl21, self.ui1.le_tbl23, self.ui1.le_tbl24,
                      self.ui1.le_tbl25, self.ui1.le_tbl26, self.ui1.le_tbl28,
                      self.ui1.le_tbl30, self.ui1.le_tbl32, self.ui1.le_tbl33,
                      self.ui1.le_tbl34
                      ]
        list = []
        with open('tmp_1.txt', 'r') as f:
            for line in f:
                list.append(line.replace('\n', ''))
            for i in range(len(not_Checked)):
                if list[i] == 'True':
                    not_Checked[i].setChecked(True)
                if list[i] == 'False':
                    not_Checked[i].setChecked(False)
        f.close()

        text_list = []
        with open('tmp_2.txt', 'r') as f_2:
            for line in f_2:
                text_list.append(line.replace('\n', ''))
            for p in range(len(where_set)):
                where_set[p].setText(text_list[p])
        f_2.close()


    # --------------------------------------- ПРОЦЕДУРА СТИРАНИЯ ДАННЫХ С WINDOW 1 -------------------------------------
    def clear_main(self):
        self.ui1.chb_go1.setChecked(False)                                                                               # Удаление ChekBox Грузоотправителя
        self.ui1.chb_go2.setChecked(False)
        self.ui1.chb_go3.setChecked(False)
        self.ui1.chb_go4.setChecked(False)
        self.ui1.chb_go5.setChecked(False)
        self.ui1.chb_go6.setChecked(False)
        self.ui1.chb_go7.setChecked(False)
        self.ui1.chb_go8.setChecked(False)
        self.ui1.chb_go9.setChecked(False)
        self.ui1.chb_go10.setChecked(False)
        self.ui1.chb_go11.setChecked(False)
        self.ui1.chb_go12.setChecked(False)
        self.ui1.chb_go13.setChecked(False)
        self.ui1.chb_go14.setChecked(False)
        self.ui1.chb_go15.setChecked(False)
        self.ui1.chb_go16.setChecked(False)
        self.ui1.chb_go17.setChecked(False)
        self.ui1.chb_go18.setChecked(False)
        self.ui1.chb_go19.setChecked(False)
        self.ui1.chb_go20.setChecked(False)
        self.ui1.chb_go21.setChecked(False)

        self.ui1.chb_gp1.setChecked(False)                                                                               # Удаление ChekBox Грузополучателя
        self.ui1.chb_gp2.setChecked(False)
        self.ui1.chb_gp3.setChecked(False)
        self.ui1.chb_gp4.setChecked(False)
        self.ui1.chb_gp5.setChecked(False)
        self.ui1.chb_gp6.setChecked(False)
        self.ui1.chb_gp7.setChecked(False)
        self.ui1.chb_gp8.setChecked(False)
        self.ui1.chb_gp9.setChecked(False)
        self.ui1.chb_gp10.setChecked(False)
        self.ui1.chb_gp11.setChecked(False)
        self.ui1.chb_gp12.setChecked(False)
        self.ui1.chb_gp13.setChecked(False)
        self.ui1.chb_gp14.setChecked(False)
        self.ui1.chb_gp15.setChecked(False)
        self.ui1.chb_gp16.setChecked(False)
        self.ui1.chb_gp17.setChecked(False)
        self.ui1.chb_gp18.setChecked(False)
        self.ui1.chb_gp19.setChecked(False)
        self.ui1.chb_gp20.setChecked(False)
        self.ui1.chb_gp21.setChecked(False)

        self.ui1.chb_tbl1.setChecked(False)                                                                               # Удаление ChekBox Формы таблицы
        self.ui1.chb_tbl2.setChecked(False)
        self.ui1.chb_tbl3.setChecked(False)
        self.ui1.chb_tbl4.setChecked(False)
        self.ui1.chb_tbl5.setChecked(False)
        self.ui1.chb_tbl6.setChecked(False)
        self.ui1.chb_tbl7.setChecked(False)
        self.ui1.chb_tbl8.setChecked(False)
        self.ui1.chb_tbl9.setChecked(False)
        self.ui1.chb_tbl10.setChecked(False)
        self.ui1.chb_tbl11.setChecked(False)
        self.ui1.chb_tbl12.setChecked(False)
        self.ui1.chb_tbl13.setChecked(False)
        self.ui1.chb_tbl14.setChecked(False)
        self.ui1.chb_tbl15.setChecked(False)
        self.ui1.chb_tbl16.setChecked(False)
        self.ui1.chb_tbl17.setChecked(False)
        self.ui1.chb_tbl18.setChecked(False)
        self.ui1.chb_tbl19.setChecked(False)
        self.ui1.chb_tbl20.setChecked(False)
        self.ui1.chb_tbl21.setChecked(False)
        self.ui1.chb_tbl22.setChecked(False)
        self.ui1.chb_tbl23.setChecked(False)
        self.ui1.chb_tbl24.setChecked(False)
        self.ui1.chb_tbl25.setChecked(False)
        self.ui1.chb_tbl26.setChecked(False)
        self.ui1.chb_tbl27.setChecked(False)
        self.ui1.chb_tbl28.setChecked(False)
        self.ui1.chb_tbl29.setChecked(False)
        self.ui1.chb_tbl30.setChecked(False)
        self.ui1.chb_tbl31.setChecked(False)
        self.ui1.chb_tbl32.setChecked(False)
        self.ui1.chb_tbl33.setChecked(False)
        self.ui1.chb_tbl34.setChecked(False)
        self.ui1.chb_tbl35.setChecked(False)
        self.ui1.chb_tbl36.setChecked(False)
        self.ui1.chb_tbl37.setChecked(False)

        self.ui1.le_go1.setText('')                                                                                      # Удаление lineEdit Грузоотправителя
        self.ui1.le_go2.setText('')
        self.ui1.le_go3.setText('')
        self.ui1.le_go4.setText('')
        self.ui1.le_go5.setText('')
        self.ui1.le_go6.setText('')
        self.ui1.le_go7.setText('')
        self.ui1.le_go8.setText('')
        self.ui1.le_go9.setText('')
        self.ui1.le_go10.setText('')
        self.ui1.le_go11.setText('')
        self.ui1.le_go12.setText('')
        self.ui1.le_go13.setText('')
        self.ui1.le_go14.setText('')
        self.ui1.le_go15.setText('')
        self.ui1.le_go16.setText('')
        self.ui1.le_go17.setText('')
        self.ui1.le_go18.setText('')
        self.ui1.le_go19.setText('')
        self.ui1.le_go20.setText('')
        self.ui1.le_go21.setText('')

        self.ui1.le_gp1.setText('')                                                                                      # Удаление lineEdit Грузополучателя
        self.ui1.le_gp2.setText('')
        self.ui1.le_gp3.setText('')
        self.ui1.le_gp4.setText('')
        self.ui1.le_gp5.setText('')
        self.ui1.le_gp6.setText('')
        self.ui1.le_gp7.setText('')
        self.ui1.le_gp8.setText('')
        self.ui1.le_gp9.setText('')
        self.ui1.le_gp10.setText('')
        self.ui1.le_gp11.setText('')
        self.ui1.le_gp12.setText('')
        self.ui1.le_gp13.setText('')
        self.ui1.le_gp14.setText('')
        self.ui1.le_gp15.setText('')
        self.ui1.le_gp16.setText('')
        self.ui1.le_gp17.setText('')
        self.ui1.le_gp18.setText('')
        self.ui1.le_gp19.setText('')
        self.ui1.le_gp20.setText('')
        self.ui1.le_gp21.setText('')

        self.ui1.le_tbl1.setText('')                                                                                      # Удаление lineEdit Формы таблицы
        self.ui1.le_tbl2.setText('')
        self.ui1.le_tbl3.setText('')
        self.ui1.le_tbl4.setText('')
        self.ui1.le_tbl5.setText('')
        self.ui1.le_tbl6.setText('')
        self.ui1.le_tbl7.setText('')
        self.ui1.le_tbl8.setText('')
        self.ui1.le_tbl9.setText('')
        self.ui1.le_tbl10.setText('')
        self.ui1.le_tbl11.setText('')
        self.ui1.le_tbl12.setText('')
        self.ui1.le_tbl13.setText('')
        self.ui1.le_tbl14.setText('')
        self.ui1.le_tbl15.setText('')
        self.ui1.le_tbl16.setText('')
        self.ui1.le_tbl17.setText('')
        self.ui1.le_tbl18.setText('')
        self.ui1.le_tbl19.setText('')
        self.ui1.le_tbl20.setText('')
        self.ui1.le_tbl21.setText('')
        self.ui1.le_tbl22.setText('')
        self.ui1.le_tbl23.setText('')
        self.ui1.le_tbl24.setText('')
        self.ui1.le_tbl25.setText('')
        self.ui1.le_tbl26.setText('')
        self.ui1.le_tbl27.setText('')
        self.ui1.le_tbl28.setText('')
        self.ui1.le_tbl29.setText('')
        self.ui1.le_tbl30.setText('')
        self.ui1.le_tbl31.setText('')
        self.ui1.le_tbl32.setText('')
        self.ui1.le_tbl33.setText('')
        self.ui1.le_tbl34.setText('')
        self.ui1.le_tbl35.setText('')
        self.ui1.le_tbl36.setText('')
        self.ui1.le_tbl37.setText('')

    def collect_column(self):
        index = []
        col_index = []
        headers = []
        isChecked =[self.ui1.chb_tbl1.isChecked(), self.ui1.chb_tbl2.isChecked(), self.ui1.chb_tbl3.isChecked(),
                    self.ui1.chb_tbl4.isChecked(), self.ui1.chb_tbl5.isChecked(), self.ui1.chb_tbl6.isChecked(),
                    self.ui1.chb_tbl7.isChecked(), self.ui1.chb_tbl8.isChecked(), self.ui1.chb_tbl9.isChecked(),
                    self.ui1.chb_tbl10.isChecked(), self.ui1.chb_tbl11.isChecked(), self.ui1.chb_tbl12.isChecked(),
                    self.ui1.chb_tbl13.isChecked(), self.ui1.chb_tbl14.isChecked(), self.ui1.chb_tbl15.isChecked(),
                    self.ui1.chb_tbl18.isChecked(), self.ui1.chb_tbl19.isChecked(), self.ui1.chb_tbl20.isChecked(),
                    self.ui1.chb_tbl22.isChecked(), self.ui1.chb_tbl27.isChecked(), self.ui1.chb_tbl29.isChecked(),
                    self.ui1.chb_tbl35.isChecked(), self.ui1.chb_tbl36.isChecked(), self.ui1.chb_tbl37.isChecked(),

                    self.ui1.chb_tbl16.isChecked(), self.ui1.chb_tbl17.isChecked(), self.ui1.chb_tbl31.isChecked(),

                    self.ui1.chb_go10.isChecked(), self.ui1.chb_go11.isChecked(), self.ui1.chb_go12.isChecked(),
                    self.ui1.chb_go13.isChecked(), self.ui1.chb_go14.isChecked(), self.ui1.chb_go15.isChecked(),
                    self.ui1.chb_go16.isChecked(), self.ui1.chb_go17.isChecked(), self.ui1.chb_go18.isChecked(),
                    self.ui1.chb_go19.isChecked(), self.ui1.chb_go20.isChecked(), self.ui1.chb_go21.isChecked(),

                    self.ui1.chb_gp10.isChecked(), self.ui1.chb_gp11.isChecked(), self.ui1.chb_gp12.isChecked(),
                    self.ui1.chb_gp13.isChecked(), self.ui1.chb_gp14.isChecked(), self.ui1.chb_gp15.isChecked(),
                    self.ui1.chb_gp16.isChecked(), self.ui1.chb_gp17.isChecked(), self.ui1.chb_gp18.isChecked(),
                    self.ui1.chb_gp19.isChecked(), self.ui1.chb_gp20.isChecked(), self.ui1.chb_gp21.isChecked(),

                     self.ui1.chb_go1.isChecked(), self.ui1.chb_go2.isChecked(), self.ui1.chb_go3.isChecked(),
                     self.ui1.chb_go4.isChecked(), self.ui1.chb_go5.isChecked(), self.ui1.chb_go6.isChecked(),
                     self.ui1.chb_go7.isChecked(), self.ui1.chb_go8.isChecked(), self.ui1.chb_go9.isChecked(),

                    self.ui1.chb_gp1.isChecked(), self.ui1.chb_gp2.isChecked(), self.ui1.chb_gp3.isChecked(),
                    self.ui1.chb_gp4.isChecked(), self.ui1.chb_gp5.isChecked(), self.ui1.chb_gp6.isChecked(),
                    self.ui1.chb_gp7.isChecked(), self.ui1.chb_gp8.isChecked(), self.ui1.chb_gp9.isChecked(),

                    self.ui1.chb_tbl21.isChecked(), self.ui1.chb_tbl23.isChecked(), self.ui1.chb_tbl24.isChecked(),
                    self.ui1.chb_tbl25.isChecked(), self.ui1.chb_tbl26.isChecked(), self.ui1.chb_tbl28.isChecked(),
                    self.ui1.chb_tbl30.isChecked(), self.ui1.chb_tbl32.isChecked(), self.ui1.chb_tbl33.isChecked(),
                    self.ui1.chb_tbl34.isChecked()
                    ]

        db_list = [delivery.kodclienta, delivery.client, delivery.kodotprgruzanashe, delivery.okpootprnashe, delivery.kodpoluchgruzanashe,
                   delivery.okpopoluchnashe, delivery.kodgruza, delivery.weight, delivery.kolvovagon, delivery.tonnokilomet,
                   delivery.dayotgr, delivery.monthotgr, delivery.daypoluch, delivery.monthpoluch, delivery.characperev,
                   delivery.otchmes, delivery.otchgod, delivery.kodstanotprzagran, delivery.countrydeliver, delivery.kodstannaznachzagran,
                   delivery.countrynaznach, delivery.rodvagon1, delivery.rodvagon2, delivery.rodvagon3,

                   division.product, division.podgruppa, division.nomer_gruppy,

                   palias1.naimenovanie, palias1.okato, palias1.okved, palias1.raschif_okved, palias1.okonh,
                   palias1.rasshif_okonh,
                   palias1.inn, palias1.pochtov_indeks, palias1.urid_adres, palias1.urid_telefon, palias1.urid_faks,
                   palias1.urid_email,

                   palias2.naimenovanie, palias2.okato, palias2.okved, palias2.raschif_okved, palias2.okonh,
                   palias2.rasshif_okonh,
                   palias2.inn, palias2.pochtov_indeks, palias2.urid_adres, palias2.urid_telefon, palias2.urid_faks,
                   palias2.urid_email,

                   talias1.kod_point, talias1.point, talias1.region, talias1.district, talias1.locality, talias1.country,
                   talias1.market, talias1.category, talias1.direction,

                   talias2.kod_point, talias2.point, talias2.region, talias2.district, talias2.locality, talias2.country,
                   talias2.market, talias2.category, talias2.direction,

                   zagran_otpr.c.point, zagran_otpr.c.country, zagran_otpr.c.region, zagran_otpr.c.category, zagran_otpr.c.direction,
                   zagran_naznach.c.point, zagran_naznach.c.country, zagran_naznach.c.region, zagran_naznach.c.category, zagran_naznach.c.direction
                   ]

        head = ['Код клиента', 'Клиент', 'Код отправителя', 'ОКПО отправителя', 'Код получателя', 'ОКПО получателя',
                   'Код груза', 'Вес груза', 'Кол-во вагонов', 'Тонно-километры', 'Дата отгрузки (день)',
                   'Дата отгрузки (месяц)', 'Дата получения (день)', 'Дата получения (месяц)', 'Характеристика перевозок',
                   'Отчётный месяц', 'Год', 'Код ст. отправ. загран', 'Страна отправления', 'Код ст. назнач. загран',
                   'Страна назначения', 'Тип вагона1', 'Тип вагона2', 'Тип вагона3',

                'Продукт', 'Подгруппа', 'Номер группы продукта',

                'Наименование', 'ОКАТО', 'ОКВЕД', 'Расшифровка ОКВЕД', 'ОКОНХ', 'Расш ОКОНХ', 'ИНН', 'Юр. индекс',
                'Юридический адрес', 'Юридический телефон', 'Юридический факс', 'E-Mail',

                'Наименование', 'ОКАТО', 'ОКВЕД', 'Расшифровка ОКВЕД', 'ОКОНХ', 'Расш ОКОНХ', 'ИНН', 'Юр. индекс',
                'Юридический адрес', 'Юридический телефон', 'Юридический факс', 'E-Mail',

                   'Код станции', 'Станция', 'Регион', 'Район', 'Населенный пункт', 'Страна', 'Рынок', 'Категория','Направление/Порт',
                   'Код станции', 'Станция', 'Регион', 'Район', 'Населенный пункт', 'Страна', 'Рынок', 'Категория', 'Направление/Порт',

                'Ст. отправ. загран.', 'Страна отправления ЖД', 'Регион отправ. загран.', 'Категория отправ. загран.', 'Направл/порт. отп. загран.',
                'Ст. назнач. загран.', 'Страна назначения ЖД', 'Регион назнач. загран.', 'Категория назнач. загран.', 'Направл/порт назн. загран.'
                   ]

        for i in range(79):
            if isChecked[i] == True:
                col_index.append(i)
                index.append(db_list[i])
                headers.append(head[i])
        return index, headers, col_index

    def collect_where(self):
        text = []
        text_index = []
        index_where = []
        where_list = [self.ui1.le_tbl1.text(), self.ui1.le_tbl2.text(), self.ui1.le_tbl3.text(),
                      self.ui1.le_tbl4.text(), self.ui1.le_tbl5.text(), self.ui1.le_tbl6.text(),
                      self.ui1.le_tbl7.text(), self.ui1.le_tbl8.text(), self.ui1.le_tbl9.text(),
                      self.ui1.le_tbl10.text(), self.ui1.le_tbl11.text(), self.ui1.le_tbl12.text(),
                      self.ui1.le_tbl13.text(), self.ui1.le_tbl14.text(), self.ui1.le_tbl15.text(),
                      self.ui1.le_tbl18.text(), self.ui1.le_tbl19.text(), self.ui1.le_tbl20.text(),
                      self.ui1.le_tbl22.text(), self.ui1.le_tbl27.text(), self.ui1.le_tbl29.text(),
                      self.ui1.le_tbl35.text(), self.ui1.le_tbl36.text(), self.ui1.le_tbl37.text(),

                      self.ui1.le_tbl16.text(), self.ui1.le_tbl17.text(), self.ui1.le_tbl31.text(),

                      self.ui1.le_go10.text(), self.ui1.le_go11.text(), self.ui1.le_go12.text(),
                      self.ui1.le_go13.text(), self.ui1.le_go14.text(), self.ui1.le_go15.text(),
                      self.ui1.le_go16.text(), self.ui1.le_go17.text(), self.ui1.le_go18.text(),
                      self.ui1.le_go19.text(), self.ui1.le_go20.text(), self.ui1.le_go21.text(),

                      self.ui1.le_gp10.text(), self.ui1.le_gp11.text(), self.ui1.le_gp12.text(),
                      self.ui1.le_gp13.text(), self.ui1.le_gp14.text(), self.ui1.le_gp15.text(),
                      self.ui1.le_gp16.text(), self.ui1.le_gp17.text(), self.ui1.le_gp18.text(),
                      self.ui1.le_gp19.text(), self.ui1.le_gp20.text(), self.ui1.le_gp21.text(),

                      self.ui1.le_go1.text(), self.ui1.le_go2.text(), self.ui1.le_go3.text(),
                      self.ui1.le_go4.text(), self.ui1.le_go5.text(), self.ui1.le_go6.text(),
                      self.ui1.le_go7.text(), self.ui1.le_go8.text(), self.ui1.le_go9.text(),

                      self.ui1.le_gp1.text(), self.ui1.le_gp2.text(), self.ui1.le_gp3.text(),
                      self.ui1.le_gp4.text(), self.ui1.le_gp5.text(), self.ui1.le_gp6.text(),
                      self.ui1.le_gp7.text(), self.ui1.le_gp8.text(), self.ui1.le_gp9.text(),

                      self.ui1.le_tbl21.text(), self.ui1.le_tbl23.text(), self.ui1.le_tbl24.text(),
                      self.ui1.le_tbl25.text(), self.ui1.le_tbl26.text(), self.ui1.le_tbl28.text(),
                      self.ui1.le_tbl30.text(), self.ui1.le_tbl32.text(), self.ui1.le_tbl33.text(),
                      self.ui1.le_tbl34.text()
                      ]
        db_list = [delivery.kodclienta, delivery.client, delivery.kodotprgruzanashe, delivery.okpootprnashe, delivery.kodpoluchgruzanashe,
                   delivery.okpopoluchnashe, delivery.kodgruza, delivery.weight, delivery.kolvovagon, delivery.tonnokilomet,
                   delivery.dayotgr, delivery.monthotgr, delivery.daypoluch, delivery.monthpoluch, delivery.characperev,
                   delivery.otchmes, delivery.otchgod, delivery.kodstanotprzagran, delivery.countrydeliver, delivery.kodstannaznachzagran,
                   delivery.countrynaznach, delivery.rodvagon1, delivery.rodvagon2, delivery.rodvagon3,

                   division.product, division.podgruppa, division.nomer_gruppy,

                   palias1.naimenovanie, palias1.okato, palias1.okved, palias1.raschif_okved, palias1.okonh,
                   palias1.rasshif_okonh,
                   palias1.inn, palias1.pochtov_indeks, palias1.urid_adres, palias1.urid_telefon, palias1.urid_faks,
                   palias1.urid_email,

                   palias2.naimenovanie, palias2.okato, palias2.okved, palias2.raschif_okved, palias2.okonh,
                   palias2.rasshif_okonh,
                   palias2.inn, palias2.pochtov_indeks, palias2.urid_adres, palias2.urid_telefon, palias2.urid_faks,
                   palias2.urid_email,

                   talias1.kod_point, talias1.point, talias1.region, talias1.district, talias1.locality, talias1.country,
                   talias1.market, talias1.category, talias1.direction,

                   talias2.kod_point, talias2.point, talias2.region, talias2.district, talias2.locality, talias2.country,
                   talias2.market, talias2.category, talias2.direction,

                   zagran_otpr.c.point, zagran_otpr.c.country, zagran_otpr.c.region, zagran_otpr.c.category, zagran_otpr.c.direction,
                   zagran_naznach.c.point, zagran_naznach.c.country, zagran_naznach.c.region, zagran_naznach.c.category, zagran_naznach.c.direction
                   ]

        for i in range(79):
            if where_list[i] != '':
                text_index.append(i)
                index_where.append(db_list[i])
                add_text = where_list[i].split('/')
                text.append(add_text)


        return index_where, text, text_index


    # ----------------------------- БЛОК ФУНКЦИЙ --- WINDOW 2 --- 3 аргумента ------------------------------------------
    def show_window_2(self, x, arg1, arg2, arg3, headers, name_editline):
        self.w2 = QWidget()                                                                                              # открывается окно 2
        self.ui2 = Window2(self.w2)
        self.w2.setWindowTitle('Окно поиска по '+ str(headers[0]))
        self.w2.setWindowIcon(QIcon('logo.png'))
        self.w2.show()

        self.ui2.tableWidget.setColumnCount(x)                                                                           # задаётся количество колонок для таблицы

        session = Session()

        q = session.query(arg1, arg2, arg3)                                                                              # запрос для заполнения таблицы
        result = q.all()
        self.ui2.tableWidget.setHorizontalHeaderLabels(headers)                                                          # задаётся название колонок
        for row_number, row_data in enumerate(result):                                                                   # заполнение таблицы данными из базы
            self.ui2.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui2.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        header = self.ui2.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        self.ui2.tableWidget.cellDoubleClicked[int, int].connect(self.choose_item)                                       # сигнал для выбора ячейки
        self.ui2.listWidget_2.itemDoubleClicked.connect(self.del_item)                                                   # сигнал для удаления ячейки

        self.ui2.pushButton_2.clicked.connect(self.clear_list)                                                           # сигнал кнопки очистить

        head = []
        head.append(headers[0])
        name_line = self.ui2.lineEdit

        self.ui2.pushButton.clicked.connect(lambda checked, arg1=arg1, head=head, name_line=name_line:
                                            self.show_window_4(arg1, head, name_line))                                   # сигнал кнопки добавить

        self.ui2.pushButton_3.clicked.connect(lambda checked, name_editline=name_editline:                               # сигнал кнопки ОК
                                              self.ad_item_widow1(name_editline))
        session.commit()
        session.close()

    def choose_item(self, row, column):                                                                                  # добавление элементов в лист поиска
        self.ui2.listWidget_2.addItem(self.ui2.tableWidget.item(row, 0).text())

    def choose_item_2(self, row, column):                                                                                # добавление элементов Window4 в лист поиска Window2
        self.ui2.listWidget_2.addItem(self.ui4.tableWidget.item(row, 0).text())

    def del_item(self, item):                                                                                            # убрать элемент из списка по двойному клику мыши
        index = self.ui2.listWidget_2.row(item)
        self.ui2.listWidget_2.takeItem(index)

    def clear_list(self):                                                                                                # очистить список по нажатию кнопки ОЧИСТИТЬ
        self.ui2.listWidget_2.clear()

    def search_listedit_item(self):                                                                                      # Поиск и добавление введённого значения
        search_text = self.ui2.lineEdit.text()
        self.ui2.listWidget_2.addItem(search_text)                                                                       # Добавление в список

    def ad_item_widow1(self, name_editline):                                                                             # добавление выбранных значений в главное окно
        ad_items = ''
        count_listWidget_2 = self.ui2.listWidget_2.count()
        for i in range (count_listWidget_2):
            ad_item = self.ui2.listWidget_2.item(i)
            search = ad_item.text()
            if i == count_listWidget_2-1:
                ad_items += ad_item.text()
            else:
                ad_items += ad_item.text() + '/'
        name_editline.setText(ad_items)
        self.w2.close()

    # -------------------------------- БЛОК ФУНКЦИЙ --- WINDOW 2 --- 1 аргумент ----------------------------------------
    def show_window_2_1(self, arg1, headers, name_editline):
        self.w2 = QWidget()  # открывается окно 2
        self.ui2 = Window2(self.w2)
        self.w2.setWindowTitle('Окно поиска по '+ str(headers[0]))
        self.w2.setWindowIcon(QIcon('logo.png'))
        self.w2.show()

        self.ui2.tableWidget.setColumnCount(1)                                                                           # задаётся количество колонок для таблицы
        session = Session()

        q = session.query(arg1).group_by(arg1)                                                                           # запрос для заполнения таблицы
        result = q.all()
        self.ui2.tableWidget.setHorizontalHeaderLabels(headers)                                                          # задаётся название колонок
        for row_number, row_data in enumerate(result):                                                                   # заполнение таблицы данными из базы
            self.ui2.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui2.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        header = self.ui2.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.ui2.tableWidget.cellDoubleClicked[int, int].connect(self.choose_item)                                       # сигнал для выбора ячейки
        self.ui2.listWidget_2.itemDoubleClicked.connect(self.del_item)                                                   # сигнал для удаления ячейки

        self.ui2.pushButton_2.clicked.connect(self.clear_list)                                                           # сигнал кнопки очистить

        self.ui2.pushButton_3.clicked.connect(lambda checked, name_editline=name_editline:                               # сигнал кнопки ОК
                                                self.ad_item_widow1(name_editline))

        head = []
        head.append(headers[0])
        name_line = self.ui2.lineEdit

        self.ui2.pushButton.clicked.connect(lambda checked, arg1=arg1, head=head, name_line=name_line:
                                            self.show_window_4(arg1, head, name_line))                                           # сигнал кнопки добавить

        session.commit()
        session.close()


    # -------------------------------- БЛОК ФУНКЦИЙ --- WINDOW 4 --- ПОИСК ---------------------------------------------
    def show_window_4(self, arg1, head, name_line):
        self.w4 = QWidget()  # открывается окно 4
        self.ui4 = Window4(self.w4)
        self.w4.setWindowTitle('Пользовательский поиск')
        self.w4.setWindowIcon(QIcon('logo.png'))
        self.w4.show()

        add = '%' + name_line.text() + '%'

        self.ui4.tableWidget.setColumnCount(1)
        session = Session()

        q = session.query(arg1).filter(arg1.like(add)).group_by(arg1)  # запрос для заполнения таблицы
        result = q.all()
        self.ui4.tableWidget.setHorizontalHeaderLabels(head)  # задаётся название колонок
        for row_number, row_data in enumerate(result):  # заполнение таблицы данными из базы
            self.ui4.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui4.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        header = self.ui4.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)

        self.ui4.tableWidget.cellDoubleClicked[int, int].connect(self.choose_item_2)  # сигнал для выбора ячейки

        session.commit()
        session.close()

     # -------------------------- БЛОК ФУНКЦИЙ --- WINDOW 3 ------------------------------------------------------------
    def show_window_3(self):
        self.w3 = QWidget()                                                                                              # открывается окно 3
        self.ui3 = Window3(self.w3)
        self.w3.setWindowTitle('Результаты запроса')
        self.w3.setWindowIcon(QIcon('logo.png'))
        self.w3.show()

        session = Session()

        index, headers, col_index = self.collect_column()
        index_where, text, text_index = self.collect_where()

        i = len(index)

        if i == 0: pass
        if i == 1: query = session.query(index[0])
        if i == 2: query = session.query(index[0], index[1])
        if i == 3: query = session.query(index[0], index[1], index[2])
        if i == 4: query = session.query(index[0], index[1], index[2], index[3])
        if i == 5: query = session.query(index[0], index[1], index[2], index[3], index[4])
        if i == 6: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5])
        if i == 7: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6])
        if i == 8: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7])
        if i == 9: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8])
        if i == 10: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9])
        if i == 11: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10])
        if i == 12: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11])
        if i == 13: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12])
        if i == 14: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13])
        if i == 15: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14])
        if i == 16: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15])
        if i == 17: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16])
        if i == 18: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17])
        if i == 19: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18])
        if i == 20: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19])
        if i == 21: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20])
        if i == 22: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21])
        if i == 23: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22])
        if i == 24: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23])
        if i == 25: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24])
        if i == 26: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25])
        if i == 27: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26])
        if i == 28: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27])
        if i == 29: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28])
        if i == 30: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29])
        if i == 31: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30])
        if i == 32: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31])
        if i == 33: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32])
        if i == 34: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33])
        if i == 35: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34])
        if i == 36: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35])
        if i == 37: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36])
        if i == 38: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37])
        if i == 39: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38])
        if i == 40: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39])
        if i == 41: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40])
        if i == 42: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41])
        if i == 43: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42])
        if i == 44: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43])
        if i == 45: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44])
        if i == 46: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45])
        if i == 47: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46])
        if i == 48: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47])
        if i == 49: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48])
        if i == 50: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49])
        if i == 51: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50])
        if i == 52: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51])
        if i == 53: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52])
        if i == 54: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53])
        if i == 55: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54])
        if i == 56: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55])
        if i == 57: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56])
        if i == 58: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57])
        if i == 59: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58])
        if i == 60: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59])
        if i == 61: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60])
        if i == 62: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61])
        if i == 63: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62])
        if i == 64: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63])
        if i == 65: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64])
        if i == 66: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65])
        if i == 67: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66])
        if i == 68: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67])
        if i == 69: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68])
        if i == 70: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69])
        if i == 71: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70])
        if i == 72: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71])
        if i == 73: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71], index[72])
        if i == 74: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71], index[72], index[73])
        if i == 75: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71], index[72], index[73], index[74])
        if i == 76: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71], index[72], index[73], index[74], index[75])
        if i == 77: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71], index[72], index[73], index[74], index[75], index[76])
        if i == 78: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71], index[72], index[73], index[74], index[75], index[76], index[77])
        if i == 79: query = session.query(index[0], index[1], index[2], index[3], index[4], index[5], index[6], index[7], index[8], index[9], index[10], index[11], index[12], index[13], index[14], index[15], index[16], index[17], index[18], index[19], index[20], index[21], index[22], index[23], index[24], index[25], index[26], index[27], index[28], index[29], index[30], index[31], index[32], index[33], index[34], index[35], index[36], index[37], index[38], index[39], index[40], index[41], index[42], index[43], index[44], index[45], index[46], index[47], index[48], index[49], index[50], index[51], index[52], index[53], index[54], index[55], index[56], index[57], index[58], index[59], index[60], index[61], index[62], index[63], index[64], index[65], index[66], index[67], index[68], index[69], index[70], index[71], index[72], index[73], index[74], index[75], index[76], index[77], index[78])

        db_label_delivery = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
        db_label_division = [24, 25, 26]
        db_label_partner1 = [27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38]
        db_label_partner2 = [39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        db_label_point1 = [51, 52, 53, 54, 55, 56, 57, 58, 59]
        db_label_point2 = [60, 61, 62, 63, 64, 65, 66, 67, 68]
        db_label_zagran_otpr = [69, 70, 71, 72, 73]
        db_label_zagran_naznach = [74, 75, 76, 77, 78]

        list = [[], [], [], [], [], [], [], []]

        for n in range(len(text_index)):
            if text_index[n] not in col_index:
                col_index.append(text_index[n])

        for j in range(len(col_index)):
            if col_index[j] in db_label_delivery:
                list[0].append(col_index[j])
            if col_index[j] in db_label_division:
                list[1].append(col_index[j])
            if col_index[j] in db_label_partner1:
                list[2].append(col_index[j])
            if col_index[j] in db_label_partner2:
                list[3].append(col_index[j])
            if col_index[j] in db_label_point1:
                list[4].append(col_index[j])
            if col_index[j] in db_label_point2:
                list[5].append(col_index[j])
            if col_index[j] in db_label_zagran_otpr:
                list[6].append(col_index[j])
            if col_index[j] in db_label_zagran_naznach:
                list[7].append(col_index[j])

        if len(list[1]) > 0 and len(list[0]) > 0: query = query.join(division, division.kod_produkta == delivery.kodgruza)
        if len(list[2]) > 0 and len(list[0]) > 0: query = query.join(palias1, palias1.okpo == delivery.okpootprnashe)
        if len(list[3]) > 0 and len(list[0]) > 0: query = query.join(palias2, palias2.okpo == delivery.okpopoluchnashe)
        if len(list[4]) > 0 and len(list[0]) > 0: query = query.join(talias1, talias1.kod_point == delivery.kodstanotpr)
        if len(list[5]) > 0 and len(list[0]) > 0: query = query.join(talias2, talias2.kod_point == delivery.kodstannaznach)
        if len(list[6]) > 0 and len(list[0]) > 0: query = query.join(zagran_otpr, zagran_otpr.c.kod_point == delivery.kodstanotprzagran)
        if len(list[7]) > 0 and len(list[0]) > 0: query = query.join(zagran_naznach, zagran_naznach.c.kod_point == delivery.kodstannaznachzagran)


        for k in range(len(index_where)):
            query = query.filter(index_where[k].in_(text[k]))

        result = query.all()


        self.ui3.tableWidget.setColumnCount(i)                # задаётся количество колонок для таблицы
        self.ui3.tableWidget.setHorizontalHeaderLabels(headers)


        for row_number, row_data in enumerate(result):  # заполнение таблицы данными из базы
            self.ui3.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui3.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))

        header = self.ui3.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        session.commit()
        session.close()

     # ____________ !!! СИГНАЛЫ КНОПОК Window3 !!! ____________________________
        self.ui3.pushButton.clicked.connect(lambda checked, headers=headers: self.savefile(headers))              # Сигнал кнопки экспорт в excel
        self.ui3.pushButton_2.clicked.connect(self.w3.close)            # Сигнал кнопки выход

     # _____________!!! ФУНКЦИЯ СОХРАНЕНИЯ ДАННЫХ В EXCEL !!! _____________________
    def savefile(self, headers):                                          # Сохранение данных в файл эксель
        fname, _ = QFileDialog.getSaveFileName(self, 'Save', self.fname, "*.csv")
        if not fname: return
        self.fname = fname
        f = open(fname, 'w')
        for row in range(1):
            tmp = []
            for col in range(len(headers)):
                try:
                    tmp.append(headers[col])
                except:
                    tmp.append('')
            f.write(';'.join(tmp) + '\n')
        for row in range(self.ui3.tableWidget.rowCount()):
            tmp = []
            for col in range(self.ui3.tableWidget.columnCount()):
                try:
                    tmp.append(self.ui3.tableWidget.item(row, col).text())
                except:
                    tmp.append('')
            f.write(';'.join(tmp) + '\n')
        f.close()




app = QApplication(sys.argv)
w = MainWindow()
w.show_window_1()
sys.exit(app.exec_())


