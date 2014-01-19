bloggr
======

website blog built in flask

Install
=======

All non app files can be found in the tools folder
Install all the packages in the apt-get file
run pip install virtualenv
change to the directory that you have pulled the code into and then run
     virtualenv env

now install all the packages required for the app
     pip install -r requirements.txt

copy the nginx file ot the sites-available folder in nginx and restart the server
copy the bloggr.conf.init to /etc/init/bloggr.conf
run initctl reload-configuration
run service bloggr restart
