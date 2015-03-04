import os
import sys

from config import *
from cache.cache import *

Bitmessage = getattr(__import__('bitmessage.bitmessage', fromlist=['']), 'Bitmessage')
Collection = getattr(__import__('models.collection', fromlist=['']), 'Collection')
FJMessage = getattr(__import__('backend.datastructures.fj_message', fromlist=['']), 'FJMessage')
Document = getattr(__import__('models.document', fromlist=['']), 'Document')
Keyword = getattr(__import__('models.keyword', fromlist=['']), 'Keyword')
CollectionHandler = getattr(__import__('backend.collection_handler', fromlist=['']), 'CollectionHandler')

