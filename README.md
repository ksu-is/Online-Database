# Online-Database

This program is intended to run a questionnaire that takes users inputs and stores them in an online database for easier manipulation, access and, use of the data. The previous system was paper based and now we are able to use this database to handle the data more efficiently and effectively. 

This program runs in the terminal and allows users to view, insert, update and delete data in the connected SQLite database.

Use your code editor and open it to the folder named "Python Project" in this repository.
Run the "santascaravan.py" file in the terminal and follow the promtpts: 

Welcome to Santa's Carvan Database!

1 to view the data

2 to insert a new data record    

3 to update a data record

4 to delete a data record

X to exit

When entering information do not leave any data questions blank or you will recieve an error message and the data will not save. use "-" for any data that you do not have or do not know.

Once you have finished modifying data you can view the data in a more user friendly interface with the DB Browser program downloaded at https://sqlitebrowser.org/
In DB Browser you can open the "scaravan.db" file from the python project folder to see the information you have input from the terminal. From the DB Browser you can export the data in the tables to a CSV file or JSON to run reports on the data.

In the future as I continue to work on the project I will attempting to make the django survey site work so the data inputting will be much more user friendly and less intimidating to those not familiar with technology. This will also allow for the data input to be run on a server for multiple users to add data at the same time.
