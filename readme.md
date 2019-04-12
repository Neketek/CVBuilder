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
1. Put your cv data into the ``cv/data`` directory
2. Put your photo if you need it into ``cv/data/photo`` directory
3. Run ``make run``
4. Run ``compose <filename without extension> --width <width in cm> --height <height in cm> --template <template folder name>``
5. Your CV will be stored in ``cv/out`` directory
6. ???
7. PROFIT!!!

## Contribution:
You can contribute by any means. The preferable way is the creation of new CV templates. Take the default template as an example.
