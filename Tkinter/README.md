# Python-GUI-Apps
Tkinter Graphical UI Application Scripts for Software Prototyping

The challenge for this project was to create a script connected to Tkinter in order to display a fully functioning software widget app. It would have to convert content from a database to be parsed and launched into a new web browser window. I took the following actions to implement the features below:
* Add new body of text<br>
* Fetch stored content from sqlite3 database<br>
* Display this content in a listbox grid layout<br>
* Ability to select text entries on display and return them in entry field<br>
* Use selected text entries to parse as HTML and automatically open a default web browser window<br>

I created one initial draft of the specs using a pack geometry layout. Then I converted and switched over to a grid geometry layout for more functionality and modularity in selecting/returning the text entries. The final project was converted back to Python 2 for Python 2/3 compatibility using http://python-future.org  - The widget served as a software prototype with a simple UI that is user-centric and easy to navigate.
