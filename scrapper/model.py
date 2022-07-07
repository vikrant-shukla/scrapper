from db.session import get_db
from scrapper.schema import ScrapperSchema

db = get_db()


class ScrapperModel:
    @classmethod
    def create(cls, **kw):
        obj = ScrapperSchema(**kw)
        try:
            db.add(obj)
            db.commit()
            db.refresh(obj)
            return obj
        except Exception as e:
            db.rollback()
            db.close()
            raise e

    @classmethod
    def getdetails(cls, id: str):
        query = db.query(ScrapperSchema).filter(ScrapperSchema.registration_id == str(id)).first()

        return query
