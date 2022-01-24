# Resume generator

Simple one page generator.

## System requirements:
 - Linux (I'm using Debian 11)
 - Python > 3.6
   - reportlab (3.6.5)


## Installation 
   git clone https://github.com/8tm/resume_generator && cd resume_generator
   pip install .
   
## Usage

INPUT_PATH: Path to folder with files (json, images, fonts)

OUTPUT_PATH: Path to the pdf file or to directory where that pdf file will be generated

Usage:

    resume_generator -p <INPUT_PATH>
    resume_generator -p /home/${USER}/Desktop/My_CV/

Or:
   
    resume_generator -p <INPUT_PATH> -o <OUTPUT_PATH>
    resume_generator -p /home/${USER}/Desktop/My_CV/ -o resume_generator -p /home/${USER}/Desktop/My_CV/
    resume_generator -p /home/${USER}/Desktop/My_CV/ -o resume_generator -p /home/${USER}/Desktop/My_CV/My_CV_2022.pdf
   
## Json file

Script will search for file `cv.json` in INPUT_PATH.

Example of simple CV json file can be found in `examples` directory. 
