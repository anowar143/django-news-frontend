
# Django-news-Frontend
> As a django beginer project.
---

## Features


#### News category 

* National
* International
* Entertainment
* Lifestyle
* Art Literature
* Sport
* Other
---

#### Name of App
* List of Category 
---

#### Used Technologies
* Docker
* Python
* Django
* Pillow
* PostgreSQL
* Redis

---
## installation

#### Linux
#### Step 1
```
install Docker & Docker-compose
install virtualenv
create env
workon env
git clone https://github.com/anowar143/drf-news-api.git
pip install -r requirements.txt
```
---
#### Step 2

```
docker-compose up --build
```
---

#### Step 3

```
docker-compose exec app bash
cd src
./manage.py makemigrations
./manage.py migrate
```
