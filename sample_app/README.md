# Ruby on Rails Tutorial (adapted for Django): sample application

I want to learn Django. I've been through the Rails Tutorial before
and found it useful to figure out how all the pieces worked together.
So, I'm going to follow the
[Ruby on Rails Tutorial](http://railstutorial.org), but try to figure
out how to do the equivalent actions in Django. I'm not going to be
100% faithful, just enough to teach my what I'm doing.

Source: Ruby on Rails Tutorial by
[Michael hartl](http://michaelhartl.com).

http://project.adlakeside.com/projects/saleor-dashboard/repository



https://en.exmail.qq.com/cgi-bin/frame_html?sid=1CihemA8dlenXnMt,2&sign_type=&r=4ca056038f745df7e2e2cceede389d2f



https://docs.saleor.io/docs/next/developer/installation/windows
TUE 8:42 AM



https://docs.saleor.io/docs/2.8.0/getting-started/installation-linux/



http://project.adlakeside.com/projects/saleor-django/repository/revisions/master/entry/requirements.txt



requirements.txt = Gemfile
TUE 10:43 AM



python -m venv saleor-venv\
    cd saleor-venv\Scripts\
    activate
    cd ../..
    python -m pip install -r requirements.txt



python -m pip install --upgrade pip



python manage.py migrate
 python manage.py makemigrations
 python manage.py makemigrations purchase
 python manage.py makemigrations transfer
 python manage.py makemigrations chat



seed



http://project.adlakeside.com/projects/saleor-dashboard/wiki/import-data



saleor/settings.py = config/database.yml



http://127.0.0.1:63465/browser/



pg Admin
TUE 1:14 PM



34  cd saleor
    35  cd saleor-dashboard\
    36  npm i
    37  npm audit fix
    38  webpack-dev-server --open -d
    python manage.py createsuperuser
    python manage.py runserver
    npm start



saleor-venv\Scripts\
    activate
    cd ../..
    python manage.py runserver



import dj_database_url
import os.path

DATABASES = {
    "default": dj_database_url.config(
        default="postgres://postgres:password@localhost:5432/saleor1", conn_max_age=600
    )
}

def get_list(text):
    return [item.strip() for item in text.split(",")]


ALLOWED_HOSTS = get_list(os.environ.get("ALLOWED_HOSTS",
                                        "*"
                                        ))



debug python



PyCharm



Eclipse



.env



$API_URI = http://127.0.0.1:8000/graphql/
WED 10:21 AM



C:\Program Files\PostgreSQL\12\bin



https://docs.saleor.io/docs/next/dashboard/index
WED 3:13 PM



queries mutation



schema



CustomizeFB -> List View -> data.precustomer.edges.map -> Backend: schema --> Controller: saleor -> graphql (queries mutation)



saleor magento rails https://awesomeopensource.com/projects/ecommerce
