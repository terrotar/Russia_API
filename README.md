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
OK

- Use pytest(ex, invalid input)
OK


*** How to run the program ***

First, you must install all the dependencies found inside Pipfile(similar to requirements.txt).

Then you just have to open a terminal inside the directory and type:
    flask run

After that, connect to your localhost in your web browser. There you will have the home page with some instructions about how to use the API and a more visual option to calculate the distance and get data of a certain seach address with a city or street name or with coordinates with buttons too.


*** About the project ***

It's in the format of Blueprints, something that I confess I didn't use too much as I should and after that experience in my futures projects I will thing about it. Spent a little time to study the concept again but it is extremelly awsome the way it works. It makes your code fluid naturally, more simple to read and understand, cleaner and let you more awarness about your code behaviour. Also, I tried to comment a lot during the code, to make the reader understand a little better what was my logic developing it.

If the specified address is located inside the MKAD, the distance won't be calculated.To calculate that distance was used the
library haversine found in Pipfile. Basically, haversine will calculate the distance between 2 coordinates points and returns it with the parameter you desire, such as miles, kms, meters. The result of MKAD's location less Moscow's location was 12.9 kms rounded, so from Moscow
until 12.9 kms(MKAD) the program won't calculate due to consider it's a range inside MKAD - the location of MKAD and Moscow was used by the API when searching a coordinate by it's name in the follow link as example: https://yandex.com/dev/maps/geocoder/doc/desc/examples/geocoder_examples.html.

Also I did a special feature to help those who are not used to use API and to get used of how it works, with the functions of calculate distance between MKAD and a coordinate gave by the user in format of coordinate(longitude and latitude) and another to get data of a certain
coordinate(finding name and country of the place) or a certain city or street(and get the coordinates of that place). Those features are well
explained when you acess your localhost with the flask application running in background and they were made in format of buttons and results in JSON(get data function) and in section Results in home page(function calculate), with distance in kilometers and miles.

All requests using the API or the home page through the buttons, like get data of a city or using API to calculate distance will be recorded
in directory logs. It's using the library loguru, something that I had never worked before and think it's insane! I've never done any kind of
log system in my others projects and got shocked how that library made it easy and familiar with and it's extremelly efficient!

There are some unit tests using pytest founded inside the directory /tests. There are 2 files, boths with the idea of invalid inputs but converted to both Blueprints, API(test_api.py) and site(test_site.py). I had used pytest once before but it was a tutorial and just followed the instructions and I found very efficient it and very easy to use. You just have to open a terminal and go inside that directory(/tests) and type: pytest test_api.py
      or
      pytest test_site.py
And don't forget to open another terminal with the application running, otherwise all tests will fail because they won't be able to connect with the URL's.

I think that Test Task was with high difficulty, I got kind a lost in the beginning because of the whole idea of the project, using MKAD(I didn't know what was it and had never heard about it) as reference, the API of yandex(I didn't know it exists, I only knew about Google and never head of it and got really impressive and started using it), token key to acess the API(I've never done it before) and deal with features I don't know well, like log files and unit tests were definitely barriers to develop it inside 1 week. To get even better, I got sick in the beggining of that week and didn't use my computer, so I used those days to study how I would achieve the deadline and what was possible with my skills and what would be a plus feature.I feel very happy that I could complete it in it's whole, even with some bonus, like the options to use the API as it was a form, to users get a way more familiar to understand how does an API work, something that was kind a misterious thing to me when I didn't know what it was a couple months ago.

In front-end was used some basic HTML and CSS with Bootstrap to get a little more "friendly face" to users. I don't have so much knowledge of
that area but I definitely could get it a little better, like insert a navbar with some guides, like 'Contact', or things like that but the
deadline of 1 week didn't allow me to do it. The color palette was decided to be the colors of Russia's flag, a homage to cheers the description and heart of that Test Task, a real challenging project like the winter of Russia, but it was awsome to do and what I've learned from it's immeasurable like Russia's size. Jokes a part, that was the most difficulty test until know and the only I could deliver with all the requirements, thanks for the opportunity to do that test and the wisdom that came with it, it certainly make my future projects better!

Hope that anyone who sees this project can achieve what they are searching for! =]
