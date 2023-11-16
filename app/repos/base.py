# -*- coding: utf-8 -*-
"""This module implements a base repository for repositories."""
from app.extensions import db
from sqlalchemy.orm.exc import NoResultFound


class BaseRepository:
    """Base repository used for repositories."""
    # pylint: disable=not-callable
    db_model = None
    db_session = db.session

    @classmethod
    def exists(cls, **query):
        """Check if there exists a record in the datastore that matches
        the query.

        Args:
            query: Used to filter records.

        Returns:
            A boolean value (True or False).
        """
        ret = cls.db_session.query(
            cls.db_model.query.filter_by(**query).exists()
        ).scalar()
        return bool(ret)

    @classmethod
    def list(cls, page=1, page_size=50):
        """Get a list of records in the datastore that matches the query.

        Args:
            page: The current page.
            page_size: How many records returned on one page.
        Returns:
            A list of database model instances.
        """
        query = cls.db_model.query
        total = query.count()
        objs = query.offset((page - 1) * page_size).limit(page_size).all()
        return total, objs

    @classmethod
    def get(cls, **query):
        """Get a record in the datastore that matches the query.

        Args:
            query: Used to filter records.

        Returns:
            Instance of a database model.
        """
        try:
            return cls.db_model.query.filter_by(**query).one()
        except NoResultFound:
            return None

    @classmethod
    def save(cls, **kwargs):
        """Save the given object into the datastore.

        Args:
            kwargs: Attributes of the object.

        Returns:
            Instance of a database model.
        """
        obj = cls.db_model(**kwargs)
        cls.db_session.add(obj)
        cls.db_session.commit()
        return obj

    @classmethod
    def update(cls, obj, **kwargs):
        """Update attributes of the given database model instance.

        Args:
            obj: Instance of a database model that you want to update.
            kwargs: Attributes in a dictionary.

        Returns:
            Instance of a database model.
        """
        for k, v in kwargs.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        cls.db_session.commit()
        return obj

    @classmethod
    def delete_by_id(cls, synchronize_session=False, **query):
        """Delete a record that matches the query.

        Args:
            synchronize_session: Set to `True` if you want to update the
                                 attributes on objects in the database session.
            query: Used to filter records.

        Returns:
            Instance of a database model.

        Raises:
            NoResultFound: If no record found with the given query.
        """
        if not synchronize_session:
            ret = cls.db_model.query.filter_by(**query).delete(
                synchronize_session=False)
            cls.db_session.commit()
            return ret
        else:
            try:
                obj = cls.db_model.query.filter_by(**query).one()
                cls.db_session.delete(obj)
                cls.db_session.commit()
                return obj
            except NoResultFound as e:
                raise e
