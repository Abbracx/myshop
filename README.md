# myshop
# Application Setup

This is a Django application that integrates Celery for asynchronous task management. Follow the instructions below to set up and run the application.

## Prerequisites

- Python 3.x
- Docker

## Installation

1. **Clone the Repository**:
   ```
    git clone git@github.com:Abbracx/myshop.git
    cd myshop
   ```

2. **Create a Virtual Environment**:
   ```python3 -m venv venv```

3. **Activate the Virtual Environment**:
    - On MAC
    ```source venv/bin/activate```

    - On Windows
    ```venv\Scripts\activate```

4. **Install Required Packages**:
    ```pip install -r requirements.txt```

5. **Install Celery**:

   ```python -m pip install celery==5.4.0```

6. **Pull RabbitMQ Docker Image**:

    ```docker pull rabbitmq:3.13.7-management```

7. **Run RabbitMQ**:

```docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.13.7-management```

8. **Install Flower (for monitoring Celery tasks)**:

```python -m pip install flower==2.0.1```

9. **Start Flower with Basic Auth**:

```celery -A myshop flower --basic-auth=user:pwd```

10. **Alternatively, Start Flower Without Auth**:

```celery -A myshop flower```

    - Access Flower at: http://localhost:5555/

11. **Access RabbitMQ Management Interface**:

    - Open your browser and go to: http://127.0.0.1:15672/ 
    (Default username: ```guest```, Password: ```guest```)

12. **Start Celery**:

```celery -A myshop worker -l info```

13. ***Run Django Development Server**:

```python manage.py runserver```




