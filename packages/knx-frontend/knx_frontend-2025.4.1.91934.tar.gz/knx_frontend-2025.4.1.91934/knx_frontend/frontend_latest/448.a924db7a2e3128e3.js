export const __webpack_ids__=["448"];export const __webpack_modules__={14716:function(e,i,t){t.d(i,{wZ:()=>a});var s=t(73525);const a=(e,i,t)=>(e=>(e.name_by_user||e.name)?.trim())(e)||t&&d(i,t)||i.localize("ui.panel.config.devices.unnamed_device",{type:i.localize(`ui.panel.config.devices.type.${e.entry_type||"device"}`)}),d=(e,i)=>{for(const t of i||[]){const i="string"==typeof t?t:t.entity_id,a=e.states[i];if(a)return(0,s.C)(a)}}},73525:function(e,i,t){t.d(i,{C:()=>a});var s=t(87729);const a=e=>{return i=e.entity_id,void 0===(t=e.attributes).friendly_name?(0,s.p)(i).replace(/_/g," "):(t.friendly_name??"").toString();var i,t}},66912:function(e,i,t){var s=t(44249),a=t(57243),d=t(50778),n=t(27486),r=t(11297),l=t(14716),o=t(79575),c=t(32770),u=t(19039),h=t(99523);t(69484),t(74064);const v=e=>a.dy`<ha-list-item .twoline=${!!e.area}>
    <span>${e.name}</span>
    <span slot="secondary">${e.area}</span>
  </ha-list-item>`;(0,s.Z)([(0,d.Mo)("ha-device-picker")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Array,attribute:"include-domains"})],key:"includeDomains",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Array,attribute:"exclude-domains"})],key:"excludeDomains",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Array,attribute:"exclude-devices"})],key:"excludeDevices",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"deviceFilter",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"entityFilter",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,d.SB)()],key:"_opened",value:void 0},{kind:"field",decorators:[(0,d.IO)("ha-combo-box",!0)],key:"comboBox",value:void 0},{kind:"field",key:"_init",value(){return!1}},{kind:"field",key:"_getDevices",value(){return(0,n.Z)(((e,i,t,s,a,d,n,r,u)=>{if(!e.length)return[{id:"no_devices",area:"",name:this.hass.localize("ui.components.device-picker.no_devices"),strings:[]}];let v={};(s||a||d||r)&&(v=(0,h.R6)(t));let y=e.filter((e=>e.id===this.value||!e.disabled_by));s&&(y=y.filter((e=>{const i=v[e.id];return!(!i||!i.length)&&v[e.id].some((e=>s.includes((0,o.M)(e.entity_id))))}))),a&&(y=y.filter((e=>{const i=v[e.id];return!i||!i.length||t.every((e=>!a.includes((0,o.M)(e.entity_id))))}))),u&&(y=y.filter((e=>!u.includes(e.id)))),d&&(y=y.filter((e=>{const i=v[e.id];return!(!i||!i.length)&&v[e.id].some((e=>{const i=this.hass.states[e.entity_id];return!!i&&(i.attributes.device_class&&d.includes(i.attributes.device_class))}))}))),r&&(y=y.filter((e=>{const i=v[e.id];return!(!i||!i.length)&&i.some((e=>{const i=this.hass.states[e.entity_id];return!!i&&r(i)}))}))),n&&(y=y.filter((e=>e.id===this.value||n(e))));const k=y.map((e=>{const t=(0,l.wZ)(e,this.hass,v[e.id]);return{id:e.id,name:t||this.hass.localize("ui.components.device-picker.unnamed_device"),area:e.area_id&&i[e.area_id]?i[e.area_id].name:this.hass.localize("ui.components.device-picker.no_area"),strings:[t||""]}}));return k.length?1===k.length?k:k.sort(((e,i)=>(0,c.$K)(e.name||"",i.name||"",this.hass.locale.language))):[{id:"no_devices",area:"",name:this.hass.localize("ui.components.device-picker.no_match"),strings:[]}]}))}},{kind:"method",key:"open",value:async function(){await this.updateComplete,await(this.comboBox?.open())}},{kind:"method",key:"focus",value:async function(){await this.updateComplete,await(this.comboBox?.focus())}},{kind:"method",key:"updated",value:function(e){if(!this._init&&this.hass||this._init&&e.has("_opened")&&this._opened){this._init=!0;const e=this._getDevices(Object.values(this.hass.devices),this.hass.areas,Object.values(this.hass.entities),this.includeDomains,this.excludeDomains,this.includeDeviceClasses,this.deviceFilter,this.entityFilter,this.excludeDevices);this.comboBox.items=e,this.comboBox.filteredItems=e}}},{kind:"method",key:"render",value:function(){return a.dy`
      <ha-combo-box
        .hass=${this.hass}
        .label=${void 0===this.label&&this.hass?this.hass.localize("ui.components.device-picker.device"):this.label}
        .value=${this._value}
        .helper=${this.helper}
        .renderer=${v}
        .disabled=${this.disabled}
        .required=${this.required}
        item-id-path="id"
        item-value-path="id"
        item-label-path="name"
        @opened-changed=${this._openedChanged}
        @value-changed=${this._deviceChanged}
        @filter-changed=${this._filterChanged}
      ></ha-combo-box>
    `}},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"method",key:"_filterChanged",value:function(e){const i=e.target,t=e.detail.value.toLowerCase();i.filteredItems=t.length?(0,u.q)(t,i.items||[]):i.items}},{kind:"method",key:"_deviceChanged",value:function(e){e.stopPropagation();let i=e.detail.value;"no_devices"===i&&(i=""),i!==this._value&&this._setValue(i)}},{kind:"method",key:"_openedChanged",value:function(e){this._opened=e.detail.value}},{kind:"method",key:"_setValue",value:function(e){this.value=e,setTimeout((()=>{(0,r.B)(this,"value-changed",{value:e}),(0,r.B)(this,"change")}),0)}}]}}),a.oi)},6732:function(e,i,t){t.r(i),t.d(i,{HaDeviceSelector:()=>y});var s=t(44249),a=t(72621),d=t(57243),n=t(50778),r=t(27486),l=t(24785),o=t(11297),c=t(99523),u=t(82659),h=t(87055),v=t(45634);t(66912);(0,s.Z)([(0,n.Mo)("ha-devices-picker")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array})],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-domains"})],key:"includeDomains",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"exclude-domains"})],key:"excludeDomains",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:"picked-device-label"})],key:"pickedDeviceLabel",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:"pick-device-label"})],key:"pickDeviceLabel",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"deviceFilter",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"entityFilter",value:void 0},{kind:"method",key:"render",value:function(){if(!this.hass)return d.Ld;const e=this._currentDevices;return d.dy`
      ${e.map((e=>d.dy`
          <div>
            <ha-device-picker
              allow-custom-entity
              .curValue=${e}
              .hass=${this.hass}
              .deviceFilter=${this.deviceFilter}
              .entityFilter=${this.entityFilter}
              .includeDomains=${this.includeDomains}
              .excludeDomains=${this.excludeDomains}
              .includeDeviceClasses=${this.includeDeviceClasses}
              .value=${e}
              .label=${this.pickedDeviceLabel}
              .disabled=${this.disabled}
              @value-changed=${this._deviceChanged}
            ></ha-device-picker>
          </div>
        `))}
      <div>
        <ha-device-picker
          allow-custom-entity
          .hass=${this.hass}
          .helper=${this.helper}
          .deviceFilter=${this.deviceFilter}
          .entityFilter=${this.entityFilter}
          .includeDomains=${this.includeDomains}
          .excludeDomains=${this.excludeDomains}
          .excludeDevices=${e}
          .includeDeviceClasses=${this.includeDeviceClasses}
          .label=${this.pickDeviceLabel}
          .disabled=${this.disabled}
          .required=${this.required&&!e.length}
          @value-changed=${this._addDevice}
        ></ha-device-picker>
      </div>
    `}},{kind:"get",key:"_currentDevices",value:function(){return this.value||[]}},{kind:"method",key:"_updateDevices",value:async function(e){(0,o.B)(this,"value-changed",{value:e}),this.value=e}},{kind:"method",key:"_deviceChanged",value:function(e){e.stopPropagation();const i=e.currentTarget.curValue,t=e.detail.value;t!==i&&(void 0===t?this._updateDevices(this._currentDevices.filter((e=>e!==i))):this._updateDevices(this._currentDevices.map((e=>e===i?t:e))))}},{kind:"method",key:"_addDevice",value:async function(e){e.stopPropagation();const i=e.detail.value;if(e.currentTarget.value="",!i)return;const t=this._currentDevices;t.includes(i)||this._updateDevices([...t,i])}},{kind:"field",static:!0,key:"styles",value(){return d.iv`
    div {
      margin-top: 8px;
    }
  `}}]}}),d.oi);let y=(0,s.Z)([(0,n.Mo)("ha-selector-device")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_entitySources",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_configEntries",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"field",key:"_deviceIntegrationLookup",value(){return(0,r.Z)(c.HP)}},{kind:"method",key:"_hasIntegration",value:function(e){return e.device?.filter&&(0,l.r)(e.device.filter).some((e=>e.integration))||e.device?.entity&&(0,l.r)(e.device.entity).some((e=>e.integration))}},{kind:"method",key:"willUpdate",value:function(e){e.has("selector")&&void 0!==this.value&&(this.selector.device?.multiple&&!Array.isArray(this.value)?(this.value=[this.value],(0,o.B)(this,"value-changed",{value:this.value})):!this.selector.device?.multiple&&Array.isArray(this.value)&&(this.value=this.value[0],(0,o.B)(this,"value-changed",{value:this.value})))}},{kind:"method",key:"updated",value:function(e){(0,a.Z)(t,"updated",this,3)([e]),e.has("selector")&&this._hasIntegration(this.selector)&&!this._entitySources&&(0,u.m)(this.hass).then((e=>{this._entitySources=e})),!this._configEntries&&this._hasIntegration(this.selector)&&(this._configEntries=[],(0,h.pB)(this.hass).then((e=>{this._configEntries=e})))}},{kind:"method",key:"render",value:function(){return this._hasIntegration(this.selector)&&!this._entitySources?d.Ld:this.selector.device?.multiple?d.dy`
      ${this.label?d.dy`<label>${this.label}</label>`:""}
      <ha-devices-picker
        .hass=${this.hass}
        .value=${this.value}
        .helper=${this.helper}
        .deviceFilter=${this._filterDevices}
        .entityFilter=${this.selector.device?.entity?this._filterEntities:void 0}
        .disabled=${this.disabled}
        .required=${this.required}
      ></ha-devices-picker>
    `:d.dy`
        <ha-device-picker
          .hass=${this.hass}
          .value=${this.value}
          .label=${this.label}
          .helper=${this.helper}
          .deviceFilter=${this._filterDevices}
          .entityFilter=${this.selector.device?.entity?this._filterEntities:void 0}
          .disabled=${this.disabled}
          .required=${this.required}
          allow-custom-entity
        ></ha-device-picker>
      `}},{kind:"field",key:"_filterDevices",value(){return e=>{if(!this.selector.device?.filter)return!0;const i=this._entitySources?this._deviceIntegrationLookup(this._entitySources,Object.values(this.hass.entities),Object.values(this.hass.devices),this._configEntries):void 0;return(0,l.r)(this.selector.device.filter).some((t=>(0,v.lE)(t,e,i)))}}},{kind:"field",key:"_filterEntities",value(){return e=>(0,l.r)(this.selector.device.entity).some((i=>(0,v.lV)(i,e,this._entitySources)))}}]}}),d.oi)},82659:function(e,i,t){t.d(i,{m:()=>d});const s=async(e,i,t,a,d,...n)=>{const r=d,l=r[e],o=l=>a&&a(d,l.result)!==l.cacheKey?(r[e]=void 0,s(e,i,t,a,d,...n)):l.result;if(l)return l instanceof Promise?l.then(o):o(l);const c=t(d,...n);return r[e]=c,c.then((t=>{r[e]={result:t,cacheKey:a?.(d,t)},setTimeout((()=>{r[e]=void 0}),i)}),(()=>{r[e]=void 0})),c},a=e=>e.callWS({type:"entity/source"}),d=e=>s("_entitySources",3e4,a,(e=>Object.keys(e.states).length),e)}};
//# sourceMappingURL=448.a924db7a2e3128e3.js.map