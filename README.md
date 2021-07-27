# Neighborhood Watch

If you are like me, You really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it.   This is a Python application based on Django framework that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

You can see the live Application here ().

## Author Information

Ephraim Kamau

## Features

- Built with Python 3.8, Djang0 3.2.5 Framework
- Styled using Bootstrap4
- Uses PostgreSQL DB and Deployed to Heroku
Allows users to:
- Sign in with the application to start using.
- Set up a profile about me and a general location and my neighborhood name.
- Find a list of different businesses in my neighborhood.
- Find Contact Information for the health department and Police authorities near my neighborhood.
- Create Posts that will be visible to everyone in my neighborhood.
- Change My neighborhood when I decide to move out.
- Only view details of a single neighborhood.

## Behavior Driven Development (BDD)

| Input                                                                                            | Output                                                                                                                                                   |
|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sign in with the application to start using.                                                     | On page load, click register on the NAV bar to register and login using created credentials to start using                                               |
| Set up a profile about me and a general location and my neighborhood name.                       | On sign up and login, click profile on navbar to navigate to your profile and update neighborhood information and your profile information               |
| Find a list of different businesses in my neighborhood.                                          | Navigate to Search dropdown on Navbar and click Search Business. In the search table, type the neighborhood your want to search                          |
| Find Contact Information for the health department and Police authorities near my neighborhood.  | Navigate to Search dropdown on Navbar and click Search Contact. In the search table, type the neighborhood your want to search                           |
| Create Posts that will be visible to everyone in my neighborhood.                                | Click on New Post on Nav bar to create new posts and click POST while done                                                                               |
| Change My neighborhood when I decide to move out.                                                | To change nighborhood, go to profile and select from the dropdown button your new neighborhood                                                           |
| Only view details of a single neighborhood.                                                      | On navigating to the neighborhood page, click the neighborhood title to navigate to enighborhood details and oncly view details of a single neighborhood |

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need to:

- Have python installed
- Have PostgreSQL DB installed
- Have a terminal to interact with the app.
- Any text editor
- Browser to view
- -Create a Virtual Environemnt, install Django >=3.2.5 and its dependencies

## Installation

    git@github.com:ephraim-kamau54/neighborhood-watch.git

## Build & Deployment

**NOTE:** You need to have fully cloned it to run it locally.

    (virtual) $ python3.8 manage.py runserver

    # it will launch the web page from local server. You can also visit the livelink [here]().
 to use the system

## Built With

- Built with Python 3.8
- Django3.2.5
- Styled using Bootstrap

## Contribute

If you want to add any new features, or improve existing ones, feel free to send a pull request!

## Known Bugs

There are currently no known bugs for the app. However, I will be updating the README incase any bugs arise.

## License

MIT License

Copyright (c) 2021 Ephraim Kamau
