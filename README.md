*** DEVELOPMENT OF TASK ***


- Create Flask app
OK

- Create Blueprint structure(main, api)
OK

- Connect with API
OK

- Comment code
OK

- Instruction inside README.md about how to run the app
OK

- Add the result to the .log file
FAIL

- Use pytest(ex, invalid input)
FAIL


*** How to run the program ***

First, you must install all the dependencies found inside Pipfile(similar to requirements.txt).

Then you just have to open a terminal inside the directory and type:
    flask run

After that, connect to your localhost in your web browser. There you will have the home page with some instructions about how to use the API and a more visual option to calculate the distance with buttons too.


*** About the project ***

If the specified address is located inside the MKAD, the distance won't be calculated.To calculate that distance was used the
library haversine found in Pipfile. Basically, haversine will calculate the distance between 2 coordinates points with the parameter
you desire, such as miles, kms, meters. The result of MKAD's location less Moscow's location was 12.9 kms rounded, so from Moscow
until 12.9 kms(MKAD) the program won't calculate due to consider it's a range inside MKAD.

Also I did a special feature to help those who are not used to use API and to get used of how it works, with the functions of calculate distance between MKAD and a coordinate gave my the user in format of coordinat(longitude and latitude) and another to get data of a certain
coordinate(finding name and country of the place) or a certain city or street(and get the coordinates of that place). Those features are well
explained when you acess your localhost with the flask application running in background and they were made in format of buttons and results in JSON(get data function) and in section Results in home page(function calculate), with distance in kilometers and miles.
