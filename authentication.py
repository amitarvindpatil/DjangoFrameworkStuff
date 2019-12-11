# Authentication
The Django authentication system handdles both authentication and authrization system.
Django comes with authentication system.It handdles user accounts, groups, permissions and cookies and user session

authentication sys consists of:
-Users
-Permissions: Binary(Yes/NO) flags designing weather user perform certain task
-Groups - A generic way of applying labels and permissions to more than one user
-A configure password hashing system
-Forms and view tools for logging in user or restrincting content
-A pluggable backend system


-The authentication system in Django aims to be very generic and doesn't provide some feature commonly
found web authentication system.Solution for some of these common problem have been implemented in third party packages

-password strangth checking
-Throlling of login attempts
-Authentication aganst third parties
-object Level Permissions


procedure-
-Authentication support is bunddled as Django Contrib Module in "Django.contrib.auth"
-requird  configure already done in setting.py file at the time of Django-admin startproject listed in INSTALLAPPS = []
1-Django.Contrib.AUTH - contains the core of authentication framework, and default models
2-Django.contrib.contenttypes - is django content tyoe system allows permissions to be associate with module you create

-Middleware setting
1-SessionMiddleware - manage session across the request
2.AuthenticationMiddleware - associate user with request using session