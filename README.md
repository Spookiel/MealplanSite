# MealplanSite
## Overview
This is a site I'm working on as a summer project. The idea is to use an AI backend to help generate recipes. The app will also include a calendar so you can swap around meals to give extra flexibility. 
The aim is that this tool will give busy people the power to make nutritious food easily.

![image](https://github.com/Spookiel/MealplanSite/assets/28538713/e28f3701-9e2a-40a9-802c-5a5d51a301a3)


### Technical details
- Uses a Django back-end with a Bootstrap and HTML frontend
- The planning and recipe generation will be handled be OpenAI's GPT-3.5 / 4 engine
- May also integrate a REST API so users can get data from AI directly.
- Database is running SQLite

## Future plans
- Make REST API for communicating between front-end and the AI back-end
- Host the website
- Switch database to Postgres (Have studied PostgreSQL so might be useful if custom code needed for migrations etc)
- Compile shopping lists automatically
- Put ingredients into online supermarket baskets automatically
- Send emails detailing the weekly plan to the user 
