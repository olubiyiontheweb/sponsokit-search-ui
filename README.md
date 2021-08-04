# sponsokit-search-ui
Influencer Search - Sponsokit challenge

Description: This is a REST API that provides a search endpoint to search over influencers. Influencers are queried from Elasticsearch

### TODO: Remaining part 
- Finalize pytest on search endpoints
- Add pagination

#### Run the following commands sequentially to start the project:

    git clone https://github.com/olubiyiontheweb/sponsokit-search-ui.git

    cd sponsokit-search-ui

    python -m venv .venv

    .\venv\Scripts\activate

    pip install -r .\requirements.txt

    uvicorn main:sponsokit_search_ui --host 0.0.0.0 --port 8000 --reload

#### Run the project on Docker with:

    docker-compose up -d

#### Execute all tests with the following commands. All tests files are in the "tests" folder incase you need to run them sequentially

    python run_tests.py

Visit http://localhost:8000/api/v1/docs to access API documentation