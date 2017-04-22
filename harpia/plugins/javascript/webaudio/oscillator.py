#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This module contains the Oscillator class.
"""
from harpia.GUI.fieldtypes import *
from harpia.plugins.javascript.webaudio.webaudioplugin import WebaudioPlugin


class Oscillator(WebaudioPlugin):

    # --------------------------------------------------------------------------
    def __init__(self):
        WebaudioPlugin.__init__(self)

        # Appearance
        self.help = "Sound output"
        self.label = "Oscillator"
        self.color = "50:150:250:150"
        self.in_ports = [{"type":"HRP_WEBAUDIO_SOUND",
                           "label":"Osc Frequency",
                           "name":"osc_freq"},
                         {"type":"HRP_WEBAUDIO_FLOAT",
                         "label":"Frequency",
                         "name":"freq"},
                         {"type":"HRP_WEBAUDIO_FLOAT",
                         "name":"type",
                         "label":"Type"}]
        self.out_ports = [{"type":"HRP_WEBAUDIO_SOUND",
                         "name":"sound_output",
                         "label":"Sound Output"}]
        self.group = "Sound"

        self.properties = [{"name": "freq",
                            "label": "Frequency",
                            "type": HARPIA_FLOAT,
                            "lower": 0,
                            "step": 1,
                            "value": 440
                            },
                           {"name": "type",
                            "label": "Type",
                            "type": HARPIA_COMBO,
                            "values": ["square",
                                       "sine",
                                       "sawtooth",
                                       "triangle"],
                            "value": "sine"
                            }
                           ]

        self.codes[0] = """
// block_$id$ = Oscillator
var block_$id$ =  context.createOscillator();
var block_$id$_i0 = block_$id$.frequency;
var block_$id$_o0 = null;
var block_$id$_i1 = function(value){
    block_$id$.frequency.value = value;
};
var block_$id$_i2 = function(value){
    oscillator = ''
    if (value < 1) oscillator = 'square';
    if (value == 1) oscillator = 'sine';
    if (value == 2) oscillator = 'sawtooth';
    if (value > 2) oscillator = 'triangle';
    block_$id$.type = oscillator;
};
"""
        self.codes[1] = """
block_$id$_o0 = block_$id$.frequency;
block_$id$.type = '$prop[type]$';
block_$id$.frequency.value = $prop[freq]$; // value in hertz
block_$id$.detune.value = 100; // value in cents
block_$id$.start(0);
"""
