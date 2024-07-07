**********
https://djangopackages.org/
https://djangopackages.org/packages/p/django-slick-reporting/
django-slick-reporting
https://django-slick-reporting.com/product-sales/

**********
virtualenv -p python ECIP_Admin
cd ECIP_Admin
mkdir src
.\Scripts\activate
cd .\src\
pip install django
django-admin startproject project .
py.exe .\manage.py startapp accounts
py.exe .\manage.py startapp contact
py.exe .\manage.py startapp device
py.exe .\manage.py startapp employee
py.exe .\manage.py startapp product
py.exe .\manage.py startapp ticket

python -m pip install -r requirements.txt

py.exe .\manage.py makemigrations
py.exe .\manage.py migrate
py.exe .\manage.py runserver 192.168.1.204:8500
*******
- frontend template
- virtualenv:
  - creat
  - activate [widows : source ./scripts/activate]
  - pip install
  - deactivate

- upload progect on github

- url : path
- view : logic
- models : db
- templates : frontend




Relations :
    - One-to-Many  [Auther - Posts]          Foreginkey
    - Many-to-Many [Admin_User - Groups]       
    - One-to-One   [User - Profile]

-----------------
** django model queryset
** django template language
** django pagination
** django slug

-----------------

static files : [frontend] images, css, javascript

media files : [upload] images

---------------

- dashboard 
    - count date (tickets, device, employees)
- Export (PDF)
    pip install reportlab
- Export (Excel)  (Done)
    pip install django-import-export
    'import_export', #on settings 
    
- Import (Excel)  (Done)

- Print

-----------------

- Login (Done)
- Logout (Done)
- Profiles (Done)
- Permissions (Done)
- Search (Done)

-----------------
- Calendar
-----------------
- Reports
-----------------

