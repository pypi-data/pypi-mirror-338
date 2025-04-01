"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["2999"],{46784:function(e,a,t){t.a(e,(async function(e,l){try{t.d(a,{u:()=>o});var i=t(69440),n=t(27486),s=e([i]);i=(s.then?(await s)():s)[0];const o=(e,a)=>{try{var t,l;return null!==(t=null===(l=u(a))||void 0===l?void 0:l.of(e))&&void 0!==t?t:e}catch(i){return e}},u=(0,n.Z)((e=>new Intl.DisplayNames(e.language,{type:"language",fallback:"code"})));l()}catch(o){l(o)}}))},96980:function(e,a,t){t.a(e,(async function(e,l){try{t.d(a,{C:()=>_});var i=t(73577),n=t(72621),s=t(69440),o=(t(71695),t(61893),t(9359),t(70104),t(47021),t(57243)),u=t(50778),d=t(27486),r=t(11297),v=t(81036),h=t(46784),c=t(32770),g=t(55534),k=(t(74064),t(58130),e([s,h]));[s,h]=k.then?(await k)():k;let f,y,b,p,m=e=>e;const _=(e,a,t,l)=>{let i=[];if(a){const a=g.o.translations;i=e.map((e=>{var t;let l=null===(t=a[e])||void 0===t?void 0:t.nativeName;if(!l)try{l=new Intl.DisplayNames(e,{type:"language",fallback:"code"}).of(e)}catch(i){l=e}return{value:e,label:l}}))}else l&&(i=e.map((e=>({value:e,label:(0,h.u)(e,l)}))));return!t&&l&&i.sort(((e,a)=>(0,c.fe)(e.label,a.label,l.language))),i};(0,i.Z)([(0,u.Mo)("ha-language-picker")],(function(e,a){class t extends a{constructor(...a){super(...a),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,u.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,u.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,u.Cb)({type:Array})],key:"languages",value:void 0},{kind:"field",decorators:[(0,u.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,u.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({attribute:"native-name",type:Boolean})],key:"nativeName",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({attribute:"no-sort",type:Boolean})],key:"noSort",value(){return!1}},{kind:"field",decorators:[(0,u.Cb)({attribute:"inline-arrow",type:Boolean})],key:"inlineArrow",value(){return!1}},{kind:"field",decorators:[(0,u.SB)()],key:"_defaultLanguages",value(){return[]}},{kind:"field",decorators:[(0,u.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,n.Z)(t,"firstUpdated",this,3)([e]),this._computeDefaultLanguageOptions()}},{kind:"method",key:"updated",value:function(e){(0,n.Z)(t,"updated",this,3)([e]);const a=e.has("hass")&&this.hass&&e.get("hass")&&e.get("hass").locale.language!==this.hass.locale.language;if(e.has("languages")||e.has("value")||a){var l,i;if(this._select.layoutOptions(),this._select.value!==this.value&&(0,r.B)(this,"value-changed",{value:this._select.value}),!this.value)return;const e=this._getLanguagesOptions(null!==(l=this.languages)&&void 0!==l?l:this._defaultLanguages,this.nativeName,this.noSort,null===(i=this.hass)||void 0===i?void 0:i.locale).findIndex((e=>e.value===this.value));-1===e&&(this.value=void 0),a&&this._select.select(e)}}},{kind:"field",key:"_getLanguagesOptions",value(){return(0,d.Z)(_)}},{kind:"method",key:"_computeDefaultLanguageOptions",value:function(){this._defaultLanguages=Object.keys(g.o.translations)}},{kind:"method",key:"render",value:function(){var e,a,t,l,i,n,s;const u=this._getLanguagesOptions(null!==(e=this.languages)&&void 0!==e?e:this._defaultLanguages,this.nativeName,this.noSort,null===(a=this.hass)||void 0===a?void 0:a.locale),d=null!==(t=this.value)&&void 0!==t?t:this.required?null===(l=u[0])||void 0===l?void 0:l.value:this.value;return(0,o.dy)(f||(f=m`
      <ha-select
        .label=${0}
        .value=${0}
        .required=${0}
        .disabled=${0}
        @selected=${0}
        @closed=${0}
        fixedMenuPosition
        naturalMenuWidth
        .inlineArrow=${0}
      >
        ${0}
      </ha-select>
    `),null!==(i=this.label)&&void 0!==i?i:(null===(n=this.hass)||void 0===n?void 0:n.localize("ui.components.language-picker.language"))||"Language",d||"",this.required,this.disabled,this._changed,v.U,this.inlineArrow,0===u.length?(0,o.dy)(y||(y=m`<ha-list-item value=""
              >${0}</ha-list-item
            >`),(null===(s=this.hass)||void 0===s?void 0:s.localize("ui.components.language-picker.no_languages"))||"No languages"):u.map((e=>(0,o.dy)(b||(b=m`
                <ha-list-item .value=${0}
                  >${0}</ha-list-item
                >
              `),e.value,e.label))))}},{kind:"field",static:!0,key:"styles",value(){return(0,o.iv)(p||(p=m`
    ha-select {
      width: 100%;
    }
  `))}},{kind:"method",key:"_changed",value:function(e){const a=e.target;""!==a.value&&a.value!==this.value&&(this.value=a.value,(0,r.B)(this,"value-changed",{value:this.value}))}}]}}),o.oi);l()}catch(f){l(f)}}))},37270:function(e,a,t){t.a(e,(async function(e,l){try{t.r(a),t.d(a,{HaLanguageSelector:()=>h});var i=t(73577),n=(t(71695),t(47021),t(57243)),s=t(50778),o=t(96980),u=e([o]);o=(u.then?(await u)():u)[0];let d,r,v=e=>e,h=(0,i.Z)([(0,s.Mo)("ha-selector-language")],(function(e,a){return{F:class extends a{constructor(...a){super(...a),e(this)}},d:[{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"method",key:"render",value:function(){var e,a,t;return(0,n.dy)(d||(d=v`
      <ha-language-picker
        .hass=${0}
        .value=${0}
        .label=${0}
        .helper=${0}
        .languages=${0}
        .nativeName=${0}
        .noSort=${0}
        .disabled=${0}
        .required=${0}
      ></ha-language-picker>
    `),this.hass,this.value,this.label,this.helper,null===(e=this.selector.language)||void 0===e?void 0:e.languages,Boolean(null===(a=this.selector)||void 0===a||null===(a=a.language)||void 0===a?void 0:a.native_name),Boolean(null===(t=this.selector)||void 0===t||null===(t=t.language)||void 0===t?void 0:t.no_sort),this.disabled,this.required)}},{kind:"field",static:!0,key:"styles",value(){return(0,n.iv)(r||(r=v`
    ha-language-picker {
      width: 100%;
    }
  `))}}]}}),n.oi);l()}catch(d){l(d)}}))}}]);
//# sourceMappingURL=2999.79f266d501035d05.js.map