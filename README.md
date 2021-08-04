# sponsokit-search-ui
Influencer Search - Sponsokit challenge

Description: This is a REST API that provides a search endpoint to search over influencers. Influencers are queried from Elasticsearch

Influencers can be searched using any of the two endpoints available depending on preference.
- The first endpoint sends parameters as URL parameters
- The second endpoint sends parameters in JSON format.

Note: You'd need to create an authentication token token and pass it to the search API to search for influencers.

Pagination is currently set to 10 items per response

### Specifications completed
- Token authentication
- Responses paginated and serialized
- Unit test
- Documentation and Readme
- Query multisearch from Elastic Search (can take a text input to search 'channel_display_name' and 'biography' and range of values a range input for follower_count)
- Influencer Search API (with JSON and URL parameter)
- Docker for quick deployment anywhere


#### Run the following commands sequentially to start the project:

    git clone https://github.com/olubiyiontheweb/sponsokit-search-ui.git

    cd sponsokit-search-ui

    python -m venv .venv

    .\venv\Scripts\activate

    pip install -r .\requirements.txt

    uvicorn main:sponsokit_search_ui --host 0.0.0.0 --port 8000

#### Run the project on Docker with:

    docker-compose up -d

or run the command below to rebuild container

    docker-compose up -d --build

#### Execute all tests with the following commands. All tests files are in the "tests" folder incase you need to run them sequentially (you will need set an environment variable SPONSOKIT_ENVIRONMENT='TEST' if you're not using the script)

    python run_tests.py

Visit http://localhost:8000/api/v1/docs to access API documentation