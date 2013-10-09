##############################################################################
#
# Copyright (C) Zenoss, Inc. 2013, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################


from Globals import InitializeClass

from Products.ZenRelations.RelSchema import ToOne, ToManyCont
from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity


class CiscoCMComponent(DeviceComponent, ManagedEntity):
    portal_type = meta_type = 'CiscoCMComponent'

    description = None

    _properties = ManagedEntity._properties + (
        {'id':'description', 'type':'string', 'mode':''},
        )

    _relations = ManagedEntity._relations + (
        ("host", ToOne(ToManyCont,
            "ZenPacks.zenoss.CUC_CM.CiscoCMDevice", "cmComponents")),
        )

    def device(self):
        return self.host()


InitializeClass(CiscoCMComponent)
