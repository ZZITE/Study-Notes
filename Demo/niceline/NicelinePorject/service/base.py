#! /usr/bin/env python
# -*- coding: utf-8 -*-
from tornado.log import gen_log


class ModelService(object):
    model = None
    unique = None

    @classmethod
    def get_object_by_id(cls, db_session, obj_id):
        obj = db_session.query(cls.model).get(obj_id)
        return obj

    @classmethod
    def create(cls, db_session, **kwargs):
        if cls.unique_exist(db_session, kwargs.get(cls.unique, None)):
            return {
                "error": 1,
                "message": "object({}) exists".format(cls.unique)
            }

        obj = cls.model(**kwargs)
        db_session.add(obj)
        result = cls.db_flush(db_session)
        if result['error'] == 0:
            result['obj'] = obj
        return result

    @classmethod
    def update(cls, db_session, obj, **kwargs):
        unique_arg = kwargs.get(cls.unique, None)
        if cls.unique and getattr(obj, cls.unique) != unique_arg:
            if cls.unique_exist(db_session, unique_arg):
                return {
                    "error": 1,
                    "message": "object({0}) exists".format(cls.unique)
                }

        for k, v in kwargs.items():
            setattr(obj, k, v)
        return cls.db_flush(db_session)

    @classmethod
    def delete(cls, db_session, obj):
        db_session.delete(obj)
        return cls.db_flush(db_session)

    @classmethod
    def unique_exist(cls, db_session, unique_value):
        if not cls.unique:
            return False
        if unique_value is None:
            return False

        unique_attr = getattr(cls.model, cls.unique)
        exists_query = (db_session.query(unique_attr)
                        .filter(unique_attr == unique_value)
                        .exists())
        exists = db_session.query(exists_query).scalar()
        return exists

    @classmethod
    def db_flush(cls, db_session):
        try:
            db_session.flush()
        except Exception as e:
            message = "database error: {0}-{1}".format(
                type(e).__name__, str(e)
            )
            gen_log.error(message, exc_info=True)
            db_session.rollback()
            return {"error": 2, "message": message}
        else:
            return {"error": 0}