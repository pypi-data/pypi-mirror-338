"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["4311"],{46784:function(e,t,i){i.a(e,(async function(e,a){try{i.d(t,{u:()=>o});var l=i(69440),s=i(27486),n=e([l]);l=(n.then?(await n)():n)[0];const o=(e,t)=>{try{var i,a;return null!==(i=null===(a=d(t))||void 0===a?void 0:a.of(e))&&void 0!==i?i:e}catch(l){return e}},d=(0,s.Z)((e=>new Intl.DisplayNames(e.language,{type:"language",fallback:"code"})));a()}catch(o){a(o)}}))},28906:function(e,t,i){var a=i(73577),l=(i(71695),i(47021),i(57243)),s=i(50778);let n,o,d=e=>e;(0,a.Z)([(0,s.Mo)("ha-dialog-header")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"method",key:"render",value:function(){return(0,l.dy)(n||(n=d`
      <header class="header">
        <div class="header-bar">
          <section class="header-navigation-icon">
            <slot name="navigationIcon"></slot>
          </section>
          <section class="header-content">
            <div class="header-title">
              <slot name="title"></slot>
            </div>
            <div class="header-subtitle">
              <slot name="subtitle"></slot>
            </div>
          </section>
          <section class="header-action-items">
            <slot name="actionItems"></slot>
          </section>
        </div>
        <slot></slot>
      </header>
    `))}},{kind:"get",static:!0,key:"styles",value:function(){return[(0,l.iv)(o||(o=d`
        :host {
          display: block;
        }
        :host([show-border]) {
          border-bottom: 1px solid
            var(--mdc-dialog-scroll-divider-color, rgba(0, 0, 0, 0.12));
        }
        .header-bar {
          display: flex;
          flex-direction: row;
          align-items: flex-start;
          padding: 4px;
          box-sizing: border-box;
        }
        .header-content {
          flex: 1;
          padding: 10px 4px;
          min-width: 0;
          overflow: hidden;
          text-overflow: ellipsis;
          white-space: nowrap;
        }
        .header-title {
          font-size: 22px;
          line-height: 28px;
          font-weight: 400;
        }
        .header-subtitle {
          font-size: 14px;
          line-height: 20px;
          color: var(--secondary-text-color);
        }
        @media all and (min-width: 450px) and (min-height: 500px) {
          .header-bar {
            padding: 12px;
          }
        }
        .header-navigation-icon {
          flex: none;
          min-width: 8px;
          height: 100%;
          display: flex;
          flex-direction: row;
        }
        .header-action-items {
          flex: none;
          min-width: 8px;
          height: 100%;
          display: flex;
          flex-direction: row;
        }
      `))]}}]}}),l.oi)},96980:function(e,t,i){i.a(e,(async function(e,a){try{i.d(t,{C:()=>_});var l=i(73577),s=i(72621),n=i(69440),o=(i(71695),i(61893),i(9359),i(70104),i(47021),i(57243)),d=i(50778),u=i(27486),r=i(11297),c=i(81036),h=i(46784),v=i(32770),g=i(55534),p=(i(74064),i(58130),e([n,h]));[n,h]=p.then?(await p)():p;let f,k,y,b,m=e=>e;const _=(e,t,i,a)=>{let l=[];if(t){const t=g.o.translations;l=e.map((e=>{var i;let a=null===(i=t[e])||void 0===i?void 0:i.nativeName;if(!a)try{a=new Intl.DisplayNames(e,{type:"language",fallback:"code"}).of(e)}catch(l){a=e}return{value:e,label:a}}))}else a&&(l=e.map((e=>({value:e,label:(0,h.u)(e,a)}))));return!i&&a&&l.sort(((e,t)=>(0,v.fe)(e.label,t.label,a.language))),l};(0,l.Z)([(0,d.Mo)("ha-language-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,d.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,d.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Array})],key:"languages",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,d.Cb)({attribute:"native-name",type:Boolean})],key:"nativeName",value(){return!1}},{kind:"field",decorators:[(0,d.Cb)({attribute:"no-sort",type:Boolean})],key:"noSort",value(){return!1}},{kind:"field",decorators:[(0,d.Cb)({attribute:"inline-arrow",type:Boolean})],key:"inlineArrow",value(){return!1}},{kind:"field",decorators:[(0,d.SB)()],key:"_defaultLanguages",value(){return[]}},{kind:"field",decorators:[(0,d.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,s.Z)(i,"firstUpdated",this,3)([e]),this._computeDefaultLanguageOptions()}},{kind:"method",key:"updated",value:function(e){(0,s.Z)(i,"updated",this,3)([e]);const t=e.has("hass")&&this.hass&&e.get("hass")&&e.get("hass").locale.language!==this.hass.locale.language;if(e.has("languages")||e.has("value")||t){var a,l;if(this._select.layoutOptions(),this._select.value!==this.value&&(0,r.B)(this,"value-changed",{value:this._select.value}),!this.value)return;const e=this._getLanguagesOptions(null!==(a=this.languages)&&void 0!==a?a:this._defaultLanguages,this.nativeName,this.noSort,null===(l=this.hass)||void 0===l?void 0:l.locale).findIndex((e=>e.value===this.value));-1===e&&(this.value=void 0),t&&this._select.select(e)}}},{kind:"field",key:"_getLanguagesOptions",value(){return(0,u.Z)(_)}},{kind:"method",key:"_computeDefaultLanguageOptions",value:function(){this._defaultLanguages=Object.keys(g.o.translations)}},{kind:"method",key:"render",value:function(){var e,t,i,a,l,s,n;const d=this._getLanguagesOptions(null!==(e=this.languages)&&void 0!==e?e:this._defaultLanguages,this.nativeName,this.noSort,null===(t=this.hass)||void 0===t?void 0:t.locale),u=null!==(i=this.value)&&void 0!==i?i:this.required?null===(a=d[0])||void 0===a?void 0:a.value:this.value;return(0,o.dy)(f||(f=m`
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
    `),null!==(l=this.label)&&void 0!==l?l:(null===(s=this.hass)||void 0===s?void 0:s.localize("ui.components.language-picker.language"))||"Language",u||"",this.required,this.disabled,this._changed,c.U,this.inlineArrow,0===d.length?(0,o.dy)(k||(k=m`<ha-list-item value=""
              >${0}</ha-list-item
            >`),(null===(n=this.hass)||void 0===n?void 0:n.localize("ui.components.language-picker.no_languages"))||"No languages"):d.map((e=>(0,o.dy)(y||(y=m`
                <ha-list-item .value=${0}
                  >${0}</ha-list-item
                >
              `),e.value,e.label))))}},{kind:"field",static:!0,key:"styles",value(){return(0,o.iv)(b||(b=m`
    ha-select {
      width: 100%;
    }
  `))}},{kind:"method",key:"_changed",value:function(e){const t=e.target;""!==t.value&&t.value!==this.value&&(this.value=t.value,(0,r.B)(this,"value-changed",{value:this.value}))}}]}}),o.oi);a()}catch(f){a(f)}}))},27556:function(e,t,i){var a=i(73577),l=i(72621),s=(i(71695),i(9359),i(1331),i(70104),i(40251),i(47021),i(57243)),n=i(50778),o=i(11297),d=i(81036),u=i(56587),r=i(421);i(74064),i(58130);let c,h,v,g,p=e=>e;const f="__NONE_OPTION__";(0,a.Z)([(0,n.Mo)("ha-tts-voice-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"engineId",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"language",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_voices",value:void 0},{kind:"field",decorators:[(0,n.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"render",value:function(){var e,t;if(!this._voices)return s.Ld;const i=null!==(e=this.value)&&void 0!==e?e:this.required?null===(t=this._voices[0])||void 0===t?void 0:t.voice_id:f;return(0,s.dy)(c||(c=p`
      <ha-select
        .label=${0}
        .value=${0}
        .required=${0}
        .disabled=${0}
        @selected=${0}
        @closed=${0}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${0}
        ${0}
      </ha-select>
    `),this.label||this.hass.localize("ui.components.tts-voice-picker.voice"),i,this.required,this.disabled,this._changed,d.U,this.required?s.Ld:(0,s.dy)(h||(h=p`<ha-list-item .value=${0}>
              ${0}
            </ha-list-item>`),f,this.hass.localize("ui.components.tts-voice-picker.none")),this._voices.map((e=>(0,s.dy)(v||(v=p`<ha-list-item .value=${0}>
              ${0}
            </ha-list-item>`),e.voice_id,e.name))))}},{kind:"method",key:"willUpdate",value:function(e){(0,l.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated?(e.has("language")||e.has("engineId"))&&this._debouncedUpdateVoices():this._updateVoices()}},{kind:"field",key:"_debouncedUpdateVoices",value(){return(0,u.D)((()=>this._updateVoices()),500)}},{kind:"method",key:"_updateVoices",value:async function(){this.engineId&&this.language?(this._voices=(await(0,r.MV)(this.hass,this.engineId,this.language)).voices,this.value&&(this._voices&&this._voices.find((e=>e.voice_id===this.value))||(this.value=void 0,(0,o.B)(this,"value-changed",{value:this.value})))):this._voices=void 0}},{kind:"method",key:"updated",value:function(e){var t,a,s;((0,l.Z)(i,"updated",this,3)([e]),e.has("_voices")&&(null===(t=this._select)||void 0===t?void 0:t.value)!==this.value)&&(null===(a=this._select)||void 0===a||a.layoutOptions(),(0,o.B)(this,"value-changed",{value:null===(s=this._select)||void 0===s?void 0:s.value}))}},{kind:"field",static:!0,key:"styles",value(){return(0,s.iv)(g||(g=p`
    ha-select {
      width: 100%;
    }
  `))}},{kind:"method",key:"_changed",value:function(e){const t=e.target;!this.hass||""===t.value||t.value===this.value||void 0===this.value&&t.value===f||(this.value=t.value===f?void 0:t.value,(0,o.B)(this,"value-changed",{value:this.value}))}}]}}),s.oi)},3079:function(e,t,i){i.d(t,{LI:()=>d,_Y:()=>s,_t:()=>o,bi:()=>n});var a=i(66374);i(19423);const l=["hass"],s=e=>{let{hass:t}=e,i=(0,a.Z)(e,l);return t.callApi("POST","cloud/login",i)},n=(e,t,i)=>e.callApi("POST","cloud/register",{email:t,password:i}),o=(e,t)=>e.callApi("POST","cloud/resend_confirm",{email:t}),d=e=>e.callWS({type:"cloud/status"})},421:function(e,t,i){i.d(t,{MV:()=>u,Wg:()=>o,Xk:()=>n,aT:()=>a,b_:()=>s,yP:()=>d});i(88044);const a=(e,t)=>e.callApi("POST","tts_get_url",t),l="media-source://tts/",s=e=>e.startsWith(l),n=e=>e.substring(19),o=(e,t,i)=>e.callWS({type:"tts/engine/list",language:t,country:i}),d=(e,t)=>e.callWS({type:"tts/engine/get",engine_id:t}),u=(e,t,i)=>e.callWS({type:"tts/engine/voices",engine_id:t,language:i})},85019:function(e,t,i){i.d(t,{X1:()=>a,u4:()=>l,zC:()=>s});i(88044);const a=e=>`https://brands.home-assistant.io/${e.brand?"brands/":""}${e.useFallback?"_/":""}${e.domain}/${e.darkOptimized?"dark_":""}${e.type}.png`,l=e=>e.split("/")[4],s=e=>e.startsWith("https://brands.home-assistant.io/")}}]);
//# sourceMappingURL=4311.6d84a5e4bbdfd0fd.js.map