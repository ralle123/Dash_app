# Data Exploration Tool

This data exploration tool flask/plotly-dash application that consist of a couple of tools that can help you view a csv file in a rush.

![Tool-login]()

It contains a Flask-login implementation on top of a Dash application for users authentication.
There are many options for user authentication in Dash, the page you should start reading is ['user authentication'](https://dash.plotly.com/authentication) The basic authentication is a good place to start using, but it provides a limited user interface. If something more involved is needed, Miguel Grinberg has a nice page that talks about ['Flask authenication'](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins) 

The example here using a sqlite database, but it can be changed to use any database by changing the `config.txt` file.

The database has already a user in it, username `raul` and password `test` but you can add more users using the `add_remove_users.ipynb` notebook. To run `add_remove_users.ipynb` simply call it from within Anaconda or go to a commandline interface and run `jupyter notebook` on the folder were the notebook is located and simply open.

### Files description:

`add_remove_users.ipynb`: A jupyter notebook to help creating and removing users<br/>
`config.txt`: configuration file<br/>
`requirements.TXT`: requirements<br/>
`users.db`: sqlite3 database with user information<br/>
`loadfile.py`: A DASH application that runs the application without authentication<br/>

### Running an app locally with authentication

To run an app locally:

1. start by running pip to make sure you have the necesary libraries in your environment `pip install -r requirements.txt`
3. proceed to the folder were you have downloaded the content and run `python app.py`
4. open http://127.0.0.1:5000 in your browser
5. once in the browser window, log into the application.
![login window](https://github.com/ralle123/Dash_app/blob/main/images/login.png)
To try it out, use username `raul` password `test` otherwise use `add_remove_users.ipynb` to add more users.
6. after login in you will reach the landing page.
![landing page](https://github.com/ralle123/Dash_app/blob/main/images/landing_page.png)
Here you can select the csv file you will be working with. You can also see in the upper right part of the page, the user that is logged in. You can also go back to `previous page` 
7. once the `Select Files to Upload` link has been selected, a new window will open so the file on your local machine can be selected. You can use the `GermanDataBinary.csv` file provided to test.
![select file](https://github.com/ralle123/Dash_app/blob/main/images/select_file.png)
![open file](https://github.com/ralle123/Dash_app/blob/main/images/open_file.png)
8. once the file has loaded succesfully, the page will show many new options now
..1. shows the content of the csv that has just been loaded
..2. shows the vertical scroll bar to see the rest of the table page shown on screen
..3. shows the horizontal scroll bar to see the rest of the table page shown on screen
..4. shows the option to change the table page shown on screen
..5. shows a dropdown that contains all the columns from the table   
![file loaded](https://github.com/ralle123/Dash_app/blob/main/images/dropdown.png)
9. a selection from an option in the dropdown will be needed now
![dropdown selection](https://github.com/ralle123/Dash_app/blob/main/images/dropdown_selection.png)
10. once a selection has been done from the dropdownlist, two different types of graphs can show:
a frequency graph if the column selected has categorical values or numerical values that have a unique value <= to 5
![frequency graph](https://github.com/ralle123/Dash_app/blob/main/images/distribution.png) and this will show a representation of how the data is distributed for this column

a distribution graph is shown if the values within the column are numerical values
![distribution graph](https://github.com/ralle123/Dash_app/blob/main/images/distribution2.png) a quick distribution can be observed from the values in the column


### Running an app locally without authentication
steps 6 to 10 from the previous section will be seen here
