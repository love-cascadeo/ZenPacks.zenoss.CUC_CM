(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'CiscoCMComponent',
    _t('Cisco CM Component'),
    _t('Cisco CM Components'));

ZC.CiscoCMComponentPanel = Ext.extend(ZC.ComponentGridPanel, {
	constructor: function(config) {
		config = Ext.applyIf(config||{}, {
			componentType: 'CiscoCMComponent',
			autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'media_description'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'}
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'media_description',
                dataIndex: 'media_description',
                header: _t('Media Device Description'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.CiscoCMComponentPanel.superclass.constructor.call(
 this, config);
    }
});

Ext.reg('CiscoCMComponentPanel', ZC.CiscoCMComponentPanel);

})();