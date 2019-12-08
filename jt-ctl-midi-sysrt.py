# JACK TRANSPORT MIDI CONTROL                       
# by Alex Phil Gunderson                            
#                                                   
# this python script takes MIDI START/STOP messages 
# as input and starts JACK transport from 0         
# or stops transport and rewinds to 0               
#                                                   
#   required modules:   mididings                   
#                       jack                        
from mididings import *
import jack

config(
        client_name='JACK_MIDI_Ctl',
        in_ports = ['SYSRT_in'],
        out_ports = ['null']
)

jack.attach('blahhh214yup')

def jackRewind(ev):
    jack.transport_stop()
    jack.transport_locate(0)

def jackTrigger(ev):
    jack.transport_locate(0)
    jack.transport_start()

run( [
        Filter(SYSRT_START) >> Process(jackTrigger),
        Filter(SYSRT_STOP) >> Process(jackRewind)
     ]
)
