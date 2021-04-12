# Doodle2code

*Turning doodle into DSL file*

![Preview](https://github.com/sketch2code-mit/doodle2code/blob/master/results.jpeg)

## Set up 

### Prerequisites
- python3
- pip


## Data Generating
![Preview](https://github.com/sketch2code-mit/doodle2code/blob/master/dataset.png)

### DSL generation
We generated DSL codes via three steps. 
First, we defined the tokens and mappped them to the corresponding HTML. We also modified the previous DSL tokens written by pix2code in order to fit the recent version of Bootstrap. Second, we defined six types of grid using single, double, and quadruple blocks. Finally, we loop through each case of grid types and randomly generate contents to be placed inside each block with [the source code](https://github.com/sketch2code-mit/data-generation).

### Sketch synthesis
Then we compiled the generated DSL codes into HTML, styled the compiled HTML codes so that they look more like sketches, and then took screenshots of the HTML pages using a [python library](https://github.com/SeleniumHQ). Alternatively, we tried pre-processing the screenshots with OpenCV and PIL library to detect the contour and acquire synthetic sketches \cite{robinson2019sketch2code, zita2020sketch2code}. The codes used for taking screenshots are at [HTML-Screenshot](https://github.com/sketch2code-mit/html-to-image). As a result, we gained 2,160 pairs of sketches and the corresponding DSL codes in addition to the existing 1,743 pairs in the pix2code dataset. 


## Network Architecture
![Preview](https://github.com/sketch2code-mit/doodle2code/blob/master/architecture.jpeg)

Our method uses a Pytorch version of Tony Beltramelli’s [Pix2Code](https://github.com/tonybeltramelli/pix2code) network, [implemented by Vaibhav Yadav](https://github.com/VaibhavYadav/pytorch\_pix2code). We changed the code to train it on a dataset of screenshots of HTMLs that were adjusted with CSS to look like sketches. We also train the model on our own dataset of automatically generated HTML files where we increase the number of tokens.


