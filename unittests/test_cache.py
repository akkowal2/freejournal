import unittest
import datetime
from global_imports import Collection, Document, Keyword
from cache.cache import create_session
import uuid


class TestCache(unittest.TestCase):
    def setUp(self):
        self.session = create_session()

    def tearDown(self):
        self.session.rollback()

    def test_add_collection(self):
        coll_address = str(uuid.uuid1())
        doc_hash_1 = str(uuid.uuid1())
        doc_hash_2 = str(uuid.uuid1())
        coll = Collection(
            title="Test",
            description="This is a collection!",
            merkle="123456789",
            address=coll_address,
            version=1,
            btc="123456789",
            keywords=[
                Keyword(name="Keyword A", id=90909090),
                Keyword(name="Keyword B", id=91919191),
            ],
            documents=[
                Document(
                    description="Test document A",
                    hash=doc_hash_1,
                    title="Test A",
                    ),
                Document(
                    description="Test document B",
                    hash=doc_hash_2,
                    title="Test B",
                    ),
            ],
            creation_date=datetime.datetime.now(),
            oldest_date=datetime.datetime.now()
        )
        self.session.add(coll)
        coll = self.session.query(Collection).filter(Collection.address == coll_address).one()
        self.assertEquals(coll.title, "Test")
        doc = self.session.query(Document).filter(Document.hash == doc_hash_2).one()
        self.assertEquals(doc.title, "Test B")
        key = self.session.query(Keyword).filter(Keyword.id == 90909090).one()
        self.assertEquals(key.name, "Keyword A")
        self.assertTrue(key in coll.keywords)


suite = unittest.TestLoader().loadTestsFromTestCase(TestCache)
unittest.TextTestRunner(verbosity=2).run(suite)
