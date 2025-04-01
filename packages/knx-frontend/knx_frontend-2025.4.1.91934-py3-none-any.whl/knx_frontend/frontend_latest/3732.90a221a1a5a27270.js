export const __webpack_ids__=["3732"];export const __webpack_modules__={47899:function(e,t,i){i.d(t,{Bt:()=>o});var s=i(88977),a=i(59176);const n=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"],o=e=>e.first_weekday===a.FS.language?"weekInfo"in Intl.Locale.prototype?new Intl.Locale(e.language).weekInfo.firstDay%7:(0,s.L)(e.language)%7:n.includes(e.first_weekday)?n.indexOf(e.first_weekday):1},52258:function(e,t,i){i.a(e,(async function(e,s){try{i.d(t,{G:()=>d});var a=i(69440),n=i(27486),o=i(66045),l=e([a,o]);[a,o]=l.then?(await l)():l;const r=(0,n.Z)((e=>new Intl.RelativeTimeFormat(e.language,{numeric:"auto"}))),d=(e,t,i,s=!0)=>{const a=(0,o.W)(e,i,t);return s?r(t).format(a.value,a.unit):Intl.NumberFormat(t.language,{style:"unit",unit:a.unit,unitDisplay:"long"}).format(Math.abs(a.value))};s()}catch(r){s(r)}}))},29332:function(e,t,i){i.d(t,{X:()=>s});const s=(e,t,i)=>(void 0!==i&&(i=!!i),e.hasAttribute(t)?!!i||(e.removeAttribute(t),!1):!1!==i&&(e.setAttribute(t,""),!0))},46784:function(e,t,i){i.a(e,(async function(e,s){try{i.d(t,{u:()=>l});var a=i(69440),n=i(27486),o=e([a]);a=(o.then?(await o)():o)[0];const l=(e,t)=>{try{return r(t)?.of(e)??e}catch{return e}},r=(0,n.Z)((e=>new Intl.DisplayNames(e.language,{type:"language",fallback:"code"})));s()}catch(l){s(l)}}))},81928:function(e,t,i){i.d(t,{f:()=>s});const s=e=>e.charAt(0).toUpperCase()+e.slice(1)},68061:function(e,t,i){i.d(t,{v:()=>s});const s=(e,t)=>{if(e===t)return!0;if(e&&t&&"object"==typeof e&&"object"==typeof t){if(e.constructor!==t.constructor)return!1;let i,a;if(Array.isArray(e)){if(a=e.length,a!==t.length)return!1;for(i=a;0!=i--;)if(!s(e[i],t[i]))return!1;return!0}if(e instanceof Map&&t instanceof Map){if(e.size!==t.size)return!1;for(i of e.entries())if(!t.has(i[0]))return!1;for(i of e.entries())if(!s(i[1],t.get(i[0])))return!1;return!0}if(e instanceof Set&&t instanceof Set){if(e.size!==t.size)return!1;for(i of e.entries())if(!t.has(i[0]))return!1;return!0}if(ArrayBuffer.isView(e)&&ArrayBuffer.isView(t)){if(a=e.length,a!==t.length)return!1;for(i=a;0!=i--;)if(e[i]!==t[i])return!1;return!0}if(e.constructor===RegExp)return e.source===t.source&&e.flags===t.flags;if(e.valueOf!==Object.prototype.valueOf)return e.valueOf()===t.valueOf();if(e.toString!==Object.prototype.toString)return e.toString()===t.toString();const n=Object.keys(e);if(a=n.length,a!==Object.keys(t).length)return!1;for(i=a;0!=i--;)if(!Object.prototype.hasOwnProperty.call(t,n[i]))return!1;for(i=a;0!=i--;){const a=n[i];if(!s(e[a],t[a]))return!1}return!0}return e!=e&&t!=t}},66045:function(e,t,i){i.a(e,(async function(e,s){try{i.d(t,{W:()=>u});var a=i(13809),n=i(29558),o=i(57829),l=i(47899);const d=1e3,c=60,h=60*c;function u(e,t=Date.now(),i,s={}){const r={...p,...s||{}},u=(+e-+t)/d;if(Math.abs(u)<r.second)return{value:Math.round(u),unit:"second"};const g=u/c;if(Math.abs(g)<r.minute)return{value:Math.round(g),unit:"minute"};const v=u/h;if(Math.abs(v)<r.hour)return{value:Math.round(v),unit:"hour"};const f=new Date(e),_=new Date(t);f.setHours(0,0,0,0),_.setHours(0,0,0,0);const y=(0,a.j)(f,_);if(0===y)return{value:Math.round(v),unit:"hour"};if(Math.abs(y)<r.day)return{value:y,unit:"day"};const k=(0,l.Bt)(i),m=(0,n.z)(f,{weekStartsOn:k}),b=(0,n.z)(_,{weekStartsOn:k}),w=(0,o.p)(m,b);if(0===w)return{value:y,unit:"day"};if(Math.abs(w)<r.week)return{value:w,unit:"week"};const $=f.getFullYear()-_.getFullYear(),C=12*$+f.getMonth()-_.getMonth();return 0===C?{value:w,unit:"week"}:Math.abs(C)<r.month||0===$?{value:C,unit:"month"}:{value:Math.round($),unit:"year"}}const p={second:45,minute:45,hour:22,day:5,week:4,month:11};s()}catch(r){s(r)}}))},1025:function(e,t,i){var s=i(44249),a=i(72621),n=i(10445),o=i(57243),l=i(50778);(0,s.Z)([(0,l.Mo)("ha-assist-chip")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,l.Cb)({type:Boolean,reflect:!0})],key:"filled",value(){return!1}},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"active",value(){return!1}},{kind:"field",static:!0,key:"styles",value(){return[...(0,a.Z)(i,"styles",this),o.iv`
      :host {
        --md-sys-color-primary: var(--primary-text-color);
        --md-sys-color-on-surface: var(--primary-text-color);
        --md-assist-chip-container-shape: var(
          --ha-assist-chip-container-shape,
          16px
        );
        --md-assist-chip-outline-color: var(--outline-color);
        --md-assist-chip-label-text-weight: 400;
      }
      /** Material 3 doesn't have a filled chip, so we have to make our own **/
      .filled {
        display: flex;
        pointer-events: none;
        border-radius: inherit;
        inset: 0;
        position: absolute;
        background-color: var(--ha-assist-chip-filled-container-color);
      }
      /** Set the size of mdc icons **/
      ::slotted([slot="icon"]),
      ::slotted([slot="trailing-icon"]) {
        display: flex;
        --mdc-icon-size: var(--md-input-chip-icon-size, 18px);
        font-size: var(--_label-text-size) !important;
      }

      .trailing.icon ::slotted(*),
      .trailing.icon svg {
        margin-inline-end: unset;
        margin-inline-start: var(--_icon-label-space);
      }
      ::before {
        background: var(--ha-assist-chip-container-color, transparent);
        opacity: var(--ha-assist-chip-container-opacity, 1);
      }
      :where(.active)::before {
        background: var(--ha-assist-chip-active-container-color);
        opacity: var(--ha-assist-chip-active-container-opacity);
      }
      .label {
        font-family: Roboto, sans-serif;
      }
    `]}},{kind:"method",key:"renderOutline",value:function(){return this.filled?o.dy`<span class="filled"></span>`:(0,a.Z)(i,"renderOutline",this,3)([])}},{kind:"method",key:"getContainerClasses",value:function(){return{...(0,a.Z)(i,"getContainerClasses",this,3)([]),active:this.active}}},{kind:"method",key:"renderPrimaryContent",value:function(){return o.dy`
      <span class="leading icon" aria-hidden="true">
        ${this.renderLeadingIcon()}
      </span>
      <span class="label">${this.label}</span>
      <span class="touch"></span>
      <span class="trailing leading icon" aria-hidden="true">
        ${this.renderTrailingIcon()}
      </span>
    `}},{kind:"method",key:"renderTrailingIcon",value:function(){return o.dy`<slot name="trailing-icon"></slot>`}}]}}),n.X)},28906:function(e,t,i){var s=i(44249),a=i(57243),n=i(50778);(0,s.Z)([(0,n.Mo)("ha-dialog-header")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"method",key:"render",value:function(){return a.dy`
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
    `}},{kind:"get",static:!0,key:"styles",value:function(){return[a.iv`
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
      `]}}]}}),a.oi)},96980:function(e,t,i){i.a(e,(async function(e,s){try{i.d(t,{C:()=>f});var a=i(44249),n=i(72621),o=i(69440),l=i(57243),r=i(50778),d=i(27486),c=i(11297),h=i(81036),u=i(46784),p=i(32770),g=i(55534),v=(i(74064),i(58130),e([o,u]));[o,u]=v.then?(await v)():v;const f=(e,t,i,s)=>{let a=[];if(t){const t=g.o.translations;a=e.map((e=>{let i=t[e]?.nativeName;if(!i)try{i=new Intl.DisplayNames(e,{type:"language",fallback:"code"}).of(e)}catch(s){i=e}return{value:e,label:i}}))}else s&&(a=e.map((e=>({value:e,label:(0,u.u)(e,s)}))));return!i&&s&&a.sort(((e,t)=>(0,p.fe)(e.label,t.label,s.language))),a};(0,a.Z)([(0,r.Mo)("ha-language-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Array})],key:"languages",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({attribute:"native-name",type:Boolean})],key:"nativeName",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({attribute:"no-sort",type:Boolean})],key:"noSort",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({attribute:"inline-arrow",type:Boolean})],key:"inlineArrow",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_defaultLanguages",value(){return[]}},{kind:"field",decorators:[(0,r.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,n.Z)(i,"firstUpdated",this,3)([e]),this._computeDefaultLanguageOptions()}},{kind:"method",key:"updated",value:function(e){(0,n.Z)(i,"updated",this,3)([e]);const t=e.has("hass")&&this.hass&&e.get("hass")&&e.get("hass").locale.language!==this.hass.locale.language;if(e.has("languages")||e.has("value")||t){if(this._select.layoutOptions(),this._select.value!==this.value&&(0,c.B)(this,"value-changed",{value:this._select.value}),!this.value)return;const e=this._getLanguagesOptions(this.languages??this._defaultLanguages,this.nativeName,this.noSort,this.hass?.locale).findIndex((e=>e.value===this.value));-1===e&&(this.value=void 0),t&&this._select.select(e)}}},{kind:"field",key:"_getLanguagesOptions",value(){return(0,d.Z)(f)}},{kind:"method",key:"_computeDefaultLanguageOptions",value:function(){this._defaultLanguages=Object.keys(g.o.translations)}},{kind:"method",key:"render",value:function(){const e=this._getLanguagesOptions(this.languages??this._defaultLanguages,this.nativeName,this.noSort,this.hass?.locale),t=this.value??(this.required?e[0]?.value:this.value);return l.dy`
      <ha-select
        .label=${this.label??(this.hass?.localize("ui.components.language-picker.language")||"Language")}
        .value=${t||""}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${h.U}
        fixedMenuPosition
        naturalMenuWidth
        .inlineArrow=${this.inlineArrow}
      >
        ${0===e.length?l.dy`<ha-list-item value=""
              >${this.hass?.localize("ui.components.language-picker.no_languages")||"No languages"}</ha-list-item
            >`:e.map((e=>l.dy`
                <ha-list-item .value=${e.value}
                  >${e.label}</ha-list-item
                >
              `))}
      </ha-select>
    `}},{kind:"field",static:!0,key:"styles",value(){return l.iv`
    ha-select {
      width: 100%;
    }
  `}},{kind:"method",key:"_changed",value:function(e){const t=e.target;""!==t.value&&t.value!==this.value&&(this.value=t.value,(0,c.B)(this,"value-changed",{value:this.value}))}}]}}),l.oi);s()}catch(f){s(f)}}))},43745:function(e,t,i){var s=i(44249),a=i(57243),n=i(50778),o=i(24067),l=i(11297),r=i(72621),d=i(13239),c=i(7162);(0,s.Z)([(0,n.Mo)("ha-menu")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"method",key:"connectedCallback",value:function(){(0,r.Z)(i,"connectedCallback",this,3)([]),this.addEventListener("close-menu",this._handleCloseMenu)}},{kind:"method",key:"_handleCloseMenu",value:function(e){e.detail.reason.kind===c.GB.KEYDOWN&&e.detail.reason.key===c.KC.ESCAPE||e.detail.initiator.clickAction?.(e.detail.initiator)}},{kind:"field",static:!0,key:"styles",value(){return[...(0,r.Z)(i,"styles",this),a.iv`
      :host {
        --md-sys-color-surface-container: var(--card-background-color);
      }
    `]}}]}}),d.xX),(0,s.Z)([(0,n.Mo)("ha-md-button-menu")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",key:o.gA,value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)()],key:"positioning",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"has-overflow"})],key:"hasOverflow",value(){return!1}},{kind:"field",decorators:[(0,n.IO)("ha-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){return this._menu.items}},{kind:"method",key:"focus",value:function(){this._menu.open?this._menu.focus():this._triggerButton?.focus()}},{kind:"method",key:"render",value:function(){return a.dy`
      <div @click=${this._handleClick}>
        <slot name="trigger" @slotchange=${this._setTriggerAria}></slot>
      </div>
      <ha-menu
        .positioning=${this.positioning}
        .hasOverflow=${this.hasOverflow}
        @opening=${this._handleOpening}
        @closing=${this._handleClosing}
      >
        <slot></slot>
      </ha-menu>
    `}},{kind:"method",key:"_handleOpening",value:function(){(0,l.B)(this,"opening",void 0,{composed:!1})}},{kind:"method",key:"_handleClosing",value:function(){(0,l.B)(this,"closing",void 0,{composed:!1})}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchorElement=this,this._menu.open?this._menu.close():this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"], ha-assist-chip[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"field",static:!0,key:"styles",value(){return a.iv`
    :host {
      display: inline-block;
      position: relative;
    }
    ::slotted([disabled]) {
      color: var(--disabled-text-color);
    }
  `}}]}}),a.oi)},69387:function(e,t,i){var s=i(44249),a=i(72621),n=i(78755),o=i(57243),l=i(50778);(0,s.Z)([(0,l.Mo)("ha-md-list-item")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",static:!0,key:"styles",value(){return[...(0,a.Z)(i,"styles",this),o.iv`
      :host {
        --ha-icon-display: block;
        --md-sys-color-primary: var(--primary-text-color);
        --md-sys-color-secondary: var(--secondary-text-color);
        --md-sys-color-surface: var(--card-background-color);
        --md-sys-color-on-surface: var(--primary-text-color);
        --md-sys-color-on-surface-variant: var(--secondary-text-color);
      }
      md-item {
        overflow: var(--md-item-overflow, hidden);
        align-items: var(--md-item-align-items, center);
      }
    `]}}]}}),n.g)},48333:function(e,t,i){var s=i(44249),a=i(72621),n=i(623),o=i(57243),l=i(50778);(0,s.Z)([(0,l.Mo)("ha-md-list")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",static:!0,key:"styles",value(){return[...(0,a.Z)(i,"styles",this),o.iv`
      :host {
        --md-sys-color-surface: var(--card-background-color);
      }
    `]}}]}}),n.j)},42781:function(e,t,i){var s=i(44249),a=i(57243),n=i(50778);i(59897),i(70596);(0,s.Z)([(0,n.Mo)("ha-password-field")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"invalid",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:"error-message"})],key:"errorMessage",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"icon",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"iconTrailing",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)()],key:"autocomplete",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"autocorrect",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:"input-spellcheck"})],key:"inputSpellcheck",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"value",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"placeholder",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"label",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Number})],key:"minLength",value(){return-1}},{kind:"field",decorators:[(0,n.Cb)({type:Number})],key:"maxLength",value(){return-1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"outlined",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"helper",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"validateOnInitialRender",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"validationMessage",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"autoValidate",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"pattern",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:Number})],key:"size",value(){return null}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"helperPersistent",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"charCounter",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"endAligned",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"prefix",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"suffix",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:String})],key:"name",value(){return""}},{kind:"field",decorators:[(0,n.Cb)({type:String,attribute:"input-mode"})],key:"inputMode",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"readOnly",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({attribute:!1,type:String})],key:"autocapitalize",value(){return""}},{kind:"field",decorators:[(0,n.SB)()],key:"_unmaskedPassword",value(){return!1}},{kind:"field",decorators:[(0,n.IO)("ha-textfield")],key:"_textField",value:void 0},{kind:"method",key:"render",value:function(){return a.dy`<ha-textfield
        .invalid=${this.invalid}
        .errorMessage=${this.errorMessage}
        .icon=${this.icon}
        .iconTrailing=${this.iconTrailing}
        .autocomplete=${this.autocomplete}
        .autocorrect=${this.autocorrect}
        .inputSpellcheck=${this.inputSpellcheck}
        .value=${this.value}
        .placeholder=${this.placeholder}
        .label=${this.label}
        .disabled=${this.disabled}
        .required=${this.required}
        .minLength=${this.minLength}
        .maxLength=${this.maxLength}
        .outlined=${this.outlined}
        .helper=${this.helper}
        .validateOnInitialRender=${this.validateOnInitialRender}
        .validationMessage=${this.validationMessage}
        .autoValidate=${this.autoValidate}
        .pattern=${this.pattern}
        .size=${this.size}
        .helperPersistent=${this.helperPersistent}
        .charCounter=${this.charCounter}
        .endAligned=${this.endAligned}
        .prefix=${this.prefix}
        .name=${this.name}
        .inputMode=${this.inputMode}
        .readOnly=${this.readOnly}
        .autocapitalize=${this.autocapitalize}
        .type=${this._unmaskedPassword?"text":"password"}
        .suffix=${a.dy`<div style="width: 24px"></div>`}
        @input=${this._handleInputEvent}
        @change=${this._handleChangeEvent}
      ></ha-textfield>
      <ha-icon-button
        .label=${this.hass?.localize(this._unmaskedPassword?"ui.components.selectors.text.hide_password":"ui.components.selectors.text.show_password")||(this._unmaskedPassword?"Hide password":"Show password")}
        @click=${this._toggleUnmaskedPassword}
        .path=${this._unmaskedPassword?"M11.83,9L15,12.16C15,12.11 15,12.05 15,12A3,3 0 0,0 12,9C11.94,9 11.89,9 11.83,9M7.53,9.8L9.08,11.35C9.03,11.56 9,11.77 9,12A3,3 0 0,0 12,15C12.22,15 12.44,14.97 12.65,14.92L14.2,16.47C13.53,16.8 12.79,17 12,17A5,5 0 0,1 7,12C7,11.21 7.2,10.47 7.53,9.8M2,4.27L4.28,6.55L4.73,7C3.08,8.3 1.78,10 1,12C2.73,16.39 7,19.5 12,19.5C13.55,19.5 15.03,19.2 16.38,18.66L16.81,19.08L19.73,22L21,20.73L3.27,3M12,7A5,5 0 0,1 17,12C17,12.64 16.87,13.26 16.64,13.82L19.57,16.75C21.07,15.5 22.27,13.86 23,12C21.27,7.61 17,4.5 12,4.5C10.6,4.5 9.26,4.75 8,5.2L10.17,7.35C10.74,7.13 11.35,7 12,7Z":"M12,9A3,3 0 0,0 9,12A3,3 0 0,0 12,15A3,3 0 0,0 15,12A3,3 0 0,0 12,9M12,17A5,5 0 0,1 7,12A5,5 0 0,1 12,7A5,5 0 0,1 17,12A5,5 0 0,1 12,17M12,4.5C7,4.5 2.73,7.61 1,12C2.73,16.39 7,19.5 12,19.5C17,19.5 21.27,16.39 23,12C21.27,7.61 17,4.5 12,4.5Z"}
      ></ha-icon-button>`}},{kind:"method",key:"focus",value:function(){this._textField.focus()}},{kind:"method",key:"checkValidity",value:function(){return this._textField.checkValidity()}},{kind:"method",key:"reportValidity",value:function(){return this._textField.reportValidity()}},{kind:"method",key:"setCustomValidity",value:function(e){return this._textField.setCustomValidity(e)}},{kind:"method",key:"layout",value:function(){return this._textField.layout()}},{kind:"method",key:"_toggleUnmaskedPassword",value:function(){this._unmaskedPassword=!this._unmaskedPassword}},{kind:"method",decorators:[(0,n.hO)({passive:!0})],key:"_handleInputEvent",value:function(e){this.value=e.target.value}},{kind:"method",decorators:[(0,n.hO)({passive:!0})],key:"_handleChangeEvent",value:function(e){this.value=e.target.value,this._reDispatchEvent(e)}},{kind:"method",key:"_reDispatchEvent",value:function(e){const t=new Event(e.type,e);this.dispatchEvent(t)}},{kind:"field",static:!0,key:"styles",value(){return a.iv`
    :host {
      display: block;
      position: relative;
    }
    ha-textfield {
      width: 100%;
    }
    ha-icon-button {
      position: absolute;
      top: 8px;
      right: 8px;
      inset-inline-start: initial;
      inset-inline-end: 8px;
      --mdc-icon-button-size: 40px;
      --mdc-icon-size: 20px;
      color: var(--secondary-text-color);
      direction: var(--direction);
    }
  `}}]}}),a.oi)},93644:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(26749),o=i(77118),l=i(57243),r=i(50778),d=e([n]);n=(d.then?(await d)():d)[0];(0,s.Z)([(0,r.Mo)("ha-progress-ring")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)()],key:"size",value:void 0},{kind:"method",key:"updated",value:function(e){if((0,a.Z)(i,"updated",this,3)([e]),e.has("size"))switch(this.size){case"tiny":this.style.setProperty("--ha-progress-ring-size","16px");break;case"small":this.style.setProperty("--ha-progress-ring-size","28px");break;case"medium":this.style.setProperty("--ha-progress-ring-size","48px");break;case"large":this.style.setProperty("--ha-progress-ring-size","68px");break;case void 0:this.style.removeProperty("--ha-progress-ring-size")}}},{kind:"field",static:!0,key:"styles",value(){return[o.Z,l.iv`
      :host {
        --indicator-color: var(
          --ha-progress-ring-indicator-color,
          var(--primary-color)
        );
        --track-color: var(
          --ha-progress-ring-divider-color,
          var(--divider-color)
        );
        --track-width: 4px;
        --speed: 3.5s;
        --size: var(--ha-progress-ring-size, 48px);
      }
    `]}}]}}),n.Z);t()}catch(c){t(c)}}))},44315:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(74760),o=i(57243),l=i(50778),r=i(52258),d=i(81928),c=e([r]);r=(c.then?(await c)():c)[0];(0,s.Z)([(0,l.Mo)("ha-relative-time")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"datetime",value:void 0},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"capitalize",value(){return!1}},{kind:"field",key:"_interval",value:void 0},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.Z)(i,"disconnectedCallback",this,3)([]),this._clearInterval()}},{kind:"method",key:"connectedCallback",value:function(){(0,a.Z)(i,"connectedCallback",this,3)([]),this.datetime&&this._startInterval()}},{kind:"method",key:"createRenderRoot",value:function(){return this}},{kind:"method",key:"firstUpdated",value:function(e){(0,a.Z)(i,"firstUpdated",this,3)([e]),this._updateRelative()}},{kind:"method",key:"update",value:function(e){(0,a.Z)(i,"update",this,3)([e]),this._updateRelative()}},{kind:"method",key:"_clearInterval",value:function(){this._interval&&(window.clearInterval(this._interval),this._interval=void 0)}},{kind:"method",key:"_startInterval",value:function(){this._clearInterval(),this._interval=window.setInterval((()=>this._updateRelative()),6e4)}},{kind:"method",key:"_updateRelative",value:function(){if(this.datetime){const e="string"==typeof this.datetime?(0,n.D)(this.datetime):this.datetime,t=(0,r.G)(e,this.hass.locale);this.innerHTML=this.capitalize?(0,d.f)(t):t}else this.innerHTML=this.hass.localize("ui.components.relative_time.never")}}]}}),o.fl);t()}catch(h){t(h)}}))},27556:function(e,t,i){var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(11297),r=i(81036),d=i(56587),c=i(421);i(74064),i(58130);const h="__NONE_OPTION__";(0,s.Z)([(0,o.Mo)("ha-tts-voice-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"engineId",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"language",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_voices",value:void 0},{kind:"field",decorators:[(0,o.IO)("ha-select")],key:"_select",value:void 0},{kind:"method",key:"render",value:function(){if(!this._voices)return n.Ld;const e=this.value??(this.required?this._voices[0]?.voice_id:h);return n.dy`
      <ha-select
        .label=${this.label||this.hass.localize("ui.components.tts-voice-picker.voice")}
        .value=${e}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${r.U}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${this.required?n.Ld:n.dy`<ha-list-item .value=${h}>
              ${this.hass.localize("ui.components.tts-voice-picker.none")}
            </ha-list-item>`}
        ${this._voices.map((e=>n.dy`<ha-list-item .value=${e.voice_id}>
              ${e.name}
            </ha-list-item>`))}
      </ha-select>
    `}},{kind:"method",key:"willUpdate",value:function(e){(0,a.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated?(e.has("language")||e.has("engineId"))&&this._debouncedUpdateVoices():this._updateVoices()}},{kind:"field",key:"_debouncedUpdateVoices",value(){return(0,d.D)((()=>this._updateVoices()),500)}},{kind:"method",key:"_updateVoices",value:async function(){this.engineId&&this.language?(this._voices=(await(0,c.MV)(this.hass,this.engineId,this.language)).voices,this.value&&(this._voices&&this._voices.find((e=>e.voice_id===this.value))||(this.value=void 0,(0,l.B)(this,"value-changed",{value:this.value})))):this._voices=void 0}},{kind:"method",key:"updated",value:function(e){(0,a.Z)(i,"updated",this,3)([e]),e.has("_voices")&&this._select?.value!==this.value&&(this._select?.layoutOptions(),(0,l.B)(this,"value-changed",{value:this._select?.value}))}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    ha-select {
      width: 100%;
    }
  `}},{kind:"method",key:"_changed",value:function(e){const t=e.target;!this.hass||""===t.value||t.value===this.value||void 0===this.value&&t.value===h||(this.value=t.value===h?void 0:t.value,(0,l.B)(this,"value-changed",{value:this.value}))}}]}}),n.oi)},4855:function(e,t,i){i.d(t,{Dy:()=>d,PA:()=>o,SC:()=>n,Xp:()=>a,af:()=>r,eP:()=>s,jZ:()=>l});const s=(e,t,i)=>"run-start"===t.type?e={init_options:i,stage:"ready",run:t.data,events:[t]}:e?((e="wake_word-start"===t.type?{...e,stage:"wake_word",wake_word:{...t.data,done:!1}}:"wake_word-end"===t.type?{...e,wake_word:{...e.wake_word,...t.data,done:!0}}:"stt-start"===t.type?{...e,stage:"stt",stt:{...t.data,done:!1}}:"stt-end"===t.type?{...e,stt:{...e.stt,...t.data,done:!0}}:"intent-start"===t.type?{...e,stage:"intent",intent:{...t.data,done:!1}}:"intent-end"===t.type?{...e,intent:{...e.intent,...t.data,done:!0}}:"tts-start"===t.type?{...e,stage:"tts",tts:{...t.data,done:!1}}:"tts-end"===t.type?{...e,tts:{...e.tts,...t.data,done:!0}}:"run-end"===t.type?{...e,stage:"done"}:"error"===t.type?{...e,stage:"error",error:t.data}:{...e}).events=[...e.events,t],e):void console.warn("Received unexpected event before receiving session",t),a=(e,t,i)=>e.connection.subscribeMessage(t,{...i,type:"assist_pipeline/run"}),n=e=>e.callWS({type:"assist_pipeline/pipeline/list"}),o=(e,t)=>e.callWS({type:"assist_pipeline/pipeline/get",pipeline_id:t}),l=(e,t)=>e.callWS({type:"assist_pipeline/pipeline/create",...t}),r=(e,t,i)=>e.callWS({type:"assist_pipeline/pipeline/update",pipeline_id:t,...i}),d=e=>e.callWS({type:"assist_pipeline/language/list"})},3079:function(e,t,i){i.d(t,{LI:()=>o,_Y:()=>s,_t:()=>n,bi:()=>a});const s=({hass:e,...t})=>e.callApi("POST","cloud/login",t),a=(e,t,i)=>e.callApi("POST","cloud/register",{email:t,password:i}),n=(e,t)=>e.callApi("POST","cloud/resend_confirm",{email:t}),o=e=>e.callWS({type:"cloud/status"})},31762:function(e,t,i){i.d(t,{KH:()=>n,rM:()=>a,zt:()=>s});let s=function(e){return e[e.CONTROL=1]="CONTROL",e}({});const a=(e,t,i)=>e.callWS({type:"conversation/agent/list",language:t,country:i}),n=(e,t,i)=>e.callWS({type:"conversation/agent/homeassistant/language_scores",language:t,country:i})},60498:function(e,t,i){i.d(t,{Iq:()=>l,L3:()=>o,Mw:()=>d,vA:()=>n,w1:()=>r});var s=i(27486),a=i(73525);i(32770);const n=(e,t)=>{if(t.name)return t.name;const i=e.states[t.entity_id];return i?(0,a.C)(i):t.original_name?t.original_name:t.entity_id},o=(e,t)=>e.callWS({type:"config/entity_registry/get",entity_id:t}),l=(e,t)=>e.callWS({type:"config/entity_registry/get_entries",entity_ids:t}),r=(0,s.Z)((e=>{const t={};for(const i of e)t[i.entity_id]=i;return t})),d=(0,s.Z)((e=>{const t={};for(const i of e)t[i.id]=i;return t}))},46999:function(e,t,i){i.d(t,{yt:()=>n,fU:()=>l,kP:()=>o});var s=i(99642),a=i(81054);const n=async e=>(0,s.I)(e.config.version,2021,2,4)?e.callWS({type:"supervisor/api",endpoint:"/addons",method:"get"}):(0,a.rY)(await e.callApi("GET","hassio/addons")),o=async(e,t)=>(0,s.I)(e.config.version,2021,2,4)?e.callWS({type:"supervisor/api",endpoint:`/addons/${t}/start`,method:"post",timeout:null}):e.callApi("POST",`hassio/addons/${t}/start`),l=async(e,t)=>{(0,s.I)(e.config.version,2021,2,4)?await e.callWS({type:"supervisor/api",endpoint:`/addons/${t}/install`,method:"post",timeout:null}):await e.callApi("POST",`hassio/addons/${t}/install`)}},81054:function(e,t,i){i.d(t,{js:()=>a,rY:()=>s});const s=e=>e.data,a=e=>"object"==typeof e?"object"==typeof e.body?e.body.message||"Unknown error, see supervisor logs":e.body||e.message||"Unknown error, see supervisor logs":e;new Set([502,503,504])},44074:function(e,t,i){i.d(t,{n:()=>s});const s=(e,t,i)=>e.callService("select","select_option",{option:i},{entity_id:t})},52829:function(e,t,i){i.d(t,{m:()=>s});const s=(e,t,i)=>e.callWS({type:"stt/engine/list",language:t,country:i})},421:function(e,t,i){i.d(t,{MV:()=>d,Wg:()=>l,Xk:()=>o,aT:()=>s,b_:()=>n,yP:()=>r});const s=(e,t)=>e.callApi("POST","tts_get_url",t),a="media-source://tts/",n=e=>e.startsWith(a),o=e=>e.substring(19),l=(e,t,i)=>e.callWS({type:"tts/engine/list",language:t,country:i}),r=(e,t)=>e.callWS({type:"tts/engine/get",engine_id:t}),d=(e,t,i)=>e.callWS({type:"tts/engine/voices",engine_id:t,language:i})},28726:function(e,t,i){i.d(t,{w:()=>s});const s=e=>e.callWS({type:"wyoming/info"})},33346:function(e,t,i){var s=i(44249),a=i(57243),n=i(50778),o=i(11297),l=(i(20095),i(10508),i(85019)),r=i(42717);(0,s.Z)([(0,n.Mo)("cloud-step-intro")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"method",key:"render",value:function(){return a.dy`<div class="content">
        <img
          src=${`/static/images/logo_nabu_casa${this.hass.themes?.darkMode?"_dark":""}.png`}
          alt="Nabu Casa logo"
        />
        <h1>
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.cloud.title")}
        </h1>
        <div class="features">
          <div class="feature speech">
            <div class="logos">
              <div class="round-icon">
                <ha-svg-icon .path=${"M8,7A2,2 0 0,1 10,9V14A2,2 0 0,1 8,16A2,2 0 0,1 6,14V9A2,2 0 0,1 8,7M14,14C14,16.97 11.84,19.44 9,19.92V22H7V19.92C4.16,19.44 2,16.97 2,14H4A4,4 0 0,0 8,18A4,4 0 0,0 12,14H14M21.41,9.41L17.17,13.66L18.18,10H14A2,2 0 0,1 12,8V4A2,2 0 0,1 14,2H20A2,2 0 0,1 22,4V8C22,8.55 21.78,9.05 21.41,9.41Z"}></ha-svg-icon>
              </div>
            </div>
            <h2>
              ${this.hass.localize("ui.panel.config.voice_assistants.assistants.cloud.features.speech.title")}
              <span class="no-wrap"></span>
            </h2>
            <p>
              ${this.hass.localize("ui.panel.config.voice_assistants.assistants.cloud.features.speech.text")}
            </p>
          </div>
          <div class="feature access">
            <div class="logos">
              <div class="round-icon">
                <ha-svg-icon .path=${"M17.9,17.39C17.64,16.59 16.89,16 16,16H15V13A1,1 0 0,0 14,12H8V10H10A1,1 0 0,0 11,9V7H13A2,2 0 0,0 15,5V4.59C17.93,5.77 20,8.64 20,12C20,14.08 19.2,15.97 17.9,17.39M11,19.93C7.05,19.44 4,16.08 4,12C4,11.38 4.08,10.78 4.21,10.21L9,15V16A2,2 0 0,0 11,18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z"}></ha-svg-icon>
              </div>
            </div>
            <h2>
              ${this.hass.localize("ui.panel.config.voice_assistants.assistants.cloud.features.remote_access.title")}
              <span class="no-wrap"></span>
            </h2>
            <p>
              ${this.hass.localize("ui.panel.config.voice_assistants.assistants.cloud.features.remote_access.text")}
            </p>
          </div>
          <div class="feature">
            <div class="logos">
              <img
                alt="Google Assistant"
                src=${(0,l.X1)({domain:"google_assistant",type:"icon",darkOptimized:this.hass.themes?.darkMode})}
                crossorigin="anonymous"
                referrerpolicy="no-referrer"
              />
              <img
                alt="Amazon Alexa"
                src=${(0,l.X1)({domain:"alexa",type:"icon",darkOptimized:this.hass.themes?.darkMode})}
                crossorigin="anonymous"
                referrerpolicy="no-referrer"
              />
            </div>
            <h2>
              ${this.hass.localize("ui.panel.config.voice_assistants.assistants.cloud.features.assistants.title")}
            </h2>
            <p>
              ${this.hass.localize("ui.panel.config.voice_assistants.assistants.cloud.features.assistants.text")}
            </p>
          </div>
        </div>
      </div>
      <div class="footer side-by-side">
        <a
          href="https://www.nabucasa.com"
          target="_blank"
          rel="noreferrer noopener"
        >
          <ha-button>
            <ha-svg-icon .path=${"M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z"} slot="icon"></ha-svg-icon>
            nabucasa.com
          </ha-button>
        </a>
        <ha-button unelevated @click=${this._signUp}
          >${this.hass.localize("ui.panel.config.cloud.register.headline")}</ha-button
        >
      </div>`}},{kind:"method",key:"_signUp",value:function(){(0,o.B)(this,"cloud-step",{step:"SIGNUP"})}},{kind:"field",static:!0,key:"styles",value(){return[r._,a.iv`
      :host {
        display: flex;
      }
      .features {
        display: flex;
        flex-direction: column;
        grid-gap: 16px;
        padding: 16px;
      }
      .feature {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
        margin-bottom: 16px;
      }
      .feature .logos {
        margin-bottom: 16px;
      }
      .feature .logos > * {
        width: 40px;
        height: 40px;
        margin: 0 4px;
      }
      .round-icon {
        border-radius: 50%;
        color: #6e41ab;
        background-color: #e8dcf7;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 24px;
      }
      .access .round-icon {
        color: #00aef8;
        background-color: #cceffe;
      }
      .feature h2 {
        font-weight: 500;
        font-size: 16px;
        line-height: 24px;
        margin-top: 0;
        margin-bottom: 8px;
      }
      .feature p {
        font-weight: 400;
        font-size: 14px;
        line-height: 20px;
        margin: 0;
      }
    `]}}]}}),a.oi)},60771:function(e,t,i){var s=i(44249),a=i(57243),n=i(50778),o=i(11297),l=i(64364),r=(i(17949),i(20095),i(42781),i(10508),i(70596),i(3079));var d=i(4557),c=i(42717);(0,s.Z)([(0,n.Mo)("cloud-step-signin")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_requestInProgress",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_checkConnection",value(){return!0}},{kind:"field",decorators:[(0,n.IO)("#email",!0)],key:"_emailField",value:void 0},{kind:"field",decorators:[(0,n.IO)("#password",!0)],key:"_passwordField",value:void 0},{kind:"method",key:"render",value:function(){return a.dy`<div class="content">
        <img
          src=${`/static/images/logo_nabu_casa${this.hass.themes?.darkMode?"_dark":""}.png`}
          alt="Nabu Casa logo"
        />
        <h1>${this.hass.localize("ui.panel.config.cloud.login.sign_in")}</h1>
        ${this._error?a.dy`<ha-alert alert-type="error">${this._error}</ha-alert>`:""}
        <ha-textfield
          autofocus
          id="email"
          name="email"
          .label=${this.hass.localize("ui.panel.config.cloud.register.email_address")}
          .disabled=${this._requestInProgress}
          type="email"
          autocomplete="email"
          required
          @keydown=${this._keyDown}
          validationMessage=${this.hass.localize("ui.panel.config.cloud.register.email_error_msg")}
        ></ha-textfield>
        <ha-password-field
          id="password"
          name="password"
          .label=${this.hass.localize("ui.panel.config.cloud.register.password")}
          .disabled=${this._requestInProgress}
          autocomplete="new-password"
          minlength="8"
          required
          @keydown=${this._keyDown}
          validationMessage=${this.hass.localize("ui.panel.config.cloud.register.password_error_msg")}
        ></ha-password-field>
      </div>
      <div class="footer">
        <ha-button
          unelevated
          @click=${this._handleLogin}
          .disabled=${this._requestInProgress}
          >${this.hass.localize("ui.panel.config.cloud.login.sign_in")}</ha-button
        >
      </div>`}},{kind:"method",key:"_keyDown",value:function(e){"Enter"===e.key&&this._handleLogin()}},{kind:"method",key:"_handleLogin",value:async function(){const e=this._emailField,t=this._passwordField,s=e.value,a=t.value;if(!e.reportValidity())return t.reportValidity(),void e.focus();if(!t.reportValidity())return void t.focus();this._requestInProgress=!0;const n=async(t,s)=>{try{await(0,r._Y)({hass:this.hass,email:t,...s?{code:s}:{password:a},check_connection:this._checkConnection})}catch(u){const s=u&&u.body&&u.body.code;if("mfarequired"===s){const e=await(0,d.D9)(this,{title:this.hass.localize("ui.panel.config.cloud.login.totp_code_prompt_title"),inputLabel:this.hass.localize("ui.panel.config.cloud.login.totp_code"),inputType:"text",defaultValue:"",confirmText:this.hass.localize("ui.panel.config.cloud.login.submit")});if(null!==e&&""!==e)return void(await n(t,e))}if("alreadyconnectederror"===s)return c=this,h={details:JSON.parse(u.body.message),logInHereAction:()=>{this._checkConnection=!1,n(t)},closeDialog:()=>{this._requestInProgress=!1}},void new Promise((e=>{const t=h.closeDialog,s=h.logInHereAction;(0,o.B)(c,"show-dialog",{dialogTag:"dialog-cloud-already-connected",dialogImport:()=>i.e("8393").then(i.bind(i,9852)),dialogParams:{...h,closeDialog:()=>{t?.(),e(!1)},logInHereAction:()=>{s?.(),e(!0)}}})}));if("usernotfound"===s&&t!==t.toLowerCase())return void(await n(t.toLowerCase()));if("PasswordChangeRequired"===s)return(0,d.Ys)(this,{title:this.hass.localize("ui.panel.config.cloud.login.alert_password_change_required")}),(0,l.c)("/config/cloud/forgot-password"),void(0,o.B)(this,"closed");switch(this._requestInProgress=!1,s){case"UserNotConfirmed":this._error=this.hass.localize("ui.panel.config.cloud.login.alert_email_confirm_necessary");break;case"mfarequired":this._error=this.hass.localize("ui.panel.config.cloud.login.alert_mfa_code_required");break;case"mfaexpiredornotstarted":this._error=this.hass.localize("ui.panel.config.cloud.login.alert_mfa_expired_or_not_started");break;case"invalidtotpcode":this._error=this.hass.localize("ui.panel.config.cloud.login.alert_totp_code_invalid");break;default:this._error=u&&u.body&&u.body.message?u.body.message:"Unknown error"}e.focus()}var c,h};await n(s)}},{kind:"field",static:!0,key:"styles",value(){return[c._,a.iv`
      :host {
        display: block;
      }
      ha-textfield,
      ha-password-field {
        display: block;
      }
    `]}}]}}),a.oi)},96404:function(e,t,i){var s=i(44249),a=i(57243),n=i(50778),o=i(11297),l=(i(17949),i(20095),i(42781),i(10508),i(70596),i(3079)),r=i(42717);(0,s.Z)([(0,n.Mo)("cloud-step-signup")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_requestInProgress",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_email",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_password",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_state",value:void 0},{kind:"field",decorators:[(0,n.IO)("#email",!0)],key:"_emailField",value:void 0},{kind:"field",decorators:[(0,n.IO)("#password",!0)],key:"_passwordField",value:void 0},{kind:"method",key:"render",value:function(){return a.dy`<div class="content">
        <img
          src=${`/static/images/logo_nabu_casa${this.hass.themes?.darkMode?"_dark":""}.png`}
          alt="Nabu Casa logo"
        />
        <h1>
          ${this.hass.localize("ui.panel.config.cloud.register.create_account")}
        </h1>
        ${this._error?a.dy`<ha-alert alert-type="error">${this._error}</ha-alert>`:""}
        ${"VERIFY"===this._state?a.dy`<p>
              ${this.hass.localize("ui.panel.config.cloud.register.confirm_email",{email:this._email})}
            </p>`:a.dy`<ha-textfield
                autofocus
                id="email"
                name="email"
                .label=${this.hass.localize("ui.panel.config.cloud.register.email_address")}
                .disabled=${this._requestInProgress}
                type="email"
                autocomplete="email"
                required
                @keydown=${this._keyDown}
                validationMessage=${this.hass.localize("ui.panel.config.cloud.register.email_error_msg")}
              ></ha-textfield>
              <ha-password-field
                id="password"
                name="password"
                .label=${this.hass.localize("ui.panel.config.cloud.register.password")}
                .disabled=${this._requestInProgress}
                autocomplete="new-password"
                minlength="8"
                required
                @keydown=${this._keyDown}
                validationMessage=${this.hass.localize("ui.panel.config.cloud.register.password_error_msg")}
              ></ha-password-field>`}
      </div>
      <div class="footer side-by-side">
        ${"VERIFY"===this._state?a.dy`<ha-button
                @click=${this._handleResendVerifyEmail}
                .disabled=${this._requestInProgress}
                >${this.hass.localize("ui.panel.config.cloud.register.resend_confirm_email")}</ha-button
              ><ha-button
                unelevated
                @click=${this._login}
                .disabled=${this._requestInProgress}
                >${this.hass.localize("ui.panel.config.cloud.register.clicked_confirm")}</ha-button
              >`:a.dy`<ha-button
                @click=${this._signIn}
                .disabled=${this._requestInProgress}
                >${this.hass.localize("ui.panel.config.cloud.login.sign_in")}</ha-button
              >
              <ha-button
                unelevated
                @click=${this._handleRegister}
                .disabled=${this._requestInProgress}
                >${this.hass.localize("ui.common.next")}</ha-button
              >`}
      </div>`}},{kind:"method",key:"_signIn",value:function(){(0,o.B)(this,"cloud-step",{step:"SIGNIN"})}},{kind:"method",key:"_keyDown",value:function(e){"Enter"===e.key&&this._handleRegister()}},{kind:"method",key:"_handleRegister",value:async function(){const e=this._emailField,t=this._passwordField;if(!e.reportValidity())return t.reportValidity(),void e.focus();if(!t.reportValidity())return void t.focus();const i=e.value.toLowerCase(),s=t.value;this._requestInProgress=!0;try{await(0,l.bi)(this.hass,i,s),this._email=i,this._password=s,this._verificationEmailSent()}catch(a){this._password="",this._error=a&&a.body&&a.body.message?a.body.message:"Unknown error"}finally{this._requestInProgress=!1}}},{kind:"method",key:"_handleResendVerifyEmail",value:async function(){if(this._email)try{await(0,l._t)(this.hass,this._email),this._verificationEmailSent()}catch(e){this._error=e&&e.body&&e.body.message?e.body.message:"Unknown error"}}},{kind:"method",key:"_verificationEmailSent",value:function(){this._state="VERIFY",setTimeout((()=>this._login()),5e3)}},{kind:"method",key:"_login",value:async function(){if(this._email&&this._password)try{await(0,l._Y)({hass:this.hass,email:this._email,password:this._password}),(0,o.B)(this,"cloud-step",{step:"DONE"})}catch(e){"usernotconfirmed"===e?.body?.code?this._verificationEmailSent():this._error="Something went wrong. Please try again."}}},{kind:"field",static:!0,key:"styles",value(){return[r._,a.iv`
      .content {
        width: 100%;
      }
      ha-textfield,
      ha-password-field {
        display: block;
      }
    `]}}]}}),a.oi)},42717:function(e,t,i){i.d(t,{_:()=>a});var s=i(57243);const a=[i(66193).Qx,s.iv`
    :host {
      align-items: center;
      text-align: center;
      min-height: 400px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      height: 100%;
      padding: 24px;
      box-sizing: border-box;
    }
    .content {
      flex: 1;
    }
    .content img {
      width: 120px;
    }
    @media all and (max-width: 450px), all and (max-height: 500px) {
      :host {
        min-height: 100%;
        height: auto;
      }
      .content img {
        margin-top: 68px;
        margin-bottom: 68px;
      }
    }
    .footer {
      display: flex;
      width: 100%;
      flex-direction: row;
      justify-content: flex-end;
    }
    .footer.full-width {
      flex-direction: column;
    }
    .footer.full-width ha-button {
      width: 100%;
    }
    .footer.centered {
      justify-content: center;
    }
    .footer.side-by-side {
      justify-content: space-between;
    }
  `]},66738:function(e,t,i){i.a(e,(async function(e,s){try{i.r(t),i.d(t,{HaVoiceAssistantSetupDialog:()=>L,STEP:()=>E});var a=i(44249),n=(i(31622),i(57243)),o=i(50778),l=i(27486),r=i(11297),d=i(79575),c=i(46784),h=(i(1025),i(44118),i(96980)),u=(i(43745),i(80495)),p=i(31762),g=i(36719),v=i(66193),f=(i(62455),i(28573)),_=i(97400),y=i(33743),k=i(99881),m=i(17802),b=i(59487),w=i(22467),$=i(34315),C=e([f,_,y,k,m,b,w,$,c,h]);[f,_,y,k,m,b,w,$,c,h]=C.then?(await C)():C;const x="M15.41,16.58L10.83,12L15.41,7.41L14,6L8,12L14,18L15.41,16.58Z",S="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",z="M7,10L12,15L17,10H7Z";let E=function(e){return e[e.INIT=0]="INIT",e[e.UPDATE=1]="UPDATE",e[e.CHECK=2]="CHECK",e[e.WAKEWORD=3]="WAKEWORD",e[e.AREA=4]="AREA",e[e.PIPELINE=5]="PIPELINE",e[e.SUCCESS=6]="SUCCESS",e[e.CLOUD=7]="CLOUD",e[e.LOCAL=8]="LOCAL",e[e.CHANGE_WAKEWORD=9]="CHANGE_WAKEWORD",e}({}),L=(0,a.Z)([(0,o.Mo)("ha-voice-assistant-setup-dialog")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_step",value(){return E.INIT}},{kind:"field",decorators:[(0,o.SB)()],key:"_assistConfiguration",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_language",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_languages",value(){return[]}},{kind:"field",decorators:[(0,o.SB)()],key:"_localOption",value:void 0},{kind:"field",key:"_previousSteps",value(){return[]}},{kind:"field",key:"_nextStep",value:void 0},{kind:"method",key:"showDialog",value:async function(e){this._params=e,await this._fetchAssistConfiguration(),this._step=E.UPDATE}},{kind:"method",key:"closeDialog",value:async function(){this.renderRoot.querySelector("ha-dialog")?.close()}},{kind:"method",key:"willUpdate",value:function(e){e.has("_step")&&this._step===E.PIPELINE&&this._getLanguages()}},{kind:"method",key:"_dialogClosed",value:function(){this._params=void 0,this._assistConfiguration=void 0,this._previousSteps=[],this._nextStep=void 0,this._step=E.INIT,(0,r.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"field",key:"_deviceEntities",value(){return(0,l.Z)(((e,t)=>Object.values(t).filter((t=>t.device_id===e))))}},{kind:"field",key:"_findDomainEntityId",value(){return(0,l.Z)(((e,t,i)=>{const s=this._deviceEntities(e,t);return s.find((e=>(0,d.M)(e.entity_id)===i))?.entity_id}))}},{kind:"method",key:"render",value:function(){if(!this._params)return n.Ld;const e=this._findDomainEntityId(this._params.deviceId,this.hass.entities,"assist_satellite"),t=e?this.hass.states[e]:void 0;return n.dy`
      <ha-dialog
        open
        @closed=${this._dialogClosed}
        .heading=${"Voice Satellite setup"}
        hideActions
        escapeKeyAction
        scrimClickAction
      >
        <ha-dialog-header slot="heading">
          ${this._step===E.LOCAL?n.Ld:this._previousSteps.length?n.dy`<ha-icon-button
                  slot="navigationIcon"
                  .label=${this.hass.localize("ui.common.back")??"Back"}
                  .path=${x}
                  @click=${this._goToPreviousStep}
                ></ha-icon-button>`:this._step!==E.UPDATE?n.dy`<ha-icon-button
                    slot="navigationIcon"
                    .label=${this.hass.localize("ui.common.close")??"Close"}
                    .path=${S}
                    @click=${this.closeDialog}
                  ></ha-icon-button>`:n.Ld}
          ${this._step===E.WAKEWORD||this._step===E.AREA?n.dy`<ha-button
                @click=${this._goToNextStep}
                class="skip-btn"
                slot="actionItems"
                >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.skip")}</ha-button
              >`:this._step===E.PIPELINE&&this._language?n.dy`<ha-md-button-menu
                    slot="actionItems"
                    positioning="fixed"
                  >
                    <ha-assist-chip
                      .label=${(0,c.u)(this._language,this.hass.locale)}
                      slot="trigger"
                    >
                      <ha-svg-icon
                        slot="trailing-icon"
                        .path=${z}
                      ></ha-svg-icon
                    ></ha-assist-chip>
                    ${(0,h.C)(this._languages,!1,!1,this.hass.locale).map((e=>n.dy`<ha-md-menu-item
                          .value=${e.value}
                          @click=${this._handlePickLanguage}
                          @keydown=${this._handlePickLanguage}
                          .selected=${this._language===e.value}
                        >
                          ${e.label}
                        </ha-md-menu-item>`))}
                  </ha-md-button-menu>`:n.Ld}
        </ha-dialog-header>
        <div
          class="content"
          @next-step=${this._goToNextStep}
          @prev-step=${this._goToPreviousStep}
        >
          ${this._step===E.UPDATE?n.dy`<ha-voice-assistant-setup-step-update
                .hass=${this.hass}
                .updateEntityId=${this._findDomainEntityId(this._params.deviceId,this.hass.entities,"update")}
              ></ha-voice-assistant-setup-step-update>`:this._error?n.dy`<ha-alert alert-type="error">${this._error}</ha-alert>`:t?.state===g.nZ?n.dy`<ha-alert alert-type="error"
                    >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.not_available")}</ha-alert
                  >`:this._step===E.CHECK?n.dy`<ha-voice-assistant-setup-step-check
                      .hass=${this.hass}
                      .assistEntityId=${e}
                    ></ha-voice-assistant-setup-step-check>`:this._step===E.WAKEWORD?n.dy`<ha-voice-assistant-setup-step-wake-word
                        .hass=${this.hass}
                        .assistConfiguration=${this._assistConfiguration}
                        .assistEntityId=${e}
                        .deviceEntities=${this._deviceEntities(this._params.deviceId,this.hass.entities)}
                      ></ha-voice-assistant-setup-step-wake-word>`:this._step===E.CHANGE_WAKEWORD?n.dy`
                          <ha-voice-assistant-setup-step-change-wake-word
                            .hass=${this.hass}
                            .assistConfiguration=${this._assistConfiguration}
                            .assistEntityId=${e}
                          ></ha-voice-assistant-setup-step-change-wake-word>
                        `:this._step===E.AREA?n.dy`
                            <ha-voice-assistant-setup-step-area
                              .hass=${this.hass}
                              .deviceId=${this._params.deviceId}
                            ></ha-voice-assistant-setup-step-area>
                          `:this._step===E.PIPELINE?n.dy`<ha-voice-assistant-setup-step-pipeline
                              .hass=${this.hass}
                              .languages=${this._languages}
                              .language=${this._language}
                              .assistConfiguration=${this._assistConfiguration}
                              .assistEntityId=${e}
                              @language-changed=${this._languageChanged}
                            ></ha-voice-assistant-setup-step-pipeline>`:this._step===E.CLOUD?n.dy`<ha-voice-assistant-setup-step-cloud
                                .hass=${this.hass}
                              ></ha-voice-assistant-setup-step-cloud>`:this._step===E.LOCAL?n.dy`<ha-voice-assistant-setup-step-local
                                  .hass=${this.hass}
                                  .language=${this._language}
                                  .localOption=${this._localOption}
                                  .assistConfiguration=${this._assistConfiguration}
                                ></ha-voice-assistant-setup-step-local>`:this._step===E.SUCCESS?n.dy`<ha-voice-assistant-setup-step-success
                                    .hass=${this.hass}
                                    .assistConfiguration=${this._assistConfiguration}
                                    .assistEntityId=${e}
                                  ></ha-voice-assistant-setup-step-success>`:n.Ld}
        </div>
      </ha-dialog>
    `}},{kind:"method",key:"_getLanguages",value:async function(){if(this._languages.length)return;const e=await(0,p.KH)(this.hass);this._languages=Object.entries(e.languages).filter((([e,t])=>t.cloud>0||t.full_local>0||t.focused_local>0)).map((([e,t])=>e)),this._language=e.preferred_language&&this._languages.includes(e.preferred_language)?e.preferred_language:void 0}},{kind:"method",key:"_fetchAssistConfiguration",value:async function(){try{this._assistConfiguration=await(0,u.ko)(this.hass,this._findDomainEntityId(this._params.deviceId,this.hass.entities,"assist_satellite"))}catch(e){this._error=e.message}}},{kind:"method",key:"_handlePickLanguage",value:function(e){"keydown"===e.type&&"Enter"!==e.key&&" "!==e.key||(this._language=e.target.value)}},{kind:"method",key:"_languageChanged",value:function(e){e.detail.value&&(this._language=e.detail.value)}},{kind:"method",key:"_goToPreviousStep",value:function(){this._previousSteps.length&&(this._step=this._previousSteps.pop())}},{kind:"method",key:"_goToNextStep",value:function(e){e?.detail?.updateConfig&&this._fetchAssistConfiguration(),e?.detail?.nextStep&&(this._nextStep=e.detail.nextStep),e?.detail?.noPrevious||this._previousSteps.push(this._step),e?.detail?.step?(this._step=e.detail.step,e.detail.step===E.LOCAL&&(this._localOption=e.detail.option)):this._nextStep?(this._step=this._nextStep,this._nextStep=void 0):this._step+=1}},{kind:"get",static:!0,key:"styles",value:function(){return[v.yu,n.iv`
        ha-dialog {
          --dialog-content-padding: 0;
        }
        @media all and (min-width: 450px) and (min-height: 500px) {
          ha-dialog {
            --mdc-dialog-min-width: 560px;
            --mdc-dialog-max-width: 560px;
            --mdc-dialog-min-width: min(560px, 95vw);
            --mdc-dialog-max-width: min(560px, 95vw);
          }
        }
        ha-dialog-header {
          height: 56px;
        }
        @media all and (max-width: 450px), all and (max-height: 500px) {
          .content {
            height: calc(100vh - 56px);
          }
        }
        .skip-btn {
          margin-top: 6px;
        }
        ha-alert {
          margin: 24px;
          display: block;
        }
        ha-md-button-menu {
          height: 48px;
          display: flex;
          align-items: center;
          margin-right: 12px;
          margin-inline-end: 12px;
        }
      `]}}]}}),n.oi);s()}catch(x){s(x)}}))},62455:function(e,t,i){var s=i(44249),a=i(57243),n=i(50778),o=i(11297),l=i(99523),r=i(4557),d=i(42717);i(69181);(0,s.Z)([(0,n.Mo)("ha-voice-assistant-setup-step-area")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"deviceId",value:void 0},{kind:"method",key:"render",value:function(){const e=this.hass.devices[this.deviceId];return a.dy`<div class="content">
        <img
          src="/static/images/voice-assistant/area.png"
          alt="Casita Home Assistant logo"
        />
        <h1>
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.area.title")}
        </h1>
        <p class="secondary">
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.area.secondary")}
        </p>
        <ha-area-picker
          .hass=${this.hass}
          .value=${e.area_id}
        ></ha-area-picker>
      </div>
      <div class="footer">
        <ha-button @click=${this._setArea} unelevated
          >${this.hass.localize("ui.common.next")}</ha-button
        >
      </div>`}},{kind:"method",key:"_setArea",value:async function(){const e=this.shadowRoot.querySelector("ha-area-picker").value;e?(await(0,l.t1)(this.hass,this.deviceId,{area_id:e}),this._nextStep()):(0,r.Ys)(this,{text:this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.area.no_selection")})}},{kind:"method",key:"_nextStep",value:function(){(0,o.B)(this,"next-step")}},{kind:"field",static:!0,key:"styles",value(){return[d._,a.iv`
      ha-area-picker {
        display: block;
        width: 100%;
        margin-bottom: 24px;
      }
    `]}}]}}),a.oi)},28573:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(57243),n=i(50778),o=i(11297),l=(i(48333),i(69387),i(80495)),r=i(42717),d=i(66738),c=e([d]);d=(c.then?(await c)():c)[0];(0,s.Z)([(0,n.Mo)("ha-voice-assistant-setup-step-change-wake-word")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"assistConfiguration",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"assistEntityId",value:void 0},{kind:"method",key:"render",value:function(){return a.dy`<div class="padding content">
        <img
          src="/static/images/voice-assistant/change-wake-word.png"
          alt="Casita Home Assistant logo"
        />
        <h1>
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.change_wake_word.title")}
        </h1>
        <p class="secondary">
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.change_wake_word.secondary")}
        </p>
      </div>
      <ha-md-list>
        ${this.assistConfiguration.available_wake_words.map((e=>a.dy`<ha-md-list-item
              interactive
              type="button"
              @click=${this._wakeWordPicked}
              .value=${e.id}
            >
              ${e.wake_word}
              <ha-icon-next slot="end"></ha-icon-next>
            </ha-md-list-item>`))}
      </ha-md-list>`}},{kind:"method",key:"_wakeWordPicked",value:async function(e){if(!this.assistEntityId)return;const t=e.currentTarget.value;await(0,l.DT)(this.hass,this.assistEntityId,[t]),this._nextStep()}},{kind:"method",key:"_nextStep",value:function(){(0,o.B)(this,"next-step",{step:d.STEP.WAKEWORD,updateConfig:!0})}},{kind:"field",static:!0,key:"styles",value(){return[r._,a.iv`
      :host {
        padding: 0;
      }
      .padding {
        padding: 24px;
      }
      ha-md-list {
        width: 100%;
        text-align: initial;
        margin-bottom: 24px;
      }
    `]}}]}}),a.oi);t()}catch(h){t(h)}}))},97400:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(11297),r=(i(20095),i(19537)),d=i(80495),c=i(42717),h=i(26205),u=e([r]);r=(u.then?(await u)():u)[0];(0,s.Z)([(0,o.Mo)("ha-voice-assistant-setup-step-check")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistEntityId",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_status",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_showLoader",value(){return!1}},{kind:"method",key:"willUpdate",value:function(e){(0,a.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated?"success"===this._status&&e.has("hass")&&"idle"===this.hass.states[this.assistEntityId]?.state&&this._nextStep():this._testConnection()}},{kind:"method",key:"render",value:function(){return n.dy`<div class="content">
      ${"timeout"===this._status?n.dy`<img
              src="/static/images/voice-assistant/error.png"
              alt="Casita Home Assistant error logo"
            />
            <h1>
              ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.check.failed_title")}
            </h1>
            <p class="secondary">
              ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.check.failed_secondary")}
            </p>
            <div class="footer">
              <a
                href=${(0,h.R)(this.hass,"/voice_control/troubleshooting/#i-dont-get-a-voice-response")}
                ><ha-button
                  >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.check.help")}</ha-button
                ></a
              >
              <ha-button @click=${this._testConnection}
                >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.check.retry")}</ha-button
              >
            </div>`:n.dy`<img
              src="/static/images/voice-assistant/hi.png"
              alt="Casita Home Assistant hi logo"
            />
            <h1>
              ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.check.title")}
            </h1>
            <p class="secondary">
              ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.check.secondary")}
            </p>

            ${this._showLoader?n.dy`<ha-spinner></ha-spinner>`:n.Ld}`}
    </div>`}},{kind:"method",key:"_testConnection",value:async function(){this._status=void 0,this._showLoader=!1;const e=setTimeout((()=>{this._showLoader=!0}),3e3),t=await(0,d.cz)(this.hass,this.assistEntityId);clearTimeout(e),this._showLoader=!1,this._status=t.status}},{kind:"method",key:"_nextStep",value:function(){(0,l.B)(this,"next-step",{noPrevious:!0})}},{kind:"field",static:!0,key:"styles",value(){return c._}}]}}),n.oi);t()}catch(p){t(p)}}))},33743:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(57243),n=i(50778),o=(i(33346),i(60771),i(96404),i(11297)),l=i(66738),r=e([l]);l=(r.then?(await r)():r)[0];(0,s.Z)([(0,n.Mo)("ha-voice-assistant-setup-step-cloud")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_state",value(){return"INTRO"}},{kind:"method",key:"render",value:function(){return"SIGNUP"===this._state?a.dy`<cloud-step-signup
        .hass=${this.hass}
        @cloud-step=${this._cloudStep}
      ></cloud-step-signup>`:"SIGNIN"===this._state?a.dy`<cloud-step-signin
        .hass=${this.hass}
        @cloud-step=${this._cloudStep}
      ></cloud-step-signin>`:a.dy`<cloud-step-intro
      .hass=${this.hass}
      @cloud-step=${this._cloudStep}
    ></cloud-step-intro>`}},{kind:"method",key:"_cloudStep",value:function(e){"DONE"!==e.detail.step?this._state=e.detail.step:(0,o.B)(this,"next-step",{step:l.STEP.PIPELINE,noPrevious:!0})}}]}}),a.oi);t()}catch(d){t(d)}}))},99881:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(49672),r=i(11297),d=i(79575),c=i(19537),h=i(4855),u=i(79983),p=i(60498),g=i(46999),v=i(52829),f=i(421),_=i(28726),y=i(26205),k=i(42717),m=i(66738),b=i(31762),w=e([c,m]);[c,m]=w.then?(await w)():w;const $="M14,3V5H17.59L7.76,14.83L9.17,16.24L19,6.41V10H21V3M19,19H5V5H12V3H5C3.89,3 3,3.9 3,5V19A2,2 0 0,0 5,21H19A2,2 0 0,0 21,19V12H19V19Z";(0,s.Z)([(0,o.Mo)("ha-voice-assistant-setup-step-local")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistConfiguration",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"localOption",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"language",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_state",value(){return"INTRO"}},{kind:"field",decorators:[(0,o.SB)()],key:"_detailState",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_error",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_localTts",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_localStt",value:void 0},{kind:"method",key:"render",value:function(){return n.dy`<div class="content">
      ${"INSTALLING"===this._state?n.dy`<img
              src="/static/images/voice-assistant/update.png"
              alt="Casita Home Assistant loading logo"
            />
            <h1>
              ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.title")}
            </h1>
            <p>
              ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.secondary")}
            </p>
            <ha-spinner></ha-spinner>
            <p>
              ${this._detailState||"Installation can take several minutes"}
            </p>`:"ERROR"===this._state?n.dy` <img
                src="/static/images/voice-assistant/error.png"
                alt="Casita Home Assistant error logo"
              />
              <h1>
                ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.failed_title")}
              </h1>
              <p>${this._error}</p>
              <p>
                ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.failed_secondary")}
              </p>
              <ha-button @click=${this._prevStep}
                >${this.hass.localize("ui.common.back")}</ha-button
              >
              <a
                href=${(0,y.R)(this.hass,"/voice_control/voice_remote_local_assistant/")}
                target="_blank"
                rel="noreferrer noopener"
              >
                <ha-button>
                  <ha-svg-icon .path=${$} slot="icon"></ha-svg-icon>
                  ${this.hass.localize("ui.panel.config.common.learn_more")}</ha-button
                >
              </a>`:"NOT_SUPPORTED"===this._state?n.dy`<img
                  src="/static/images/voice-assistant/error.png"
                  alt="Casita Home Assistant error logo"
                />
                <h1>
                  ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.not_supported_title")}
                </h1>
                <p>
                  ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.not_supported_secondary")}
                </p>
                <ha-button @click=${this._prevStep}
                  >${this.hass.localize("ui.common.back")}</ha-button
                >
                <a
                  href=${(0,y.R)(this.hass,"/voice_control/voice_remote_local_assistant/")}
                  target="_blank"
                  rel="noreferrer noopener"
                >
                  <ha-button>
                    <ha-svg-icon
                      .path=${$}
                      slot="icon"
                    ></ha-svg-icon>
                    ${this.hass.localize("ui.panel.config.common.learn_more")}</ha-button
                  >
                </a>`:n.Ld}
    </div>`}},{kind:"method",key:"willUpdate",value:function(e){(0,a.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated||this._checkLocal()}},{kind:"method",key:"_prevStep",value:function(){(0,r.B)(this,"prev-step")}},{kind:"method",key:"_nextStep",value:function(){(0,r.B)(this,"next-step",{step:m.STEP.SUCCESS,noPrevious:!0})}},{kind:"method",key:"_checkLocal",value:async function(){if(await this._findLocalEntities(),this._localTts&&this._localStt)try{if(this._localTts.length&&this._localStt.length)return void(await this._pickOrCreatePipelineExists());if(!(0,l.p)(this.hass,"hassio"))return void(this._state="NOT_SUPPORTED");this._state="INSTALLING";const{addons:e}=await(0,g.yt)(this.hass),t=e.find((e=>e.slug===this._ttsAddonName)),i=e.find((e=>e.slug===this._sttAddonName));this._localTts.length||(t||(this._detailState=this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.state.installing_${this._ttsProviderName}`),await(0,g.fU)(this.hass,this._ttsAddonName)),t&&"started"===t.state||(this._detailState=this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.state.starting_${this._ttsProviderName}`),await(0,g.kP)(this.hass,this._ttsAddonName)),this._detailState=this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.state.setup_${this._ttsProviderName}`),await this._setupConfigEntry("tts")),this._localStt.length||(i||(this._detailState=this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.state.installing_${this._sttProviderName}`),await(0,g.fU)(this.hass,this._sttAddonName)),i&&"started"===i.state||(this._detailState=this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.state.starting_${this._sttProviderName}`),await(0,g.kP)(this.hass,this._sttAddonName)),this._detailState=this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.state.setup_${this._sttProviderName}`),await this._setupConfigEntry("stt")),this._detailState=this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.state.creating_pipeline"),await this._findEntitiesAndCreatePipeline()}catch(e){this._state="ERROR",this._error=e.message}}},{kind:"field",key:"_ttsProviderName",value(){return"piper"}},{kind:"field",key:"_ttsAddonName",value(){return"core_piper"}},{kind:"field",key:"_ttsHostName",value(){return"core-piper"}},{kind:"field",key:"_ttsPort",value(){return 10200}},{kind:"get",key:"_sttProviderName",value:function(){return"focused_local"===this.localOption?"speech-to-phrase":"faster-whisper"}},{kind:"get",key:"_sttAddonName",value:function(){return"focused_local"===this.localOption?"core_speech-to-phrase":"core_whisper"}},{kind:"get",key:"_sttHostName",value:function(){return"focused_local"===this.localOption?"core-speech-to-phrase":"core-whisper"}},{kind:"field",key:"_sttPort",value(){return 10300}},{kind:"method",key:"_findLocalEntities",value:async function(){const e=Object.values(this.hass.entities).filter((e=>"wyoming"===e.platform));if(!e.length)return this._localStt=[],void(this._localTts=[]);const t=await(0,_.w)(this.hass),i=Object.values(await(0,p.Iq)(this.hass,e.map((e=>e.entity_id))));this._localTts=i.filter((e=>"tts"===(0,d.M)(e.entity_id)&&e.config_entry_id&&t.info[e.config_entry_id]?.tts.some((e=>e.name===this._ttsProviderName)))),this._localStt=i.filter((e=>"stt"===(0,d.M)(e.entity_id)&&e.config_entry_id&&t.info[e.config_entry_id]?.asr.some((e=>e.name===this._sttProviderName))))}},{kind:"method",key:"_setupConfigEntry",value:async function(e){const t=await this._findConfigFlowInProgress(e);if(t){if("create_entry"===(await(0,u.XO)(this.hass,t.flow_id,{})).type)return}return this._createConfigEntry(e)}},{kind:"method",key:"_findConfigFlowInProgress",value:async function(e){return(await(0,u.D7)(this.hass.connection)).find((t=>"wyoming"===t.handler&&"hassio"===t.context.source&&(t.context.configuration_url&&t.context.configuration_url.includes("tts"===e?this._ttsAddonName:this._sttAddonName)||t.context.title_placeholders.name&&t.context.title_placeholders.name.toLowerCase().includes("tts"===e?this._ttsProviderName:this._sttProviderName))))}},{kind:"method",key:"_createConfigEntry",value:async function(e){const t=await(0,u.Ky)(this.hass,"wyoming"),i=await(0,u.XO)(this.hass,t.flow_id,{host:"tts"===e?this._ttsHostName:this._sttHostName,port:"tts"===e?this._ttsPort:this._sttPort});if("create_entry"!==i.type)throw new Error(`${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.errors.failed_create_entry",{addon:"tts"===e?this._ttsProviderName:this._sttProviderName})}${"errors"in i?`: ${i.errors.base}`:""}`)}},{kind:"method",key:"_pickOrCreatePipelineExists",value:async function(){if(!this._localStt?.length||!this._localTts?.length)return;const e=await(0,h.SC)(this.hass);e.preferred_pipeline&&e.pipelines.sort((t=>t.id===e.preferred_pipeline?-1:0));const t=this._localTts.map((e=>e.entity_id)),i=this._localStt.map((e=>e.entity_id));let s=e.pipelines.find((e=>"conversation.home_assistant"===e.conversation_engine&&e.tts_engine&&t.includes(e.tts_engine)&&e.stt_engine&&i.includes(e.stt_engine)&&e.language.split("-")[0]===this.language.split("-")[0]));s||(s=await this._createPipeline(this._localTts[0].entity_id,this._localStt[0].entity_id)),await this.hass.callService("select","select_option",{option:s.name},{entity_id:this.assistConfiguration?.pipeline_entity_id}),this._nextStep()}},{kind:"method",key:"_createPipeline",value:async function(e,t){const i=await(0,h.SC)(this.hass),s=(await(0,b.rM)(this.hass,this.language||this.hass.config.language,this.hass.config.country||void 0)).agents.find((e=>"conversation.home_assistant"===e.id));if(!s?.supported_languages.length)throw new Error("Conversation agent does not support requested language.");const a=(await(0,f.Wg)(this.hass,this.language,this.hass.config.country||void 0)).providers.find((t=>t.engine_id===e));if(!a?.supported_languages?.length)throw new Error("TTS engine does not support requested language.");const n=await(0,f.MV)(this.hass,e,a.supported_languages[0]);if(!n.voices?.length)throw new Error("No voice available for requested language.");const o=(await(0,v.m)(this.hass,this.language,this.hass.config.country||void 0)).providers.find((e=>e.engine_id===t));if(!o?.supported_languages?.length)throw new Error("STT engine does not support requested language.");let l=this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.${this.localOption}_pipeline`),r=1;for(;i.pipelines.find((e=>e.name===l));)l=`${this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.local.${this.localOption}_pipeline`)} ${r}`,r++;return(0,h.jZ)(this.hass,{name:l,language:this.language.split("-")[0],conversation_engine:"conversation.home_assistant",conversation_language:s.supported_languages[0],stt_engine:t,stt_language:o.supported_languages[0],tts_engine:e,tts_language:a.supported_languages[0],tts_voice:n.voices[0].voice_id,wake_word_entity:null,wake_word_id:null})}},{kind:"method",key:"_findEntitiesAndCreatePipeline",value:async function(e=0){if(await this._findLocalEntities(),!this._localTts?.length||!this._localStt?.length){if(e>3)throw new Error(this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.local.errors.could_not_find_entities"));return await new Promise((e=>{setTimeout(e,2e3)})),this._findEntitiesAndCreatePipeline(e+1)}const t=await this._createPipeline(this._localTts[0].entity_id,this._localStt[0].entity_id);await this.hass.callService("select","select_option",{option:t.name},{entity_id:this.assistConfiguration?.pipeline_entity_id}),this._nextStep()}},{kind:"field",static:!0,key:"styles",value(){return[k._,n.iv`
      ha-spinner {
        margin-top: 24px;
        margin-bottom: 24px;
      }
    `]}}]}}),n.oi);t()}catch($){t($)}}))},17802:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(27486),r=i(49672),d=i(11297),c=i(79575),h=i(46784),u=(i(41141),i(4855)),p=i(3079),g=i(31762),v=i(52829),f=i(421),_=i(42717),y=i(66738),k=i(26205),m=e([h,y]);[h,y]=m.then?(await m)():m;const b=["cloud","focused_local","full_local"],w={cloud:0,focused_local:0,full_local:0};(0,s.Z)([(0,o.Mo)("ha-voice-assistant-setup-step-pipeline")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistConfiguration",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"deviceId",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistEntityId",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"language",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"languages",value(){return[]}},{kind:"field",decorators:[(0,o.SB)()],key:"_cloudChecked",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_value",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_languageScores",value:void 0},{kind:"method",key:"willUpdate",value:function(e){if((0,a.Z)(i,"willUpdate",this,3)([e]),this.hasUpdated||this._fetchData(),(e.has("language")||e.has("_languageScores"))&&this.language&&this._languageScores){const e=this.language;this._value&&0===this._languageScores[e]?.[this._value]&&(this._value=void 0),this._value||(this._value=this._getOptions(this._languageScores[e]||w,this.hass.localize).supportedOptions[0]?.value)}}},{kind:"field",key:"_getOptions",value(){return(0,l.Z)(((e,t)=>{const i=[],s=[];return b.forEach((a=>{e[a]>0?i.push({label:t(`ui.panel.config.voice_assistants.satellite_wizard.pipeline.options.${a}.label`),description:t(`ui.panel.config.voice_assistants.satellite_wizard.pipeline.options.${a}.description`),value:a}):s.push({label:t(`ui.panel.config.voice_assistants.satellite_wizard.pipeline.options.${a}.label`),value:a})})),{supportedOptions:i,unsupportedOptions:s}}))}},{kind:"method",key:"render",value:function(){if(!this._cloudChecked||!this._languageScores)return n.Ld;if(!this.language){const e=(0,h.u)(this.hass.config.language,this.hass.locale);return n.dy`<div class="content">
        <h1>
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.unsupported_language.header")}
        </h1>
        ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.unsupported_language.secondary",{language:e})}
        <ha-language-picker
          .hass=${this.hass}
          .label=${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.unsupported_language.language_picker")}
          .languages=${this.languages}
          @value-changed=${this._languageChanged}
        ></ha-language-picker>

        <a
          href=${(0,k.R)(this.hass,"/voice_control/contribute-voice/")}
          >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.unsupported_language.contribute",{language:e})}</a
        >
      </div>`}const e=this._languageScores[this.language]||w,t=this._getOptions(e,this.hass.localize),i=this._value?"full_local"===this._value?"low":"high":"",s=this._value?e[this._value]>2?"high":e[this._value]>1?"ready":e[this._value]>0?"low":"":"";return n.dy`<div class="content">
        <h1>
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.title")}
        </h1>
        <div class="bar-header">
          <span
            >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.performance.header")}</span
          ><span
            >${i?this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.pipeline.performance.${i}`):""}</span
          >
        </div>
        <div class="perf-bar ${i}">
          <div class="segment"></div>
          <div class="segment"></div>
          <div class="segment"></div>
        </div>
        <div class="bar-header">
          <span
            >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.commands.header")}</span
          ><span
            >${s?this.hass.localize(`ui.panel.config.voice_assistants.satellite_wizard.pipeline.commands.${s}`):""}</span
          >
        </div>
        <div class="perf-bar ${s}">
          <div class="segment"></div>
          <div class="segment"></div>
          <div class="segment"></div>
        </div>
        <ha-select-box
          max_columns="1"
          .options=${t.supportedOptions}
          .value=${this._value}
          @value-changed=${this._valueChanged}
        ></ha-select-box>
        ${t.unsupportedOptions.length?n.dy`<h3>
                ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.pipeline.unsupported")}
              </h3>
              <ha-select-box
                max_columns="1"
                .options=${t.unsupportedOptions}
                disabled
              ></ha-select-box>`:n.Ld}
      </div>
      <div class="footer">
        <ha-button
          @click=${this._createPipeline}
          unelevated
          .disabled=${!this._value}
          >${this.hass.localize("ui.common.next")}</ha-button
        >
      </div>`}},{kind:"method",key:"_fetchData",value:async function(){await this._hasCloud()&&await this._createCloudPipeline(!1)||(this._cloudChecked=!0,this._languageScores=(await(0,g.KH)(this.hass)).languages)}},{kind:"method",key:"_hasCloud",value:async function(){if(!(0,r.p)(this.hass,"cloud"))return!1;const e=await(0,p.LI)(this.hass);return!(!e.logged_in||!e.active_subscription)}},{kind:"method",key:"_createCloudPipeline",value:async function(e){let t,i;for(const a of Object.values(this.hass.entities))if("cloud"===a.platform){const e=(0,c.M)(a.entity_id);if("tts"===e)t=a.entity_id;else{if("stt"!==e)continue;i=a.entity_id}if(t&&i)break}try{const s=await(0,u.SC)(this.hass);s.preferred_pipeline&&s.pipelines.sort((e=>e.id===s.preferred_pipeline?-1:0));let a=s.pipelines.find((s=>"conversation.home_assistant"===s.conversation_engine&&s.tts_engine===t&&s.stt_engine===i&&(!e||s.language.split("-")[0]===this.language.split("-")[0])));if(!a){const e=(await(0,g.rM)(this.hass,this.language||this.hass.config.language,this.hass.config.country||void 0)).agents.find((e=>"conversation.home_assistant"===e.id));if(!e?.supported_languages.length)return!1;const n=(await(0,f.Wg)(this.hass,this.language||this.hass.config.language,this.hass.config.country||void 0)).providers.find((e=>e.engine_id===t));if(!n?.supported_languages?.length)return!1;const o=await(0,f.MV)(this.hass,t,n.supported_languages[0]),l=(await(0,v.m)(this.hass,this.language||this.hass.config.language,this.hass.config.country||void 0)).providers.find((e=>e.engine_id===i));if(!l?.supported_languages?.length)return!1;let r="Home Assistant Cloud",d=1;for(;s.pipelines.find((e=>e.name===r));)r=`Home Assistant Cloud ${d}`,d++;a=await(0,u.jZ)(this.hass,{name:r,language:(this.language||this.hass.config.language).split("-")[0],conversation_engine:"conversation.home_assistant",conversation_language:e.supported_languages[0],stt_engine:i,stt_language:l.supported_languages[0],tts_engine:t,tts_language:n.supported_languages[0],tts_voice:o.voices[0].voice_id,wake_word_entity:null,wake_word_id:null})}return await this.hass.callService("select","select_option",{option:a.name},{entity_id:this.assistConfiguration?.pipeline_entity_id}),(0,d.B)(this,"next-step",{step:y.STEP.SUCCESS,noPrevious:!0}),!0}catch(s){return!1}}},{kind:"method",key:"_valueChanged",value:function(e){this._value=e.detail.value}},{kind:"method",key:"_setupCloud",value:async function(){await this._hasCloud()?this._createCloudPipeline(!0):(0,d.B)(this,"next-step",{step:y.STEP.CLOUD})}},{kind:"method",key:"_createPipeline",value:function(){"cloud"===this._value?this._setupCloud():"focused_local"===this._value?this._setupLocalFocused():this._setupLocalFull()}},{kind:"method",key:"_setupLocalFocused",value:function(){(0,d.B)(this,"next-step",{step:y.STEP.LOCAL,option:this._value})}},{kind:"method",key:"_setupLocalFull",value:function(){(0,d.B)(this,"next-step",{step:y.STEP.LOCAL,option:this._value})}},{kind:"method",key:"_languageChanged",value:function(e){e.detail.value&&(0,d.B)(this,"language-changed",{value:e.detail.value})}},{kind:"field",static:!0,key:"styles",value(){return[_._,n.iv`
      :host {
        text-align: left;
      }
      .perf-bar {
        width: 100%;
        height: 10px;
        display: flex;
        gap: 4px;
        margin: 8px 0;
      }
      .segment {
        flex-grow: 1;
        background-color: var(--disabled-color);
        transition: background-color 0.3s;
      }
      .segment:first-child {
        border-radius: 4px 0 0 4px;
      }
      .segment:last-child {
        border-radius: 0 4px 4px 0;
      }
      .perf-bar.high .segment {
        background-color: var(--success-color);
      }
      .perf-bar.ready .segment:nth-child(-n + 2) {
        background-color: var(--warning-color);
      }
      .perf-bar.low .segment:nth-child(1) {
        background-color: var(--error-color);
      }
      .bar-header {
        display: flex;
        justify-content: space-between;
        margin: 8px 0;
        margin-top: 16px;
      }
      ha-select-box {
        display: block;
      }
      ha-select-box:first-of-type {
        margin-top: 32px;
      }
      .footer {
        margin-top: 16px;
      }
      ha-language-picker {
        display: block;
        margin-top: 16px;
        margin-bottom: 16px;
      }
    `]}}]}}),n.oi);t()}catch(b){t(b)}}))},59487:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(11297),r=i(81036),d=(i(58130),i(27556),i(4855)),c=i(80495),h=i(3079),u=i(44074),p=i(93942),g=i(4264),v=i(42717),f=i(66738),_=i(85128),y=e([g,f]);[g,f]=y.then?(await y)():y;const k="M12,15.5A3.5,3.5 0 0,1 8.5,12A3.5,3.5 0 0,1 12,8.5A3.5,3.5 0 0,1 15.5,12A3.5,3.5 0 0,1 12,15.5M19.43,12.97C19.47,12.65 19.5,12.33 19.5,12C19.5,11.67 19.47,11.34 19.43,11L21.54,9.37C21.73,9.22 21.78,8.95 21.66,8.73L19.66,5.27C19.54,5.05 19.27,4.96 19.05,5.05L16.56,6.05C16.04,5.66 15.5,5.32 14.87,5.07L14.5,2.42C14.46,2.18 14.25,2 14,2H10C9.75,2 9.54,2.18 9.5,2.42L9.13,5.07C8.5,5.32 7.96,5.66 7.44,6.05L4.95,5.05C4.73,4.96 4.46,5.05 4.34,5.27L2.34,8.73C2.21,8.95 2.27,9.22 2.46,9.37L4.57,11C4.53,11.34 4.5,11.67 4.5,12C4.5,12.33 4.53,12.65 4.57,12.97L2.46,14.63C2.27,14.78 2.21,15.05 2.34,15.27L4.34,18.73C4.46,18.95 4.73,19.03 4.95,18.95L7.44,17.94C7.96,18.34 8.5,18.68 9.13,18.93L9.5,21.58C9.54,21.82 9.75,22 10,22H14C14.25,22 14.46,21.82 14.5,21.58L14.87,18.93C15.5,18.67 16.04,18.34 16.56,17.94L19.05,18.95C19.27,19.03 19.54,18.95 19.66,18.73L21.66,15.27C21.78,15.05 21.73,14.78 21.54,14.63L19.43,12.97Z",m="M12,2A3,3 0 0,1 15,5V11A3,3 0 0,1 12,14A3,3 0 0,1 9,11V5A3,3 0 0,1 12,2M19,11C19,14.53 16.39,17.44 13,17.93V21H11V17.93C7.61,17.44 5,14.53 5,11H7A5,5 0 0,0 12,16A5,5 0 0,0 17,11H19Z",b="M8,5.14V19.14L19,12.14L8,5.14Z";(0,s.Z)([(0,o.Mo)("ha-voice-assistant-setup-step-success")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistConfiguration",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"deviceId",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistEntityId",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_ttsSettings",value:void 0},{kind:"method",key:"willUpdate",value:function(e){if((0,a.Z)(i,"willUpdate",this,3)([e]),e.has("assistConfiguration"))this._setTtsSettings();else if(e.has("hass")&&this.assistConfiguration){const t=e.get("hass");if(t){const e=t.states[this.assistConfiguration.pipeline_entity_id],i=this.hass.states[this.assistConfiguration.pipeline_entity_id];e.state!==i.state&&this._setTtsSettings()}}}},{kind:"method",key:"render",value:function(){const e=this.assistConfiguration?this.hass.states[this.assistConfiguration.pipeline_entity_id]:void 0;return n.dy`<div class="content">
        <img
          src="/static/images/voice-assistant/heart.png"
          alt="Casita Home Assistant logo"
        />
        <h1>
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.success.title")}
        </h1>
        <p class="secondary">
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.success.secondary")}
        </p>
        <div class="rows">
          ${this.assistConfiguration&&this.assistConfiguration.available_wake_words.length>1?n.dy`<div class="row">
                <ha-select
                  .label=${"Wake word"}
                  @closed=${r.U}
                  fixedMenuPosition
                  naturalMenuWidth
                  .value=${this.assistConfiguration.active_wake_words[0]}
                  @selected=${this._wakeWordPicked}
                >
                  ${this.assistConfiguration.available_wake_words.map((e=>n.dy`<ha-list-item .value=${e.id}>
                        ${e.wake_word}
                      </ha-list-item>`))}
                </ha-select>
                <ha-button @click=${this._testWakeWord}>
                  <ha-svg-icon slot="icon" .path=${m}></ha-svg-icon>
                  Test
                </ha-button>
              </div>`:n.Ld}
          ${e?n.dy`<div class="row">
                <ha-select
                  .label=${"Assistant"}
                  @closed=${r.U}
                  .value=${e?.state}
                  fixedMenuPosition
                  naturalMenuWidth
                  @selected=${this._pipelinePicked}
                >
                  ${e?.attributes.options.map((t=>n.dy`<ha-list-item .value=${t}>
                        ${this.hass.formatEntityState(e,t)}
                      </ha-list-item>`))}
                </ha-select>
                <ha-button @click=${this._openPipeline}>
                  <ha-svg-icon slot="icon" .path=${k}></ha-svg-icon>
                  Edit
                </ha-button>
              </div>`:n.Ld}
          ${this._ttsSettings?n.dy`<div class="row">
                <ha-tts-voice-picker
                  .hass=${this.hass}
                  .engineId=${this._ttsSettings.engine}
                  .language=${this._ttsSettings.language}
                  .value=${this._ttsSettings.voice}
                  @value-changed=${this._voicePicked}
                  @closed=${r.U}
                ></ha-tts-voice-picker>
                <ha-button @click=${this._testTts}>
                  <ha-svg-icon slot="icon" .path=${b}></ha-svg-icon>
                  Try
                </ha-button>
              </div>`:n.Ld}
        </div>
      </div>
      <div class="footer">
        <ha-button @click=${this._close} unelevated>Done</ha-button>
      </div>`}},{kind:"method",key:"_getPipeline",value:async function(){if(!this.assistConfiguration?.pipeline_entity_id)return[void 0,void 0];const e=this.hass.states[this.assistConfiguration?.pipeline_entity_id].state,t=await(0,d.SC)(this.hass);let i;return i="preferred"===e?t.pipelines.find((e=>e.id===t.preferred_pipeline)):t.pipelines.find((t=>t.name===e)),[i,t.preferred_pipeline]}},{kind:"method",key:"_wakeWordPicked",value:async function(e){const t=e.target.value;await(0,c.DT)(this.hass,this.assistEntityId,[t])}},{kind:"method",key:"_pipelinePicked",value:function(e){const t=this.hass.states[this.assistConfiguration.pipeline_entity_id],i=e.target.value;i!==t.state&&t.attributes.options.includes(i)&&(0,u.n)(this.hass,t.entity_id,i)}},{kind:"method",key:"_setTtsSettings",value:async function(){const[e]=await this._getPipeline();this._ttsSettings=e?{engine:e.tts_engine,voice:e.tts_voice,language:e.tts_language}:void 0}},{kind:"method",key:"_voicePicked",value:async function(e){const[t]=await this._getPipeline();t&&await(0,d.af)(this.hass,t.id,{...t,tts_voice:e.detail.value})}},{kind:"method",key:"_testTts",value:async function(){const[e]=await this._getPipeline();if(e){if(e.language!==this.hass.locale.language)try{const t=await(0,_.i0)(null,e.language,!1);return void this._announce(t.data["ui.dialogs.tts-try.message_example"])}catch(t){}this._announce(this.hass.localize("ui.dialogs.tts-try.message_example"))}}},{kind:"method",key:"_announce",value:async function(e){this.assistEntityId&&await(0,c.SY)(this.hass,this.assistEntityId,{message:e,preannounce_media_id:null})}},{kind:"method",key:"_testWakeWord",value:function(){(0,l.B)(this,"next-step",{step:f.STEP.WAKEWORD,nextStep:f.STEP.SUCCESS,updateConfig:!0})}},{kind:"method",key:"_openPipeline",value:async function(){const[e]=await this._getPipeline();if(!e)return;const t=await(0,h.LI)(this.hass);(0,p.t)(this,{cloudActiveSubscription:t.logged_in&&t.active_subscription,pipeline:e,updatePipeline:async t=>{await(0,d.af)(this.hass,e.id,t)},hideWakeWord:!0})}},{kind:"method",key:"_close",value:function(){(0,l.B)(this,"closed")}},{kind:"field",static:!0,key:"styles",value(){return[v._,n.iv`
      ha-md-list-item {
        text-align: initial;
      }
      ha-tts-voice-picker {
        display: block;
      }
      .footer {
        margin-top: 24px;
      }
      .rows {
        gap: 16px;
        display: flex;
        flex-direction: column;
      }
      .row {
        display: flex;
        justify-content: space-between;
        align-items: center;
      }
      .row > *:first-child {
        flex: 1;
        margin-right: 4px;
      }
      .row ha-button {
        width: 82px;
      }
    `]}}]}}),n.oi);t()}catch(k){t(k)}}))},22467:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(11297),r=i(93644),d=i(19537),c=i(36719),h=i(57566),u=i(42717),p=e([r,d,h]);[r,d,h]=p.then?(await p)():p;(0,s.Z)([(0,o.Mo)("ha-voice-assistant-setup-step-update")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"updateEntityId",value:void 0},{kind:"field",key:"_updated",value(){return!1}},{kind:"field",key:"_refreshTimeout",value:void 0},{kind:"method",key:"willUpdate",value:function(e){if((0,a.Z)(i,"willUpdate",this,3)([e]),this.updateEntityId){if(e.has("hass")&&this.updateEntityId){const t=e.get("hass");if(t){const e=t.states[this.updateEntityId],i=this.hass.states[this.updateEntityId];if(e?.state===c.nZ&&i?.state!==c.nZ||e?.state!==c.ON&&i?.state===c.ON)return void this._tryUpdate(!1)}}e.has("updateEntityId")&&this._tryUpdate(!0)}else this._nextStep()}},{kind:"method",key:"render",value:function(){if(!this.updateEntityId||!(this.updateEntityId in this.hass.states))return n.Ld;const e=this.hass.states[this.updateEntityId],t=e&&(0,h.SO)(e);return n.dy`<div class="content">
      <img
        src="/static/images/voice-assistant/update.png"
        alt="Casita Home Assistant loading logo"
      />
      <h1>
        ${e&&("unavailable"===e.state||(0,h.Sk)(e))?this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.update.title"):this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.update.checking")}
      </h1>
      <p class="secondary">
        ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.update.secondary")}
      </p>
      ${t?n.dy`
            <ha-progress-ring
              .value=${e.attributes.update_percentage}
            ></ha-progress-ring>
          `:n.dy`<ha-spinner></ha-spinner>`}
      <p>
        ${e?.state===c.nZ?"Restarting voice assistant":t?`Installing ${e.attributes.update_percentage}%`:""}
      </p>
    </div>`}},{kind:"method",key:"_tryUpdate",value:async function(e){if(clearTimeout(this._refreshTimeout),!this.updateEntityId)return;const t=this.hass.states[this.updateEntityId];t&&this.hass.states[t.entity_id].state===c.ON&&(0,h.hF)(t)?(this._updated=!0,await this.hass.callService("update","install",{},{entity_id:t.entity_id})):e?(await this.hass.callService("homeassistant","update_entity",{},{entity_id:this.updateEntityId}),this._refreshTimeout=window.setTimeout((()=>{this._nextStep()}),5e3)):this._nextStep()}},{kind:"method",key:"_nextStep",value:function(){(0,l.B)(this,"next-step",{noPrevious:!0,updateConfig:this._updated})}},{kind:"field",static:!0,key:"styles",value(){return[u._,n.iv`
      ha-progress-ring,
      ha-spinner {
        margin-top: 24px;
        margin-bottom: 24px;
      }
    `]}}]}}),n.oi);t()}catch(g){t(g)}}))},34315:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(27486),r=i(11297),d=(i(20095),i(19537)),c=(i(28906),i(80495)),h=i(42717),u=i(66738),p=i(79575),g=e([d,u]);[d,u]=g.then?(await g)():g;(0,s.Z)([(0,o.Mo)("ha-voice-assistant-setup-step-wake-word")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistConfiguration",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"assistEntityId",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"deviceEntities",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_muteSwitchEntity",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_detected",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_timedout",value(){return!1}},{kind:"field",key:"_sub",value:void 0},{kind:"field",key:"_timeout",value:void 0},{kind:"method",key:"disconnectedCallback",value:function(){(0,a.Z)(i,"disconnectedCallback",this,3)([]),this._stopListeningWakeWord()}},{kind:"method",key:"willUpdate",value:function(e){(0,a.Z)(i,"willUpdate",this,3)([e]),e.has("assistConfiguration")&&this.assistConfiguration&&!this.assistConfiguration.available_wake_words.length&&this._nextStep(),e.has("assistEntityId")&&(this._detected=!1,this._muteSwitchEntity=this.deviceEntities?.find((e=>"switch"===(0,p.M)(e.entity_id)&&e.entity_id.includes("mute")))?.entity_id,this._muteSwitchEntity||this._startTimeOut(),this._listenWakeWord())}},{kind:"method",key:"_startTimeOut",value:function(){this._timeout=window.setTimeout((()=>{this._timeout=void 0,this._timedout=!0}),15e3)}},{kind:"field",key:"_activeWakeWord",value(){return(0,l.Z)((e=>{if(!e)return"";const t=e.active_wake_words[0];return e.available_wake_words.find((e=>e.id===t))?.wake_word}))}},{kind:"method",key:"render",value:function(){if(!this.assistEntityId)return n.Ld;return"idle"!==this.hass.states[this.assistEntityId].state?n.dy`<ha-spinner></ha-spinner>`:n.dy`<div class="content">
        ${this._detected?n.dy`<img
                src="/static/images/voice-assistant/ok-nabu.png"
                alt="Casita Home Assistant logo"
              />
              <h1>
                ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.title_2",{wakeword:this._activeWakeWord(this.assistConfiguration)})}
              </h1>
              <p class="secondary">
                ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.secondary_2")}
              </p>`:n.dy`
          <img src="/static/images/voice-assistant/sleep.png" alt="Casita Home Assistant logo"/>
          <h1>
          ${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.title",{wakeword:this._activeWakeWord(this.assistConfiguration)})}  
          </h1>
          <p class="secondary">${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.secondary")}</p>
        </div>`}
        ${this._timedout?n.dy`<ha-alert alert-type="warning"
              >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.time_out")}</ha-alert
            >`:this._muteSwitchEntity&&"on"===this.hass.states[this._muteSwitchEntity].state?n.dy`<ha-alert
                alert-type="warning"
                .title=${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.muted")}
                >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.muted_description")}</ha-alert
              >`:n.Ld}
      </div>
      ${this.assistConfiguration&&this.assistConfiguration.available_wake_words.length>1?n.dy`<div class="footer centered">
            <ha-button @click=${this._changeWakeWord}
              >${this.hass.localize("ui.panel.config.voice_assistants.satellite_wizard.wake_word.change_wake_word")}</ha-button
            >
          </div>`:n.Ld}`}},{kind:"method",key:"_listenWakeWord",value:async function(){const e=this.assistEntityId;e&&(await this._stopListeningWakeWord(),this._sub=(0,c.aJ)(this.hass,e,(()=>{this._timedout=!1,clearTimeout(this._timeout),this._stopListeningWakeWord(),this._detected?this._nextStep():(this._detected=!0,this._listenWakeWord())})))}},{kind:"method",key:"_stopListeningWakeWord",value:async function(){try{(await this._sub)?.()}catch(e){}this._sub=void 0}},{kind:"method",key:"_nextStep",value:function(){(0,r.B)(this,"next-step")}},{kind:"method",key:"_changeWakeWord",value:function(){(0,r.B)(this,"next-step",{step:u.STEP.CHANGE_WAKEWORD})}},{kind:"field",static:!0,key:"styles",value(){return h._}}]}}),n.oi);t()}catch(v){t(v)}}))},93942:function(e,t,i){i.d(t,{t:()=>n});var s=i(11297);const a=()=>i.e("9329").then(i.bind(i,26942)),n=(e,t)=>{(0,s.B)(e,"show-dialog",{dialogTag:"dialog-voice-assistant-pipeline-detail",dialogImport:a,dialogParams:t})}},74910:function(e,t,i){i.d(t,{K:()=>c});var s=i(57243),a=i(45779),n=i(11297),o=i(68061),l=i(21234);class r extends HTMLElement{constructor(...e){super(...e),this.holdTime=500,this.timer=void 0,this.held=!1,this.cancelled=!1,this.dblClickTimeout=void 0}connectedCallback(){Object.assign(this.style,{position:"fixed",width:l.T?"100px":"50px",height:l.T?"100px":"50px",transform:"translate(-50%, -50%) scale(0)",pointerEvents:"none",zIndex:"999",background:"var(--primary-color)",display:null,opacity:"0.2",borderRadius:"50%",transition:"transform 180ms ease-in-out"}),["touchcancel","mouseout","mouseup","touchmove","mousewheel","wheel","scroll"].forEach((e=>{document.addEventListener(e,(()=>{this.cancelled=!0,this.timer&&(this._stopAnimation(),clearTimeout(this.timer),this.timer=void 0)}),{passive:!0})}))}bind(e,t={}){e.actionHandler&&(0,o.v)(t,e.actionHandler.options)||(e.actionHandler?(e.removeEventListener("touchstart",e.actionHandler.start),e.removeEventListener("touchend",e.actionHandler.end),e.removeEventListener("touchcancel",e.actionHandler.end),e.removeEventListener("mousedown",e.actionHandler.start),e.removeEventListener("click",e.actionHandler.end),e.removeEventListener("keydown",e.actionHandler.handleKeyDown)):e.addEventListener("contextmenu",(e=>{const t=e||window.event;return t.preventDefault&&t.preventDefault(),t.stopPropagation&&t.stopPropagation(),t.cancelBubble=!0,t.returnValue=!1,!1})),e.actionHandler={options:t},t.disabled||(e.actionHandler.start=e=>{let i,s;this.cancelled=!1,e.touches?(i=e.touches[0].clientX,s=e.touches[0].clientY):(i=e.clientX,s=e.clientY),t.hasHold&&(this.held=!1,this.timer=window.setTimeout((()=>{this._startAnimation(i,s),this.held=!0}),this.holdTime))},e.actionHandler.end=e=>{if("touchcancel"===e.type||"touchend"===e.type&&this.cancelled)return;const i=e.target;e.cancelable&&e.preventDefault(),t.hasHold&&(clearTimeout(this.timer),this._stopAnimation(),this.timer=void 0),t.hasHold&&this.held?(0,n.B)(i,"action",{action:"hold"}):t.hasDoubleClick?"click"===e.type&&e.detail<2||!this.dblClickTimeout?this.dblClickTimeout=window.setTimeout((()=>{this.dblClickTimeout=void 0,(0,n.B)(i,"action",{action:"tap"})}),250):(clearTimeout(this.dblClickTimeout),this.dblClickTimeout=void 0,(0,n.B)(i,"action",{action:"double_tap"})):(0,n.B)(i,"action",{action:"tap"})},e.actionHandler.handleKeyDown=e=>{["Enter"," "].includes(e.key)&&e.currentTarget.actionHandler.end(e)},e.addEventListener("touchstart",e.actionHandler.start,{passive:!0}),e.addEventListener("touchend",e.actionHandler.end),e.addEventListener("touchcancel",e.actionHandler.end),e.addEventListener("mousedown",e.actionHandler.start,{passive:!0}),e.addEventListener("click",e.actionHandler.end),e.addEventListener("keydown",e.actionHandler.handleKeyDown)))}_startAnimation(e,t){Object.assign(this.style,{left:`${e}px`,top:`${t}px`,transform:"translate(-50%, -50%) scale(1)"})}_stopAnimation(){Object.assign(this.style,{left:null,top:null,transform:"translate(-50%, -50%) scale(0)"})}}customElements.define("action-handler",r);const d=(e,t)=>{const i=(()=>{const e=document.body;if(e.querySelector("action-handler"))return e.querySelector("action-handler");const t=document.createElement("action-handler");return e.appendChild(t),t})();i&&i.bind(e,t)},c=(0,a.XM)(class extends a.Xe{update(e,[t]){return d(e.element,t),s.Jb}render(e){}})},24874:function(e,t,i){i.d(t,{G:()=>p});var s=i(11297),a=i(64364),n=i(26610),o=i(1275),l=i(4557);const r=()=>i.e("1261").then(i.bind(i,46915));var d=i(46694),c=i(24963),h=i(79575);const u=(e,t)=>((e,t,i=!0)=>{const s=(0,h.M)(t),a="group"===s?"homeassistant":s;let n;switch(s){case"lock":n=i?"unlock":"lock";break;case"cover":n=i?"open_cover":"close_cover";break;case"button":case"input_button":n="press";break;case"scene":n="turn_on";break;case"valve":n=i?"open_valve":"close_valve";break;default:n=i?"turn_on":"turn_off"}return e.callService(a,n,{entity_id:t})})(e,t,c.tj.includes(e.states[t].state)),p=async(e,t,i,c)=>{let h;if("double_tap"===c&&i.double_tap_action?h=i.double_tap_action:"hold"===c&&i.hold_action?h=i.hold_action:"tap"===c&&i.tap_action&&(h=i.tap_action),h||(h={action:"more-info"}),h.confirmation&&(!h.confirmation.exemptions||!h.confirmation.exemptions.some((e=>e.user===t.user?.id)))){let i;if((0,n.j)("warning"),"call-service"===h.action||"perform-action"===h.action){const[e,s]=(h.perform_action||h.service).split(".",2),a=t.services;if(e in a&&s in a[e]){await t.loadBackendTranslation("title");const n=await t.loadBackendTranslation("services");i=`${(0,o.Lh)(n,e)}: ${n(`component.${e}.services.${i}.name`)||a[e][s].name||s}`}}if(!(await(0,l.g7)(e,{text:h.confirmation.text||t.localize("ui.panel.lovelace.cards.actions.action_confirmation",{action:i||t.localize(`ui.panel.lovelace.editor.action-editor.actions.${h.action}`)||h.action})})))return}switch(h.action){case"more-info":{const a=h.entity||i.entity||i.camera_image||i.image_entity;a?(0,s.B)(e,"hass-more-info",{entityId:a}):((0,d.C)(e,{message:t.localize("ui.panel.lovelace.cards.actions.no_entity_more_info")}),(0,n.j)("failure"));break}case"navigate":h.navigation_path?(0,a.c)(h.navigation_path,{replace:h.navigation_replace}):((0,d.C)(e,{message:t.localize("ui.panel.lovelace.cards.actions.no_navigation_path")}),(0,n.j)("failure"));break;case"url":h.url_path?window.open(h.url_path):((0,d.C)(e,{message:t.localize("ui.panel.lovelace.cards.actions.no_url")}),(0,n.j)("failure"));break;case"toggle":i.entity?(u(t,i.entity),(0,n.j)("light")):((0,d.C)(e,{message:t.localize("ui.panel.lovelace.cards.actions.no_entity_toggle")}),(0,n.j)("failure"));break;case"perform-action":case"call-service":{if(!h.perform_action&&!h.service)return(0,d.C)(e,{message:t.localize("ui.panel.lovelace.cards.actions.no_action")}),void(0,n.j)("failure");const[i,s]=(h.perform_action||h.service).split(".",2);t.callService(i,s,h.data??h.service_data,h.target),(0,n.j)("light");break}case"assist":((e,t,i)=>{t.auth.external?.config.hasAssist?t.auth.external.fireMessage({type:"assist/show",payload:{pipeline_id:i.pipeline_id,start_listening:i.start_listening??!0}}):(0,s.B)(e,"show-dialog",{dialogTag:"ha-voice-command-dialog",dialogImport:r,dialogParams:{pipeline_id:i.pipeline_id,start_listening:i.start_listening??!1}})})(e,t,{start_listening:h.start_listening??!1,pipeline_id:h.pipeline_id??"last_used"});break;case"fire-dom-event":(0,s.B)(e,"ll-custom",h)}}},77099:function(e,t,i){function s(e){return void 0!==e&&"none"!==e.action}function a(e){return!e.tap_action||s(e.tap_action)||s(e.hold_action)||s(e.double_tap_action)}i.d(t,{_:()=>s,q:()=>a})},37876:function(e,t,i){function s(e,t){if(t.has("_config"))return!0;if(!t.has("hass"))return!1;const i=t.get("hass");return!i||(i.connected!==e.hass.connected||i.themes!==e.hass.themes||i.locale!==e.hass.locale||i.localize!==e.hass.localize||i.formatEntityState!==e.hass.formatEntityState||i.formatEntityAttributeName!==e.hass.formatEntityAttributeName||i.formatEntityAttributeValue!==e.hass.formatEntityAttributeValue||i.config.state!==e.hass.config.state)}function a(e,t,i){return e.states[i]!==t.states[i]}function n(e,t,i){const s=e.entities[i],a=t.entities[i];return s?.display_precision!==a?.display_precision}function o(e,t){if(s(e,t))return!0;if(!t.has("hass"))return!1;const i=t.get("hass"),o=e.hass;return a(i,o,e._config.entity)||n(i,o,e._config.entity)}i.d(t,{G2:()=>o})},69546:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=i(72621),n=i(57243),o=i(50778),l=i(35359),r=i(20552),d=i(24963),c=i(29332),h=i(79575),u=i(73525),p=i(21881),g=i(44315),v=i(74910),f=i(24874),_=i(77099),y=i(32545),k=e([p,g]);[p,g]=k.then?(await k)():k;(0,s.Z)([(0,o.Mo)("hui-generic-entity-row")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"config",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:"secondary-text"})],key:"secondaryText",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:"hide-name",type:Boolean})],key:"hideName",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({attribute:"catch-interaction",type:Boolean})],key:"catchInteraction",value:void 0},{kind:"method",key:"render",value:function(){if(!this.hass||!this.config)return n.Ld;const e=this.config.entity?this.hass.states[this.config.entity]:void 0;if(!e)return n.dy`
        <hui-warning>
          ${(0,y.i)(this.hass,this.config.entity)}
        </hui-warning>
      `;const t=(0,h.M)(this.config.entity),i=(0,_.q)(this.config),s=this.secondaryText||this.config.secondary_info,a=this.config.name??(0,u.C)(e);return n.dy`
      <state-badge
        class=${(0,l.$)({pointer:i})}
        .hass=${this.hass}
        .stateObj=${e}
        .overrideIcon=${this.config.icon}
        .overrideImage=${this.config.image}
        .stateColor=${this.config.state_color}
        @action=${this._handleAction}
        .actionHandler=${(0,v.K)({hasHold:(0,_._)(this.config.hold_action),hasDoubleClick:(0,_._)(this.config.double_tap_action)})}
        tabindex=${(0,r.o)(!this.config.tap_action||(0,_._)(this.config.tap_action)?"0":void 0)}
      ></state-badge>
      ${this.hideName?n.Ld:n.dy`<div
            class="info ${(0,l.$)({pointer:i,"text-content":!s})}"
            @action=${this._handleAction}
            .actionHandler=${(0,v.K)({hasHold:(0,_._)(this.config.hold_action),hasDoubleClick:(0,_._)(this.config.double_tap_action)})}
            .title=${a}
          >
            ${this.config.name||(0,u.C)(e)}
            ${s?n.dy`
                  <div class="secondary">
                    ${this.secondaryText||("entity-id"===this.config.secondary_info?e.entity_id:"last-changed"===this.config.secondary_info?n.dy`
                            <ha-relative-time
                              .hass=${this.hass}
                              .datetime=${e.last_changed}
                              capitalize
                            ></ha-relative-time>
                          `:"last-updated"===this.config.secondary_info?n.dy`
                              <ha-relative-time
                                .hass=${this.hass}
                                .datetime=${e.last_updated}
                                capitalize
                              ></ha-relative-time>
                            `:"last-triggered"===this.config.secondary_info?e.attributes.last_triggered?n.dy`
                                  <ha-relative-time
                                    .hass=${this.hass}
                                    .datetime=${e.attributes.last_triggered}
                                    capitalize
                                  ></ha-relative-time>
                                `:this.hass.localize("ui.panel.lovelace.cards.entities.never_triggered"):"position"===this.config.secondary_info&&void 0!==e.attributes.current_position?`${this.hass.localize("ui.card.cover.position")}: ${e.attributes.current_position}`:"tilt-position"===this.config.secondary_info&&void 0!==e.attributes.current_tilt_position?`${this.hass.localize("ui.card.cover.tilt_position")}: ${e.attributes.current_tilt_position}`:"brightness"===this.config.secondary_info&&e.attributes.brightness?n.dy`${Math.round(e.attributes.brightness/255*100)}
                                    %`:"")}
                  </div>
                `:""}
          </div>`}
      ${this.catchInteraction??!d.AF.includes(t)?n.dy`<div
            class="text-content value ${(0,l.$)({pointer:i})}"
            @action=${this._handleAction}
            .actionHandler=${(0,v.K)({hasHold:(0,_._)(this.config.hold_action),hasDoubleClick:(0,_._)(this.config.double_tap_action)})}
          >
            <div class="state"><slot></slot></div>
          </div>`:n.dy`<slot></slot>`}
    `}},{kind:"method",key:"updated",value:function(e){(0,a.Z)(i,"updated",this,3)([e]),(0,c.X)(this,"no-secondary",!this.secondaryText&&!this.config?.secondary_info)}},{kind:"method",key:"_handleAction",value:function(e){(0,f.G)(this,this.hass,this.config,e.detail.action)}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    :host {
      display: flex;
      align-items: center;
      flex-direction: row;
    }
    .info {
      padding-left: 16px;
      padding-right: 8px;
      padding-inline-start: 16px;
      padding-inline-end: 8px;
      flex: 1 1 30%;
    }
    .info,
    .info > * {
      white-space: nowrap;
      overflow: hidden;
      text-overflow: ellipsis;
    }
    .flex ::slotted(*) {
      margin-left: 8px;
      margin-inline-start: 8px;
      margin-inline-end: initial;
      min-width: 0;
    }
    .flex ::slotted([slot="secondary"]) {
      margin-left: 0;
      margin-inline-start: 0;
      margin-inline-end: initial;
    }
    .secondary,
    ha-relative-time {
      color: var(--secondary-text-color);
    }
    state-badge {
      flex: 0 0 40px;
    }
    .pointer {
      cursor: pointer;
    }
    .state {
      text-align: var(--float-end);
    }
    .value {
      direction: ltr;
    }
  `}}]}}),n.oi);t()}catch(m){t(m)}}))},32545:function(e,t,i){i.d(t,{i:()=>l});var s=i(44249),a=i(94277),n=i(57243),o=i(50778);i(17949);const l=(e,t)=>e.config.state!==a.UE?e.localize("ui.panel.lovelace.warning.entity_not_found",{entity:t||"[empty]"}):e.localize("ui.panel.lovelace.warning.starting");(0,s.Z)([(0,o.Mo)("hui-warning")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"method",key:"render",value:function(){return n.dy`<ha-alert alert-type="warning"><slot></slot></ha-alert> `}}]}}),n.oi)},4264:function(e,t,i){i.a(e,(async function(e,t){try{var s=i(44249),a=(i(87319),i(57243)),n=i(50778),o=i(81036),l=i(73525),r=(i(58130),i(36719)),d=i(26610),c=i(44074),h=i(37876),u=i(69546),p=i(32545),g=e([u]);u=(g.then?(await g)():g)[0];(0,s.Z)([(0,n.Mo)("hui-select-entity-row")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_config",value:void 0},{kind:"method",key:"setConfig",value:function(e){if(!e||!e.entity)throw new Error("Entity must be specified");this._config=e}},{kind:"method",key:"shouldUpdate",value:function(e){return(0,h.G2)(this,e)}},{kind:"method",key:"render",value:function(){if(!this.hass||!this._config)return a.Ld;const e=this.hass.states[this._config.entity];return e?a.dy`
      <hui-generic-entity-row
        .hass=${this.hass}
        .config=${this._config}
        hide-name
      >
        <ha-select
          .label=${this._config.name||(0,l.C)(e)}
          .value=${e.state}
          .options=${e.attributes.options}
          .disabled=${e.state===r.nZ}
          naturalMenuWidth
          @action=${this._handleAction}
          @click=${o.U}
          @closed=${o.U}
        >
          ${e.attributes.options?e.attributes.options.map((t=>a.dy`
                  <mwc-list-item .value=${t}>
                    ${this.hass.formatEntityState(e,t)}
                  </mwc-list-item>
                `)):""}
        </ha-select>
      </hui-generic-entity-row>
    `:a.dy`
        <hui-warning>
          ${(0,p.i)(this.hass,this._config.entity)}
        </hui-warning>
      `}},{kind:"field",static:!0,key:"styles",value(){return a.iv`
    hui-generic-entity-row {
      display: flex;
      align-items: center;
    }
    ha-select {
      width: 100%;
      --ha-select-min-width: 0;
    }
  `}},{kind:"method",key:"_handleAction",value:function(e){const t=this.hass.states[this._config.entity],i=e.target.value;i!==t.state&&t.attributes.options.includes(i)&&((0,d.j)("light"),(0,c.n)(this.hass,t.entity_id,i))}}]}}),a.oi);t()}catch(v){t(v)}}))},85019:function(e,t,i){i.d(t,{X1:()=>s,u4:()=>a,zC:()=>n});const s=e=>`https://brands.home-assistant.io/${e.brand?"brands/":""}${e.useFallback?"_/":""}${e.domain}/${e.darkOptimized?"dark_":""}${e.type}.png`,a=e=>e.split("/")[4],n=e=>e.startsWith("https://brands.home-assistant.io/")},21234:function(e,t,i){i.d(t,{T:()=>s});const s="ontouchstart"in window||navigator.maxTouchPoints>0||navigator.msMaxTouchPoints>0},46694:function(e,t,i){i.d(t,{C:()=>a});var s=i(11297);const a=(e,t)=>(0,s.B)(e,"hass-notification",t)}};
//# sourceMappingURL=3732.90a221a1a5a27270.js.map