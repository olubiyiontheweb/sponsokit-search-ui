# sponsokit-search-ui
Influencer Search - Sponsokit challenge

### TODO: Reorganize and describe api in readme

### TODO: Remaining part 
- Finalize pytest on search endpoints
- Add pagination
- complete readme file (describe the project and how to set it up).
- Retest project in docker environment and submit

#### Run the project with

    git clone https://github.com/olubiyiontheweb/sponsokit-search-ui.git

    cd sponsokit-search-ui

    python -m venv .venv

    .\venv\Scripts\activate

    pip install -r .\requirements.txt

    uvicorn main:sponsokit_search_ui --host 0.0.0.0 --port 8000 --reload

#### Run the project on Docker with 

    docker-compose up -d

Visit http://localhost:8000/api/v1/docs to access API documentation