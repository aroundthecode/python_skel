Simplest python project skeleton for quick startup.

You can use rename.sh script to rename "myproject" into a more significant name.


## Folder structure:

```
/
|->myproject
  |
  +-> backend - put here your business logic API
  | +-> sample.py find here a sample of biz logic api
  |
  +-> rest - flask code automatically imported to expose backend methods as REST API
  | +-> web_sample.py find here a sample on how to expose rest api with automatic swagger documentation
  |
  +-> utils - common code utils
  |
  +-> cli.py - click code to expose backend methods as CLI commands (find sample biz logic integraton at the bottom of the file)
  +-> web.py - flash / flagger configuration and setup
  ```

## Bootstrapping project 
(using python 3.6+ ):

1) create virtualenv
```
make venv
```

2) activate it
```
source ./venv/bin/activate   
```

3) bootstrap code
```
make bootstrap
```

ready to go!

## CLI interface 
To test CLI interface you can invoke

* help menu
```
myproject-cli -h 
```

* get project version
```
myproject-cli version
```

* invoke sample backend code with default values
```
myproject-cli sample
```

* invoke sample backend code passing arguments
```
myproject-cli sample -n you
```

## WEB interface

first of all start flask webserver 
```
myproject-api
```

you can find a health endpoint at [http://localhost:5000/health](http://localhost:5000/health)

and a swagger interface for all rest/*.py modules at [http://localhost:5000/apidocs](http://localhost:5000/apidocs)

or directly invoke sample API interface at [http://localhost:5000/sample/you](http://localhost:5000/sample/you)

## Running Unit Test

Put your code in tests folder and invoke
```
make test
```

for CLI report or
```
make test_report
```


for HTML report
