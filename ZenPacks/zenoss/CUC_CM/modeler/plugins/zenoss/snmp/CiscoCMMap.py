##############################################################################
#
# Copyright (C) Zenoss, Inc. 2013, all rights reserved.
#
# This content is made available according to terms specified in
# License.zenoss under the directory where your Zenoss product is installed.
#
##############################################################################


from Products.ZenUtils.Utils import prepId
from Products.DataCollector.plugins.CollectorPlugin \
    import SnmpPlugin, GetTableMap


class CiscoCMMap(SnmpPlugin):
    relname = "cmComponents"
    modname = "ZenPacks.zenoss.CUC_CM.CiscoCMComponent"
    usageColumns = {
        '.1.2': 'mediaDeviceName',
        '.1.4': 'mediaDeviceDescription',
        '.1.5': 'mediaDeviceStatus',
        }

    snmpGetTableMaps = (
        GetTableMap('ccmMediaDeviceTable', '.1.3.6.1.4.1.9.9.156.1.6.1',
            usageColumns),
        )

    def process(self, device, results, log):

        log.info('Processing %s for device %s', self.name(), device.id)
        getdata, tabledata = results
        log.debug("%s getdata = %s", device.id, getdata)
        log.debug("%s tabledata = %s", device.id, tabledata)

        usageTable = tabledata.get("ccmMediaDeviceTable", None)
        if usageTable is None:
            return None
        rm = self.relMap()

        for snmpindex, cmcomponent in usageTable.items():
            if not self.checkColumns(cmcomponent, self.usageColumns, log):
                continue
            om = self.objectMap(cmcomponent)
            log.debug("%s objectMap = %s", device.id, om)
            om.snmpindex = snmpindex
            om.id = om.mediaDeviceName
            om.description = om.mediaDeviceDescription
            log.debug("%s objectMap = %s", device.id, om)

            rm.append(om)

        return rm


