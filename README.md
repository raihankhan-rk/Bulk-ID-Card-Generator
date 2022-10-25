## Installation

- Install PIL
```sh
pip install Pillow qrcode
```
## Setup

- Enter the path to blank ID Card template in the script.
- enter the path to your desired font. 
- > Note: The font file should be a .ttf one.
- Enter the coordinates where you want the name to be written.
- Enter the coordinates where you want the QR to be.
- Enter the RGB values of the colour you want the names to be written in.
- Enter the path of the directory you want to save the generated ID Cards in.
- Enter the path to the csv file containing all the names in the following line in the scriopt.
```sh
 names = idcardgen(' --PATH TO CSV CONTAINING ALL THE NAMES-- ')
```

> Note: The csv should contain names in the following pattern. (The first row should be named as 'Names')


| Names | 
| ------ | 
| Raihan Khan |
| John Wick | 
| Abraham Hogg | 
| Nancy Drew |
| Percy Jackson | 
| Robin Centineo | 

- Run the main.py script
```sh
 python3 main.py
```
