export const __webpack_ids__=["2999"];export const __webpack_modules__={46784:function(e,a,t){t.a(e,(async function(e,l){try{t.d(a,{u:()=>u});var i=t(69440),s=t(27486),n=e([i]);i=(n.then?(await n)():n)[0];const u=(e,a)=>{try{return o(a)?.of(e)??e}catch{return e}},o=(0,s.Z)((e=>new Intl.DisplayNames(e.language,{type:"language",fallback:"code"})));l()}catch(u){l(u)}}))},96980:function(e,a,t){t.a(e,(async function(e,l){try{t.d(a,{C:()=>y});var i=t(44249),s=t(72621),n=t(69440),u=t(57243),o=t(50778),r=t(27486),d=t(11297),c=t(81036),h=t(46784),g=t(32770),v=t(55534),k=(t(74064),t(58130),e([n,h]));[n,h]=k.then?(await k)():k;const y=(e,a,t,l)=>{let i=[];if(a){const a=v.o.translations;i=e.map((e=>{let t=a[e]?.nativeName;if(!t)try{t=new Intl.DisplayNames(e,{type:"language",fallback:"code"}).of(e)}catch(l){t=e}return{value:e,label:t}}))}else l&&(i=e.map((e=>({value:e,label:(0,h.u)(e,l)}))));return!t&&l&&i.sort(((e,a)=>(0,g.fe)(e.label,a.label,l.language))),i};(0,i.Z)([(0,o.Mo)("ha-language-picker")],(function(e,a){class t extends a{constructor(...a){super(...a),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,o.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Array})],key:"languages",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({attribute:"native-name",type:Boolean})],key:"nativeName",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({attribute:"no-sort",type:Boolean})],key:"noSort",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({attribute:"inline-arrow",type:Boolean})],key:"inlineArrow",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_defaultLanguages",value(){return[]}},{kind:"field",decorators:[(0,o.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,s.Z)(t,"firstUpdated",this,3)([e]),this._computeDefaultLanguageOptions()}},{kind:"method",key:"updated",value:function(e){(0,s.Z)(t,"updated",this,3)([e]);const a=e.has("hass")&&this.hass&&e.get("hass")&&e.get("hass").locale.language!==this.hass.locale.language;if(e.has("languages")||e.has("value")||a){if(this._select.layoutOptions(),this._select.value!==this.value&&(0,d.B)(this,"value-changed",{value:this._select.value}),!this.value)return;const e=this._getLanguagesOptions(this.languages??this._defaultLanguages,this.nativeName,this.noSort,this.hass?.locale).findIndex((e=>e.value===this.value));-1===e&&(this.value=void 0),a&&this._select.select(e)}}},{kind:"field",key:"_getLanguagesOptions",value(){return(0,r.Z)(y)}},{kind:"method",key:"_computeDefaultLanguageOptions",value:function(){this._defaultLanguages=Object.keys(v.o.translations)}},{kind:"method",key:"render",value:function(){const e=this._getLanguagesOptions(this.languages??this._defaultLanguages,this.nativeName,this.noSort,this.hass?.locale),a=this.value??(this.required?e[0]?.value:this.value);return u.dy`
      <ha-select
        .label=${this.label??(this.hass?.localize("ui.components.language-picker.language")||"Language")}
        .value=${a||""}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${c.U}
        fixedMenuPosition
        naturalMenuWidth
        .inlineArrow=${this.inlineArrow}
      >
        ${0===e.length?u.dy`<ha-list-item value=""
              >${this.hass?.localize("ui.components.language-picker.no_languages")||"No languages"}</ha-list-item
            >`:e.map((e=>u.dy`
                <ha-list-item .value=${e.value}
                  >${e.label}</ha-list-item
                >
              `))}
      </ha-select>
    `}},{kind:"field",static:!0,key:"styles",value(){return u.iv`
    ha-select {
      width: 100%;
    }
  `}},{kind:"method",key:"_changed",value:function(e){const a=e.target;""!==a.value&&a.value!==this.value&&(this.value=a.value,(0,d.B)(this,"value-changed",{value:this.value}))}}]}}),u.oi);l()}catch(y){l(y)}}))},37270:function(e,a,t){t.a(e,(async function(e,l){try{t.r(a),t.d(a,{HaLanguageSelector:()=>r});var i=t(44249),s=t(57243),n=t(50778),u=t(96980),o=e([u]);u=(o.then?(await o)():o)[0];let r=(0,i.Z)([(0,n.Mo)("ha-selector-language")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"method",key:"render",value:function(){return s.dy`
      <ha-language-picker
        .hass=${this.hass}
        .value=${this.value}
        .label=${this.label}
        .helper=${this.helper}
        .languages=${this.selector.language?.languages}
        .nativeName=${Boolean(this.selector?.language?.native_name)}
        .noSort=${Boolean(this.selector?.language?.no_sort)}
        .disabled=${this.disabled}
        .required=${this.required}
      ></ha-language-picker>
    `}},{kind:"field",static:!0,key:"styles",value(){return s.iv`
    ha-language-picker {
      width: 100%;
    }
  `}}]}}),s.oi);l()}catch(r){l(r)}}))}};
//# sourceMappingURL=2999.99b9139799f003ba.js.map