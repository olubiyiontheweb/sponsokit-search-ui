import logging
from config.config_loader import settings
from fastapi.encoders import jsonable_encoder
from schema.influencer import InfluencerSchema

from elasticsearch import Elasticsearch, AsyncElasticsearch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ElasticSearchQuery:
    """
     Initialize and manage connection to Elasticsearch.
    """

    def __init__(self):
        self.client = AsyncElasticsearch(
            hosts=["https://qcfu7ne0hw:d68q5s6a5k@sponsokit-influence--468124831.eu-central-1.bonsaisearch.net"], timeout=settings.ELASTICSEARCH_TIMEOUT)
        logger.info("Connection session initialized")

    async def search_influencers(self, search_text, page_no, **kwargs):

        query_body = {
            "query": {
                "bool": {
                    "should": [
                    ]
                }
            },
            "from": (page_no - 1) * settings.ELASTICSEARCH_PAGE_SIZE,
            "size": settings.ELASTICSEARCH_PAGE_SIZE
        }

        if search_text:
            query_body["query"]["bool"]["should"].append(
                {"multi_match": {"query": search_text, "fields": ["channel_display_name", "biography"]}})

        if kwargs["min_follower_count"] or kwargs["max_follower_count"]:
            query_body["query"]["bool"]["should"].append(
                {"range": {"follower_count": {
                    "gte": kwargs["min_follower_count"], "lte": kwargs["max_follower_count"]}}}
            )

        # execute search and return only page size
        response = await self.client.search(
            body=query_body, size=settings.ELASTICSEARCH_PAGE_SIZE)

        logger.info("page number: {0}, page size: {1}, length: {2}, previous_page: {3}, next_page: {4}".format(
            page_no, settings.ELASTICSEARCH_PAGE_SIZE, len(response["hits"]["hits"]), settings.ELASTICSEARCH_PAGE_SIZE * (page_no - 1), settings.ELASTICSEARCH_PAGE_SIZE * page_no))

        response = [x["_source"] for x in response["hits"]["hits"]]

        return response


# initiallize elasticsearch connection settings
elastic_search_query = ElasticSearchQuery()
