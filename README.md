# To_Do_App
By design, our app *should be able to*:
  - Create task categories
  - Edit task categories
  - Delete task categories
  - Create tasks
  - Edit tasks
  - Delete tasks
  - Register users
  - Allow to login users in their accounts
  
What can our application do now:
  - [X] Create task categories
  - [ ] Edit task categories
  - [ ] Delete task categories
  - [ ] Create tasks
  - [ ] Edit tasks
  - [ ] Delete tasks
  - [ ] Register users
  - [ ] Allow to login users in their accounts
  
  #
  # Installation
  1. Install all dependences with command:
  ```console
  pip install -r requirments.txt
  ```
  2. create folder <code>project_settings</code> in <code>to_do_list/to_do_list</code> and and inside the <code>project_settings</code> directory
  create <code>settings_for_db.json</code>
  3. Open <code>settings_for_db.json</code> file and write config for database and django settings like this:  
  ```
  { "SECRET_KEY": "Your django's project secret key",
    "NAME": "Name of your db",
    "USER": "User for your db",
    "PASSWORD": "Your db user's password",
    "HOST": "Your host",
    "PORT": "Your port"
 }
 ```
 4. In terminal go to directory ```to_do_list``` (Where ```manage.py``` file) and run command for applying ready-made migrations:  
 ```console
 python manage.py migrate
 ```
 5. In ```to_do_list``` (Where ```settings.py``` file) create ```asgi.py``` and  ```wsgi.py``` files and inside them paste django-generated code like this:  
```python
#asgi.py
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do_list.settings')

application = get_asgi_application()
```
 ```python
#wsgi.py 
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'to_do_list.settings')

application = get_wsgi_application()
 ```
#### Or write your custom code for these files 
6. Run command: 
```console
python manage.py runserver
```
 And use my project
 
 # Releases
 ### V0.1-Pre-Release  
   
 #### In this release implemented:
  - Html templates
  - ```Category``` view
  - Models ```Category```, ```Task```
  - ```Category``` creating
  
 ### V0.1.1-Pre-Release
 
 #### In this release implemented:
  - ```Todos``` view for ```Task``` model
  - Base rendering for ```Todos``` view
  
### V0.1.2-Pre-Release

####  In this release:
  - Created ```todo.html``` to render tasks associated with categories and ```todo.css``` for this html file
  - Css-code for ```category.html``` is placed from ```base.css``` to  ```category.css```
  - In ```views.py``` class ```Todos``` was rewritten, now if you haven't any tasks, in ```todo.html``` a message will be displayed that there are no tasks
#  
