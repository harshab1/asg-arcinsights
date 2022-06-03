#!/bin/bash
brew install mysql 
brew services start mysql
mysql_secure_installation
brew services stop mysql
mysql.server start
mysql -u root -p -e "create database stocks_data"
exit