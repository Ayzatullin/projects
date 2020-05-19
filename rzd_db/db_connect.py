from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import aliased

Base = declarative_base()

# Описание таблиц базы данных

# Таблица основа, в ней содержатся основные сведения о поставках российского топлива за 2019 год
class delivery(Base):
    __tablename__= 'osnova'
    otchgod = Column('Отчгод', Integer)
    otchmes = Column('Отчмес', String)
    kodclienta = Column('Код клиента', Integer, primary_key=True)
    client = Column('Клиент', String)
    kodotprgruzanashe = Column('Код отправителя груза НАШЕ', Integer)
    okpootprnashe = Column('ОКПО отправителя НАШЕ', Integer)
    kodpoluchgruzanashe = Column('Код получателя груза НАШЕ', Integer)
    okpopoluchnashe = Column('ОКПО получателя НАШЕ', Integer)
    weight = Column('Вес', Integer)
    kolvovagon = Column('Количество вагонов', Integer)
    tonnokilomet = Column('Тоннокилометры', Integer)
    dayotgr = Column('День отгрузки', Integer)
    monthotgr = Column('Месяц отгрузки', Integer)
    daypoluch = Column('День получения', Integer)
    monthpoluch = Column('Месяц получения', Integer)
    characperev = Column('Характеристика перевозок', String)
    kodgruza = Column('Код груза', Integer)
    kodstanotpr = Column('Код станции отправления', Integer)
    kodstanotprzagran = Column('Код станции отправления загран', Integer)
    kodcountryotpr = Column('Код страны отправления', Integer)
    countrydeliver = Column('Страна отправления', String)
    kodstannaznach = Column('Код станции назначения', Integer)
    kodstannaznachzagran = Column('Код станции назнач загран', Integer)
    kodstranynaznach = Column('Код страны назначения', Integer)
    countrynaznach = Column('Страна назначения', String)
    rodvagon1 = Column('Род вагона1', String)
    rodvagon2 = Column('Род вагона2', String)
    rodvagon3 = Column('Род вагона3', String)

    def __init__(self, otchgod, otchmes, kodclienta, client, kodotprgruzanashe, okpootprnashe, kodpoluchgruzanashe, \
                 okpopoluchnashe, weight, kolvovagon, tonnokilomet, dayotgr, monthotgr, daypoluch, monthpoluch, characperev, \
                 kodgruza, kodstanotpr, kodstanotprzagran, kodcountryotpr, countrydeliver, kodstannaznach, kodstannaznachzagran, \
                 kodstranynaznach, countrynaznach, rodvagon1, rodvagon2, rodvagon3):
        self.otchgod = otchgod
        self.otchmes = otchmes
        self.kodclienta = kodclienta
        self.client = client
        self.kodotprgruzanashe = kodotprgruzanashe
        self.okpootprnashe = okpootprnashe
        self.kodpoluchgruzanashe = kodpoluchgruzanashe
        self.okpopoluchnashe = okpopoluchnashe
        self.weight = weight
        self.kolvovagon = kolvovagon
        self.tonnokilomet = tonnokilomet
        self.dayotgr = dayotgr
        self.monthotgr = monthotgr
        self.daypoluch = daypoluch
        self.monthpoluch = monthpoluch
        self.characperev = characperev
        self.kodgruza = kodgruza
        self.kodstanotpr = kodstanotpr
        self.kodstanotprzagran = kodstanotprzagran
        self.kodcountryotpr = kodcountryotpr
        self.countrydeliver = countrydeliver
        self.kodstannaznach = kodstannaznach
        self.kodstannaznachzagran = kodstannaznachzagran
        self.kodstranynaznach = kodstranynaznach
        self.countrynaznach = countrynaznach
        self.rodvagon1 = rodvagon1
        self.rodvagon2 = rodvagon2
        self.rodvagon3 = rodvagon3

