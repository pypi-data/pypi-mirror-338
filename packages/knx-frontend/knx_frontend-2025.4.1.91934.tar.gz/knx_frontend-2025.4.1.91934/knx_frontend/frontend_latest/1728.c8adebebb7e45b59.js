export const __webpack_ids__=["1728"];export const __webpack_modules__={73525:function(e,t,i){i.d(t,{C:()=>a});var s=i(87729);const a=e=>{return t=e.entity_id,void 0===(i=e.attributes).friendly_name?(0,s.p)(t).replace(/_/g," "):(i.friendly_name??"").toString();var t,i}},19082:function(e,t,i){i.r(t),i.d(t,{HaTTSSelector:()=>g});var s=i(44249),a=i(57243),n=i(50778),d=i(72621),l=i(11297),r=i(81036),u=i(73525),o=i(56587),h=i(421),c=(i(74064),i(58130),i(79575));const v="__NONE_OPTION__";(0,s.Z)([(0,n.Mo)("ha-tts-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"language",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_engines",value:void 0},{kind:"method",key:"render",value:function(){if(!this._engines)return a.Ld;let e=this.value;if(!e&&this.required){for(const t of Object.values(this.hass.entities))if("cloud"===t.platform&&"tts"===(0,c.M)(t.entity_id)){e=t.entity_id;break}if(!e)for(const t of this._engines)if(0!==t?.supported_languages?.length){e=t.engine_id;break}}return e||(e=v),a.dy`
      <ha-select
        .label=${this.label||this.hass.localize("ui.components.tts-picker.tts")}
        .value=${e}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${r.U}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${this.required?a.Ld:a.dy`<ha-list-item .value=${v}>
              ${this.hass.localize("ui.components.tts-picker.none")}
            </ha-list-item>`}
        ${this._engines.map((t=>{if(t.deprecated&&t.engine_id!==e)return a.Ld;let i;if(t.engine_id.includes(".")){const e=this.hass.states[t.engine_id];i=e?(0,u.C)(e):t.engine_id}else i=t.name||t.engine_id;return a.dy`<ha-list-item
            .value=${t.engine_id}
            .disabled=${0===t.supported_languages?.length}
          >
            ${i}
          </ha-list-item>`}))}
      </ha-select>
    `}},{kind:"method",key:"willUpdate",value:function(e){(0,d.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated?e.has("language")&&this._debouncedUpdateEngines():this._updateEngines()}},{kind:"field",key:"_debouncedUpdateEngines",value(){return(0,o.D)((()=>this._updateEngines()),500)}},{kind:"method",key:"_updateEngines",value:async function(){if(this._engines=(await(0,h.Wg)(this.hass,this.language,this.hass.config.country||void 0)).providers,!this.value)return;const e=this._engines.find((e=>e.engine_id===this.value));(0,l.B)(this,"supported-languages-changed",{value:e?.supported_languages}),e&&0!==e.supported_languages?.length||(this.value=void 0,(0,l.B)(this,"value-changed",{value:this.value}))}},{kind:"field",static:!0,key:"styles",value(){return a.iv`
    ha-select {
      width: 100%;
    }
  `}},{kind:"method",key:"_changed",value:function(e){const t=e.target;!this.hass||""===t.value||t.value===this.value||void 0===this.value&&t.value===v||(this.value=t.value===v?void 0:t.value,(0,l.B)(this,"value-changed",{value:this.value}),(0,l.B)(this,"supported-languages-changed",{value:this._engines.find((e=>e.engine_id===this.value))?.supported_languages}))}}]}}),a.oi);let g=(0,s.Z)([(0,n.Mo)("ha-selector-tts")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"context",value:void 0},{kind:"method",key:"render",value:function(){return a.dy`<ha-tts-picker
      .hass=${this.hass}
      .value=${this.value}
      .label=${this.label}
      .helper=${this.helper}
      .language=${this.selector.tts?.language||this.context?.language}
      .disabled=${this.disabled}
      .required=${this.required}
    ></ha-tts-picker>`}},{kind:"field",static:!0,key:"styles",value(){return a.iv`
    ha-tts-picker {
      width: 100%;
    }
  `}}]}}),a.oi)},421:function(e,t,i){i.d(t,{MV:()=>u,Wg:()=>l,Xk:()=>d,aT:()=>s,b_:()=>n,yP:()=>r});const s=(e,t)=>e.callApi("POST","tts_get_url",t),a="media-source://tts/",n=e=>e.startsWith(a),d=e=>e.substring(19),l=(e,t,i)=>e.callWS({type:"tts/engine/list",language:t,country:i}),r=(e,t)=>e.callWS({type:"tts/engine/get",engine_id:t}),u=(e,t,i)=>e.callWS({type:"tts/engine/voices",engine_id:t,language:i})}};
//# sourceMappingURL=1728.c8adebebb7e45b59.js.map