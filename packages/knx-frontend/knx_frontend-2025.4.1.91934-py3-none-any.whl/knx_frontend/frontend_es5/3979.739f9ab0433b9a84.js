/*! For license information please see 3979.739f9ab0433b9a84.js.LICENSE.txt */
"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["3979"],{34082:function(e,t,i){i.d(t,{T:()=>n});i(19134),i(5740);const s=/^(\w+)\.(\w+)$/,n=e=>s.test(e)},94999:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(73577),n=(i(19083),i(71695),i(9359),i(56475),i(70104),i(40251),i(61006),i(47021),i(57243)),r=i(50778),a=i(27486),l=i(11297),d=i(34082),u=i(59498),o=e([u]);u=(o.then?(await o)():o)[0];let c,h,v,y=e=>e;(0,s.Z)([(0,r.Mo)("ha-entities-picker")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array})],key:"value",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array,attribute:"include-domains"})],key:"includeDomains",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array,attribute:"exclude-domains"})],key:"excludeDomains",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array,attribute:"include-device-classes"})],key:"includeDeviceClasses",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array,attribute:"include-unit-of-measurement"})],key:"includeUnitOfMeasurement",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array,attribute:"include-entities"})],key:"includeEntities",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array,attribute:"exclude-entities"})],key:"excludeEntities",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:"picked-entity-label"})],key:"pickedEntityLabel",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:"pick-entity-label"})],key:"pickEntityLabel",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"entityFilter",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1,type:Array})],key:"createDomains",value:void 0},{kind:"method",key:"render",value:function(){if(!this.hass)return n.Ld;const e=this._currentEntities;return(0,n.dy)(c||(c=y`
      ${0}
      <div>
        <ha-entity-picker
          allow-custom-entity
          .hass=${0}
          .includeDomains=${0}
          .excludeDomains=${0}
          .includeEntities=${0}
          .excludeEntities=${0}
          .includeDeviceClasses=${0}
          .includeUnitOfMeasurement=${0}
          .entityFilter=${0}
          .label=${0}
          .helper=${0}
          .disabled=${0}
          .createDomains=${0}
          .required=${0}
          @value-changed=${0}
        ></ha-entity-picker>
      </div>
    `),e.map((e=>(0,n.dy)(h||(h=y`
          <div>
            <ha-entity-picker
              allow-custom-entity
              .curValue=${0}
              .hass=${0}
              .includeDomains=${0}
              .excludeDomains=${0}
              .includeEntities=${0}
              .excludeEntities=${0}
              .includeDeviceClasses=${0}
              .includeUnitOfMeasurement=${0}
              .entityFilter=${0}
              .value=${0}
              .label=${0}
              .disabled=${0}
              .createDomains=${0}
              @value-changed=${0}
            ></ha-entity-picker>
          </div>
        `),e,this.hass,this.includeDomains,this.excludeDomains,this.includeEntities,this.excludeEntities,this.includeDeviceClasses,this.includeUnitOfMeasurement,this.entityFilter,e,this.pickedEntityLabel,this.disabled,this.createDomains,this._entityChanged))),this.hass,this.includeDomains,this.excludeDomains,this.includeEntities,this._excludeEntities(this.value,this.excludeEntities),this.includeDeviceClasses,this.includeUnitOfMeasurement,this.entityFilter,this.pickEntityLabel,this.helper,this.disabled,this.createDomains,this.required&&!e.length,this._addEntity)}},{kind:"field",key:"_excludeEntities",value(){return(0,a.Z)(((e,t)=>void 0===e?t:[...t||[],...e]))}},{kind:"get",key:"_currentEntities",value:function(){return this.value||[]}},{kind:"method",key:"_updateEntities",value:async function(e){this.value=e,(0,l.B)(this,"value-changed",{value:e})}},{kind:"method",key:"_entityChanged",value:function(e){e.stopPropagation();const t=e.currentTarget.curValue,i=e.detail.value;if(i===t||void 0!==i&&!(0,d.T)(i))return;const s=this._currentEntities;i&&!s.includes(i)?this._updateEntities(s.map((e=>e===t?i:e))):this._updateEntities(s.filter((e=>e!==t)))}},{kind:"method",key:"_addEntity",value:async function(e){e.stopPropagation();const t=e.detail.value;if(!t)return;if(e.currentTarget.value="",!t)return;const i=this._currentEntities;i.includes(t)||this._updateEntities([...i,t])}},{kind:"field",static:!0,key:"styles",value(){return(0,n.iv)(v||(v=y`
    div {
      margin-top: 8px;
    }
  `))}}]}}),n.oi);t()}catch(c){t(c)}}))},92697:function(e,t,i){i.a(e,(async function(e,s){try{i.r(t),i.d(t,{HaEntitySelector:()=>p});var n=i(73577),r=i(72621),a=(i(71695),i(9359),i(56475),i(52924),i(47021),i(57243)),l=i(50778),d=i(24785),u=i(11297),o=i(82659),c=i(45634),h=i(94999),v=i(59498),y=e([h,v]);[h,v]=y.then?(await y)():y;let k,f,$,b=e=>e,p=(0,n.Z)([(0,l.Mo)("ha-selector-entity")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,l.SB)()],key:"_entitySources",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"field",decorators:[(0,l.SB)()],key:"_createDomains",value:void 0},{kind:"method",key:"_hasIntegration",value:function(e){var t;return(null===(t=e.entity)||void 0===t?void 0:t.filter)&&(0,d.r)(e.entity.filter).some((e=>e.integration))}},{kind:"method",key:"willUpdate",value:function(e){var t,i;e.has("selector")&&void 0!==this.value&&(null!==(t=this.selector.entity)&&void 0!==t&&t.multiple&&!Array.isArray(this.value)?(this.value=[this.value],(0,u.B)(this,"value-changed",{value:this.value})):null!==(i=this.selector.entity)&&void 0!==i&&i.multiple||!Array.isArray(this.value)||(this.value=this.value[0],(0,u.B)(this,"value-changed",{value:this.value})))}},{kind:"method",key:"render",value:function(){var e,t,i;return this._hasIntegration(this.selector)&&!this._entitySources?a.Ld:null!==(e=this.selector.entity)&&void 0!==e&&e.multiple?(0,a.dy)(f||(f=b`
      ${0}
      <ha-entities-picker
        .hass=${0}
        .value=${0}
        .helper=${0}
        .includeEntities=${0}
        .excludeEntities=${0}
        .entityFilter=${0}
        .createDomains=${0}
        .disabled=${0}
        .required=${0}
      ></ha-entities-picker>
    `),this.label?(0,a.dy)($||($=b`<label>${0}</label>`),this.label):"",this.hass,this.value,this.helper,this.selector.entity.include_entities,this.selector.entity.exclude_entities,this._filterEntities,this._createDomains,this.disabled,this.required):(0,a.dy)(k||(k=b`<ha-entity-picker
        .hass=${0}
        .value=${0}
        .label=${0}
        .helper=${0}
        .includeEntities=${0}
        .excludeEntities=${0}
        .entityFilter=${0}
        .createDomains=${0}
        .disabled=${0}
        .required=${0}
        allow-custom-entity
      ></ha-entity-picker>`),this.hass,this.value,this.label,this.helper,null===(t=this.selector.entity)||void 0===t?void 0:t.include_entities,null===(i=this.selector.entity)||void 0===i?void 0:i.exclude_entities,this._filterEntities,this._createDomains,this.disabled,this.required)}},{kind:"method",key:"updated",value:function(e){(0,r.Z)(i,"updated",this,3)([e]),e.has("selector")&&this._hasIntegration(this.selector)&&!this._entitySources&&(0,o.m)(this.hass).then((e=>{this._entitySources=e})),e.has("selector")&&(this._createDomains=(0,c.bq)(this.selector))}},{kind:"field",key:"_filterEntities",value(){return e=>{var t;return null===(t=this.selector)||void 0===t||null===(t=t.entity)||void 0===t||!t.filter||(0,d.r)(this.selector.entity.filter).some((t=>(0,c.lV)(t,e,this._entitySources)))}}}]}}),a.oi);s()}catch(k){s(k)}}))},82659:function(e,t,i){i.d(t,{m:()=>r});i(71695),i(40251),i(47021);const s=async(e,t,i,n,r,...a)=>{const l=r,d=l[e],u=d=>n&&n(r,d.result)!==d.cacheKey?(l[e]=void 0,s(e,t,i,n,r,...a)):d.result;if(d)return d instanceof Promise?d.then(u):u(d);const o=i(r,...a);return l[e]=o,o.then((i=>{l[e]={result:i,cacheKey:null==n?void 0:n(r,i)},setTimeout((()=>{l[e]=void 0}),t)}),(()=>{l[e]=void 0})),o},n=e=>e.callWS({type:"entity/source"}),r=e=>s("_entitySources",3e4,n,(e=>Object.keys(e.states).length),e)},31050:function(e,t,i){i.d(t,{C:()=>h});i(71695),i(9359),i(1331),i(40251),i(47021);var s=i(57708),n=i(53232),r=i(1714);i(63721),i(88230),i(52247);class a{constructor(e){this.G=e}disconnect(){this.G=void 0}reconnect(e){this.G=e}deref(){return this.G}}class l{constructor(){this.Y=void 0,this.Z=void 0}get(){return this.Y}pause(){var e;null!==(e=this.Y)&&void 0!==e||(this.Y=new Promise((e=>this.Z=e)))}resume(){var e;null===(e=this.Z)||void 0===e||e.call(this),this.Y=this.Z=void 0}}var d=i(45779);const u=e=>!(0,n.pt)(e)&&"function"==typeof e.then,o=1073741823;class c extends r.sR{constructor(){super(...arguments),this._$C_t=o,this._$Cwt=[],this._$Cq=new a(this),this._$CK=new l}render(...e){var t;return null!==(t=e.find((e=>!u(e))))&&void 0!==t?t:s.Jb}update(e,t){const i=this._$Cwt;let n=i.length;this._$Cwt=t;const r=this._$Cq,a=this._$CK;this.isConnected||this.disconnected();for(let s=0;s<t.length&&!(s>this._$C_t);s++){const e=t[s];if(!u(e))return this._$C_t=s,e;s<n&&e===i[s]||(this._$C_t=o,n=0,Promise.resolve(e).then((async t=>{for(;a.get();)await a.get();const i=r.deref();if(void 0!==i){const s=i._$Cwt.indexOf(e);s>-1&&s<i._$C_t&&(i._$C_t=s,i.setValue(t))}})))}return s.Jb}disconnected(){this._$Cq.disconnect(),this._$CK.pause()}reconnected(){this._$Cq.reconnect(this),this._$CK.resume()}}const h=(0,d.XM)(c)}}]);
//# sourceMappingURL=3979.739f9ab0433b9a84.js.map