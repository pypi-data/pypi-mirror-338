/*! For license information please see 7634.dc5d21a52d88b0a6.js.LICENSE.txt */
"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["7634"],{47899:function(e,t,r){r.a(e,(async function(e,n){try{r.d(t,{Bt:()=>d});r(19083);var a=r(69440),i=r(88977),o=r(50177),s=e([a]);a=(s.then?(await s)():s)[0];const l=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"],d=e=>e.first_weekday===o.FS.language?"weekInfo"in Intl.Locale.prototype?new Intl.Locale(e.language).weekInfo.firstDay%7:(0,i.L)(e.language)%7:l.includes(e.first_weekday)?l.indexOf(e.first_weekday):1;n()}catch(l){n(l)}}))},52258:function(e,t,r){r.a(e,(async function(e,n){try{r.d(t,{G:()=>d});var a=r(69440),i=r(27486),o=r(66045),s=e([a,o]);[a,o]=s.then?(await s)():s;const l=(0,i.Z)((e=>new Intl.RelativeTimeFormat(e.language,{numeric:"auto"}))),d=(e,t,r,n=!0)=>{const a=(0,o.W)(e,r,t);return n?l(t).format(a.value,a.unit):Intl.NumberFormat(t.language,{style:"unit",unit:a.unit,unitDisplay:"long"}).format(Math.abs(a.value))};n()}catch(l){n(l)}}))},66045:function(e,t,r){r.a(e,(async function(e,n){try{r.d(t,{W:()=>h});r(19423);var a=r(13809),i=r(29558),o=r(57829),s=r(47899),l=e([s]);s=(l.then?(await l)():l)[0];const c=1e3,u=60,p=60*u;function h(e,t=Date.now(),r,n={}){const l=Object.assign(Object.assign({},g),n||{}),d=(+e-+t)/c;if(Math.abs(d)<l.second)return{value:Math.round(d),unit:"second"};const h=d/u;if(Math.abs(h)<l.minute)return{value:Math.round(h),unit:"minute"};const v=d/p;if(Math.abs(v)<l.hour)return{value:Math.round(v),unit:"hour"};const m=new Date(e),f=new Date(t);m.setHours(0,0,0,0),f.setHours(0,0,0,0);const b=(0,a.j)(m,f);if(0===b)return{value:Math.round(v),unit:"hour"};if(Math.abs(b)<l.day)return{value:b,unit:"day"};const y=(0,s.Bt)(r),k=(0,i.z)(m,{weekStartsOn:y}),x=(0,i.z)(f,{weekStartsOn:y}),w=(0,o.p)(k,x);if(0===w)return{value:b,unit:"day"};if(Math.abs(w)<l.week)return{value:w,unit:"week"};const _=m.getFullYear()-f.getFullYear(),$=12*_+m.getMonth()-f.getMonth();return 0===$?{value:w,unit:"week"}:Math.abs($)<l.month||0===_?{value:$,unit:"month"}:{value:Math.round(_),unit:"year"}}const g={second:45,minute:45,hour:22,day:5,week:4,month:11};n()}catch(d){n(d)}}))},43527:function(e,t,r){var n=r(73577),a=r(72621),i=(r(71695),r(9359),r(31526),r(47021),r(22997),r(57243)),o=r(50778),s=r(80155),l=r(24067);let d,c,u=e=>e;(0,n.Z)([(0,o.Mo)("ha-button-menu")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",key:l.gA,value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"corner",value(){return"BOTTOM_START"}},{kind:"field",decorators:[(0,o.Cb)({attribute:"menu-corner"})],key:"menuCorner",value(){return"START"}},{kind:"field",decorators:[(0,o.Cb)({type:Number})],key:"x",value(){return null}},{kind:"field",decorators:[(0,o.Cb)({type:Number})],key:"y",value(){return null}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"multi",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"activatable",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"fixed",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,attribute:"no-anchor"})],key:"noAnchor",value(){return!1}},{kind:"field",decorators:[(0,o.IO)("mwc-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){var e;return null===(e=this._menu)||void 0===e?void 0:e.items}},{kind:"get",key:"selected",value:function(){var e;return null===(e=this._menu)||void 0===e?void 0:e.selected}},{kind:"method",key:"focus",value:function(){var e,t;null!==(e=this._menu)&&void 0!==e&&e.open?this._menu.focusItemAtIndex(0):null===(t=this._triggerButton)||void 0===t||t.focus()}},{kind:"method",key:"render",value:function(){return(0,i.dy)(d||(d=u`
      <div @click=${0}>
        <slot name="trigger" @slotchange=${0}></slot>
      </div>
      <mwc-menu
        .corner=${0}
        .menuCorner=${0}
        .fixed=${0}
        .multi=${0}
        .activatable=${0}
        .y=${0}
        .x=${0}
      >
        <slot></slot>
      </mwc-menu>
    `),this._handleClick,this._setTriggerAria,this.corner,this.menuCorner,this.fixed,this.multi,this.activatable,this.y,this.x)}},{kind:"method",key:"firstUpdated",value:function(e){(0,a.Z)(r,"firstUpdated",this,3)([e]),"rtl"===s.E.document.dir&&this.updateComplete.then((()=>{this.querySelectorAll("mwc-list-item").forEach((e=>{const t=document.createElement("style");t.innerHTML="span.material-icons:first-of-type { margin-left: var(--mdc-list-item-graphic-margin, 32px) !important; margin-right: 0px !important;}",e.shadowRoot.appendChild(t)}))}))}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchor=this.noAnchor?null:this,this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"field",static:!0,key:"styles",value(){return(0,i.iv)(c||(c=u`
    :host {
      display: inline-block;
      position: relative;
    }
    ::slotted([disabled]) {
      color: var(--disabled-text-color);
    }
  `))}}]}}),i.oi)},1192:function(e,t,r){var n=r(73577),a=(r(71695),r(47021),r(57243)),i=r(50778);let o,s,l,d=e=>e;(0,n.Z)([(0,i.Mo)("ha-card")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)()],key:"header",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,reflect:!0})],key:"raised",value(){return!1}},{kind:"field",static:!0,key:"styles",value(){return(0,a.iv)(o||(o=d`
    :host {
      background: var(
        --ha-card-background,
        var(--card-background-color, white)
      );
      -webkit-backdrop-filter: var(--ha-card-backdrop-filter, none);
      backdrop-filter: var(--ha-card-backdrop-filter, none);
      box-shadow: var(--ha-card-box-shadow, none);
      box-sizing: border-box;
      border-radius: var(--ha-card-border-radius, 12px);
      border-width: var(--ha-card-border-width, 1px);
      border-style: solid;
      border-color: var(--ha-card-border-color, var(--divider-color, #e0e0e0));
      color: var(--primary-text-color);
      display: block;
      transition: all 0.3s ease-out;
      position: relative;
    }

    :host([raised]) {
      border: none;
      box-shadow: var(
        --ha-card-box-shadow,
        0px 2px 1px -1px rgba(0, 0, 0, 0.2),
        0px 1px 1px 0px rgba(0, 0, 0, 0.14),
        0px 1px 3px 0px rgba(0, 0, 0, 0.12)
      );
    }

    .card-header,
    :host ::slotted(.card-header) {
      color: var(--ha-card-header-color, var(--primary-text-color));
      font-family: var(--ha-card-header-font-family, inherit);
      font-size: var(--ha-card-header-font-size, 24px);
      letter-spacing: -0.012em;
      line-height: 48px;
      padding: 12px 16px 16px;
      display: block;
      margin-block-start: 0px;
      margin-block-end: 0px;
      font-weight: normal;
    }

    :host ::slotted(.card-content:not(:first-child)),
    slot:not(:first-child)::slotted(.card-content) {
      padding-top: 0px;
      margin-top: -8px;
    }

    :host ::slotted(.card-content) {
      padding: 16px;
    }

    :host ::slotted(.card-actions) {
      border-top: 1px solid var(--divider-color, #e8e8e8);
      padding: 5px 16px;
    }
  `))}},{kind:"method",key:"render",value:function(){return(0,a.dy)(s||(s=d`
      ${0}
      <slot></slot>
    `),this.header?(0,a.dy)(l||(l=d`<h1 class="card-header">${0}</h1>`),this.header):a.Ld)}}]}}),a.oi)},65099:function(e,t,r){r.a(e,(async function(e,n){try{r.r(t),r.d(t,{HaIconOverflowMenu:()=>x});var a=r(73577),i=(r(71695),r(9359),r(70104),r(47021),r(57243)),o=r(50778),s=r(35359),l=r(66193),d=(r(43527),r(59897),r(74064),r(10508),r(20418)),c=e([d]);d=(c.then?(await c)():c)[0];let u,p,h,g,v,m,f,b,y=e=>e;const k="M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z";let x=(0,a.Z)([(0,o.Mo)("ha-icon-overflow-menu")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Array})],key:"items",value(){return[]}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"narrow",value(){return!1}},{kind:"method",key:"render",value:function(){return(0,i.dy)(u||(u=y`
      ${0}
    `),this.narrow?(0,i.dy)(p||(p=y` <!-- Collapsed representation for small screens -->
            <ha-button-menu
              @click=${0}
              @closed=${0}
              class="ha-icon-overflow-menu-overflow"
              absolute
            >
              <ha-icon-button
                .label=${0}
                .path=${0}
                slot="trigger"
              ></ha-icon-button>

              ${0}
            </ha-button-menu>`),this._handleIconOverflowMenuOpened,this._handleIconOverflowMenuClosed,this.hass.localize("ui.common.overflow_menu"),k,this.items.map((e=>e.divider?(0,i.dy)(h||(h=y`<li divider role="separator"></li>`)):(0,i.dy)(g||(g=y`<ha-list-item
                      graphic="icon"
                      ?disabled=${0}
                      @click=${0}
                      class=${0}
                    >
                      <div slot="graphic">
                        <ha-svg-icon
                          class=${0}
                          .path=${0}
                        ></ha-svg-icon>
                      </div>
                      ${0}
                    </ha-list-item> `),e.disabled,e.action,(0,s.$)({warning:Boolean(e.warning)}),(0,s.$)({warning:Boolean(e.warning)}),e.path,e.label)))):(0,i.dy)(v||(v=y`
            <!-- Icon representation for big screens -->
            ${0}
          `),this.items.map((e=>{var t;return e.narrowOnly?i.Ld:e.divider?(0,i.dy)(m||(m=y`<div role="separator"></div>`)):(0,i.dy)(f||(f=y`<ha-tooltip
                      .disabled=${0}
                      .content=${0}
                    >
                      <ha-icon-button
                        @click=${0}
                        .label=${0}
                        .path=${0}
                        ?disabled=${0}
                      ></ha-icon-button>
                    </ha-tooltip>`),!e.tooltip,null!==(t=e.tooltip)&&void 0!==t?t:"",e.action,e.label,e.path,e.disabled)}))))}},{kind:"method",key:"_handleIconOverflowMenuOpened",value:function(e){e.stopPropagation();const t=this.closest(".mdc-data-table__row");t&&(t.style.zIndex="1")}},{kind:"method",key:"_handleIconOverflowMenuClosed",value:function(){const e=this.closest(".mdc-data-table__row");e&&(e.style.zIndex="")}},{kind:"get",static:!0,key:"styles",value:function(){return[l.Qx,(0,i.iv)(b||(b=y`
        :host {
          display: flex;
          justify-content: flex-end;
        }
        li[role="separator"] {
          border-bottom-color: var(--divider-color);
        }
        div[role="separator"] {
          border-right: 1px solid var(--divider-color);
          width: 1px;
        }
        ha-list-item[disabled] ha-svg-icon {
          color: var(--disabled-text-color);
        }
      `))]}}]}}),i.oi);n()}catch(u){n(u)}}))},74064:function(e,t,r){var n=r(73577),a=r(72621),i=(r(71695),r(47021),r(65703)),o=r(46289),s=r(57243),l=r(50778);let d,c,u,p=e=>e;(0,n.Z)([(0,l.Mo)("ha-list-item")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"method",key:"renderRipple",value:function(){return this.noninteractive?"":(0,a.Z)(r,"renderRipple",this,3)([])}},{kind:"get",static:!0,key:"styles",value:function(){return[o.W,(0,s.iv)(d||(d=p`
        :host {
          padding-left: var(
            --mdc-list-side-padding-left,
            var(--mdc-list-side-padding, 20px)
          );
          padding-inline-start: var(
            --mdc-list-side-padding-left,
            var(--mdc-list-side-padding, 20px)
          );
          padding-right: var(
            --mdc-list-side-padding-right,
            var(--mdc-list-side-padding, 20px)
          );
          padding-inline-end: var(
            --mdc-list-side-padding-right,
            var(--mdc-list-side-padding, 20px)
          );
        }
        :host([graphic="avatar"]:not([twoLine])),
        :host([graphic="icon"]:not([twoLine])) {
          height: 48px;
        }
        span.material-icons:first-of-type {
          margin-inline-start: 0px !important;
          margin-inline-end: var(
            --mdc-list-item-graphic-margin,
            16px
          ) !important;
          direction: var(--direction) !important;
        }
        span.material-icons:last-of-type {
          margin-inline-start: auto !important;
          margin-inline-end: 0px !important;
          direction: var(--direction) !important;
        }
        .mdc-deprecated-list-item__meta {
          display: var(--mdc-list-item-meta-display);
          align-items: center;
          flex-shrink: 0;
        }
        :host([graphic="icon"]:not([twoline]))
          .mdc-deprecated-list-item__graphic {
          margin-inline-end: var(
            --mdc-list-item-graphic-margin,
            20px
          ) !important;
        }
        :host([multiline-secondary]) {
          height: auto;
        }
        :host([multiline-secondary]) .mdc-deprecated-list-item__text {
          padding: 8px 0;
        }
        :host([multiline-secondary]) .mdc-deprecated-list-item__secondary-text {
          text-overflow: initial;
          white-space: normal;
          overflow: auto;
          display: inline-block;
          margin-top: 10px;
        }
        :host([multiline-secondary]) .mdc-deprecated-list-item__primary-text {
          margin-top: 10px;
        }
        :host([multiline-secondary])
          .mdc-deprecated-list-item__secondary-text::before {
          display: none;
        }
        :host([multiline-secondary])
          .mdc-deprecated-list-item__primary-text::before {
          display: none;
        }
        :host([disabled]) {
          color: var(--disabled-text-color);
        }
        :host([noninteractive]) {
          pointer-events: unset;
        }
      `)),"rtl"===document.dir?(0,s.iv)(c||(c=p`
            span.material-icons:first-of-type,
            span.material-icons:last-of-type {
              direction: rtl !important;
              --direction: rtl;
            }
          `)):(0,s.iv)(u||(u=p``))]}}]}}),i.K)},20418:function(e,t,r){r.a(e,(async function(e,t){try{var n=r(73577),a=(r(71695),r(47021),r(80519)),i=r(1261),o=r(57243),s=r(50778),l=r(85605),d=e([a]);a=(d.then?(await d)():d)[0];let c,u=e=>e;(0,l.jx)("tooltip.show",{keyframes:[{opacity:0},{opacity:1}],options:{duration:150,easing:"ease"}}),(0,l.jx)("tooltip.hide",{keyframes:[{opacity:1},{opacity:0}],options:{duration:400,easing:"ease"}});(0,n.Z)([(0,s.Mo)("ha-tooltip")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",static:!0,key:"styles",value(){return[i.Z,(0,o.iv)(c||(c=u`
      :host {
        --sl-tooltip-background-color: var(--secondary-background-color);
        --sl-tooltip-color: var(--primary-text-color);
        --sl-tooltip-font-family: Roboto, sans-serif;
        --sl-tooltip-font-size: 12px;
        --sl-tooltip-font-weight: normal;
        --sl-tooltip-line-height: 1;
        --sl-tooltip-padding: 8px;
        --sl-tooltip-border-radius: var(--ha-tooltip-border-radius, 4px);
        --sl-tooltip-arrow-size: var(--ha-tooltip-arrow-size, 8px);
        --sl-z-index-tooltip: var(--ha-tooltip-z-index, 1000);
      }
    `))]}}]}}),a.Z);t()}catch(c){t(c)}}))},89595:function(e,t,r){r.d(t,{q:()=>d});r(52247),r(19083),r(61006),r(71695),r(23669),r(19134),r(44495),r(47021);const n=/^[v^~<>=]*?(\d+)(?:\.([x*]|\d+)(?:\.([x*]|\d+)(?:\.([x*]|\d+))?(?:-([\da-z\-]+(?:\.[\da-z\-]+)*))?(?:\+[\da-z\-]+(?:\.[\da-z\-]+)*)?)?)?$/i,a=e=>{if("string"!=typeof e)throw new TypeError("Invalid argument expected string");const t=e.match(n);if(!t)throw new Error(`Invalid argument not valid semver ('${e}' received)`);return t.shift(),t},i=e=>"*"===e||"x"===e||"X"===e,o=e=>{const t=parseInt(e,10);return isNaN(t)?e:t},s=(e,t)=>{if(i(e)||i(t))return 0;const[r,n]=((e,t)=>typeof e!=typeof t?[String(e),String(t)]:[e,t])(o(e),o(t));return r>n?1:r<n?-1:0},l=(e,t)=>{for(let r=0;r<Math.max(e.length,t.length);r++){const n=s(e[r]||"0",t[r]||"0");if(0!==n)return n}return 0},d=(e,t,r)=>{p(r);const n=((e,t)=>{const r=a(e),n=a(t),i=r.pop(),o=n.pop(),s=l(r,n);return 0!==s?s:i&&o?l(i.split("."),o.split(".")):i||o?i?-1:1:0})(e,t);return c[r].includes(n)},c={">":[1],">=":[0,1],"=":[0],"<=":[-1,0],"<":[-1],"!=":[-1,1]},u=Object.keys(c),p=e=>{if("string"!=typeof e)throw new TypeError("Invalid operator type, expected string but got "+typeof e);if(-1===u.indexOf(e))throw new Error(`Invalid operator, expected one of ${u.join("|")}`)}},12582:function(e,t,r){r.d(t,{Z:()=>n});r(9359),r(31526),r(70104),r(11740);function n(e){if(!e||"object"!=typeof e)return e;if("[object Date]"==Object.prototype.toString.call(e))return new Date(e.getTime());if(Array.isArray(e))return e.map(n);var t={};return Object.keys(e).forEach((function(r){t[r]=n(e[r])})),t}},94964:function(e,t,r){var n=r(73577),a=r(72621),i=(r(71695),r(52805),r(9359),r(31526),r(70104),r(48136),r(47021),r(57243)),o=r(50778),s=r(35359),l=r(11297),d=r(57586);let c,u,p,h,g,v,m=e=>e;const f=new d.r("knx-project-tree-view");(0,n.Z)([(0,o.Mo)("knx-project-tree-view")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"multiselect",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_selectableRanges",value(){return{}}},{kind:"method",key:"connectedCallback",value:function(){(0,a.Z)(r,"connectedCallback",this,3)([]);const e=t=>{Object.entries(t).forEach((([t,r])=>{r.group_addresses.length>0&&(this._selectableRanges[t]={selected:!1,groupAddresses:r.group_addresses}),e(r.group_ranges)}))};e(this.data.group_ranges),f.debug("ranges",this._selectableRanges)}},{kind:"method",key:"render",value:function(){return(0,i.dy)(c||(c=m`<div class="ha-tree-view">${0}</div>`),this._recurseData(this.data.group_ranges))}},{kind:"method",key:"_recurseData",value:function(e,t=0){const r=Object.entries(e).map((([e,r])=>{const n=Object.keys(r.group_ranges).length>0;if(!(n||r.group_addresses.length>0))return i.Ld;const a=e in this._selectableRanges,o=!!a&&this._selectableRanges[e].selected,l={"range-item":!0,"root-range":0===t,"sub-range":t>0,selectable:a,"selected-range":o,"non-selected-range":a&&!o},d=(0,i.dy)(u||(u=m`<div
        class=${0}
        toggle-range=${0}
        @click=${0}
      >
        <span class="range-key">${0}</span>
        <span class="range-text">${0}</span>
      </div>`),(0,s.$)(l),a?e:i.Ld,a?this.multiselect?this._selectionChangedMulti:this._selectionChangedSingle:i.Ld,e,r.name);if(n){const e={"root-group":0===t,"sub-group":0!==t};return(0,i.dy)(p||(p=m`<div class=${0}>
          ${0} ${0}
        </div>`),(0,s.$)(e),d,this._recurseData(r.group_ranges,t+1))}return(0,i.dy)(h||(h=m`${0}`),d)}));return(0,i.dy)(g||(g=m`${0}`),r)}},{kind:"method",key:"_selectionChangedMulti",value:function(e){const t=e.target.getAttribute("toggle-range");this._selectableRanges[t].selected=!this._selectableRanges[t].selected,this._selectionUpdate(),this.requestUpdate()}},{kind:"method",key:"_selectionChangedSingle",value:function(e){const t=e.target.getAttribute("toggle-range"),r=this._selectableRanges[t].selected;Object.values(this._selectableRanges).forEach((e=>{e.selected=!1})),this._selectableRanges[t].selected=!r,this._selectionUpdate(),this.requestUpdate()}},{kind:"method",key:"_selectionUpdate",value:function(){const e=Object.values(this._selectableRanges).reduce(((e,t)=>t.selected?e.concat(t.groupAddresses):e),[]);f.debug("selection changed",e),(0,l.B)(this,"knx-group-range-selection-changed",{groupAddresses:e})}},{kind:"field",static:!0,key:"styles",value(){return(0,i.iv)(v||(v=m`
    :host {
      margin: 0;
      height: 100%;
      overflow-y: scroll;
      overflow-x: hidden;
      background-color: var(--card-background-color);
    }

    .ha-tree-view {
      cursor: default;
    }

    .root-group {
      margin-bottom: 8px;
    }

    .root-group > * {
      padding-top: 5px;
      padding-bottom: 5px;
    }

    .range-item {
      display: block;
      overflow: hidden;
      white-space: nowrap;
      text-overflow: ellipsis;
      font-size: 0.875rem;
    }

    .range-item > * {
      vertical-align: middle;
      pointer-events: none;
    }

    .range-key {
      color: var(--text-primary-color);
      font-size: 0.75rem;
      font-weight: 700;
      background-color: var(--label-badge-grey);
      border-radius: 4px;
      padding: 1px 4px;
      margin-right: 2px;
    }

    .root-range {
      padding-left: 8px;
      font-weight: 500;
      background-color: var(--secondary-background-color);

      & .range-key {
        color: var(--primary-text-color);
        background-color: var(--card-background-color);
      }
    }

    .sub-range {
      padding-left: 13px;
    }

    .selectable {
      cursor: pointer;
    }

    .selectable:hover {
      background-color: rgba(var(--rgb-primary-text-color), 0.04);
    }

    .selected-range {
      background-color: rgba(var(--rgb-primary-color), 0.12);

      & .range-key {
        background-color: var(--primary-color);
      }
    }

    .selected-range:hover {
      background-color: rgba(var(--rgb-primary-color), 0.07);
    }

    .non-selected-range {
      background-color: var(--card-background-color);
    }
  `))}}]}}),i.oi)},88769:function(e,t,r){r.d(t,{W:()=>i,f:()=>a});r(52805),r(9359),r(48136),r(11740);var n=r(76848);const a={payload:e=>null==e.payload?"":Array.isArray(e.payload)?e.payload.reduce(((e,t)=>e+t.toString(16).padStart(2,"0")),"0x"):e.payload.toString(),valueWithUnit:e=>null==e.value?"":"number"==typeof e.value||"boolean"==typeof e.value||"string"==typeof e.value?e.value.toString()+(e.unit?" "+e.unit:""):(0,n.$w)(e.value),timeWithMilliseconds:e=>new Date(e.timestamp).toLocaleTimeString(["en-US"],{hour12:!1,hour:"2-digit",minute:"2-digit",second:"2-digit",fractionalSecondDigits:3}),dateWithMilliseconds:e=>new Date(e.timestamp).toLocaleTimeString([],{year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",second:"2-digit",fractionalSecondDigits:3}),dptNumber:e=>null==e.dpt_main?"":null==e.dpt_sub?e.dpt_main.toString():e.dpt_main.toString()+"."+e.dpt_sub.toString().padStart(3,"0"),dptNameNumber:e=>{const t=a.dptNumber(e);return null==e.dpt_name?`DPT ${t}`:t?`DPT ${t} ${e.dpt_name}`:e.dpt_name}},i=e=>null==e?"":e.main+(e.sub?"."+e.sub.toString().padStart(3,"0"):"")},53463:function(e,t,r){r.a(e,(async function(e,n){try{r.r(t),r.d(t,{KNXProjectView:()=>L});var a=r(73577),i=r(72621),o=(r(19083),r(71695),r(92745),r(52805),r(9359),r(48136),r(19423),r(40251),r(11740),r(61006),r(47021),r(57243)),s=r(50778),l=r(27486),d=r(64364),c=r(68455),u=(r(32422),r(1192),r(59897),r(65099)),p=(r(26299),r(52258)),h=(r(94964),r(89595)),g=r(57259),v=r(57586),m=r(88769),f=e([c,u,p]);[c,u,p]=f.then?(await f)():f;let b,y,k,x,w,_,$,j,A,M,S,C,O=e=>e;const z="M6,13H18V11H6M3,6V8H21V6M10,18H14V16H10V18Z",R="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z",E=new v.r("knx-project-view"),T="3.3.0";let L=(0,a.Z)([(0,s.Mo)("knx-project-view")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,s.Cb)({type:Object})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"knx",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Object})],key:"route",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Array,reflect:!1})],key:"tabs",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean,reflect:!0,attribute:"range-selector-hidden"})],key:"rangeSelectorHidden",value(){return!0}},{kind:"field",decorators:[(0,s.SB)()],key:"_visibleGroupAddresses",value(){return[]}},{kind:"field",decorators:[(0,s.SB)()],key:"_groupRangeAvailable",value(){return!1}},{kind:"field",decorators:[(0,s.SB)()],key:"_subscribed",value:void 0},{kind:"field",decorators:[(0,s.SB)()],key:"_lastTelegrams",value(){return{}}},{kind:"method",key:"disconnectedCallback",value:function(){(0,i.Z)(r,"disconnectedCallback",this,3)([]),this._subscribed&&(this._subscribed(),this._subscribed=void 0)}},{kind:"method",key:"firstUpdated",value:async function(){this.knx.project?this._isGroupRangeAvailable():this.knx.loadProject().then((()=>{this._isGroupRangeAvailable(),this.requestUpdate()})),(0,g.ze)(this.hass).then((e=>{this._lastTelegrams=e})).catch((e=>{E.error("getGroupTelegrams",e),(0,d.c)("/knx/error",{replace:!0,data:e})})),this._subscribed=await(0,g.IP)(this.hass,(e=>{this.telegram_callback(e)}))}},{kind:"method",key:"_isGroupRangeAvailable",value:function(){var e,t;const r=null!==(e=null===(t=this.knx.project)||void 0===t?void 0:t.knxproject.info.xknxproject_version)&&void 0!==e?e:"0.0.0";E.debug("project version: "+r),this._groupRangeAvailable=(0,h.q)(r,T,">=")}},{kind:"method",key:"telegram_callback",value:function(e){this._lastTelegrams=Object.assign(Object.assign({},this._lastTelegrams),{},{[e.destination]:e})}},{kind:"field",key:"_columns",value(){return(0,l.Z)(((e,t)=>({address:{filterable:!0,sortable:!0,title:this.knx.localize("project_view_table_address"),flex:1,minWidth:"100px"},name:{filterable:!0,sortable:!0,title:this.knx.localize("project_view_table_name"),flex:3},dpt:{sortable:!0,filterable:!0,title:this.knx.localize("project_view_table_dpt"),flex:1,minWidth:"82px",template:e=>e.dpt?(0,o.dy)(b||(b=O`<span style="display:inline-block;width:24px;text-align:right;"
                  >${0}</span
                >${0} `),e.dpt.main,e.dpt.sub?"."+e.dpt.sub.toString().padStart(3,"0"):""):""},lastValue:{filterable:!0,title:this.knx.localize("project_view_table_last_value"),flex:2,template:e=>{const t=this._lastTelegrams[e.address];if(!t)return"";const r=m.f.payload(t);return null==t.value?(0,o.dy)(y||(y=O`<code>${0}</code>`),r):(0,o.dy)(k||(k=O`<div title=${0}>
            ${0}
          </div>`),r,m.f.valueWithUnit(this._lastTelegrams[e.address]))}},updated:{title:this.knx.localize("project_view_table_updated"),flex:1,showNarrow:!1,template:e=>{const t=this._lastTelegrams[e.address];if(!t)return"";const r=`${m.f.dateWithMilliseconds(t)}\n\n${t.source} ${t.source_name}`;return(0,o.dy)(x||(x=O`<div title=${0}>
            ${0}
          </div>`),r,(0,p.G)(new Date(t.timestamp),this.hass.locale))}},actions:{title:"",minWidth:"72px",type:"overflow-menu",template:e=>this._groupAddressMenu(e)}})))}},{kind:"method",key:"_groupAddressMenu",value:function(e){var t;const r=[];return 1===(null===(t=e.dpt)||void 0===t?void 0:t.main)&&r.push({path:R,label:"Create binary sensor",action:()=>{(0,d.c)("/knx/entities/create/binary_sensor?knx.ga_sensor.state="+e.address)}}),r.length?(0,o.dy)(w||(w=O`
          <ha-icon-overflow-menu .hass=${0} narrow .items=${0}> </ha-icon-overflow-menu>
        `),this.hass,r):o.Ld}},{kind:"method",key:"_getRows",value:function(e){return e.length?Object.entries(this.knx.project.knxproject.group_addresses).reduce(((t,[r,n])=>(e.includes(r)&&t.push(n),t)),[]):Object.values(this.knx.project.knxproject.group_addresses)}},{kind:"method",key:"_visibleAddressesChanged",value:function(e){this._visibleGroupAddresses=e.detail.groupAddresses}},{kind:"method",key:"render",value:function(){if(!this.hass||!this.knx.project)return(0,o.dy)(_||(_=O` <hass-loading-screen></hass-loading-screen> `));const e=this._getRows(this._visibleGroupAddresses);return(0,o.dy)($||($=O`
      <hass-tabs-subpage
        .hass=${0}
        .narrow=${0}
        .route=${0}
        .tabs=${0}
        .localizeFunc=${0}
      >
        ${0}
      </hass-tabs-subpage>
    `),this.hass,this.narrow,this.route,this.tabs,this.knx.localize,this.knx.project.project_loaded?(0,o.dy)(j||(j=O`${0}
              <div class="sections">
                ${0}
                <ha-data-table
                  class="ga-table"
                  .hass=${0}
                  .columns=${0}
                  .data=${0}
                  .hasFab=${0}
                  .searchLabel=${0}
                  .clickable=${0}
                ></ha-data-table>
              </div>`),this.narrow&&this._groupRangeAvailable?(0,o.dy)(A||(A=O`<ha-icon-button
                    slot="toolbar-icon"
                    .label=${0}
                    .path=${0}
                    @click=${0}
                  ></ha-icon-button>`),this.hass.localize("ui.components.related-filter-menu.filter"),z,this._toggleRangeSelector):o.Ld,this._groupRangeAvailable?(0,o.dy)(M||(M=O`
                      <knx-project-tree-view
                        .data=${0}
                        @knx-group-range-selection-changed=${0}
                      ></knx-project-tree-view>
                    `),this.knx.project.knxproject,this._visibleAddressesChanged):o.Ld,this.hass,this._columns(this.narrow,this.hass.language),e,!1,this.hass.localize("ui.components.data-table.search"),!1):(0,o.dy)(S||(S=O` <ha-card .header=${0}>
              <div class="card-content">
                <p>${0}</p>
              </div>
            </ha-card>`),this.knx.localize("attention"),this.knx.localize("project_view_upload")))}},{kind:"method",key:"_toggleRangeSelector",value:function(){this.rangeSelectorHidden=!this.rangeSelectorHidden}},{kind:"field",static:!0,key:"styles",value(){return(0,o.iv)(C||(C=O`
    hass-loading-screen {
      --app-header-background-color: var(--sidebar-background-color);
      --app-header-text-color: var(--sidebar-text-color);
    }
    .sections {
      display: flex;
      flex-direction: row;
      height: 100%;
    }

    :host([narrow]) knx-project-tree-view {
      position: absolute;
      max-width: calc(100% - 60px); /* 100% -> max 871px before not narrow */
      z-index: 1;
      right: 0;
      transition: 0.5s;
      border-left: 1px solid var(--divider-color);
    }

    :host([narrow][range-selector-hidden]) knx-project-tree-view {
      width: 0;
    }

    :host(:not([narrow])) knx-project-tree-view {
      max-width: 255px; /* min 616px - 816px for tree-view + ga-table (depending on side menu) */
    }

    .ga-table {
      flex: 1;
    }
  `))}}]}}),o.oi);n()}catch(b){n(b)}}))},75351:function(e,t,r){r.d(t,{Ud:()=>p});r(63721),r(52247),r(71695),r(52805),r(43451),r(9359),r(70104),r(48136),r(19423),r(40251),r(69235),r(12385),r(19134),r(5740),r(11740),r(46692),r(47021);const n=Symbol("Comlink.proxy"),a=Symbol("Comlink.endpoint"),i=Symbol("Comlink.releaseProxy"),o=Symbol("Comlink.finalizer"),s=Symbol("Comlink.thrown"),l=e=>"object"==typeof e&&null!==e||"function"==typeof e,d=new Map([["proxy",{canHandle:e=>l(e)&&e[n],serialize(e){const{port1:t,port2:r}=new MessageChannel;return c(e,t),[r,[r]]},deserialize(e){return e.start(),p(e)}}],["throw",{canHandle:e=>l(e)&&s in e,serialize({value:e}){let t;return t=e instanceof Error?{isError:!0,value:{message:e.message,name:e.name,stack:e.stack}}:{isError:!1,value:e},[t,[]]},deserialize(e){if(e.isError)throw Object.assign(new Error(e.value.message),e.value);throw e.value}}]]);function c(e,t=globalThis,r=["*"]){t.addEventListener("message",(function a(i){if(!i||!i.data)return;if(!function(e,t){for(const r of e){if(t===r||"*"===r)return!0;if(r instanceof RegExp&&r.test(t))return!0}return!1}(r,i.origin))return void console.warn(`Invalid origin '${i.origin}' for comlink proxy`);const{id:l,type:d,path:p}=Object.assign({path:[]},i.data),h=(i.data.argumentList||[]).map(x);let g;try{const t=p.slice(0,-1).reduce(((e,t)=>e[t]),e),r=p.reduce(((e,t)=>e[t]),e);switch(d){case"GET":g=r;break;case"SET":t[p.slice(-1)[0]]=x(i.data.value),g=!0;break;case"APPLY":g=r.apply(t,h);break;case"CONSTRUCT":g=function(e){return Object.assign(e,{[n]:!0})}(new r(...h));break;case"ENDPOINT":{const{port1:t,port2:r}=new MessageChannel;c(e,r),g=function(e,t){return y.set(e,t),e}(t,[t])}break;case"RELEASE":g=void 0;break;default:return}}catch(v){g={value:v,[s]:0}}Promise.resolve(g).catch((e=>({value:e,[s]:0}))).then((r=>{const[n,i]=k(r);t.postMessage(Object.assign(Object.assign({},n),{id:l}),i),"RELEASE"===d&&(t.removeEventListener("message",a),u(t),o in e&&"function"==typeof e[o]&&e[o]())})).catch((e=>{const[r,n]=k({value:new TypeError("Unserializable return value"),[s]:0});t.postMessage(Object.assign(Object.assign({},r),{id:l}),n)}))})),t.start&&t.start()}function u(e){(function(e){return"MessagePort"===e.constructor.name})(e)&&e.close()}function p(e,t){const r=new Map;return e.addEventListener("message",(function(e){const{data:t}=e;if(!t||!t.id)return;const n=r.get(t.id);if(n)try{n(t)}finally{r.delete(t.id)}})),f(e,r,[],t)}function h(e){if(e)throw new Error("Proxy has been released and is not useable")}function g(e){return w(e,new Map,{type:"RELEASE"}).then((()=>{u(e)}))}const v=new WeakMap,m="FinalizationRegistry"in globalThis&&new FinalizationRegistry((e=>{const t=(v.get(e)||0)-1;v.set(e,t),0===t&&g(e)}));function f(e,t,r=[],n=function(){}){let o=!1;const s=new Proxy(n,{get(n,a){if(h(o),a===i)return()=>{!function(e){m&&m.unregister(e)}(s),g(e),t.clear(),o=!0};if("then"===a){if(0===r.length)return{then:()=>s};const n=w(e,t,{type:"GET",path:r.map((e=>e.toString()))}).then(x);return n.then.bind(n)}return f(e,t,[...r,a])},set(n,a,i){h(o);const[s,l]=k(i);return w(e,t,{type:"SET",path:[...r,a].map((e=>e.toString())),value:s},l).then(x)},apply(n,i,s){h(o);const l=r[r.length-1];if(l===a)return w(e,t,{type:"ENDPOINT"}).then(x);if("bind"===l)return f(e,t,r.slice(0,-1));const[d,c]=b(s);return w(e,t,{type:"APPLY",path:r.map((e=>e.toString())),argumentList:d},c).then(x)},construct(n,a){h(o);const[i,s]=b(a);return w(e,t,{type:"CONSTRUCT",path:r.map((e=>e.toString())),argumentList:i},s).then(x)}});return function(e,t){const r=(v.get(t)||0)+1;v.set(t,r),m&&m.register(e,t,e)}(s,e),s}function b(e){const t=e.map(k);return[t.map((e=>e[0])),(r=t.map((e=>e[1])),Array.prototype.concat.apply([],r))];var r}const y=new WeakMap;function k(e){for(const[t,r]of d)if(r.canHandle(e)){const[n,a]=r.serialize(e);return[{type:"HANDLER",name:t,value:n},a]}return[{type:"RAW",value:e},y.get(e)||[]]}function x(e){switch(e.type){case"HANDLER":return d.get(e.name).deserialize(e.value);case"RAW":return e.value}}function w(e,t,r,n){return new Promise((a=>{const i=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");t.set(i,a),e.start&&e.start(),e.postMessage(Object.assign({id:i},r),n)}))}}}]);
//# sourceMappingURL=7634.dc5d21a52d88b0a6.js.map