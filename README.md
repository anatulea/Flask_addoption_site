###  Flask and  SQLite simple application
The code from this application is from the online udemy course by Jose Portilla

Check out the course : [Python and Flask Bootcamp: Create Websites using Flask!](https://www.udemy.com/course/python-and-flask-bootcamp-create-websites-using-flask/)

### Getting Started
1. Fork or clone this repository to your local machine
2. Create the Virtual Environment for the app to help manage dependencies.
    - If you have Anaconda run `conda create --name myenv` in the terminal to create your environment

    - Conda may then ask you to proceed (y/n)? Go ahead and press y to continue.
    - To create an environment with a specific package included: `conda create -n myenv numpy`
    - To create an environment with a specific version of Python you can do: `conda create --name myenv python=3.5`
    - To list out all your environments:`conda env list`

3. Make sure you’ve installed Flask! with `conda install flask` or `pip install flask`
4. Instal dependencies `pip install Flask-WTF` and `pip install -U WTForms` to create forms from our flask python scripts
5. Instal dependencies for database 
    - Flask-SQLAlchemy is an extension that allows for an easy connection of Flask with SQLAlchemy
        `pip install Flask-SQLAlchemy`

    - To migrate changes to database install `pip install Flask-Migrate`


6. Set the FLASK_APP environment Variable
    - MacOS/Linux export `FLASK_APP=adoption_site.py`
    - Windows  `set FLASK_APP=adoption_site.py`

    - Sets up the migrations directory: `flask db init`
    - Sets up the migration file: `flask db migrate -m “some message”`
    - Updates the database with the migration: `flask db upgrade`

7. Run in terminal `python adoption_site.py` and the open the browser at http://127.0.0.1:5000/

