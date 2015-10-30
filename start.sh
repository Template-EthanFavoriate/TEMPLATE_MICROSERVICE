#!/usr/bin/python

echo 'Now Setting this entire project for you'

BASEDIR=$(dirname $0)
echo $BASEDIR

pip install $BASEDIR/keplerapp_tb* --upgrade

python $BASEDIR/keplerweb/manage.py syncdb

python $BASEDIR/keplerweb/manage.py runserver 8000