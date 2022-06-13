#!/bin/bash
if python3 --version ;
then
	pip3 install numpy
	pip3 install flask
	pip3 install flask_jwt
	pip3 install flask_restful
	pip3 install flask_sqlalchemy

else
	echo "No Python3 executable is found. Please install Python3 first"
fi

