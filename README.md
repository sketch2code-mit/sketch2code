# Doodle2code

*Turning doodle into DSL file*

![Preview](https://github.com/sketch2code-mit/doodle2code/blob/master/results.JPG)

There has been a growing interest in automating the conversion of a graphical user interface screenshot created by a designer into code. It is typical for designers and people who want to make a website to find some reference website designs to define the style of the website, draw a simple sketch, and mock up it in low and high resolution. However, due to the time and skill limitation, it is hard for those who design and mock up to do the developing work at the same time. Thus, this paper aims to take the existing literature to the next step by exploring transforming a sketch and style reference to the HTML code. A sketch is restricted to a portrait image of a black-and-white, rough drawing without a lot of details. An existing website screenshot or picture works as supplementary material for stylizing the website with CSS code.

## Set up 

### Dependencies
- python3
- pytorch
- numpy
- Pillow

## Data Generation
![Preview](https://github.com/sketch2code-mit/doodle2code/blob/master/dataset.png)

### DSL generation
We generated DSL codes via three steps. 
First, we defined the tokens and mappped them to the corresponding HTML. We also modified the previous DSL tokens written by pix2code in order to fit the recent version of Bootstrap. Second, we defined six types of grid using single, double, and quadruple blocks. Finally, we loop through each case of grid types and randomly generate contents to be placed inside each block with [the source code](https://github.com/sketch2code-mit/data-generation).

### Sketch synthesis
Then we compiled the generated DSL codes into HTML, styled the compiled HTML codes so that they look more like sketches, and then took screenshots of the HTML pages using a [python library](https://github.com/SeleniumHQ). Alternatively, we tried pre-processing the screenshots with OpenCV and PIL library to detect the contour and acquire synthetic sketches \cite{robinson2019sketch2code, zita2020sketch2code}. The codes used for taking screenshots are at [HTML-Screenshot](https://github.com/sketch2code-mit/html-to-image). As a result, we gained 2,160 pairs of sketches and the corresponding DSL codes in addition to the existing 1,743 pairs in the pix2code dataset. 


## Network Architecture
![Preview](https://github.com/sketch2code-mit/doodle2code/blob/master/Architecture_doodle2code.jpg)

Our method uses a Pytorch version of Tony Beltramelli’s [Pix2Code](https://github.com/tonybeltramelli/pix2code) network, [implemented by Vaibhav Yadav](https://github.com/VaibhavYadav/pytorch\_pix2code). We changed the code to train it on a dataset of screenshots of HTMLs that were adjusted with CSS to look like sketches. We also train the model on our own dataset of automatically generated HTML files where we increase the number of tokens.


Read [more](https://github.com/sketch2code-mit/doodle2code/blob/master/2021_6_862_ML.pdf) about our process.
