# WebRedis-Docker

1. Install and activate VENV:  
    #### 1.1 Install venv:
        
        python -m venv venv

    #### 1.2 Activate venv

        Linux:  
            ./venv/Scripts/Activate

        Windows:
            .\venv\Scripts\Activate  

        if it doesn't work then։
        
            Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
            .\venv\Scripts\Activat  
2. Install requirements:
    ```bash
    pip install -r .\requirements.txt

3. Build and running:
    ```bash
    sudo docker-compose up --build

## Usage
    ```bash
    curl -X POST http://localhost:8000/