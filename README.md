# INF560HW2
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/Jinhong1003/INF560HW2/master)


scripts of INF560HW2


DOI:10.5281/zenodo.4048887

#HW4

1.

<img width="432" alt="图片 1" src="https://user-images.githubusercontent.com/54864182/97096845-cdaa7200-1626-11eb-9e71-90d2c4bacd7b.png">

2.

<img width="432" alt="图片 2" src="https://user-images.githubusercontent.com/54864182/97096853-f6cb0280-1626-11eb-8368-61e2fd719fba.png">

3.

<img width="432" alt="图片 3" src="https://user-images.githubusercontent.com/54864182/97096861-0a766900-1627-11eb-85ce-162f5daa8d5c.png">

4a.

The packages that I manually installed using pip install or conda install command require us to download the exact packages and execute them.

The dependency list I extracted is just a text file that contains the name and the version of the packages which are needed in the execution of the project. It is not the actual package that we will use. When we create a new environment, there are only standard libraries and these packages are not existing in our environment originally.

When I want to download matplotlib by pip, I only execute this command line once, however it download many sub-packages in my environment , so in my requiremens.txt , there are other packages as well.

6a.

<1>enter the directory of the project.

<2>pip install pip virtualenv, download the packeget for creating a new environment

<3>virtualenv dsci560h4, Create a virtual environment--dsci560H4(based on python3) ,under the directory of project

<4>source dsci560H4/bin/activate, activate the envronment

<5>python3 Create_number.py, execute Create_number.py in order to get 1000 random number between 0 and 100, write them into a txt file.

<6>python3 New_number.py, execute New_number.py in ordr to create 1000 new numbers based on the former 1000 numbers, write them into a txt file.

<7>python3 Number_visualization.py, show the result of 5 and 6 steps in coordinate system while x axis is the orginal number, y axis is new numbers

<8>jupyter notebook, execute HW2_task5.ipynb, run the codes in this file step by step.

<9>deactivate,deactivate the environment

