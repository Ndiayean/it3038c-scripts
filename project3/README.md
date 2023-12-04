============
# Welcome to My Linux Event Flyer Creator V1

============


#### This app allows the user to create an Flyer for an Event using the terminal. It will prompt the user to input the Event Name, the Descrition, price , location, time , and select a picture. Once all of the information from the user is recorded the contents will then be transfered and saved in a word document for the user to print out and distribute.




### How to Use the app
1. On a Linux computer Download all of the content for this project including the script and pictures into a folder of your choice

2. Navigate to the folder and give the file execute permissions
        ```bash
        chmod +x EventFlyerCreator.py
        ```
3. Create a virual venv
	- To create the virtual venv use the command
	 ```bash
	 python3 -m venv venv
	 ```
	- To activate the venv use the command:
	```bash
	 . venv/bin/activate
	```
4. In the bash terminal install the python library called docx
	```bash
	pip install python-docx
	``` 

5. run the script
        ```bash
        ./EventFlyerCreator.py
        ```
   - or run the command

        ```bash
        python3 EventFlyerCreator.py
	```

6. Follow the prompts provided by the running script.

7. Navigate to the directory containing the script

8. Open the ***EventFlyer.docx*** Document and view the Flyer

==================

#### Sources
1. [https://python-docx.readthedocs.io/en/latest] (https://python-docx.readthedocs.io/en/latest/)
2. [https://www.youtube.com/watch?v=ZBx7oWCJ4aY] (https://www.youtube.com/watch?v=ZBx7oWCJ4aY)

