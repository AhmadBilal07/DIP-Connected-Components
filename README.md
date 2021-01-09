# DIP-Connected-Components
### What does the code do?<br/>
This Python code finds Connected Components in an image<br/>
### Which libraries does it use ?<br/>
Numpy and PIL. The code doesn't using Open-CV function.<br/>
### Purpose:<br/>
To get better understanding of the connected components
### Sample Images <br/>

![shapes2](https://user-images.githubusercontent.com/19593774/104092578-ad459780-52a6-11eb-869b-a7571ad2ede6.png)
![shapes3](https://user-images.githubusercontent.com/19593774/104092580-ae76c480-52a6-11eb-85eb-72f4768aa347.png)<br/>
![shapes](https://user-images.githubusercontent.com/19593774/104093136-5cd03900-52aa-11eb-9965-d37f64463e06.png)<br/>
### Threshold Images Result <br/>

![bw1](https://user-images.githubusercontent.com/19593774/104093301-92295680-52ab-11eb-9f72-6b5bf11c37b6.JPG)
![bw2](https://user-images.githubusercontent.com/19593774/104093242-0adbe300-52ab-11eb-8301-712bc56a54f3.JPG) <br/>
![bw](https://user-images.githubusercontent.com/19593774/104093466-7e322480-52ac-11eb-87e0-2d0902af5a4a.JPG) <br/>
### Bounding Box Images Result

![bw1c](https://user-images.githubusercontent.com/19593774/104093630-82127680-52ad-11eb-91e6-91dc6e3e1e65.JPG)
![bw2c](https://user-images.githubusercontent.com/19593774/104093632-82ab0d00-52ad-11eb-9943-09eb140b33ee.JPG)<br/>
![BWC](https://user-images.githubusercontent.com/19593774/104093633-83dc3a00-52ad-11eb-9a1e-b285ebf2e620.JPG)<br/>

### Output -> This information is related to first image only. 
The code also returns the following information:<br/>
![R](https://user-images.githubusercontent.com/19593774/104093884-4f697d80-52af-11eb-821d-4bb077f183e3.JPG) <br/>
Where Components list contains following information:<br/>
[componentNumber,ComponentColourValue,x1,y1,x2,y2]
