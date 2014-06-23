# Setting up supervisord

[My usual setup of supervisor on WebFaction](http://skipperkongen.dk/2013/01/02/deploying-a-tornado-project-in-production-using-github-and-webfaction/)

* `supervisord`: start supervisor
* `supervisorctl stop|start|restart mytornado`: stop, start, restart the mytornado server
* `supervisorctl shutdown`: Stop supervisord completely and all the processes managed by it.