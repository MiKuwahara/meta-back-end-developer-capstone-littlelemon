## 🛠️ Tech Stack (Prerequisites)
- Python
- MySQL
- VS Code
- Insomnia or Postman
- Git & Github

## 📂 Setup Instructions
### 1. Clone repository:
Click the "Code" button and copy the HTTPS URL. Then navigate to your terminal and type the following, replacing the URL with your copied one.

```sh
git clone https://github.com/<username>/<repo-name>.git
```

### 2. Navigate to project directory:
You may have to change directory a few times to get to the project directory called littlelemon.

```sh
cd <folder-name>
```


### 3. Create virtual environment:
Run this command inside the littlelemon where the Pipfile is located.
```
pipenv shell
```
### 4. Install dependencies:
This will install all packages inside the pipfile and creates the Pipfile.lock. 
```sh
pipenv install
```

### 5. Configure MySQL:
Open the settings.py and make changes as necessary to connect to your local database.
```sh

'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'username',
        'PASSWORD': 'password',
```

### 6. Run migrations:

```sh
python manage.py makemigrations
python manage.py migrate

```

### 7. Start server:

```sh
python manage.py runserver
```

## 🔗 API Endpoints (For Testing)
These are the API endpoints and testing can be done using one of your preferred API testing platform.
### 🔐 Authentication
POST /auth/users/ - Register user to get a token to use to login
```sh
{
    "email": "",
    "username": "",
    "password": ""
}
```

POST /auth/token/login/ - Login user


```sh
{
    "username": "",
    "password": ""
}
```

```sh
Authorization Token <token>
```

POST /auth/token/logout/  - Logout user

```sh
Authorization Token <token>
```
### 📋 Menu Items
GET /restaurant/menu/ - Retrieve all menu items. This is a public route, so token is not needed.

GET /restaurant/menu/pk/ - Retrieve a single menu item via its primary key, so don't forget to replace pk with the item's actually key. Example:
```sh
/restaurant/menu/3/
```
### 🪑 Table Bookings
GET /restaurant/booking/ - Retrieve all bookings. This is a protected route, so users must have a token to access it.

```sh
Authorization Token <token>
```
