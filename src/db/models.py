from datetime import datetime
from sqlalchemy import create_engine, Column, Float, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
engine = create_engine('sqlite:///db/currency_value.db', echo=False)
Session = sessionmaker(bind=engine)
session = Session()


class Currency(Base):
    __tablename__ = "currency"

    id_pk = Column(Integer, primary_key=True, index=True, autoincrement=True)
    cur_id = Column(Integer)
    cur_abbreviation = Column(String(5))
    cur_scale = Column(Integer)
    cur_name = Column(String(20))
    cur_official_rate = Column(Float)
    date_time = Column(String(30))
    last_query_time = Column(DateTime(),
                             default=datetime.now,
                             onupdate=datetime.now)

    def __repr__(self):
        return f'{self.id_pk}, {self.cur_id}, ' \
               f'{self.cur_abbreviation}, {self.cur_name}, \n' \
               f'{self.cur_scale}, {self.date_time}, {self.last_query_time} \n'


class History(Base):
    __tablename__ = "history_of_query"
    """
    Необходимо переназвать переназвать в соотвенствии с convert.py
    """
    id_pk = Column(Integer, primary_key=True, index=True, autoincrement=True)
    date_and_time = Column(DateTime, default=datetime.now)
    cur_id_convertible = Column(Integer)
    cur_abbreviation_convertible = Column(String(5))
    cur_scale_convertible = Column(Integer)
    cur_name_convertible = Column(String(20))
    cur_official_rate_convertible = Column(Float)
    cur_id_wanted = Column(Integer)
    cur_abbreviation_wanted = Column(String(5))
    cur_scale_wanted = Column(Integer)
    cur_name_wanted = Column(String(20))
    cur_official_rate_wanted = Column(Float)
    actual_curs_date = Column(String(30))
    convertible_amount = Column(Float)
    wanted_currency_result = Column(Float)

    def __str__(self):
        return f'{self.id_pk:^5}|' \
               f'{str(self.date_and_time):^26}|' \
               f'{self.cur_id_convertible:^24}|' \
               f'{self.cur_abbreviation_convertible:^33}|' \
               f'{self.cur_scale_convertible:^18}|' \
               f'{self.cur_name_convertible:^20}|' \
               f'{self.cur_official_rate_convertible:^11}|' \
               f'{self.cur_id_wanted:^24}|' \
               f'{self.cur_abbreviation_wanted:^33}|' \
               f'{self.cur_scale_wanted:^18}|' \
               f'{self.cur_name_wanted:^20}|' \
               f'{self.cur_official_rate_wanted:^11}|' \
               f'{self.actual_curs_date:^21}|' \
               f'{self.convertible_amount:^18}|' \
               f'{self.wanted_currency_result:^9};\n'


Base.metadata.create_all(engine)
