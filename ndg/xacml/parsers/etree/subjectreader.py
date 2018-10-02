"""NDG XACML ElementTree based Subject Element reader 

NERC DataGrid
"""
__author__ = "P J Kershaw"
__date__ = "16/03/10"
__copyright__ = "Copyright 2018 United Kingdom Research and Innovation"
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__license__ = "BSD - see LICENSE file in top-level package directory"
__contact__ = "Philip.Kershaw@stfc.ac.uk"
__revision__ = "$Id$"
from ndg.xacml.core.subject import Subject
from ndg.xacml.parsers.etree.targetchildreader import TargetChildReader
    

class SubjectReader(TargetChildReader):
    '''ElementTree based XACML Rule parser
    @cvar TYPE: XACML type to instantiate from parsed object
    @type TYPE: type
    '''
    TYPE = Subject
