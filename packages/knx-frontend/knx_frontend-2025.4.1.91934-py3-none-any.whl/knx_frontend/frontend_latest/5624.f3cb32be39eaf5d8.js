export const __webpack_ids__=["5624"];export const __webpack_modules__={90842:function(e,t,s){s.d(t,{t:()=>o});class a{constructor(e=window.localStorage){this.storage=void 0,this._storage={},this._listeners={},this.storage=e,e===window.localStorage&&window.addEventListener("storage",(e=>{e.key&&this.hasKey(e.key)&&(this._storage[e.key]=e.newValue?JSON.parse(e.newValue):e.newValue,this._listeners[e.key]&&this._listeners[e.key].forEach((t=>t(e.oldValue?JSON.parse(e.oldValue):e.oldValue,this._storage[e.key]))))}))}addFromStorage(e){if(!this._storage[e]){const t=this.storage.getItem(e);t&&(this._storage[e]=JSON.parse(t))}}subscribeChanges(e,t){return this._listeners[e]?this._listeners[e].push(t):this._listeners[e]=[t],()=>{this.unsubscribeChanges(e,t)}}unsubscribeChanges(e,t){if(!(e in this._listeners))return;const s=this._listeners[e].indexOf(t);-1!==s&&this._listeners[e].splice(s,1)}hasKey(e){return e in this._storage}getValue(e){return this._storage[e]}setValue(e,t){const s=this._storage[e];this._storage[e]=t;try{void 0===t?this.storage.removeItem(e):this.storage.setItem(e,JSON.stringify(t))}catch(a){}finally{this._listeners[e]&&this._listeners[e].forEach((e=>e(s,t)))}}}const i={},o=e=>t=>{const s=e.storage||"localStorage";let o;s&&s in i?o=i[s]:(o=new a(window[s]),i[s]=o);const r=String(t.key),n=e.key||String(t.key),l=t.initializer?t.initializer():void 0;o.addFromStorage(n);const d=!1!==e.subscribe?e=>o.subscribeChanges(n,((s,a)=>{e.requestUpdate(t.key,s)})):void 0,h=()=>o.hasKey(n)?e.deserializer?e.deserializer(o.getValue(n)):o.getValue(n):l;return{kind:"method",placement:"prototype",key:t.key,descriptor:{set(s){((s,a)=>{let i;e.state&&(i=h()),o.setValue(n,e.serializer?e.serializer(a):a),e.state&&s.requestUpdate(t.key,i)})(this,s)},get(){return h()},enumerable:!0,configurable:!0},finisher(s){if(e.state&&e.subscribe){const e=s.prototype.connectedCallback,t=s.prototype.disconnectedCallback;s.prototype.connectedCallback=function(){e.call(this),this[`__unbsubLocalStorage${r}`]=d?.(this)},s.prototype.disconnectedCallback=function(){t.call(this),this[`__unbsubLocalStorage${r}`]?.(),this[`__unbsubLocalStorage${r}`]=void 0}}e.state&&s.createProperty(t.key,{noAccessor:!0,...e.stateOptions})}}}},88283:function(e,t,s){s.a(e,(async function(e,t){try{var a=s(44249),i=s(57243),o=s(50778),r=(s(20095),s(19537)),n=(s(10508),e([r]));r=(n.then?(await n)():n)[0];const l="M2.2,16.06L3.88,12L2.2,7.94L6.26,6.26L7.94,2.2L12,3.88L16.06,2.2L17.74,6.26L21.8,7.94L20.12,12L21.8,16.06L17.74,17.74L16.06,21.8L12,20.12L7.94,21.8L6.26,17.74L2.2,16.06M13,17V15H11V17H13M13,13V7H11V13H13Z",d="M9,20.42L2.79,14.21L5.62,11.38L9,14.77L18.88,4.88L21.71,7.71L9,20.42Z";(0,a.Z)([(0,o.Mo)("ha-progress-button")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"progress",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"raised",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"unelevated",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_result",value:void 0},{kind:"method",key:"render",value:function(){const e=this._result||this.progress;return i.dy`
      <ha-button
        .raised=${this.raised}
        .label=${this.label}
        .unelevated=${this.unelevated}
        .disabled=${this.disabled||this.progress}
        class=${this._result||""}
      >
        <slot name="icon" slot="icon"></slot>
        <slot></slot>
      </ha-button>
      ${e?i.dy`
            <div class="progress">
              ${"success"===this._result?i.dy`<ha-svg-icon .path=${d}></ha-svg-icon>`:"error"===this._result?i.dy`<ha-svg-icon .path=${l}></ha-svg-icon>`:this.progress?i.dy`<ha-spinner size="small"></ha-spinner>`:i.Ld}
            </div>
          `:i.Ld}
    `}},{kind:"method",key:"actionSuccess",value:function(){this._setResult("success")}},{kind:"method",key:"actionError",value:function(){this._setResult("error")}},{kind:"method",key:"_setResult",value:function(e){this._result=e,setTimeout((()=>{this._result=void 0}),2e3)}},{kind:"field",static:!0,key:"styles",value(){return i.iv`
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
  `}}]}}),i.oi);t()}catch(l){t(l)}}))},40137:function(e,t,s){s.a(e,(async function(e,a){try{s.r(t),s.d(t,{TTSTryDialog:()=>y});var i=s(44249),o=s(57243),r=s(50778),n=s(90842),l=s(11297),d=s(44118),h=(s(54993),s(421)),c=s(4557),u=s(88283),g=e([u]);u=(g.then?(await g)():g)[0];const p="M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M10,16.5L16,12L10,7.5V16.5Z";let y=(0,i.Z)([(0,r.Mo)("dialog-tts-try")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_loadingExample",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_valid",value(){return!1}},{kind:"field",decorators:[(0,r.IO)("#message")],key:"_messageInput",value:void 0},{kind:"field",decorators:[(0,n.t)({key:"ttsTryMessages",state:!1,subscribe:!1})],key:"_messages",value:void 0},{kind:"method",key:"showDialog",value:function(e){this._params=e,this._valid=Boolean(this._defaultMessage)}},{kind:"method",key:"closeDialog",value:function(){this._params=void 0,(0,l.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"get",key:"_defaultMessage",value:function(){const e=this._params.language?.substring(0,2),t=this.hass.locale.language.substring(0,2);return e&&this._messages?.[e]?this._messages[e]:e===t?this.hass.localize("ui.dialogs.tts-try.message_example"):""}},{kind:"method",key:"render",value:function(){return this._params?o.dy`
      <ha-dialog
        open
        @closed=${this.closeDialog}
        .heading=${(0,d.i)(this.hass,this.hass.localize("ui.dialogs.tts-try.header"))}
      >
        <ha-textarea
          autogrow
          id="message"
          .label=${this.hass.localize("ui.dialogs.tts-try.message")}
          .placeholder=${this.hass.localize("ui.dialogs.tts-try.message_placeholder")}
          .value=${this._defaultMessage}
          @input=${this._inputChanged}
          ?dialogInitialFocus=${!this._defaultMessage}
        >
        </ha-textarea>

        <ha-progress-button
          .progress=${this._loadingExample}
          ?dialogInitialFocus=${Boolean(this._defaultMessage)}
          slot="primaryAction"
          .label=${this.hass.localize("ui.dialogs.tts-try.play")}
          @click=${this._playExample}
          .disabled=${!this._valid}
        >
          <ha-svg-icon slot="icon" .path=${p}></ha-svg-icon>
        </ha-progress-button>
      </ha-dialog>
    `:o.Ld}},{kind:"method",key:"_inputChanged",value:async function(){this._valid=Boolean(this._messageInput?.value)}},{kind:"method",key:"_playExample",value:async function(){const e=this._messageInput?.value;if(!e)return;const t=this._params.engine,s=this._params.language,a=this._params.voice;s&&(this._messages={...this._messages,[s.substring(0,2)]:e}),this._loadingExample=!0;const i=new Audio;let o;i.play();try{o=(await(0,h.aT)(this.hass,{platform:t,message:e,language:s,options:{voice:a}})).path}catch(r){return this._loadingExample=!1,void(0,c.Ys)(this,{text:`Unable to load example. ${r.error||r.body||r}`,warning:!0})}i.src=o,i.addEventListener("canplaythrough",(()=>i.play())),i.addEventListener("playing",(()=>{this._loadingExample=!1})),i.addEventListener("error",(()=>{(0,c.Ys)(this,{title:"Error playing audio."}),this._loadingExample=!1}))}},{kind:"field",static:!0,key:"styles",value(){return o.iv`
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
  `}}]}}),o.oi);a()}catch(p){a(p)}}))}};
//# sourceMappingURL=5624.f3cb32be39eaf5d8.js.map