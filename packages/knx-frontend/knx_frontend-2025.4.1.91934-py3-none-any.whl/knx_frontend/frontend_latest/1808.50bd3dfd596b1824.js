/*! For license information please see 1808.50bd3dfd596b1824.js.LICENSE.txt */
export const __webpack_ids__=["1808"];export const __webpack_modules__={43527:function(e,t,i){var o=i(44249),n=i(72621),r=(i(22997),i(57243)),a=i(50778),s=i(80155),d=i(24067);(0,o.Z)([(0,a.Mo)("ha-button-menu")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",key:d.gA,value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"corner",value(){return"BOTTOM_START"}},{kind:"field",decorators:[(0,a.Cb)({attribute:"menu-corner"})],key:"menuCorner",value(){return"START"}},{kind:"field",decorators:[(0,a.Cb)({type:Number})],key:"x",value(){return null}},{kind:"field",decorators:[(0,a.Cb)({type:Number})],key:"y",value(){return null}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"multi",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"activatable",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"fixed",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:"no-anchor"})],key:"noAnchor",value(){return!1}},{kind:"field",decorators:[(0,a.IO)("mwc-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){return this._menu?.items}},{kind:"get",key:"selected",value:function(){return this._menu?.selected}},{kind:"method",key:"focus",value:function(){this._menu?.open?this._menu.focusItemAtIndex(0):this._triggerButton?.focus()}},{kind:"method",key:"render",value:function(){return r.dy`
      <div @click=${this._handleClick}>
        <slot name="trigger" @slotchange=${this._setTriggerAria}></slot>
      </div>
      <mwc-menu
        .corner=${this.corner}
        .menuCorner=${this.menuCorner}
        .fixed=${this.fixed}
        .multi=${this.multi}
        .activatable=${this.activatable}
        .y=${this.y}
        .x=${this.x}
      >
        <slot></slot>
      </mwc-menu>
    `}},{kind:"method",key:"firstUpdated",value:function(e){(0,n.Z)(i,"firstUpdated",this,3)([e]),"rtl"===s.E.document.dir&&this.updateComplete.then((()=>{this.querySelectorAll("mwc-list-item").forEach((e=>{const t=document.createElement("style");t.innerHTML="span.material-icons:first-of-type { margin-left: var(--mdc-list-item-graphic-margin, 32px) !important; margin-right: 0px !important;}",e.shadowRoot.appendChild(t)}))}))}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchor=this.noAnchor?null:this,this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"field",static:!0,key:"styles",value(){return r.iv`
    :host {
      display: inline-block;
      position: relative;
    }
    ::slotted([disabled]) {
      color: var(--disabled-text-color);
    }
  `}}]}}),r.oi)},43685:function(e,t,i){var o=i(44249),n=i(72621),r=i(57243),a=i(9065),s=i(50778),d=i(92444),l=i(76688);let c=class extends d.A{};c.styles=[l.W],c=(0,a.__decorate)([(0,s.Mo)("mwc-checkbox")],c);var h=i(35359),m=i(65703);class u extends m.K{constructor(){super(...arguments),this.left=!1,this.graphic="control"}render(){const e={"mdc-deprecated-list-item__graphic":this.left,"mdc-deprecated-list-item__meta":!this.left},t=this.renderText(),i=this.graphic&&"control"!==this.graphic&&!this.left?this.renderGraphic():r.dy``,o=this.hasMeta&&this.left?this.renderMeta():r.dy``,n=this.renderRipple();return r.dy`
      ${n}
      ${i}
      ${this.left?"":t}
      <span class=${(0,h.$)(e)}>
        <mwc-checkbox
            reducedTouchTarget
            tabindex=${this.tabindex}
            .checked=${this.selected}
            ?disabled=${this.disabled}
            @change=${this.onChange}>
        </mwc-checkbox>
      </span>
      ${this.left?t:""}
      ${o}`}async onChange(e){const t=e.target;this.selected===t.checked||(this._skipPropRequest=!0,this.selected=t.checked,await this.updateComplete,this._skipPropRequest=!1)}}(0,a.__decorate)([(0,s.IO)("slot")],u.prototype,"slotElement",void 0),(0,a.__decorate)([(0,s.IO)("mwc-checkbox")],u.prototype,"checkboxElement",void 0),(0,a.__decorate)([(0,s.Cb)({type:Boolean})],u.prototype,"left",void 0),(0,a.__decorate)([(0,s.Cb)({type:String,reflect:!0})],u.prototype,"graphic",void 0);const p=r.iv`:host(:not([twoline])){height:56px}:host(:not([left])) .mdc-deprecated-list-item__meta{height:40px;width:40px}`;var g=i(46289),y=i(11297);(0,o.Z)([(0,s.Mo)("ha-check-list-item")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"method",key:"onChange",value:async function(e){(0,n.Z)(i,"onChange",this,3)([e]),(0,y.B)(this,e.type)}},{kind:"field",static:!0,key:"styles",value(){return[g.W,p,r.iv`
      :host {
        --mdc-theme-secondary: var(--primary-color);
      }

      :host([graphic="avatar"]) .mdc-deprecated-list-item__graphic,
      :host([graphic="medium"]) .mdc-deprecated-list-item__graphic,
      :host([graphic="large"]) .mdc-deprecated-list-item__graphic,
      :host([graphic="control"]) .mdc-deprecated-list-item__graphic {
        margin-inline-end: var(--mdc-list-item-graphic-margin, 16px);
        margin-inline-start: 0px;
        direction: var(--direction);
      }
      .mdc-deprecated-list-item__meta {
        flex-shrink: 0;
        direction: var(--direction);
        margin-inline-start: auto;
        margin-inline-end: 0;
      }
      .mdc-deprecated-list-item__graphic {
        margin-top: var(--check-list-item-graphic-margin-top);
      }
      :host([graphic="icon"]) .mdc-deprecated-list-item__graphic {
        margin-inline-start: 0;
        margin-inline-end: var(--mdc-list-item-graphic-margin, 32px);
      }
    `]}}]}}),u)},87092:function(e,t,i){i.r(t),i.d(t,{HaFormMultiSelect:()=>l});var o=i(44249),n=i(57243),r=i(50778),a=i(11297);i(43527),i(43685),i(76418),i(52158),i(59897),i(70596),i(43745),i(88002);function s(e){return Array.isArray(e)?e[0]:e}function d(e){return Array.isArray(e)?e[1]||e[0]:e}let l=(0,o.Z)([(0,r.Mo)("ha-form-multi_select")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_opened",value(){return!1}},{kind:"field",decorators:[(0,r.IO)("ha-button-menu")],key:"_input",value:void 0},{kind:"method",key:"focus",value:function(){this._input&&this._input.focus()}},{kind:"method",key:"render",value:function(){const e=Array.isArray(this.schema.options)?this.schema.options:Object.entries(this.schema.options),t=this.data||[];return e.length<6?n.dy`<div>
        ${this.label}${e.map((e=>{const i=s(e);return n.dy`
            <ha-formfield .label=${d(e)}>
              <ha-checkbox
                .checked=${t.includes(i)}
                .value=${i}
                .disabled=${this.disabled}
                @change=${this._valueChanged}
              ></ha-checkbox>
            </ha-formfield>
          `}))}
      </div> `:n.dy`
      <ha-md-button-menu
        .disabled=${this.disabled}
        @opening=${this._handleOpen}
        @closing=${this._handleClose}
        positioning="fixed"
      >
        <ha-textfield
          slot="trigger"
          .label=${this.label}
          .value=${t.map((t=>d(e.find((e=>s(e)===t)))||t)).join(", ")}
          .disabled=${this.disabled}
          tabindex="-1"
        ></ha-textfield>
        <ha-icon-button
          slot="trigger"
          .label=${this.label}
          .path=${this._opened?"M7,15L12,10L17,15H7Z":"M7,10L12,15L17,10H7Z"}
        ></ha-icon-button>
        ${e.map((e=>{const i=s(e),o=t.includes(i);return n.dy`<ha-md-menu-item
            type="option"
            aria-checked=${o}
            .value=${i}
            .action=${o?"remove":"add"}
            .activated=${o}
            @click=${this._toggleItem}
            @keydown=${this._keydown}
            keep-open
          >
            <ha-checkbox
              slot="start"
              tabindex="-1"
              .checked=${o}
            ></ha-checkbox>
            ${d(e)}
          </ha-md-menu-item>`}))}
      </ha-md-button-menu>
    `}},{kind:"method",key:"_keydown",value:function(e){"Space"!==e.code&&"Enter"!==e.code||(e.preventDefault(),this._toggleItem(e))}},{kind:"method",key:"_toggleItem",value:function(e){const t=this.data||[];let i;i="add"===e.currentTarget.action?[...t,e.currentTarget.value]:t.filter((t=>t!==e.currentTarget.value)),(0,a.B)(this,"value-changed",{value:i})}},{kind:"method",key:"firstUpdated",value:function(){this.updateComplete.then((()=>{const{formElement:e,mdcRoot:t}=this.shadowRoot?.querySelector("ha-textfield")||{};e&&(e.style.textOverflow="ellipsis"),t&&(t.style.cursor="pointer")}))}},{kind:"method",key:"updated",value:function(e){e.has("schema")&&this.toggleAttribute("own-margin",Object.keys(this.schema.options).length>=6&&!!this.schema.required)}},{kind:"method",key:"_valueChanged",value:function(e){const{value:t,checked:i}=e.target;this._handleValueChanged(t,i)}},{kind:"method",key:"_handleValueChanged",value:function(e,t){let i;if(t)if(this.data){if(this.data.includes(e))return;i=[...this.data,e]}else i=[e];else{if(!this.data.includes(e))return;i=this.data.filter((t=>t!==e))}(0,a.B)(this,"value-changed",{value:i})}},{kind:"method",key:"_handleOpen",value:function(e){e.stopPropagation(),this._opened=!0,this.toggleAttribute("opened",!0)}},{kind:"method",key:"_handleClose",value:function(e){e.stopPropagation(),this._opened=!1,this.toggleAttribute("opened",!1)}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    :host([own-margin]) {
      margin-bottom: 5px;
    }
    ha-md-button-menu {
      display: block;
      cursor: pointer;
    }
    ha-formfield {
      display: block;
      padding-right: 16px;
      padding-inline-end: 16px;
      padding-inline-start: initial;
      direction: var(--direction);
    }
    ha-textfield {
      display: block;
      width: 100%;
      pointer-events: none;
    }
    ha-icon-button {
      color: var(--input-dropdown-icon-color);
      position: absolute;
      right: 1em;
      top: 4px;
      cursor: pointer;
      inset-inline-end: 1em;
      inset-inline-start: initial;
      direction: var(--direction);
    }
    :host([opened]) ha-icon-button {
      color: var(--primary-color);
    }
    :host([opened]) ha-md-button-menu {
      --mdc-text-field-idle-line-color: var(--input-hover-line-color);
      --mdc-text-field-label-ink-color: var(--primary-color);
    }
  `}}]}}),n.oi)},43745:function(e,t,i){var o=i(44249),n=i(57243),r=i(50778),a=i(24067),s=i(11297),d=i(72621),l=i(13239),c=i(7162);(0,o.Z)([(0,r.Mo)("ha-menu")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"method",key:"connectedCallback",value:function(){(0,d.Z)(i,"connectedCallback",this,3)([]),this.addEventListener("close-menu",this._handleCloseMenu)}},{kind:"method",key:"_handleCloseMenu",value:function(e){e.detail.reason.kind===c.GB.KEYDOWN&&e.detail.reason.key===c.KC.ESCAPE||e.detail.initiator.clickAction?.(e.detail.initiator)}},{kind:"field",static:!0,key:"styles",value(){return[...(0,d.Z)(i,"styles",this),n.iv`
      :host {
        --md-sys-color-surface-container: var(--card-background-color);
      }
    `]}}]}}),l.xX),(0,o.Z)([(0,r.Mo)("ha-md-button-menu")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",key:a.gA,value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)()],key:"positioning",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean,attribute:"has-overflow"})],key:"hasOverflow",value(){return!1}},{kind:"field",decorators:[(0,r.IO)("ha-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){return this._menu.items}},{kind:"method",key:"focus",value:function(){this._menu.open?this._menu.focus():this._triggerButton?.focus()}},{kind:"method",key:"render",value:function(){return n.dy`
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
    `}},{kind:"method",key:"_handleOpening",value:function(){(0,s.B)(this,"opening",void 0,{composed:!1})}},{kind:"method",key:"_handleClosing",value:function(){(0,s.B)(this,"closing",void 0,{composed:!1})}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchorElement=this,this._menu.open?this._menu.close():this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"], ha-assist-chip[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    :host {
      display: inline-block;
      position: relative;
    }
    ::slotted([disabled]) {
      color: var(--disabled-text-color);
    }
  `}}]}}),n.oi)},88002:function(e,t,i){var o=i(44249),n=i(72621),r=i(86673),a=i(57243),s=i(50778);(0,o.Z)([(0,s.Mo)("ha-md-menu-item")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"clickAction",value:void 0},{kind:"field",static:!0,key:"styles",value(){return[...(0,n.Z)(i,"styles",this),a.iv`
      :host {
        --ha-icon-display: block;
        --md-sys-color-primary: var(--primary-text-color);
        --md-sys-color-on-primary: var(--primary-text-color);
        --md-sys-color-secondary: var(--secondary-text-color);
        --md-sys-color-surface: var(--card-background-color);
        --md-sys-color-on-surface: var(--primary-text-color);
        --md-sys-color-on-surface-variant: var(--secondary-text-color);
        --md-sys-color-secondary-container: rgba(
          var(--rgb-primary-color),
          0.15
        );
        --md-sys-color-on-secondary-container: var(--text-primary-color);
        --mdc-icon-size: 16px;

        --md-sys-color-on-primary-container: var(--primary-text-color);
        --md-sys-color-on-secondary-container: var(--primary-text-color);
        --md-menu-item-label-text-font: Roboto, sans-serif;
      }
      :host(.warning) {
        --md-menu-item-label-text-color: var(--error-color);
        --md-menu-item-leading-icon-color: var(--error-color);
      }
      ::slotted([slot="headline"]) {
        text-wrap: nowrap;
      }
    `]}}]}}),r.i)},86673:function(e,t,i){i.d(t,{i:()=>p});var o=i(9065),n=i(50778),r=(i(57618),i(26499),i(23111),i(57243)),a=i(35359),s=i(79840),d=i(13823),l=i(7162);class c{constructor(e,t){this.host=e,this.internalTypeaheadText=null,this.onClick=()=>{this.host.keepOpen||this.host.dispatchEvent((0,l.d7)(this.host,{kind:l.GB.CLICK_SELECTION}))},this.onKeydown=e=>{if(this.host.href&&"Enter"===e.code){const e=this.getInteractiveElement();e instanceof HTMLAnchorElement&&e.click()}if(e.defaultPrevented)return;const t=e.code;this.host.keepOpen&&"Escape"!==t||(0,l.kE)(t)&&(e.preventDefault(),this.host.dispatchEvent((0,l.d7)(this.host,{kind:l.GB.KEYDOWN,key:t})))},this.getHeadlineElements=t.getHeadlineElements,this.getSupportingTextElements=t.getSupportingTextElements,this.getDefaultElements=t.getDefaultElements,this.getInteractiveElement=t.getInteractiveElement,this.host.addController(this)}get typeaheadText(){if(null!==this.internalTypeaheadText)return this.internalTypeaheadText;const e=this.getHeadlineElements(),t=[];return e.forEach((e=>{e.textContent&&e.textContent.trim()&&t.push(e.textContent.trim())})),0===t.length&&this.getDefaultElements().forEach((e=>{e.textContent&&e.textContent.trim()&&t.push(e.textContent.trim())})),0===t.length&&this.getSupportingTextElements().forEach((e=>{e.textContent&&e.textContent.trim()&&t.push(e.textContent.trim())})),t.join(" ")}get tagName(){switch(this.host.type){case"link":return"a";case"button":return"button";default:return"li"}}get role(){return"option"===this.host.type?"option":"menuitem"}hostConnected(){this.host.toggleAttribute("md-menu-item",!0)}hostUpdate(){this.host.href&&(this.host.type="link")}setTypeaheadText(e){this.internalTypeaheadText=e}}const h=(0,d.T)(r.oi);class m extends h{constructor(){super(...arguments),this.disabled=!1,this.type="menuitem",this.href="",this.target="",this.keepOpen=!1,this.selected=!1,this.menuItemController=new c(this,{getHeadlineElements:()=>this.headlineElements,getSupportingTextElements:()=>this.supportingTextElements,getDefaultElements:()=>this.defaultElements,getInteractiveElement:()=>this.listItemRoot})}get typeaheadText(){return this.menuItemController.typeaheadText}set typeaheadText(e){this.menuItemController.setTypeaheadText(e)}render(){return this.renderListItem(r.dy`
      <md-item>
        <div slot="container">
          ${this.renderRipple()} ${this.renderFocusRing()}
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        ${this.renderBody()}
      </md-item>
    `)}renderListItem(e){const t="link"===this.type;let i;switch(this.menuItemController.tagName){case"a":i=s.i0`a`;break;case"button":i=s.i0`button`;break;default:i=s.i0`li`}const o=t&&this.target?this.target:r.Ld;return s.dy`
      <${i}
        id="item"
        tabindex=${this.disabled&&!t?-1:0}
        role=${this.menuItemController.role}
        aria-label=${this.ariaLabel||r.Ld}
        aria-selected=${this.ariaSelected||r.Ld}
        aria-checked=${this.ariaChecked||r.Ld}
        aria-expanded=${this.ariaExpanded||r.Ld}
        aria-haspopup=${this.ariaHasPopup||r.Ld}
        class="list-item ${(0,a.$)(this.getRenderClasses())}"
        href=${this.href||r.Ld}
        target=${o}
        @click=${this.menuItemController.onClick}
        @keydown=${this.menuItemController.onKeydown}
      >${e}</${i}>
    `}renderRipple(){return r.dy` <md-ripple
      part="ripple"
      for="item"
      ?disabled=${this.disabled}></md-ripple>`}renderFocusRing(){return r.dy` <md-focus-ring
      part="focus-ring"
      for="item"
      inward></md-focus-ring>`}getRenderClasses(){return{disabled:this.disabled,selected:this.selected}}renderBody(){return r.dy`
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot
        name="trailing-supporting-text"
        slot="trailing-supporting-text"></slot>
    `}focus(){this.listItemRoot?.focus()}}m.shadowRootOptions={...r.oi.shadowRootOptions,delegatesFocus:!0},(0,o.__decorate)([(0,n.Cb)({type:Boolean,reflect:!0})],m.prototype,"disabled",void 0),(0,o.__decorate)([(0,n.Cb)()],m.prototype,"type",void 0),(0,o.__decorate)([(0,n.Cb)()],m.prototype,"href",void 0),(0,o.__decorate)([(0,n.Cb)()],m.prototype,"target",void 0),(0,o.__decorate)([(0,n.Cb)({type:Boolean,attribute:"keep-open"})],m.prototype,"keepOpen",void 0),(0,o.__decorate)([(0,n.Cb)({type:Boolean})],m.prototype,"selected",void 0),(0,o.__decorate)([(0,n.IO)(".list-item")],m.prototype,"listItemRoot",void 0),(0,o.__decorate)([(0,n.NH)({slot:"headline"})],m.prototype,"headlineElements",void 0),(0,o.__decorate)([(0,n.NH)({slot:"supporting-text"})],m.prototype,"supportingTextElements",void 0),(0,o.__decorate)([(0,n.vZ)({slot:""})],m.prototype,"defaultElements",void 0),(0,o.__decorate)([(0,n.Cb)({attribute:"typeahead-text"})],m.prototype,"typeaheadText",null);const u=r.iv`:host{display:flex;--md-ripple-hover-color: var(--md-menu-item-hover-state-layer-color, var(--md-sys-color-on-surface, #1d1b20));--md-ripple-hover-opacity: var(--md-menu-item-hover-state-layer-opacity, 0.08);--md-ripple-pressed-color: var(--md-menu-item-pressed-state-layer-color, var(--md-sys-color-on-surface, #1d1b20));--md-ripple-pressed-opacity: var(--md-menu-item-pressed-state-layer-opacity, 0.12)}:host([disabled]){opacity:var(--md-menu-item-disabled-opacity, 0.3);pointer-events:none}md-focus-ring{z-index:1;--md-focus-ring-shape: 8px}a,button,li{background:none;border:none;padding:0;margin:0;text-align:unset;text-decoration:none}.list-item{border-radius:inherit;display:flex;flex:1;max-width:inherit;min-width:inherit;outline:none;-webkit-tap-highlight-color:rgba(0,0,0,0)}.list-item:not(.disabled){cursor:pointer}[slot=container]{pointer-events:none}md-ripple{border-radius:inherit}md-item{border-radius:inherit;flex:1;color:var(--md-menu-item-label-text-color, var(--md-sys-color-on-surface, #1d1b20));font-family:var(--md-menu-item-label-text-font, var(--md-sys-typescale-body-large-font, var(--md-ref-typeface-plain, Roboto)));font-size:var(--md-menu-item-label-text-size, var(--md-sys-typescale-body-large-size, 1rem));line-height:var(--md-menu-item-label-text-line-height, var(--md-sys-typescale-body-large-line-height, 1.5rem));font-weight:var(--md-menu-item-label-text-weight, var(--md-sys-typescale-body-large-weight, var(--md-ref-typeface-weight-regular, 400)));min-height:var(--md-menu-item-one-line-container-height, 56px);padding-top:var(--md-menu-item-top-space, 12px);padding-bottom:var(--md-menu-item-bottom-space, 12px);padding-inline-start:var(--md-menu-item-leading-space, 16px);padding-inline-end:var(--md-menu-item-trailing-space, 16px)}md-item[multiline]{min-height:var(--md-menu-item-two-line-container-height, 72px)}[slot=supporting-text]{color:var(--md-menu-item-supporting-text-color, var(--md-sys-color-on-surface-variant, #49454f));font-family:var(--md-menu-item-supporting-text-font, var(--md-sys-typescale-body-medium-font, var(--md-ref-typeface-plain, Roboto)));font-size:var(--md-menu-item-supporting-text-size, var(--md-sys-typescale-body-medium-size, 0.875rem));line-height:var(--md-menu-item-supporting-text-line-height, var(--md-sys-typescale-body-medium-line-height, 1.25rem));font-weight:var(--md-menu-item-supporting-text-weight, var(--md-sys-typescale-body-medium-weight, var(--md-ref-typeface-weight-regular, 400)))}[slot=trailing-supporting-text]{color:var(--md-menu-item-trailing-supporting-text-color, var(--md-sys-color-on-surface-variant, #49454f));font-family:var(--md-menu-item-trailing-supporting-text-font, var(--md-sys-typescale-label-small-font, var(--md-ref-typeface-plain, Roboto)));font-size:var(--md-menu-item-trailing-supporting-text-size, var(--md-sys-typescale-label-small-size, 0.6875rem));line-height:var(--md-menu-item-trailing-supporting-text-line-height, var(--md-sys-typescale-label-small-line-height, 1rem));font-weight:var(--md-menu-item-trailing-supporting-text-weight, var(--md-sys-typescale-label-small-weight, var(--md-ref-typeface-weight-medium, 500)))}:is([slot=start],[slot=end])::slotted(*){fill:currentColor}[slot=start]{color:var(--md-menu-item-leading-icon-color, var(--md-sys-color-on-surface-variant, #49454f))}[slot=end]{color:var(--md-menu-item-trailing-icon-color, var(--md-sys-color-on-surface-variant, #49454f))}.list-item{background-color:var(--md-menu-item-container-color, transparent)}.list-item.selected{background-color:var(--md-menu-item-selected-container-color, var(--md-sys-color-secondary-container, #e8def8))}.selected:not(.disabled) ::slotted(*){color:var(--md-menu-item-selected-label-text-color, var(--md-sys-color-on-secondary-container, #1d192b))}@media(forced-colors: active){:host([disabled]),:host([disabled]) slot{color:GrayText;opacity:1}.list-item{position:relative}.list-item.selected::before{content:"";position:absolute;inset:0;box-sizing:border-box;border-radius:inherit;pointer-events:none;border:3px double CanvasText}}
`;let p=class extends m{};p.styles=[u],p=(0,o.__decorate)([(0,n.Mo)("md-menu-item")],p)}};
//# sourceMappingURL=1808.50bd3dfd596b1824.js.map