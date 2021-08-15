*** DEVELOPMENT OF TASK ***


- Create Flask app
OK

- Create Blueprint structure(main, api)
OK

- Connect with API
OK

- Comment code
...

- Instruction inside README.md about how to run the app
...

- Add the result to the .log file
FAIL

- Use pytest(ex, invalid input)
FAIL


*** How to run the program ***

First, you must install all the dependencies found inside Pipfile(similar to requirements.txt).

Then you just have to open a terminal inside the directory and type:
    - flask run

    Still developing, sorry =s


*** About the project ***

    If the specified address is located inside the MKAD, the distance does not need to be calculated. I didn't know how to
specify MKAD in geolocation because it's not a point, like an address but a huge ring road, so to solve that barrier
I consider the distance between Moscow(been the center of a circular form) with MKAD, and calculate the area of that distance
in km using one library(haversine) found in Pipfile. Basically, haversine will calculate distance between 2 points with the
parameter you desire, such as miles, kms, meters. The result was 16.2 kms rounded, so from Moscow until 16.2 kms the program
won't calculate in due to consider inside MKAD.
