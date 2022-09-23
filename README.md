# Project-3
This is our third project at General Assembly.  
## Description 
Welcome to perfect match.

We are a job sieving tool built for developers by developers.

Our service forefronts user skills in order to match them with jobs that meet the criteria they feel best represents their skillset.  

We cut out the fluff and unceccsary features of other job search tools by placing the onus on the user to determine what they feel best represents their skillset.  We want to create a tool that is intuitive, easy to use and transparent.  

You can update your skill set anytime by visiting your profile link.

New results all the time. 

[Check it out](https://developer.adzuna.com/)

## Home Page
![Home page](https://i.imgur.com/d5cAxte.png)
## Log in
![Sign In](https://i.imgur.com/djBj8p7.png)
## Sign up
![Sign Up](https://i.imgur.com/yQ0Wr0O.png)
## Job listings
![Job listing](https://i.imgur.com/nNgB5w3.png)
## Job matches
![Job matches](https://i.imgur.com/NtW0Z8u.png)
## Profile
![Profile](https://i.imgur.com/T7PHycP.png)
## Saved Jobs
![Saved Jobs](https://i.imgur.com/QL1eaql.png) 
## API 
![The API we used](https://i.imgur.com/Y3gjKwQ.png)

## Technologies used 
* Django
* Python
* CSS
* HTML
* PostgreSQL
* Trello
* VScode
* Heroku
* Whimsical
* Adzuna API
* Amazon web service 
* pgAdmin 

## [Adzuna API](https://developer.adzuna.com/)
We used the Adzuna API to pull job listings from the Adzuna website. Adzuna is a job forum website similar to indeed, or glassdoor. The API returns the information for job postings that can then be filtered to fetch very content that adheres to whatever criteria are of interest. We take in this information and use it to create our own job postings, which we can then match against the user's skillset. 
<br> [Documentation for API](https://developer.adzuna.com/overview)

## [Getting started ](https://perfectmatchskills.herokuapp.com/job-listings/)
Log into the website with the log in link and then you are free to do whatever you want in the website, browse job listings, add skills, remove skills, add jobs to youre saved jobs, ANYTHING!

## Original Wireframe and Planning 
* [Trello](https://trello.com/b/YbLVf3RD/project-3#)
* [Whimsical](https://whimsical.com/project-3-5rQgxTeWbUqZtKvYZG7ZoC)

## Wins 
A major win for this project was being able to implement full CRUD (Create Read Update Delete).  Our site features at least one each CRUD operation. 
<br>
<br> Another win during this project was being able to work together as a team to impliment an agile workflow that pooled everyone's resources into solving problems.  

## Hurdles 
There were countless hurdles with the project. Almost every function we wrote, that went beyond basics, lead to a multitude of errors that usually resulted in refactoring almost all of our codebase. However, we were able to get all of the functions working and learned a lot in the process, even if at first they appeared seemingly impossible. 

<br><br>
A particularly noteworthy hurdle was when we had to change ourjob listings from being stored in a list to actually saving them as objects in the database. It resulted in unexpected errors when stored in an array, because we didn't have any persistent data.  Refacorting the function to store the data in a SQL database and then accessing that data through object queries greatly improved the performance and readability of our code. 

## Next Steps 
We have a slew of icebox features, including: 
* Moving Api into an independent folder, so we don't have to rely on it being in views, and therefor have to import views in each instance we want to use it.  
* Adding the ability to remove jobs from saved.
* Deleting jobs after a certain amount of time and replacing them with newer ones.
* Updating our API alogirthm so that the API is judiciously pinged, rather than having it ping every time a user accesses one of the URL endpoints that depend upon it. 

## Credits 
* Patrick Schenk
* George Perry 
* Payne Fulcher 
* James Fox 
* Ogan Aktolun

Instructional Team at GA, 
* Suresh Sigera 
* Nellie Bosch 
* Rondell Charles 
* Kenneth Chang

