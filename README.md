## Project Name

Blog Post Application With Flask

## Author's Information

<a href="https://github.com/edah-hub">Chepngetich Edah</a>

## Description

This is a python-based web application that allows users to view blog posts ,add their post update or delete a post and even leave a comment/feedback on other people's posts.

## User Stories

As a user, you will be able to:

  <ul>
  <li>View posts posted by other users.</li>
  <li>Sign up to the account</li>
  <li>Like and dislike posts. </li>
  <li>Submit feedback or comment on other people's posts.</li>
  <li>Submit a post in any category</li>
  <li>View a users posts by their profile.</li>
  <li>A signed user can delete and update their posts.</li>
  </ul>

## Technologies Used

<ul>
<li>Python</li>
<li>Flask</li>
<li>HTML, CSS and Bootstrap</li>

</ul>

## BBD

| Behaviour                  | Input                                                              | Output                                                  |
| -------------------------- | ------------------------------------------------------------------ | ------------------------------------------------------- |
| Register on the site       | User's username, email and password                                | User receives a welcome email                           |
| Log into the site          | Enter credentials                                                  | Gets logged in and redirected to the homepage           |
| Publish a post            | Enter a post and submit the form                                  | post is posted on the homepage                         |
| View another users profile | Click on a users name                                              | Users username, email, and posted posts are displayed |
| Comment on a pitch         | Click on a post's title or comment icon and enter comment in form | comment is posted below the post                       |

## Setup/Installation Requirements

1. Clone the application by running git clone https://github.com/edah-hub/post-Central.git on the teminal.
2. Create a virtual environment.
3. Run `Pip3 install -r requirements.txt` on your terminal.
4. Add `export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}` to the start.sh file to export the database configuration.
5. Also,create a secret key and add it to start.sh
6. Run `$./start.sh`on your terminal to start your local server and view the application on your browser.

## Link

The live deployed web app can be found <a href="#">here</a>

## Contact Information

In case of any feedback, you can reach me through: -cheruiyotedah@gmail.com

## License

The MIT License (MIT) Copyright (c) 2022 Chepngetich Edah.
