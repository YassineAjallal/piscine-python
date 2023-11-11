echo '-------------------------------------------------------------'
pip3 --version
echo '-------------------------------------------------------------'
mkdir -p local_lib
export PYTHONPATH="${PYTHONPATH}:/Users/${$USER}/Desktop/piscine-python/python-django/librairies/ex01/local_lib"
pip3 install --target=/Users/$USER/Desktop/piscine-python/python-django/librairies/ex01/local_lib --upgrade --log path.log git+https://github.com/jfavellar90/path.py
python3 test.py