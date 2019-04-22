from datetime import datetime, timezone

import pytest
from sqlalchemy import Column, Integer
from sqlalchemy.exc import StatementError

from oo.sqlalchemy import UTCDateTime
from oo.test.sqlalchemy import db


class Model(db.Base):
    __tablename__ = "models"
    id = Column(Integer, primary_key=True)
    date = Column(UTCDateTime)


db.Base.metadata.create_all(db.engine)


def test_utc_datetime():
    good_user = Model(date=datetime.now(tz=timezone.utc))
    db.session.add(good_user)
    db.session.commit()

    assert db.session.query(Model).get(good_user.id).date.tzinfo is not None

    bad_user = Model(date=datetime.now())
    db.session.add(bad_user)
    with pytest.raises(StatementError):
        db.session.commit()
