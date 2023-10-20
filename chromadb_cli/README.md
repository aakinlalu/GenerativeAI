# Chromadb on Docker and CLI

## Setup Docker Compose

### 1. Clone Chromadb
```bash
 git clone git@github.com:chroma-core/chroma.git
```

Edit the `docker-compose.yml` and add ALLOW_RESET=TRUE under environment

```yaml
...
    command: uvicorn chromadb.app:app --reload --workers 1 --host 0.0.0.0 --port 8000 --log-config log_config.yml
    environment:
      - IS_PERSISTENT=TRUE
      - ALLOW_RESET=TRUE
    ports:
      - 8000:8000
    ...
```

### 2. Build and Run
```bash
 docker-compose up -d --build
```
## 2. Install dependencies
```bash
 pip install -r requirements.txt
```

## 3. Run CLI

### 3a. Load the document and split it into chunks
```bash
 python chromadb_cli.py load_n_split_doc --filename="https://lilianweng.github.io/posts/2023-06-23-agent/"
```

### 3b. Load the documents into the database
```bash
python chromadb_cli.py load_doc_to_db  --filename="https://lilianweng.github.io/posts/2023-06-23-agent/"
```

### 3c. Perform search
```bash  
python  chromadb_cli.py perform_search  --query=what is Perceptual duplicates? 
```

