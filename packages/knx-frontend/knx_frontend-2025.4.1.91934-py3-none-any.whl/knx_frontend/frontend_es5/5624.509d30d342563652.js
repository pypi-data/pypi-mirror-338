"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["5624"],{90842:function(e,t,s){s.d(t,{t:()=>o});s(92745),s(9359),s(31526),s(77439),s(19423),s(88972);class a{constructor(e=window.localStorage){this.storage=void 0,this._storage={},this._listeners={},this.storage=e,e===window.localStorage&&window.addEventListener("storage",(e=>{e.key&&this.hasKey(e.key)&&(this._storage[e.key]=e.newValue?JSON.parse(e.newValue):e.newValue,this._listeners[e.key]&&this._listeners[e.key].forEach((t=>t(e.oldValue?JSON.parse(e.oldValue):e.oldValue,this._storage[e.key]))))}))}addFromStorage(e){if(!this._storage[e]){const t=this.storage.getItem(e);t&&(this._storage[e]=JSON.parse(t))}}subscribeChanges(e,t){return this._listeners[e]?this._listeners[e].push(t):this._listeners[e]=[t],()=>{this.unsubscribeChanges(e,t)}}unsubscribeChanges(e,t){if(!(e in this._listeners))return;const s=this._listeners[e].indexOf(t);-1!==s&&this._listeners[e].splice(s,1)}hasKey(e){return e in this._storage}getValue(e){return this._storage[e]}setValue(e,t){const s=this._storage[e];this._storage[e]=t;try{void 0===t?this.storage.removeItem(e):this.storage.setItem(e,JSON.stringify(t))}catch(a){}finally{this._listeners[e]&&this._listeners[e].forEach((e=>e(s,t)))}}}const i={},o=e=>t=>{const s=e.storage||"localStorage";let o;s&&s in i?o=i[s]:(o=new a(window[s]),i[s]=o);const r=String(t.key),n=e.key||String(t.key),l=t.initializer?t.initializer():void 0;o.addFromStorage(n);const d=!1!==e.subscribe?e=>o.subscribeChanges(n,((s,a)=>{e.requestUpdate(t.key,s)})):void 0,h=()=>o.hasKey(n)?e.deserializer?e.deserializer(o.getValue(n)):o.getValue(n):l;return{kind:"method",placement:"prototype",key:t.key,descriptor:{set(s){((s,a)=>{let i;e.state&&(i=h()),o.setValue(n,e.serializer?e.serializer(a):a),e.state&&s.requestUpdate(t.key,i)})(this,s)},get(){return h()},enumerable:!0,configurable:!0},finisher(s){if(e.state&&e.subscribe){const e=s.prototype.connectedCallback,t=s.prototype.disconnectedCallback;s.prototype.connectedCallback=function(){e.call(this),this[`__unbsubLocalStorage${r}`]=null==d?void 0:d(this)},s.prototype.disconnectedCallback=function(){var e;t.call(this),null===(e=this[`__unbsubLocalStorage${r}`])||void 0===e||e.call(this),this[`__unbsubLocalStorage${r}`]=void 0}}e.state&&s.createProperty(t.key,Object.assign({noAccessor:!0},e.stateOptions))}}}},88283:function(e,t,s){s.a(e,(async function(e,t){try{var a=s(73577),i=(s(71695),s(47021),s(57243)),o=s(50778),r=(s(20095),s(19537)),n=(s(10508),e([r]));r=(n.then?(await n)():n)[0];let l,d,h,c,u,g,p=e=>e;const y="M2.2,16.06L3.88,12L2.2,7.94L6.26,6.26L7.94,2.2L12,3.88L16.06,2.2L17.74,6.26L21.8,7.94L20.12,12L21.8,16.06L17.74,17.74L16.06,21.8L12,20.12L7.94,21.8L6.26,17.74L2.2,16.06M13,17V15H11V17H13M13,13V7H11V13H13Z",v="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z";(0,a.Z)([(0,o.Mo)("ha-progress-button")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"progress",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"raised",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"unelevated",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_result",value:void 0},{kind:"method",key:"render",value:function(){const e=this._result||this.progress;return(0,i.dy)(l||(l=p`
      <ha-button
        .raised=${0}
        .label=${0}
        .unelevated=${0}
        .disabled=${0}
        class=${0}
      >
        <slot name="icon" slot="icon"></slot>
        <slot></slot>
      </ha-button>
      ${0}
    `),this.raised,this.label,this.unelevated,this.disabled||this.progress,this._result||"",e?(0,i.dy)(d||(d=p`
            <div class="progress">
              ${0}
            </div>
          `),"success"===this._result?(0,i.dy)(h||(h=p`<ha-svg-icon .path=${0}></ha-svg-icon>`),v):"error"===this._result?(0,i.dy)(c||(c=p`<ha-svg-icon .path=${0}></ha-svg-icon>`),y):this.progress?(0,i.dy)(u||(u=p`<ha-spinner size="small"></ha-spinner>`)):i.Ld):i.Ld)}},{kind:"method",key:"actionSuccess",value:function(){this._setResult("success")}},{kind:"method",key:"actionError",value:function(){this._setResult("error")}},{kind:"method",key:"_setResult",value:function(e){this._result=e,setTimeout((()=>{this._result=void 0}),2e3)}},{kind:"field",static:!0,key:"styles",value(){return(0,i.iv)(g||(g=p`
    :host {
      outline: none;
      display: inline-block;
      position: relative;
      pointer-events: none;
    }

    ha-button {
      transition: all 1s;
      pointer-events: initial;
    }

    ha-button.success {
      --mdc-theme-primary: white;
      background-color: var(--success-color);
      transition: none;
      border-radius: 4px;
      pointer-events: none;
    }

    ha-button[unelevated].success,
    ha-button[raised].success {
      --mdc-theme-primary: var(--success-color);
      --mdc-theme-on-primary: white;
    }

    ha-button.error {
      --mdc-theme-primary: white;
      background-color: var(--error-color);
      transition: none;
      border-radius: 4px;
      pointer-events: none;
    }

    ha-button[unelevated].error,
    ha-button[raised].error {
      --mdc-theme-primary: var(--error-color);
      --mdc-theme-on-primary: white;
    }

    .progress {
      bottom: 4px;
      position: absolute;
      text-align: center;
      top: 4px;
      width: 100%;
    }

    ha-svg-icon {
      color: white;
    }

    ha-button.success slot,
    ha-button.error slot {
      visibility: hidden;
    }
    :host([destructive]) {
      --mdc-theme-primary: var(--error-color);
    }
  `))}}]}}),i.oi);t()}catch(l){t(l)}}))},40137:function(e,t,s){s.a(e,(async function(e,a){try{s.r(t),s.d(t,{TTSTryDialog:()=>k});var i=s(73577),o=(s(71695),s(19423),s(40251),s(47021),s(57243)),r=s(50778),n=s(90842),l=s(11297),d=s(44118),h=(s(54993),s(421)),c=s(4557),u=s(88283),g=e([u]);u=(g.then?(await g)():g)[0];let p,y,v=e=>e;const m="M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M10,16.5L16,12L10,7.5V16.5Z";let k=(0,i.Z)([(0,r.Mo)("dialog-tts-try")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_loadingExample",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_valid",value(){return!1}},{kind:"field",decorators:[(0,r.IO)("#message")],key:"_messageInput",value:void 0},{kind:"field",decorators:[(0,n.t)({key:"ttsTryMessages",state:!1,subscribe:!1})],key:"_messages",value:void 0},{kind:"method",key:"showDialog",value:function(e){this._params=e,this._valid=Boolean(this._defaultMessage)}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,(0,l.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"get",key:"_defaultMessage",value:function(){var e,t;const s=null===(e=this._params.language)||void 0===e?void 0:e.substring(0,2),a=this.hass.locale.language.substring(0,2);return s&&null!==(t=this._messages)&&void 0!==t&&t[s]?this._messages[s]:s===a?this.hass.localize("ui.dialogs.tts-try.message_example"):""}},{kind:"method",key:"render",value:function(){return this._params?(0,o.dy)(p||(p=v`
      <ha-dialog
        open
        @closed=${0}
        .heading=${0}
      >
        <ha-textarea
          autogrow
          id="message"
          .label=${0}
          .placeholder=${0}
          .value=${0}
          @input=${0}
          ?dialogInitialFocus=${0}
        >
        </ha-textarea>

        <ha-progress-button
          .progress=${0}
          ?dialogInitialFocus=${0}
          slot="primaryAction"
          .label=${0}
          @click=${0}
          .disabled=${0}
        >
          <ha-svg-icon slot="icon" .path=${0}></ha-svg-icon>
        </ha-progress-button>
      </ha-dialog>
    `),this.closeDialog,(0,d.i)(this.hass,this.hass.localize("ui.dialogs.tts-try.header")),this.hass.localize("ui.dialogs.tts-try.message"),this.hass.localize("ui.dialogs.tts-try.message_placeholder"),this._defaultMessage,this._inputChanged,!this._defaultMessage,this._loadingExample,Boolean(this._defaultMessage),this.hass.localize("ui.dialogs.tts-try.play"),this._playExample,!this._valid,m):o.Ld}},{kind:"method",key:"_inputChanged",value:async function(){var e;this._valid=Boolean(null===(e=this._messageInput)||void 0===e?void 0:e.value)}},{kind:"method",key:"_playExample",value:async function(){var e;const t=null===(e=this._messageInput)||void 0===e?void 0:e.value;if(!t)return;const s=this._params.engine,a=this._params.language,i=this._params.voice;a&&(this._messages=Object.assign(Object.assign({},this._messages),{},{[a.substring(0,2)]:t})),this._loadingExample=!0;const o=new Audio;let r;o.play();try{r=(await(0,h.aT)(this.hass,{platform:s,message:t,language:a,options:{voice:i}})).path}catch(n){return this._loadingExample=!1,void(0,c.Ys)(this,{text:`Unable to load example. ${n.error||n.body||n}`,warning:!0})}o.src=r,o.addEventListener("canplaythrough",(()=>o.play())),o.addEventListener("playing",(()=>{this._loadingExample=!1})),o.addEventListener("error",(()=>{(0,c.Ys)(this,{title:"Error playing audio."}),this._loadingExample=!1}))}},{kind:"field",static:!0,key:"styles",value(){return(0,o.iv)(y||(y=v`
    ha-dialog {
      --mdc-dialog-max-width: 500px;
    }
    ha-textarea,
    ha-select {
      width: 100%;
    }
    ha-select {
      margin-top: 8px;
    }
    .loading {
      height: 36px;
    }
  `))}}]}}),o.oi);a()}catch(p){a(p)}}))}}]);
//# sourceMappingURL=5624.509d30d342563652.js.map