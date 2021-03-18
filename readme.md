```
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install pytest allure-pytest
pip install plugin_first/ plugin_second/ plugin_third/
python -m pytest --first-option --alluredir=output --trace-config
```