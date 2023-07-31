#!/usr/bin/env python3

#import the digital assistant class
from assignment_5 import DigitalAssistant 

#instantiate a new DigitalAssistant object
joshua = DigitalAssistant('Falken', "The Software (or System) Development Life Cycle (SDLC) is a systematic approach that breaks the software process into phases--planning, analysis, design, implementation and maintenance.\n", "Implementation is setting up the hardware and components of the system or writing the actual code for the software product.\n" )
joshua.alive_statement()
print(joshua.greeting1)
print(joshua.greeting2)
joshua.menu()