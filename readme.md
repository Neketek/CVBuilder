# **CVBuilder**

## Description:

This Linux tool is designed to provide an ability to create long single page CVs in pdf format.  It uses HTML/CSS & Jinja2 to create documents layout. CV data is stored in YAML files.  HTML/CSS to PDF conversion is done by wkhtmltopdf tool.  Additionally, the tool utilizes SCSS&Autoprefixer to avoid problems with unsupported CSS properties because wkhtmltopdf uses a fairly old version of WebKit to render web pages to PDF files.

## Dependencies:
1. Docker
2. Make

## Installation:
1. Get Docker
2. Git clone or download the project.
3. CD to the project root directory
4. Run ``make build`` and wait until the image is built.

## Usage:
1. Put your CV data into the ``cv/data`` directory. You can find an example of the data structure for a particular template in ``cv/templates/<template_name>/data-example.yml`` file.
2. Put your photo if you need it into ``cv/data/photo`` directory
3. Run ``make run``
4. Run ``compose <filename without extension> --width <width in cm> --height <height in cm> --template <template folder name>``.
5. Your CV will be stored in ``cv/out`` directory
6. ???
7. PROFIT!!!

## Contribution:
You can contribute by any means. The preferable way is the creation of new CV templates. Take the default template as an example.



## Create Template (HOWTO):
1. Create a new directory under ``cv/templates`` directory. In the end path to it should look like ``cv/templates/<template_name>`` where template_name is a name you chose for your template.
2. Inside template directory create two files ``index.html`` and ``index.scss``. These two will be SCSS and HTML templates entries which composer will use to create HTML/CSS template of your CV.
3. Create ``loc/en.yml`` file. This file should contain default localization.
4. Create ``dataparser.py``. This file should contain function which will receive a loaded data  and return it back after all required modifications are done.
5. Create ``data-example.yml``. This file should contain an example of data for your CV template.
6. ???
7. PROFIT!!! Now you can start the creation of your beautiful CV template. And if you feel generous and opensourcy share a template with a community.

#### data-example.yml
```yaml
# special key which will be replaced by link to your photo
photo: yourphotofilename.png
# special key which will be replaced by corresponding localization data
loc: en
# do not use special keys for CV data
```


#### dataparser.py
```python
def parse(data:dict) -> dict:
  """
  Here you can do anything with CV data.
  Args:
    data: CV data in dict format
  Returns:
    Modified CV data.
  """
  return data
```
