# Face_recognition
A desktop application which will detect the face if stored in database or if face is not stored it will add the user 

1) You should have Python Install on your Pc,(Python Version : 3.10.11) Link to download Python(https://www.python.org/download/releases/2.5/msi/)
2) Clone the project in newfolder name facedetection using command git clone "https://github.com/Abhi-30/Face_Detection.git"
3) Create a virtual enviornment name test in same folder. Command to create 'python -m venv test'
   Steps to activate virtual enviornment
   1) go inside the test folder using command 'cd test'
   2) then go inside the Scripts folder using command 'cd Scripts'
   3) then activate the envionment using 'activate'
   4) Then come out of test Folder 
5) For Installing dlib library we have to download CMake from https://cmake.org/download/
   After installing, add it to system path (Environmental Variables > Path > Click New and Add the Path There > Click OK to Save)
   eg: C:\Program Files\CMake\bin
6) The dlib package depends on c++ so we need to install visual studio 2019 and select python and c++ windows application and install visualstudio 2019
7) Install all the package needed for face_recognization using command pip install -r requirement.txt
8) Once all the packages are installed then start the program
9) Then Run the program by running the file using 'python index2.py'(Now the program will run . For database we are using sqlite database which is default) 
