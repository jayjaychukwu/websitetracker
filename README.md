# websitetracker
A website up and down time tracker with multiple features and functionalities

The aim is to have a background worker that runs a task every minute that call a background task function that checks if all the websites in the database are up and relays that information in a predefined way back to the database.

It is an API that allows you do the following:
1. Register an account and login
2. Allows you to add websites to monitor with the following fields: the url of the website, the authorization type and the authorization information(key)
3. Allows you to add emails to receive notifications (a restriction of 5 emails per account would be placed here)

