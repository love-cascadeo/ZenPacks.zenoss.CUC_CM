##############################################################################
#
# Copyright (C) Zenoss, Inc. 2013, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################

from Products.Zuul.interfaces import IComponentInfo, IRRDDataSourceInfo
from Products.Zuul.form import schema
from Products.Zuul.utils import ZuulMessageFactory as _t

class ICMComponentInfo(IComponentInfo):
    media_description = schema.TextLine(title=_t(u'Type'), group='Detail', readonly=True)