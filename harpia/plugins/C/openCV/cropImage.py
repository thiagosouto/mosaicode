#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.constants import *
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *
from harpia.model.plugin import Plugin

class CropImage(Plugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        Plugin.__init__(self)
        self.id = -1
        self.type = self.__class__.__module__
        self.x0 = 0
        self.y0 = 0
        self.width = 640
        self.height = 480

    # ----------------------------------------------------------------------
    def get_help(self):#Função que chama a help
        return "Corta a Imagem de acordo com o Retangulo\n de entrada."

    # ----------------------------------------------------------------------
    def generate(self, blockTemplate):
        blockTemplate.imagesIO = \
            'IplImage * block$id$_img_i1 = NULL;\n' + \
            'IplImage * block$id$_img_o1 = NULL;\n' + \
            'CvRect  block$id$_rect_i2 = cvRect($x0$, $y0$, $width$, $height$);\n'
        blockTemplate.functionCall = '\nif(block$id$_img_i1){\n' + \
                 '	block$id$_rect_i2.x = MAX(0,block$id$_rect_i2.x);//Check whether point is negative\n' + \
                 '	block$id$_rect_i2.y = MAX(0,block$id$_rect_i2.y);\n' + \
                 '	block$id$_rect_i2.x = MIN(block$id$_img_i1->width-1,block$id$_rect_i2.x);//Check whether point is out of the image\n' + \
                 '	block$id$_rect_i2.y = MIN(block$id$_img_i1->height-1,block$id$_rect_i2.y);\n' + \
                 '	block$id$_rect_i2.width = MIN(block$id$_img_i1->width-block$id$_rect_i2.x,block$id$_rect_i2.width);//Check whether rect reaches out of the image\n' + \
                 '	block$id$_rect_i2.height = MIN(block$id$_img_i1->height-block$id$_rect_i2.y,block$id$_rect_i2.height);\n' + \
                 '	block$id$_img_o1 = cvCreateImage(cvSize(block$id$_rect_i2.width,block$id$_rect_i2.height),' + \
                 ' block$id$_img_i1->depth,block$id$_img_i1->nChannels);\n' + \
                 '	cvSetImageROI(block$id$_img_i1,block$id$_rect_i2);\n' + \
                 '	cvCopyImage(block$id$_img_i1,block$id$_img_o1);\n' + \
                 '}\n'
        blockTemplate.dealloc = 'cvReleaseImage(&block$id$_img_o1);\n' + \
                                'cvReleaseImage(&block$id$_img_i1);\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
            'Label': _('Crop Image'),
            'Icon': 'images/cropImage.png',
            'Color': '50:50:200:150',
            'InTypes': {0: 'HRP_IMAGE', 1: 'HRP_RECT'},
            'OutTypes': {0: 'HRP_IMAGE'},
            'Description': _('Crops the input image according to input Rectangle'),
            'TreeGroup': _('Experimental')
            }

    # ----------------------------------------------------------------------
    def get_properties(self):
        return {"x0":{"name": "X",
                            "type": HARPIA_INT,
                            "value": self.x0,
                            "lower":1,
                            "upper":65535,
                            "step":1
                            },
                "y0":{"name": "Y",
                            "type": HARPIA_INT,
                            "value": self.y0,
                            "lower":1,
                            "upper":65535,
                            "step":1
                            },
                "width":{"name": "Width",
                            "type": HARPIA_INT,
                            "value": self.width,
                            "lower":1,
                            "upper":65535,
                            "step":1
                            },
                "height":{"name": "Height",
                            "type": HARPIA_INT,
                            "value": self.height,
                            "lower":1,
                            "upper":65535,
                            "step":1
                            }
                }

# ------------------------------------------------------------------------------

