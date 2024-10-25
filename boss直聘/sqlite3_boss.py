#! -*-coding: UTF-8 -*-
# @公众号: 海哥python

from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from contextlib import contextmanager

Base = declarative_base()


class SQLAlchemyDB:
    def __init__(self, db_url, echo=False):
        self.engine = create_engine(db_url, echo=echo)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        self.Base = Base

    @contextmanager
    def session_scope(self):
        """提供一个事务范围内的会话"""
        session = self.Session()
        try:
            yield session
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def create_all(self):
        """创建所有表"""
        self.Base.metadata.create_all(self.engine)

    def drop_all(self):
        """删除所有表"""
        self.Base.metadata.drop_all(self.engine)

    def add(self, instance):
        """添加单个实例"""
        with self.session_scope() as session:
            session.add(instance)

    def add_all(self, instances):
        """批量添加实例"""
        with self.session_scope() as session:
            session.add_all(instances)

    def query(self, model, **kwargs):
        """查询数据"""
        with self.session_scope() as session:
            query = session.query(model)
            if kwargs:
                query = query.filter_by(**kwargs)
            return query.all()

    def get(self, model, **kwargs):
        """查询单条记录"""
        with self.session_scope() as session:
            return session.query(model).filter_by(**kwargs).first()

    def update(self, model, filters, updates):
        """更新数据"""
        with self.session_scope() as session:
            session.query(model).filter_by(**filters).update(updates)

    def delete(self, model, **kwargs):
        """删除数据"""
        with self.session_scope() as session:
            session.query(model).filter_by(**kwargs).delete()


# 定义模型
class Job(Base):
    __tablename__ = 'job'
    id = Column(Integer, primary_key=True, comment="job id")
    jobName = Column(String, comment="职位名称")
    cityName = Column(String, comment="城市")
    areaDistrict = Column(String, comment="区")
    brandName = Column(String, comment="公司名")
    salaryDesc = Column(String, comment="薪资范围")
    link = Column(String, comment="详情页链接")
    desc = Column(String, comment="职位描述")
    jobLabels = Column(String, comment="职位标签")
    jobDegree = Column(String, comment="学历")
    brandScaleName = Column(String, comment="公司规模")
    brandStageName = Column(String, comment="公司发展阶段")
    brandIndustry = Column(String, comment="公司行业")


if __name__ == "__main__":
    # 创建数据库实例
    db = SQLAlchemyDB('sqlite:///boss_job.db', echo=True)

    # 创建表
    db.create_all()