# Таблица партнёры - справочник организаций
class partner(Base):
    __tablename__ = 'okpo1'
    dat_poluch_dan = Column('Дата получения данных', String)
    kategoriya = Column('Категория', String)
    audit = Column('Аудит', String)
    okpo = Column('ОКПО', Integer, primary_key=True)
    naimenovanie = Column('Наименование', String)
    okato = Column('ОКАТО', String)
    okved = Column('ОКВЕД', String)
    raschif_okved = Column('Расшифровка ОКВЕД', String)
    okonh = Column('ОКОНХ', String)
    rasshif_okonh = Column('Расш ОКОНХ', String)
    inn = Column('ИНН', String)
    place = Column('Месторасположение', String)
    territor_raspolog = Column('Территория расположения (Юридическая)', String)
    dolghnost = Column('Должность', String)
    fio = Column('ФИО', String)
    pochtov_indeks = Column('Почтовый индекс', String)
    urid_adres = Column('Юридический адрес', String)
    urid_telefon = Column('Юридический телефон', String)
    urid_faks = Column('Юридический факс', String)
    urid_email = Column('Юридический E-Mail', String)
    faktich_indeks = Column('Фактический индекс', String)
    faktich_adres = Column('Фактический адрес', String)
    faktich_telefon = Column('Фактический телефон', String)
    faktich_faks = Column('Фактический факс', String)
    email = Column('E-Mail', String)
    status = Column('Статус', String)
    region_faktich = Column('Регион Фактический', String)
    okrug = Column('Округ', String)

    def __init__(self, dat_poluch_dan, kategoriya, audit, okpo, naimenovanie, okato, okved, raschif_okved, okonh, rasshif_okonh, \
                 inn, place, territor_raspolog, dolghnost, fio, pochtov_indeks, urid_adres, urid_telefon, urid_faks, urid_email, \
                 faktich_indeks, faktich_adres, faktich_telefon, faktich_faks, email, status, region_faktich, okrug):
        self.dat_poluch_dan = dat_poluch_dan
        self.kategoriya = kategoriya
        self.audit = audit
        self.okpo = okpo
        self.naimenovanie = naimenovanie
        self.okato = okato
        self.okved = okved
        self.raschif_okved = raschif_okved
        self.okonh = okonh
        self.rasshif_okonh = rasshif_okonh
        self.inn = inn
        self.place = place
        self.territor_raspolog = territor_raspolog
        self.dolghnost = dolghnost
        self.fio = fio
        self.pochtov_indeks = pochtov_indeks
        self.urid_adres = urid_adres
        self.urid_telefon = urid_telefon
        self.urid_faks = urid_faks
        self.urid_email = urid_email
        self.faktich_indeks = faktich_indeks
        self.faktich_adres = faktich_adres
        self.faktich_telefon = faktich_telefon
        self.faktich_faks = faktich_faks
        self.email = email
        self.status = status
        self.region_faktich = region_faktich
        self.okrug = okrug

# Это таблица с расшифровками кодов ОКВЭД
class activities(Base):
     __tablename__ = 'okved'
     okved_okved = Column('ОКВЕД', String, primary_key=True)
     vid_deyatelnosti = Column('Вид деятельности', String)

     def __init__(self, okved_okved, vid_deyatelnosti):
         self.okved_okved = okved_okved
         self.vid_deyatelnosti = vid_deyatelnosti

# Таблица - справочник по продукту
class division(Base):
    __tablename__ = 'classifier'
    metka = Column('метка', String)
    kod_produkta = Column('Код продукта', Integer, primary_key=True)
    podgruppa = Column('Подгруппа', String)
    product = Column('Продукт', String)
    commentarii = Column('Комментарий', String)
    nomer_gruppy = Column('Номер группы', Integer)

    def __init__(self, metka, kod_produkta, podgruppa, product, commentarii, nomer_gruppy):
        self.metka = metka
        self.kod_produkta = kod_produkta
        self.podgruppa = podgruppa
        self.product = product
        self.commentarii = commentarii
        self.nomer_gruppy = nomer_gruppy

# Таблица справочник по станциям отгрузки/назначения
class point(Base):
    __tablename__ = 'station'
    kod_point = Column('Код станции', Integer, primary_key=True)
    point = Column('Станция', String)
    country = Column('Страна', String)
    region = Column('Регион', String)
    district = Column('Район', String)
    locality = Column('Населенный пункт', String)
    market = Column('Рынок', String)
    category = Column('Категория', String)
    direction = Column('Направление/Порт', String)

    def __init__(self, kod_point, point, country, region, district, locality, market, category, direction):
        self.kod_point = kod_point
        self.point = point
        self.country = country
        self.region = region
        self.district = district
        self.locality = locality
        self.market = market
        self.category = category
        self.direction = direction

palias1 = aliased(partner)
palias2 = aliased(partner)

talias1 = aliased(point)
talias2 = aliased(point)


