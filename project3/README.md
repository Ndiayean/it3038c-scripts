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
	- To activate the venv use the command: . venv/bin/activate

4. In the bash terminal install the python library called docx
	```bash
	pip install python-docx
	``` 

5. run the script
        ```bash
        ./EventFlyerCreator.py
        ```
   or run the command
        ```python
        python3 EventFlyerCreator.py

6. Follow the prompts provided by the running script.

7. Navigate to the directory containing the script

8. Open the ***EventFlyer.docx*** Document and view the Flyer

==================

#### Sources
1. [https://www.pythontutorial.net/python-basics/python-write-text-file/] (https://www.pythontutorial.net/python-basics/python-write-text-file/)
2. [https://www.geeksforgeeks.org/shutil-module-in-python/#] (https://www.geeksforgeeks.org/shutil-module-in-python/#)

3. [https://www.geeksforgeeks.org/python-os-makedirs-method/] (https://www.geeksforgeeks.org/python-os-makedirs-method/)

4. [https://stackoverflow.com/questions/34530237/find-files-in-a-directory-containing-desired-string-in-python] (https://stackoverflow.com/questions/34530237/find-files-in-a-directory-containing-desired-string-in-python)

