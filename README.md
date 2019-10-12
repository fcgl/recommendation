# Recommendation Microservices

**Note:** 
    * You will only need docker installed on your computer to run this app

## Git Steps
1. Fork Branch
2. Open terminal and clone **forked branch**: `git clone https://github.com/<YOUR USERNAME>/recommendation.git`
3. Go inside point-system directory: `cd recommendation`
3. Add upstream repo: `git remote add upstream https://github.com/fcgl/recommendation.git`
4. Confirm that you have an origin and upstream repos: `git remote -v`

## Build & Run App

This build should work for both macOS and Linux

1. Download docker for your operating system
2. From project root run the following commands:
    * **Build And Run:** `docker-compose up --build`

## Health Endpoint

Confirm everything was ran correctly by going to the following endpoint: 
    * http://localhost:5000/health/v1/marco
    
## Toggling the User Recommendation process... Should be ran every 24 houra
TODO: Automate this so the process is automatically ran every 24 hours

Logic:

1. Endpoint `user_recommendation/v1/toggle` is ran every 24 hours
2. The endpoint runs a process that inserts UserRecommendation objects into the database.
The UserRecommendation objects hold a list of Product Ids. The UserRecommendation Id's are
referenced in the User object
    * Initially the user is given recommendations based on what's popular
    * As we get more data we will turn on our recommendation process which gives
    more user specific recommendations
3. When the user opens up the application an API request will be made to
endpoint `user_recommendation/v1` to get the products recommended to the user

## Development Testing
1. Make an api request to `http://localhost:5000/dev/v1/populate_data`
    * This will populate your database with 2 Users and 3 Products. This is enough
    to test the generic version of the recommendation system (based on popularity)
2. To toggle the recommendation process make an API request to `http://localhost:5000/user_recommendation/v1/toggle`
3. To see a user's recommendation make an api request to `http://localhost:5000/user_recommendation/v1?userId=1` 
(Where userId can be the id of any user in the database)
