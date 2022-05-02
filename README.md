#### Wozap

An application that consumes the News - API and displays news sources and articles.

## Contribution
Emmaculate Kamau

## Technology used
1. Python
2. Flask
3. HTML
4. CSS3

## Requirements
An IDE such as VS code with Python version 3 installed,a terminal and a browser. 

## Setup and Instruction
1. Clone the repository at [here](https://github.com/emmakamau/Wozap.git.
2. Extract and open the folder on VS code or navigate to the folder on your terminal.
3. On the terminal, create a virtual environment `python3 -m venv virtual` and activate it `source virtual/bin/activate`. NB **virtual** is the name of the environment.
4. Pip install dependancies highlighted on the **requirements.txt** by running `pip install -r requirements.txt`
5. Create a **start.sh** file in the root directory of the folder and define the **api key**. You can generate the api key from the News API [here](https://newsapi.org/)
6. Run `chmod +x start.sh` and `./start.sh` respectively on the terminal.
7. View the application on your browser through `http://127.0.0.1:5000`.


## Behaviour Driven Development

BDD focuses on how the user will interact with the application.

What you will see and experience:
1. A landing page with a navbar, a Tech section, list of resources, What's new and a footer.
2. The navbar contains link with various types of news. Click on the **Kenya** link and get redirected to view Kenyan news articles.
3. The search form on the navbar allows the user to search for any article desired. Type in for example, **shoes** and submit. You'll get redirected to a search page with the number of articles related to shoes. 
4. On the **News Sources Available**, click to be redirected to the sources main websites.
5. The news articles are displayed on cards, click on **read article** or **view more** to get redirected to the main article or video on the source website.
6. On the footer, click on the social icons to interact with the owners of the website.

## Development
To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request

## Known Bugs

If you find a bug or would like to request a new function, reach out to me via Email: emmaculatewkamau@gmail.com or on [LinkedIn](https://www.linkedin.com/in/emmaculate-k-987353104/)

## License

[MIT](https://choosealicense.com/licenses/mit/)

Copyright (c) 2022 **Emmaculate Kamau**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
