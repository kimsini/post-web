# Post-Web

## Overview
This project was created to manage the device.
Device, Manager, information about changing the device, in other words, we are dealing with information about them.
You can register to write as an administrator on this project.
Authorized administrators can register, add, delete, etc, you can take advantage of a variety of device management functionality, the modified information for the log.

## How to Build "Post-Web"?
### Install them for developing ( Ubuntu 14.04 LTS )
* python 2.7 && pip
* django 1.9.7
* virtualevu

1.  Update your local package index first :

    ```bash
    $ sudo apt-get update && sudo apt-get upgrade
    ```
1. If python is not installed, and then you select the command that that are appropriate for the operating system
   Type it in the console

    ```bash
    Debian or Ubuntu
    $ sudo apt-get install python
    Fedora(~21)
    $ sudo yum install python
    Fedora(22~)
    $ sudo dnf install python
    openSUSE
    $ sudo zypper install python
    ```
2.  Install git to clone this project :

    ```bash
    $ sudo apt-get install git
    ```
3.  Install python-django package & pip :

    ```bash
    $ sudo apt-get install python-django
    $ sudo apt-get install python-pip
    ```
    
4.  Install django & virtualevu :

    ```bash
    $ sudo pip install django
    $ sudo pip install virtualenv
    ```
      If the version is the latest, you can input this command
       ```bash
    $ pip install --upgrade django==1.9.7
       ```
       
5. Clone it:
    ```bash
    $ git clone https://github.com/kimsini/post-web.git
    ```    
    
6. install packages into the isolated environment & Run the server:
    ```bash
    $ cd post-web
    $ source proevu/bin/activate
    $ cd security
    $ python manage.py runserver
   
    ```
    
7. Visit your server's IP address followed by :8000 in your web browser :
    ```bash
    127.0.0.1:8000
    ```
    
8. Enjoy Post-Web

### ThirdParty Libraries
* django -https://www.djangoproject.com/
* jQuery -http://jquery.com/
* Bootstrap -http://getbootstrap.com/
* font-awesome -https://fortawesome.github.io/Font-Awesome/
* javascript -https://www.javascript.com/
* sqlite -https://www.sqlite.org/
