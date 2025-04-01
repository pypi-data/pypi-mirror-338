export const __webpack_ids__=["8046"];export const __webpack_modules__={73525:function(e,i,t){t.d(i,{C:()=>s});var a=t(87729);const s=e=>{return i=e.entity_id,void 0===(t=e.attributes).friendly_name?(0,a.p)(i).replace(/_/g," "):(t.friendly_name??"").toString();var i,t}},59498:function(e,i,t){t.a(e,(async function(e,i){try{var a=t(44249),s=(t(74064),t(57243)),n=t(50778),o=t(27486),l=t(11297),d=t(79575),r=t(73525),h=t(19039),c=(t(69484),t(59897),t(10508),t(21881)),u=t(32770),_=t(73976),m=t(1275),y=t(56395),f=e([c]);c=(f.then?(await f)():f)[0];const v="___create-new-entity___";(0,a.Z)([(0,n.Mo)("ha-entity-picker")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"autofocus",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"allow-custom-entity"})],key:"allowCustomEntity",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1,type:Array})],key:"createDomains",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-domains"})],key:"includeDomains",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"exclude-domains"})],key:"excludeDomains",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-unit-of-measurement"})],key:"includeUnitOfMeasurement",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-entities"})],key:"includeEntities",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"exclude-entities"})],key:"excludeEntities",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"entityFilter",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:"hide-clear-icon",type:Boolean})],key:"hideClearIcon",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({attribute:"item-label-path"})],key:"itemLabelPath",value(){return"friendly_name"}},{kind:"field",decorators:[(0,n.SB)()],key:"_opened",value(){return!1}},{kind:"field",decorators:[(0,n.IO)("ha-combo-box",!0)],key:"comboBox",value:void 0},{kind:"method",key:"open",value:async function(){await this.updateComplete,await(this.comboBox?.open())}},{kind:"method",key:"focus",value:async function(){await this.updateComplete,await(this.comboBox?.focus())}},{kind:"field",key:"_initedStates",value(){return!1}},{kind:"field",key:"_states",value(){return[]}},{kind:"field",key:"_rowRenderer",value(){return e=>s.dy`<ha-list-item graphic="avatar" .twoline=${!!e.entity_id}>
      ${e.state?s.dy`<state-badge
            slot="graphic"
            .stateObj=${e}
            .hass=${this.hass}
          ></state-badge>`:""}
      <span>${e.friendly_name}</span>
      <span slot="secondary"
        >${e.entity_id.startsWith(v)?this.hass.localize("ui.components.entity.entity-picker.new_entity"):e.entity_id}</span
      >
    </ha-list-item>`}},{kind:"field",key:"_getStates",value(){return(0,o.Z)(((e,i,t,a,s,n,o,l,h,c)=>{let _=[];if(!i)return[];let f=Object.keys(i.states);const p=c?.length?c.map((e=>{const t=i.localize("ui.components.entity.entity-picker.create_helper",{domain:(0,y.X)(e)?i.localize(`ui.panel.config.helpers.types.${e}`):(0,m.Lh)(i.localize,e)});return{entity_id:v+e,state:"on",last_changed:"",last_updated:"",context:{id:"",user_id:null,parent_id:null},friendly_name:t,attributes:{icon:"mdi:plus"},strings:[e,t]}})):[];return f.length?(l&&(f=f.filter((e=>l.includes(e)))),h&&(f=f.filter((e=>!h.includes(e)))),t&&(f=f.filter((e=>t.includes((0,d.M)(e))))),a&&(f=f.filter((e=>!a.includes((0,d.M)(e))))),_=f.map((e=>{const t=(0,r.C)(i.states[e])||e;return{...i.states[e],friendly_name:t,strings:[e,t]}})).sort(((e,i)=>(0,u.fe)(e.friendly_name,i.friendly_name,this.hass.locale.language))),n&&(_=_.filter((e=>e.entity_id===this.value||e.attributes.device_class&&n.includes(e.attributes.device_class)))),o&&(_=_.filter((e=>e.entity_id===this.value||e.attributes.unit_of_measurement&&o.includes(e.attributes.unit_of_measurement)))),s&&(_=_.filter((e=>e.entity_id===this.value||s(e)))),_.length?(p?.length&&_.push(...p),_):[{entity_id:"",state:"",last_changed:"",last_updated:"",context:{id:"",user_id:null,parent_id:null},friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_match"),attributes:{friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_match"),icon:"mdi:magnify"},strings:[]},...p]):[{entity_id:"",state:"",last_changed:"",last_updated:"",context:{id:"",user_id:null,parent_id:null},friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_entities"),attributes:{friendly_name:this.hass.localize("ui.components.entity.entity-picker.no_entities"),icon:"mdi:magnify"},strings:[]},...p]}))}},{kind:"method",key:"shouldUpdate",value:function(e){return!!(e.has("value")||e.has("label")||e.has("disabled"))||!(!e.has("_opened")&&this._opened)}},{kind:"method",key:"willUpdate",value:function(e){(!this._initedStates||e.has("_opened")&&this._opened)&&(this._states=this._getStates(this._opened,this.hass,this.includeDomains,this.excludeDomains,this.entityFilter,this.includeDeviceClasses,this.includeUnitOfMeasurement,this.includeEntities,this.excludeEntities,this.createDomains),this._initedStates&&(this.comboBox.filteredItems=this._states),this._initedStates=!0),e.has("createDomains")&&this.createDomains?.length&&this.hass.loadFragmentTranslation("config")}},{kind:"method",key:"render",value:function(){return s.dy`
      <ha-combo-box
        item-value-path="entity_id"
        .itemLabelPath=${this.itemLabelPath}
        .hass=${this.hass}
        .value=${this._value}
        .label=${void 0===this.label?this.hass.localize("ui.components.entity.entity-picker.entity"):this.label}
        .helper=${this.helper}
        .allowCustomValue=${this.allowCustomEntity}
        .filteredItems=${this._states}
        .renderer=${this._rowRenderer}
        .required=${this.required}
        .disabled=${this.disabled}
        @opened-changed=${this._openedChanged}
        @value-changed=${this._valueChanged}
        @filter-changed=${this._filterChanged}
      >
      </ha-combo-box>
    `}},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"method",key:"_openedChanged",value:function(e){this._opened=e.detail.value}},{kind:"method",key:"_valueChanged",value:function(e){e.stopPropagation();const i=e.detail.value?.trim();if(i&&i.startsWith(v)){const e=i.substring(v.length);(0,_.j)(this,{domain:e,dialogClosedCallback:e=>{e.entityId&&this._setValue(e.entityId)}})}else i!==this._value&&this._setValue(i)}},{kind:"method",key:"_filterChanged",value:function(e){const i=e.target,t=e.detail.value.trim().toLowerCase();i.filteredItems=t.length?(0,h.q)(t,this._states):this._states}},{kind:"method",key:"_setValue",value:function(e){this.value=e,setTimeout((()=>{(0,l.B)(this,"value-changed",{value:e}),(0,l.B)(this,"change")}),0)}}]}}),s.oi);i()}catch(v){i(v)}}))},62304:function(e,i,t){var a=t(44249),s=t(57243),n=t(50778),o=t(11297);t(26375);(0,a.Z)([(0,n.Mo)("ha-aliases-editor")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array})],key:"aliases",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"method",key:"render",value:function(){return this.aliases?s.dy`
      <ha-multi-textfield
        .hass=${this.hass}
        .value=${this.aliases}
        .disabled=${this.disabled}
        .label=${this.hass.localize("ui.dialogs.aliases.label")}
        .removeLabel=${this.hass.localize("ui.dialogs.aliases.remove")}
        .addLabel=${this.hass.localize("ui.dialogs.aliases.add")}
        item-index
        @value-changed=${this._aliasesChanged}
      >
      </ha-multi-textfield>
    `:s.Ld}},{kind:"method",key:"_aliasesChanged",value:function(e){(0,o.B)(this,"value-changed",{value:e})}}]}}),s.oi)},95241:function(e,i,t){t.d(i,{m:()=>o});var a=t(44249),s=t(57243),n=t(50778);t(10508);const o=e=>{switch(e.level){case 0:return"M11,10H13V16H11V10M22,12H19V20H5V12H2L12,3L22,12M15,10A2,2 0 0,0 13,8H11A2,2 0 0,0 9,10V16A2,2 0 0,0 11,18H13A2,2 0 0,0 15,16V10Z";case 1:return"M12,3L2,12H5V20H19V12H22L12,3M10,8H14V18H12V10H10V8Z";case 2:return"M12,3L2,12H5V20H19V12H22L12,3M9,8H13A2,2 0 0,1 15,10V12A2,2 0 0,1 13,14H11V16H15V18H9V14A2,2 0 0,1 11,12H13V10H9V8Z";case 3:return"M12,3L22,12H19V20H5V12H2L12,3M15,11.5V10C15,8.89 14.1,8 13,8H9V10H13V12H11V14H13V16H9V18H13A2,2 0 0,0 15,16V14.5A1.5,1.5 0 0,0 13.5,13A1.5,1.5 0 0,0 15,11.5Z";case-1:return"M12,3L2,12H5V20H19V12H22L12,3M11,15H7V13H11V15M15,18H13V10H11V8H15V18Z"}return"M10,20V14H14V20H19V12H22L12,3L2,12H5V20H10Z"};(0,a.Z)([(0,n.Mo)("ha-floor-icon")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"floor",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"icon",value:void 0},{kind:"method",key:"render",value:function(){if(this.floor.icon)return s.dy`<ha-icon .icon=${this.floor.icon}></ha-icon>`;const e=o(this.floor);return s.dy`<ha-svg-icon .path=${e}></ha-svg-icon>`}}]}}),s.oi)},5967:function(e,i,t){var a=t(44249),s=t(57243),n=t(50778),o=t(35359),l=t(27486),d=t(11297),r=t(79575),h=t(19039),c=t(71656),u=t(99523),_=t(20222),m=t(4557);const y=()=>Promise.all([t.e("8963"),t.e("5024")]).then(t.bind(t,89073));t(69484),t(95241),t(59897),t(74064);const f="___ADD_NEW___",v="___NO_FLOORS___",p="___ADD_NEW_SUGGESTION___",k=e=>s.dy`<ha-list-item
    graphic="icon"
    class=${(0,o.$)({"add-new":e.floor_id===f})}
  >
    <ha-floor-icon slot="graphic" .floor=${e}></ha-floor-icon>
    ${e.name}
  </ha-list-item>`;(0,a.Z)([(0,n.Mo)("ha-floor-picker")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"placeholder",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"no-add"})],key:"noAdd",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-domains"})],key:"includeDomains",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"exclude-domains"})],key:"excludeDomains",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Array,attribute:"exclude-floor"})],key:"excludeFloors",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"deviceFilter",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"entityFilter",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_opened",value:void 0},{kind:"field",decorators:[(0,n.IO)("ha-combo-box",!0)],key:"comboBox",value:void 0},{kind:"field",key:"_suggestion",value:void 0},{kind:"field",key:"_init",value(){return!1}},{kind:"method",key:"open",value:async function(){await this.updateComplete,await(this.comboBox?.open())}},{kind:"method",key:"focus",value:async function(){await this.updateComplete,await(this.comboBox?.focus())}},{kind:"field",key:"_getFloors",value(){return(0,l.Z)(((e,i,t,a,s,n,o,l,d,h,c)=>{let m,y,p={};(s||n||o||l||d)&&(p=(0,u.R6)(a),m=t,y=a.filter((e=>e.area_id)),s&&(m=m.filter((e=>{const i=p[e.id];return!(!i||!i.length)&&p[e.id].some((e=>s.includes((0,r.M)(e.entity_id))))})),y=y.filter((e=>s.includes((0,r.M)(e.entity_id))))),n&&(m=m.filter((e=>{const i=p[e.id];return!i||!i.length||a.every((e=>!n.includes((0,r.M)(e.entity_id))))})),y=y.filter((e=>!n.includes((0,r.M)(e.entity_id))))),o&&(m=m.filter((e=>{const i=p[e.id];return!(!i||!i.length)&&p[e.id].some((e=>{const i=this.hass.states[e.entity_id];return!!i&&(i.attributes.device_class&&o.includes(i.attributes.device_class))}))})),y=y.filter((e=>{const i=this.hass.states[e.entity_id];return i.attributes.device_class&&o.includes(i.attributes.device_class)}))),l&&(m=m.filter((e=>l(e)))),d&&(m=m.filter((e=>{const i=p[e.id];return!(!i||!i.length)&&p[e.id].some((e=>{const i=this.hass.states[e.entity_id];return!!i&&d(i)}))})),y=y.filter((e=>{const i=this.hass.states[e.entity_id];return!!i&&d(i)}))));let k,g=e;if(m&&(k=m.filter((e=>e.area_id)).map((e=>e.area_id))),y&&(k=(k??[]).concat(y.filter((e=>e.area_id)).map((e=>e.area_id)))),k){const e=(0,_.N5)(i);g=g.filter((i=>e[i.floor_id]?.some((e=>k.includes(e.area_id)))))}return c&&(g=g.filter((e=>!c.includes(e.floor_id)))),g.length||(g=[{floor_id:v,name:this.hass.localize("ui.components.floor-picker.no_floors"),icon:null,level:null,aliases:[],created_at:0,modified_at:0}]),h?g:[...g,{floor_id:f,name:this.hass.localize("ui.components.floor-picker.add_new"),icon:"mdi:plus",level:null,aliases:[],created_at:0,modified_at:0}]}))}},{kind:"method",key:"updated",value:function(e){if(!this._init&&this.hass||this._init&&e.has("_opened")&&this._opened){this._init=!0;const e=this._getFloors(Object.values(this.hass.floors),Object.values(this.hass.areas),Object.values(this.hass.devices),Object.values(this.hass.entities),this.includeDomains,this.excludeDomains,this.includeDeviceClasses,this.deviceFilter,this.entityFilter,this.noAdd,this.excludeFloors).map((e=>({...e,strings:[e.floor_id,e.name,...e.aliases]})));this.comboBox.items=e,this.comboBox.filteredItems=e}}},{kind:"method",key:"render",value:function(){return s.dy`
      <ha-combo-box
        .hass=${this.hass}
        .helper=${this.helper}
        item-value-path="floor_id"
        item-id-path="floor_id"
        item-label-path="name"
        .value=${this._value}
        .disabled=${this.disabled}
        .required=${this.required}
        .label=${void 0===this.label&&this.hass?this.hass.localize("ui.components.floor-picker.floor"):this.label}
        .placeholder=${this.placeholder?this.hass.floors[this.placeholder]?.name:void 0}
        .renderer=${k}
        @filter-changed=${this._filterChanged}
        @opened-changed=${this._openedChanged}
        @value-changed=${this._floorChanged}
      >
      </ha-combo-box>
    `}},{kind:"method",key:"_filterChanged",value:function(e){const i=e.target,t=e.detail.value;if(!t)return void(this.comboBox.filteredItems=this.comboBox.items);const a=(0,h.q)(t,i.items?.filter((e=>![v,f].includes(e.label_id)))||[]);0===a.length?this.noAdd?this.comboBox.filteredItems=[{floor_id:v,name:this.hass.localize("ui.components.floor-picker.no_match"),icon:null,level:null,aliases:[],created_at:0,modified_at:0}]:(this._suggestion=t,this.comboBox.filteredItems=[{floor_id:p,name:this.hass.localize("ui.components.floor-picker.add_new_sugestion",{name:this._suggestion}),icon:"mdi:plus",level:null,aliases:[],created_at:0,modified_at:0}]):this.comboBox.filteredItems=a}},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"method",key:"_openedChanged",value:function(e){this._opened=e.detail.value}},{kind:"method",key:"_floorChanged",value:function(e){e.stopPropagation();let i=e.detail.value;if(i===v)return i="",void this.comboBox.setInputValue("");var t,a;[p,f].includes(i)?(e.target.value=this._value,this.hass.loadFragmentTranslation("config"),t=this,a={suggestedName:i===p?this._suggestion:"",createEntry:async(e,i)=>{try{const t=await(0,_.z3)(this.hass,e);i.forEach((e=>{(0,c.IO)(this.hass,e,{floor_id:t.floor_id})}));const a=[...Object.values(this.hass.floors),t];this.comboBox.filteredItems=this._getFloors(a,Object.values(this.hass.areas),Object.values(this.hass.devices),Object.values(this.hass.entities),this.includeDomains,this.excludeDomains,this.includeDeviceClasses,this.deviceFilter,this.entityFilter,this.noAdd,this.excludeFloors),await this.updateComplete,await this.comboBox.updateComplete,this._setValue(t.floor_id)}catch(t){(0,m.Ys)(this,{title:this.hass.localize("ui.components.floor-picker.failed_create_floor"),text:t.message})}}},(0,d.B)(t,"show-dialog",{dialogTag:"dialog-floor-registry-detail",dialogImport:y,dialogParams:a}),this._suggestion=void 0,this.comboBox.setInputValue("")):i!==this._value&&this._setValue(i)}},{kind:"method",key:"_setValue",value:function(e){this.value=e,setTimeout((()=>{(0,d.B)(this,"value-changed",{value:e}),(0,d.B)(this,"change")}),0)}}]}}),s.oi)},36719:function(e,i,t){t.d(i,{ON:()=>o,PX:()=>l,V_:()=>d,lz:()=>n,nZ:()=>s,rk:()=>h});var a=t(95907);const s="unavailable",n="unknown",o="on",l="off",d=[s,n],r=[s,n,l],h=(0,a.z)(d);(0,a.z)(r)},20222:function(e,i,t){t.d(i,{N5:()=>s,z3:()=>a});t(32770),t(86912);const a=(e,i)=>e.callWS({type:"config/floor_registry/create",...i}),s=e=>{const i={};for(const t of e)t.floor_id&&(t.floor_id in i||(i[t.floor_id]=[]),i[t.floor_id].push(t));return i}},1275:function(e,i,t){t.d(i,{F3:()=>s,Lh:()=>a,t4:()=>n});const a=(e,i,t)=>e(`component.${i}.title`)||t?.name||i,s=(e,i)=>{const t={type:"manifest/list"};return i&&(t.integrations=i),e.callWS(t)},n=(e,i)=>e.callWS({type:"manifest/get",integration:i})},86438:function(e,i,t){t.d(i,{Ft:()=>a,S$:()=>s,sy:()=>n});const a="timestamp",s="temperature",n="humidity"},40600:function(e,i,t){t.a(e,(async function(e,a){try{t.r(i);var s=t(44249),n=t(57243),o=t(50778),l=t(11297),d=(t(17949),t(62304),t(41600),t(18805),t(5967),t(59498)),r=(t(70596),t(92687),t(71656)),h=t(66193),c=t(86438),u=t(4557),_=t(44118),m=e([d]);d=(m.then?(await m)():m)[0];const y={round:!1,type:"image/jpeg",quality:.75,aspectRatio:1.78},f=["sensor"],v=[c.S$],p=[c.sy];let k=(0,s.Z)(null,(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_name",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_aliases",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_labels",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_picture",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_icon",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_floor",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_temperatureEntity",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_humidityEntity",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_submitting",value:void 0},{kind:"method",key:"showDialog",value:async function(e){this._params=e,this._error=void 0,this._params.entry?(this._name=this._params.entry.name,this._aliases=this._params.entry.aliases,this._labels=this._params.entry.labels,this._picture=this._params.entry.picture,this._icon=this._params.entry.icon,this._floor=this._params.entry.floor_id,this._temperatureEntity=this._params.entry.temperature_entity_id,this._humidityEntity=this._params.entry.humidity_entity_id):(this._name=this._params.suggestedName||"",this._aliases=[],this._labels=[],this._picture=null,this._icon=null,this._floor=null,this._temperatureEntity=null,this._humidityEntity=null),await this.updateComplete}},{kind:"method",key:"closeDialog",value:function(){this._error="",this._params=void 0,(0,l.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"_renderSettings",value:function(e){return n.dy`
      ${e?n.dy`
            <ha-settings-row>
              <span slot="heading">
                ${this.hass.localize("ui.panel.config.areas.editor.area_id")}
              </span>
              <span slot="description"> ${e.area_id} </span>
            </ha-settings-row>
          `:n.Ld}

      <ha-textfield
        .value=${this._name}
        @input=${this._nameChanged}
        .label=${this.hass.localize("ui.panel.config.areas.editor.name")}
        .validationMessage=${this.hass.localize("ui.panel.config.areas.editor.name_required")}
        required
        dialogInitialFocus
      ></ha-textfield>

      <ha-icon-picker
        .hass=${this.hass}
        .value=${this._icon}
        @value-changed=${this._iconChanged}
        .label=${this.hass.localize("ui.panel.config.areas.editor.icon")}
      ></ha-icon-picker>

      <ha-floor-picker
        .hass=${this.hass}
        .value=${this._floor}
        @value-changed=${this._floorChanged}
        .label=${this.hass.localize("ui.panel.config.areas.editor.floor")}
      ></ha-floor-picker>

      <ha-labels-picker
        .hass=${this.hass}
        .value=${this._labels}
        @value-changed=${this._labelsChanged}
      ></ha-labels-picker>

      <ha-picture-upload
        .hass=${this.hass}
        .value=${this._picture}
        crop
        select-media
        .cropOptions=${y}
        @change=${this._pictureChanged}
      ></ha-picture-upload>
    `}},{kind:"method",key:"_renderAliasExpansion",value:function(){return n.dy`
      <ha-expansion-panel
        outlined
        .header=${this.hass.localize("ui.panel.config.areas.editor.aliases_section")}
        expanded
      >
        <div class="content">
          <p class="description">
            ${this.hass.localize("ui.panel.config.areas.editor.aliases_description")}
          </p>
          <ha-aliases-editor
            .hass=${this.hass}
            .aliases=${this._aliases}
            @value-changed=${this._aliasesChanged}
          ></ha-aliases-editor>
        </div>
      </ha-expansion-panel>
    `}},{kind:"method",key:"_renderRelatedEntitiesExpansion",value:function(){return n.dy`
      <ha-expansion-panel
        outlined
        .header=${this.hass.localize("ui.panel.config.areas.editor.related_entities_section")}
        expanded
      >
        <div class="content">
          <ha-entity-picker
            .hass=${this.hass}
            .label=${this.hass.localize("ui.panel.config.areas.editor.temperature_entity")}
            .helper=${this.hass.localize("ui.panel.config.areas.editor.temperature_entity_description")}
            .value=${this._temperatureEntity}
            .includeDomains=${f}
            .includeDeviceClasses=${v}
            .entityFilter=${this._areaEntityFilter}
            @value-changed=${this._sensorChanged}
          ></ha-entity-picker>

          <ha-entity-picker
            .hass=${this.hass}
            .label=${this.hass.localize("ui.panel.config.areas.editor.humidity_entity")}
            .helper=${this.hass.localize("ui.panel.config.areas.editor.humidity_entity_description")}
            .value=${this._humidityEntity}
            .includeDomains=${f}
            .includeDeviceClasses=${p}
            .entityFilter=${this._areaEntityFilter}
            @value-changed=${this._sensorChanged}
          ></ha-entity-picker>
        </div>
      </ha-expansion-panel>
    `}},{kind:"method",key:"render",value:function(){if(!this._params)return n.Ld;const e=this._params.entry,i=!this._isNameValid(),t=!e;return n.dy`
      <ha-dialog
        open
        @closed=${this.closeDialog}
        .heading=${(0,_.i)(this.hass,e?this.hass.localize("ui.panel.config.areas.editor.update_area"):this.hass.localize("ui.panel.config.areas.editor.create_area"))}
      >
        <div>
          ${this._error?n.dy`<ha-alert alert-type="error">${this._error}</ha-alert>`:""}
          <div class="form">
            ${this._renderSettings(e)} ${this._renderAliasExpansion()}
            ${t?n.Ld:this._renderRelatedEntitiesExpansion()}
          </div>
        </div>
        ${t?n.Ld:n.dy`<ha-button
              slot="secondaryAction"
              destructive
              @click=${this._deleteArea}
            >
              ${this.hass.localize("ui.common.delete")}
            </ha-button>`}
        <div slot="primaryAction">
          <ha-button @click=${this.closeDialog}>
            ${this.hass.localize("ui.common.cancel")}
          </ha-button>
          <ha-button
            @click=${this._updateEntry}
            .disabled=${i||this._submitting}
          >
            ${e?this.hass.localize("ui.common.save"):this.hass.localize("ui.common.create")}
          </ha-button>
        </div>
      </ha-dialog>
    `}},{kind:"method",key:"_isNameValid",value:function(){return""!==this._name.trim()}},{kind:"field",key:"_areaEntityFilter",value(){return e=>{const i=this.hass.entities[e.entity_id];if(!i)return!1;const t=this._params.entry.area_id;if(i.area_id===t)return!0;if(!i.device_id)return!1;const a=this.hass.devices[i.device_id];return a&&a.area_id===t}}},{kind:"method",key:"_nameChanged",value:function(e){this._error=void 0,this._name=e.target.value}},{kind:"method",key:"_floorChanged",value:function(e){this._error=void 0,this._floor=e.detail.value}},{kind:"method",key:"_iconChanged",value:function(e){this._error=void 0,this._icon=e.detail.value}},{kind:"method",key:"_labelsChanged",value:function(e){this._error=void 0,this._labels=e.detail.value}},{kind:"method",key:"_pictureChanged",value:function(e){this._error=void 0,this._picture=e.target.value}},{kind:"method",key:"_aliasesChanged",value:function(e){this._aliases=e.detail.value}},{kind:"method",key:"_sensorChanged",value:function(e){this[`_${e.target.includeDeviceClasses[0]}Entity`]=e.detail.value||null}},{kind:"method",key:"_updateEntry",value:async function(){const e=!this._params.entry;this._submitting=!0;try{const i={name:this._name.trim(),picture:this._picture||(e?void 0:null),icon:this._icon||(e?void 0:null),floor_id:this._floor||(e?void 0:null),labels:this._labels||null,aliases:this._aliases,temperature_entity_id:this._temperatureEntity,humidity_entity_id:this._humidityEntity};e?await this._params.createEntry(i):await this._params.updateEntry(i),this.closeDialog()}catch(i){this._error=i.message||this.hass.localize("ui.panel.config.areas.editor.unknown_error")}finally{this._submitting=!1}}},{kind:"method",key:"_deleteArea",value:async function(){if(!this._params?.entry)return;await(0,u.g7)(this,{title:this.hass.localize("ui.panel.config.areas.delete.confirmation_title",{name:this._params.entry.name}),text:this.hass.localize("ui.panel.config.areas.delete.confirmation_text"),dismissText:this.hass.localize("ui.common.cancel"),confirmText:this.hass.localize("ui.common.delete"),destructive:!0})&&(await(0,r.qv)(this.hass,this._params.entry.area_id),this.closeDialog())}},{kind:"get",static:!0,key:"styles",value:function(){return[h.yu,n.iv`
        ha-textfield {
          display: block;
        }
        ha-expansion-panel {
          --expansion-panel-content-padding: 0;
        }
        ha-aliases-editor,
        ha-entity-picker,
        ha-floor-picker,
        ha-icon-picker,
        ha-labels-picker,
        ha-picture-upload,
        ha-expansion-panel {
          display: block;
          margin-bottom: 16px;
        }
        ha-dialog {
          --mdc-dialog-min-width: min(600px, 100vw);
        }
        .content {
          padding: 12px;
        }
        .description {
          margin: 0 0 16px 0;
        }
      `]}}]}}),n.oi);customElements.define("dialog-area-registry-detail",k),a()}catch(y){a(y)}}))},73976:function(e,i,t){t.d(i,{j:()=>n});var a=t(11297);const s=()=>Promise.all([t.e("9287"),t.e("5444")]).then(t.bind(t,15808)),n=(e,i)=>{(0,a.B)(e,"show-dialog",{dialogTag:"dialog-helper-detail",dialogImport:s,dialogParams:i})}}};
//# sourceMappingURL=8046.8f697aefd7876f0a.js.map