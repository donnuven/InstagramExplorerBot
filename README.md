# Instagram Explorer Bot 

## Purpose summary:
The project as a whole is a form of designing an automation bot that is meant to browse through instagram, imitate scrolling actions, be able to select an image, go through a set of images, and search up a person and repeat the same cycle again (which is to scroll, browse, and select image) before returning to the home page.

## Additional Note:
This project uses the facebook authentication login functionality, so if you want to login directly to instagram through the standard login process, be sure to change the code accordingly, otherwise this will use the login for facebook to get to the instagram page.

## Dependencies:
This project utilized two different dependencies being: web chrome driver and selenium, which are required to run this project.

The link to chromedriver is here: http://chromedriver.chromium.org/ 

To be able to run this project:
   - Download chromedriver, unzip, move to ``/usr/local/bin`` (mac OS / linux)  
  
To be able to run this project on windows:
   - After downloading chromedriver, in order to set up the executable path by moving it to the C drive and it will look something like      this : ``C:\ path\ toyour\ chromedriver.``
   
 Make sure you have the chromedriver setup in your environment variable for the path in order to make sure chromedriver is setup.

To get the selenium dependency: ``pip install selenium`` or ``pip3 install selenium`` (this just depends on which version of pip you have)

## Additional files
 Make sure you setup a file named as secrets.py  with the following variables:
 
  `` username = 'your_username'``
  `` password = 'your_password'``
   ``person = 'person_searched_up' ``
    ``PATH = 'C:\path\toyour\chromedriver'`` (this is for windows user)
 
  The person being searched up can be changed. If there are any suggestions, feel free to add that in. 
 
  
## Final comments:
Feel free to add more features and/or tweaks to some of the functions to fit what the bot can do for you.

Happy coding! 

