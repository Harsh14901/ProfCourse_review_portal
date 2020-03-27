# Prof and Course Review Portal
A review portal for the professors and courses of IITD. This portal will help IITD students help while selecting a professor and course for their semester.

## Dependencies

This project uses the Django Framework for implementing the backend functionalities 
It can be easily installed using the following command `pip3 install django` . Further there are some addons that need to be installed for proper functionalities of the portal. The are listed below

 - The `django-allauth` module to enable social media authentication.
   Install it using `pip3 install django-allauth`
 -  The `duration widget` to help entering duration input for the admin interface. Install it using `pip3 install django-durationwidget`.
  

## Usage
 1.  Clone the repository and rename the parent folder to `RateProf` instead of the default name.
 2. Use `cd` to enter the directory
 3. When inside the directory `RateProf` that you have just renamed, in the terminal run the following command `python3 manage.py runserver` This will host a server on the port 8000 of localhost 
 4. Open your favourite browser and enter [http://127.0.0.1:8000/rate/index](http://127.0.0.1:8000/rate/index) and hit enter to access the homepage of the Web-App.

Now browse the website using the UI provided (it is kind of minimalistic right now). Kindly bear with it. To test out the features you might need to keep a few points in mind.

 - The admin page can be accessed using the URL  [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) it has the username `admin` and password `admin`
 - 10 users have been populated with usernames `user1,user2,...user10`. Each user has the same password as `password@123`.
 - The Web-App has been populated with dummy data for testing purposes. Hence the professors webpage and email adresses are dummy ones. Kindly ignore if they do not open. Also the Likes, Dislikes of a review and Credibility of a user have been simulated through a script.

**Note :** *All dummy characters appearing in this web-app are fictitious. Any resemblance to real persons, living or dead, is purely coincidental*


# Implementation

This section aims to explain the implementation of the back end of the project.

## Models
When you login as `admin` you will be able to see a list of models available to you. 
It has various sections as follows

 1. ACCOUNTS
 2. AUTHENTICATION AND AUTHORIZATION
 3. RATE
 4. SITES
 5. SOCIAL ACCOUNTS

The main section is `RATE`. It consists of all the primary models required for the app.
The `RATE` section contains the following models:

 1. **Depts** - It is a model to represent the departments available at IITD
 2. **Courses** - It is a model to represent the courses at IITD. It consists of the following fields `Department, Course Code, Course Title`
 3. **Professors** - It is a model to represent the professors of IITD. It consists of the following fields `Department, Prof name, Email, Webpage`
 4. **Reviews** - It is a model to represent the reviews given by a user. It consists of the following fields `Prof, Course, User, Rating details ` and `likes, dislikes` of the review. 
 5. **Reported Reviews** - It represents the reviews reported by users as `Fraud, Offensive, Spam` It also contains details of the `reported user , reporting user`
 6. **Warnings** - It is used to represent the warnings given to a user by the admin for unacceptable comments on professors/courses. It contains the `user, message` fields, where the `message` is sent to the user on his profile.
 7. **Banned** - It is a model to list the users that have been banned by the admin. It has the fields `user, ban start, ban end , duration, time to relieve ban` as its fields.
 8. **Activity** - It logs all the user activity including `LOGIN, LOGOUT, SIGNUP, COMMENT, REPORT, LIKE, DISLIKE`. All these events are logged into the model with a `timestamp`
 9. **Credibility** - It represents the credibility of a user.

The `AUTHENTICATION AND AUTHORIZATION` section contains the `User` model that lists all the users currently enrolled into the database.

The `SOCIAL ACCOUNTS` section lists the users that have logged in via social authentication.

The other sections do not contain any significant information and can be ignored.

## Admin Panel

The admin has been given the authority to 

 - Send warning to reported users
 - Delete reviews that have been reported 
 - Ban Users for a duration that deems fit to the admin. It is possible to ban the user **PERMANENTLY**. The banned users will be automatically allowed to re-login once their ban duration ends.

For performing these features 

![Admin Panel](https://github.com/Harsh14901/ProfCourse_review_portal/blob/master/documentation.png)
 1. Login as admin
 2. Click on the `Report Reviews` database
 3. Select some reports on which you want to perform an action
 4. Click on the action drop down and you will be presented with some options.
 5. To ban a user you can specify a duration to ban the user or ban the user permanently. The default duration is 10 days.
 6. When done selecting click on the `GO` button to execute the actions.

**Note:** Re-banning a user will override the previous ban and the new ban date will be the date and time when the new ban is applied

To see the banned user details like Time to Relieve etc. navigate to the `Banneds` database under the `RATE` section. The time to relieve displays whether the user is "Free to Relieve", "Banned Permanently" or has a  certain duration left for the ban to relieve.
# Features
This section aims to explain all the features that have been implemented by the developer for the portal.

 ### Login 

 1. The login screen can be accessed either using the `login` link on the navigation bar or by directly visiting the URL [http://127.0.0.1:8000/accounts/login/](http://127.0.0.1:8000/accounts/login/)
 2. The login screen presents you with features to login through your username and password or login through social media accounts.
 3. It also has a `Sign Up` button for new users to register to the portal. It has a `Lost Password` to allow recovery of the password. Password is reset after an email verification link
 4. The User has been provided with the ability to login through `Google` and `Github`. It will request authorization once you click the respective links.

### Signup

 1. It allows users to register **only** through their **IITD** email addresses.
 2. It disallows redundancy of email adresses that redirect to the same email. Like a user already registered with `cs5190431@iitd.ac.in` will be **disallowed** to register with `cs5190431@cse.iitd.ac.in`.
 3. It sends an email verification link to the email adress to verify the authenticity of the user. Only when the user clicks on the link sent to the email address, is he allowed to login with his credentials.

### Profile

 Once logged in you will be redirected to your profile page. It consists of the following sections

 1. **Bio** - It displays the basic info of a user like name, email-address, username etc.. It also displays the **CREDIBILITY** of the user logged in
 2. **Warnings** - It lists all the warnings of a user that have been issued by the admin. Following it will be an option to clear all the warnings after taking the consent from the user that he/she will not repeat such actions. *This section is displayed only for users that have some warnings issued*. Other users will not have this section
 3. **Recent Activity** - It displays the recent activity of a user which lists all the reviews that have been written by the user.
 4. **Linked Accounts** - It allows to link a user with social accounts like Google and Github. Once linked, signing in with those social accounts will lead to this existing user profile.

### Rate Profs

This section of the webpage lists all professors categorized and well organized by department. Hence there was no need for a search bar to search for professors as it can be readily done using `Ctrl + F` to use browser search feature.

On clicking the name of a professor the user is redirected to a profile page of the Professor. 

#### Professor Profile

 1. It displays the bio of a professor like his `name`, link to `email` him, link to his `webpage`.
 2. There are various reviews listed that have been given by the ***dummy users*** of the portal. Hence kindly note that the reviews are also ***dummy***.
 3. There is a option to add a review by clicking on the `Click here to add a review` button
 4. The form to add a review has the option to allow user to not select any prof/course to give a generic comment of the course/prof.
 
**Note:** To prevent users from adding false comments, the form to add a review autoselects the professor and lists only the courses of the respective department 

#### Review
Each review has the following features - 
 1. The details of the user like name. If the user choses to be anonymous then `ANONYMOUS` is listed against the name of a user.
 2. Along with the user details the **credibility** of the reviewing user is given to help the user judge the relevance of the review.
 3. Each **logged in user** has the option to **like or dislike** a particular review
 4. Each **logged in user** also has the option to **report** the review. On clicking it redirects to a form that asks the reason and category(`SPAM, FRAUD, OFFENSIVE`) for reporting such a comment.
**Note:** A user is not allowed to like/dislike/report his own review

### Rate Courses

The implementation is the same as **Rate Profs** except for the fact that under each department the name of course is listed instead of the professor

### Logout

A user can logout using the `logout` option on the navigation bar or manually navigating to [http://127.0.0.1:8000/accounts/logout/](http://127.0.0.1:8000/accounts/logout/)
