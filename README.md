auswendig-verben
===

Purpose
---
*auswendig-verben* is an application to help me:

    + learn the irregular German verbs
    + work with Test Driven Development
    + design a very simple API
    + work with new frameworks (for me) like Flask
    + work with Javascript


Installation for Development
---

Installation of MongoDB:

    + [MongoDB in ArchLinux](https://wiki.archlinux.org/index.php/MongoDB)
    + I was using *mongo 2.4.4* fyi
    + FIXME puppet recipe with the /etc/mongodb.conf
    + Test it:

        $ mongo
        MongoDB shell version: 2.4.4-pre-
        connecting to: test
        Welcome to the MongoDB shell.
        For interactive help, type "help".
        For more comprehensive documentation, see
        http://docs.mongodb.org/
        Questions? Try the support group
        http://groups.google.com/group/mongodb-user
        > show dbs;
        local   0.078125GB
        > use blah_test;
        switched to db blah_test
        > db.blah_collection.insert({key: 'value'})
        > show dbs;
        blah_test       0.203125GB
        local   0.078125G
        > db.dropDatabase();
        { "dropped" : "blah_test", "ok" : 1 }
        > 



Installation of the Python Virtualenv:

    mkvirtualenv --python=python2.7 auswendig-verben
    pip install -r requirement.pip # inside of the virtualenv

Invocation of the MongoDB test:

    PYTHONPATH='/home/pablo/.virtualenvs/auswendig-verben/lib/python2.7/:/home/pablo/.virtualenvs/auswendig-verben/lib/python2.7/site-packages/:/usr/lib/python2.7/lib-dynload/:/home/pablo/Workspace/auswendig-verben/' python auswendig_verben/verbs.py

