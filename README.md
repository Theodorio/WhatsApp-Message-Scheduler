# WhatsApp-Message-Scheduler
# Whatsapp Scheduler CLI

Building a CLI app to schedule whatsapp messages and send them automatically once the scheduled time has passed. For example, your app should prompt the user to write a message, their whatsapp number, the recipient’s numberand the time they intend to have it sent out.You can save this data on an SQLite Database.

[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=kahenyaa_WhatsApp-Message-Scheduler&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=kahenyaa_WhatsApp-Message-Scheduler) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=kahenyaa_WhatsApp-Message-Scheduler&metric=vulnerabilities)](https://sonarcloud.io/dashboard?id=kahenyaa_WhatsApp-Message-Scheduler) [![Code Grade](https://www.code-inspector.com/project/136/status/svg)](https://www.code-inspector.com/public/project/136/mygithubproject/dashboard)

https://www.code-inspector.com/project/24468/status/svg




## Features

- Storing Messages in Database
- Send whatsapp messages automatically
- 





##  Installation and setup

First clone this repository to your local machine using 
Checkout into the master branch using git checkout master

Create a virtualenv on your machine and install the dependencies via 

``` pip install -r requirements.txt ```

and activate it. 

cd into the app folder and run
``` python3 send_message.py ```

This file will start run the program in the background, 
the background process is the one responsible for sending whatsapp messages

run

``` python3 view.py ```

This file will open the cli interface where you can register or login into your account, 
a cli will help you navigate through the program with ease. 





## Tech

The project is built using:

- [Python3]


## Tests

To run tests ensure that you are within the virtual environment and have the following installed:

```sh 

   pytest

```

Here is a screen recording of the program

here us a link to a high resolution video https://www.youtube.com/watch?v=TZ-ECS6iwKY

https://user-images.githubusercontent.com/27253931/124198939-7d02e700-dada-11eb-8131-30d7ad07ccd2.mp4



## License

MIT

**Free Software, **

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
