##############################################################################
#
# Copyright (C) Zenoss, Inc. 2013, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################



from Products.ZenModel.Device import Device
from Products.ZenRelations.RelSchema import ToManyCont, ToOne

class CiscoCMDevice(Device):
    _relations = Device._relations + (
        ('cmComponents', ToManyCont(ToOne,
            'ZenPacks.zenoss.CUC_CM.CiscoCMComponent',
            'host',
            )),
        )
