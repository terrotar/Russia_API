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

After that, connect to your localhost in your web browser. There you will have the home page with some
instructions to use the API and a more visual option to calculate the distance too.


*** About the project ***

If the specified address is located inside the MKAD, the distance does not need to be calculated.To calculate the distance
was used the library haversine found in Pipfile. Basically, haversine will calculate distance between 2 points with the
parameter you desire, such as miles, kms, meters. The result was 12.9 kms rounded, so from Moscow until 12.9 kms(MKAD) the program
won't calculate in due to consider inside MKAD.
