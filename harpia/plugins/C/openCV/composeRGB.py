#!/usr/bin/env python
 # -*- coding: utf-8 -*-

from harpia.constants import *
import gettext
_ = gettext.gettext
gettext.bindtextdomain(APP, DIR)
gettext.textdomain(APP)

from harpia.GUI.fieldtypes import *
from harpia.model.plugin import Plugin

class ComposeRGB(Plugin):

# ------------------------------------------------------------------------------
    def __init__(self):
        Plugin.__init__(self)
        self.id = -1
        self.type = self.__class__.__module__

    # ----------------------------------------------------------------------
    def get_help(self):#Função que chama a help
        return "BLOCO Composição RGB"

    # ----------------------------------------------------------------------
    def generate(self, blockTemplate):
        blockTemplate.imagesIO = \
                     'IplImage * block$id$_img_i1 = NULL;\n' + \
                     'IplImage * block$id$_img_i2 = NULL;\n' + \
                     'IplImage * block$id$_img_i3 = NULL;\n' + \
                     'IplImage * block$id$_img_t1 = NULL;\n' + \
                     'IplImage * block$id$_img_t2 = NULL;\n' + \
                     'IplImage * block$id$_img_t3 = NULL;\n' + \
                     'IplImage * block$id$_img_o1 = NULL;\n'
        blockTemplate.functionCall = '\nif(block$id$_img_i1){\n' + \
                         'block$id$_img_o1 = cvCreateImage(cvSize(block$id$_img_i1->width,block$id$_img_i1->height), block$id$_img_i1->depth, block$id$_img_i1->nChannels);\n'+\
                          'block$id$_img_t1 = cvCreateImage(cvSize(block$id$_img_i1->width,block$id$_img_i1->height), block$id$_img_i1->depth, 1);\n'+\
                          'block$id$_img_t2 = cvCreateImage(cvSize(block$id$_img_i1->width,block$id$_img_i1->height), block$id$_img_i1->depth, 1);\n'+\
                          'block$id$_img_t3 = cvCreateImage(cvSize(block$id$_img_i1->width,block$id$_img_i1->height), block$id$_img_i1->depth, 1);\n'+\
                          'cvSplit(block$id$_img_i1 ,block$id$_img_t1  ,NULL, NULL , NULL);\n' + \
                          'cvSplit(block$id$_img_i2 ,NULL ,block$id$_img_t2, NULL, NULL);\n' + \
                          'cvSplit(block$id$_img_i3 ,NULL ,NULL, block$id$_img_t3 , NULL);\n' + \
                          'cvMerge(block$id$_img_t3 ,block$id$_img_t2 ,block$id$_img_t1 , NULL, block$id$_img_o1);}\n'
        blockTemplate.dealloc = 'cvReleaseImage(&block$id$_img_t1);\n' + \
                      'cvReleaseImage(&block$id$_img_t2);\n' + \
                      'cvReleaseImage(&block$id$_img_t3);\n' + \
                      'cvReleaseImage(&block$id$_img_o1);\n' + \
                      'cvReleaseImage(&block$id$_img_i1);\n' + \
                      'cvReleaseImage(&block$id$_img_i2);\n' + \
                      'cvReleaseImage(&block$id$_img_i3);\n'

    # ----------------------------------------------------------------------
    def __del__(self):
        pass

    # ----------------------------------------------------------------------
    def get_description(self):
        return {"Type": str(self.type),
         "Label":_("Compose RGB"),
         "Icon":"images/composeRGB.png",
         "Color":"50:125:50:150",
         "InTypes":{0:"HRP_IMAGE",1:"HRP_IMAGE",2:"HRP_IMAGE"},
         "OutTypes":{0:"HRP_IMAGE"},
         "Description":_("Compose three color channels  (R, G and B)  into one color image."),
         "TreeGroup":_("Filters and Color Conversion")
         }

    # ----------------------------------------------------------------------
    def get_properties(self):
        return {}

# ------------------------------------------------------------------------------

