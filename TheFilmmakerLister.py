# The Filmmaker Lister

#importing sqlite3 and connecting to database

import sqlite3
connection = sqlite3.connect("mediamanager.db")
cursor = connection.cursor()

#import linux os calls
import os