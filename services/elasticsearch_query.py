import logging
from config.config_loader import settings
from elasticsearch_dsl import connections, Search
from fastapi.encoders import jsonable_encoder
from schema.influencer import InfluencerSchema

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ElasticSearchQuery:
    """
     Initialize and manage connection to Elasticsearch.
    """

    def __init__(self):
        self.client = connections.create_connection(
            hosts=settings.ELASTICSEARCH_HOSTS, timeout=settings.ELASTICSEARCH_TIMEOUT)
        logger.info("Connection session initialized")

    async def search_influencers(self, search_text, min_follower_count, max_follower_count, page_no):
        s = Search(using=self.client)
        s.query("multi_match", query=search_text, fields=["channel_display_name", "biography"]).filter(
            "range", follower_count={"gte": min_follower_count, "lte": max_follower_count})

        response = s.execute()

        response = [x.to_dict() for x in response.hits[settings.ELASTICSEARCH_PAGE_SIZE *
                                                       (page_no - 1):settings.ELASTICSEARCH_PAGE_SIZE * page_no]]
        return response


# initiallize elasticsearch connection settings
elastic_search_query = ElasticSearchQuery()
