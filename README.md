# Data Exploration Tool

This is a data exploration tool flask/plotly-dash application that consists of a couple of tools that can help you view a csv file in a rush.

![load file tool](https://github.com/ralle123/Dash_app/blob/main/images/load_file.png)

It contains a Flask-login implementation on top of a Dash application for user authentication.
There are many options for user authentication in Dash. Start by reading ['user authentication'](https://dash.plotly.com/authentication) The basic authentication is a good place to start, but it provides a limited user interface. If something more involved is needed, Miguel Grinberg has a great page that talks about ['Flask authenication'](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins) 

The example here uses a sqlite database, but it can be changed to use any database by changing the `config.txt` file.

The database already has a user in it, username `raul` and password `test` but you can add more users using the `add_remove_users.ipynb` notebook. To run `add_remove_users.ipynb` simply call it from within Anaconda or go to a commandline interface and run `jupyter notebook` on the folder where the notebook is located and simply open.

### Files description:

`add_remove_users.ipynb`: A jupyter notebook to help creating and removing users<br/>
`config.txt`: configuration file<br/>
`requirements.TXT`: requirements<br/>
`users.db`: sqlite3 database with user information<br/>
`loadfile.py`: A DASH application that runs the application without authentication<br/>

### Running an app locally with authentication

To run an app locally:

1. Start by running pip to make sure you have the necesary libraries in your environment `pip install -r requirements.txt`
3. Proceed to the folder where you have downloaded the content and run `python app.py`
4. Open http://127.0.0.1:5000 in your browser
5. Once in the browser window, log into the application.
![login window](https://github.com/ralle123/Dash_app/blob/main/images/login.png)
To try it out, use username `raul` password `test` otherwise use `add_remove_users.ipynb` to add more users.
6. After login in, you will reach the landing page.
![landing page](https://github.com/ralle123/Dash_app/blob/main/images/landing_page.png)
Here you can select the csv file you will be working with. You can also see the user that is logged in in the upper right part of the page. You can also go back to `previous page` 
7. Once the `Select Files to Upload` link has been selected, a new window will open so the file on your local machine can be selected. You can use the `GermanDataBinary.csv` file provided to test.
![select file](https://github.com/ralle123/Dash_app/blob/main/images/select_file.png)
![open file](https://github.com/ralle123/Dash_app/blob/main/images/open_file.png)
8. Once the file has loaded succesfully, the page will show many new options
- 1. shows the content of the csv that has just been loaded
- 2. shows the vertical scroll bar to see the rest of the table page shown on screen
- 3. shows the horizontal scroll bar to see the rest of the table page shown on screen
- 4. shows the option to change the table page shown on screen
- 5. shows a dropdown that contains all the columns from the table   
![file loaded](https://github.com/ralle123/Dash_app/blob/main/images/dropdown.png)
9. A selection from an option in the dropdown will be needed now
![dropdown selection](https://github.com/ralle123/Dash_app/blob/main/images/dropdown_selection.png)
10. Once a selection has been made from the dropdownlist, two different types of graphs can show:
a frequency graph if the column selected has categorical values or numerical values that have a unique value <= to 5
![frequency graph](https://github.com/ralle123/Dash_app/blob/main/images/distribution.png) and this will show a representation of how the data is distributed for this column

a distribution graph is shown if the values within the column are numerical values
![distribution graph](https://github.com/ralle123/Dash_app/blob/main/images/distribution2.png) a quick distribution can be observed from the values in the column


### Running an app locally without authentication
Steps 6 to 10 from the previous section will be seen here

### Things that are needed
- More time to fix the css
- More time to add the option of changing column values based the the type of value found
