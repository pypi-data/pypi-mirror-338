/*! For license information please see 7634.57088be2accf7349.js.LICENSE.txt */
export const __webpack_ids__=["7634"];export const __webpack_modules__={47899:function(e,t,r){r.d(t,{Bt:()=>o});var n=r(88977),a=r(59176);const i=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"],o=e=>e.first_weekday===a.FS.language?"weekInfo"in Intl.Locale.prototype?new Intl.Locale(e.language).weekInfo.firstDay%7:(0,n.L)(e.language)%7:i.includes(e.first_weekday)?i.indexOf(e.first_weekday):1},52258:function(e,t,r){r.a(e,(async function(e,n){try{r.d(t,{G:()=>d});var a=r(69440),i=r(27486),o=r(66045),s=e([a,o]);[a,o]=s.then?(await s)():s;const l=(0,i.Z)((e=>new Intl.RelativeTimeFormat(e.language,{numeric:"auto"}))),d=(e,t,r,n=!0)=>{const a=(0,o.W)(e,r,t);return n?l(t).format(a.value,a.unit):Intl.NumberFormat(t.language,{style:"unit",unit:a.unit,unitDisplay:"long"}).format(Math.abs(a.value))};n()}catch(l){n(l)}}))},66045:function(e,t,r){r.a(e,(async function(e,n){try{r.d(t,{W:()=>p});var a=r(13809),i=r(29558),o=r(57829),s=r(47899);const d=1e3,c=60,u=60*c;function p(e,t=Date.now(),r,n={}){const l={...h,...n||{}},p=(+e-+t)/d;if(Math.abs(p)<l.second)return{value:Math.round(p),unit:"second"};const g=p/c;if(Math.abs(g)<l.minute)return{value:Math.round(g),unit:"minute"};const m=p/u;if(Math.abs(m)<l.hour)return{value:Math.round(m),unit:"hour"};const v=new Date(e),f=new Date(t);v.setHours(0,0,0,0),f.setHours(0,0,0,0);const y=(0,a.j)(v,f);if(0===y)return{value:Math.round(m),unit:"hour"};if(Math.abs(y)<l.day)return{value:y,unit:"day"};const b=(0,s.Bt)(r),k=(0,i.z)(v,{weekStartsOn:b}),x=(0,i.z)(f,{weekStartsOn:b}),w=(0,o.p)(k,x);if(0===w)return{value:y,unit:"day"};if(Math.abs(w)<l.week)return{value:w,unit:"week"};const _=v.getFullYear()-f.getFullYear(),$=12*_+v.getMonth()-f.getMonth();return 0===$?{value:w,unit:"week"}:Math.abs($)<l.month||0===_?{value:$,unit:"month"}:{value:Math.round(_),unit:"year"}}const h={second:45,minute:45,hour:22,day:5,week:4,month:11};n()}catch(l){n(l)}}))},43527:function(e,t,r){var n=r(44249),a=r(72621),i=(r(22997),r(57243)),o=r(50778),s=r(80155),l=r(24067);(0,n.Z)([(0,o.Mo)("ha-button-menu")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",key:l.gA,value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"corner",value(){return"BOTTOM_START"}},{kind:"field",decorators:[(0,o.Cb)({attribute:"menu-corner"})],key:"menuCorner",value(){return"START"}},{kind:"field",decorators:[(0,o.Cb)({type:Number})],key:"x",value(){return null}},{kind:"field",decorators:[(0,o.Cb)({type:Number})],key:"y",value(){return null}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"multi",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"activatable",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"fixed",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean,attribute:"no-anchor"})],key:"noAnchor",value(){return!1}},{kind:"field",decorators:[(0,o.IO)("mwc-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){return this._menu?.items}},{kind:"get",key:"selected",value:function(){return this._menu?.selected}},{kind:"method",key:"focus",value:function(){this._menu?.open?this._menu.focusItemAtIndex(0):this._triggerButton?.focus()}},{kind:"method",key:"render",value:function(){return i.dy`
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
    `}},{kind:"method",key:"firstUpdated",value:function(e){(0,a.Z)(r,"firstUpdated",this,3)([e]),"rtl"===s.E.document.dir&&this.updateComplete.then((()=>{this.querySelectorAll("mwc-list-item").forEach((e=>{const t=document.createElement("style");t.innerHTML="span.material-icons:first-of-type { margin-left: var(--mdc-list-item-graphic-margin, 32px) !important; margin-right: 0px !important;}",e.shadowRoot.appendChild(t)}))}))}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchor=this.noAnchor?null:this,this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"field",static:!0,key:"styles",value(){return i.iv`
    :host {
      display: inline-block;
      position: relative;
    }
    ::slotted([disabled]) {
      color: var(--disabled-text-color);
    }
  `}}]}}),i.oi)},1192:function(e,t,r){var n=r(44249),a=r(57243),i=r(50778);(0,n.Z)([(0,i.Mo)("ha-card")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,i.Cb)()],key:"header",value:void 0},{kind:"field",decorators:[(0,i.Cb)({type:Boolean,reflect:!0})],key:"raised",value(){return!1}},{kind:"field",static:!0,key:"styles",value(){return a.iv`
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
  `}},{kind:"method",key:"render",value:function(){return a.dy`
      ${this.header?a.dy`<h1 class="card-header">${this.header}</h1>`:a.Ld}
      <slot></slot>
    `}}]}}),a.oi)},65099:function(e,t,r){r.a(e,(async function(e,n){try{r.r(t),r.d(t,{HaIconOverflowMenu:()=>p});var a=r(44249),i=r(57243),o=r(50778),s=r(35359),l=r(66193),d=(r(43527),r(59897),r(74064),r(10508),r(20418)),c=e([d]);d=(c.then?(await c)():c)[0];const u="M12,16A2,2 0 0,1 14,18A2,2 0 0,1 12,20A2,2 0 0,1 10,18A2,2 0 0,1 12,16M12,10A2,2 0 0,1 14,12A2,2 0 0,1 12,14A2,2 0 0,1 10,12A2,2 0 0,1 12,10M12,4A2,2 0 0,1 14,6A2,2 0 0,1 12,8A2,2 0 0,1 10,6A2,2 0 0,1 12,4Z";let p=(0,a.Z)([(0,o.Mo)("ha-icon-overflow-menu")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Array})],key:"items",value(){return[]}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"narrow",value(){return!1}},{kind:"method",key:"render",value:function(){return i.dy`
      ${this.narrow?i.dy` <!-- Collapsed representation for small screens -->
            <ha-button-menu
              @click=${this._handleIconOverflowMenuOpened}
              @closed=${this._handleIconOverflowMenuClosed}
              class="ha-icon-overflow-menu-overflow"
              absolute
            >
              <ha-icon-button
                .label=${this.hass.localize("ui.common.overflow_menu")}
                .path=${u}
                slot="trigger"
              ></ha-icon-button>

              ${this.items.map((e=>e.divider?i.dy`<li divider role="separator"></li>`:i.dy`<ha-list-item
                      graphic="icon"
                      ?disabled=${e.disabled}
                      @click=${e.action}
                      class=${(0,s.$)({warning:Boolean(e.warning)})}
                    >
                      <div slot="graphic">
                        <ha-svg-icon
                          class=${(0,s.$)({warning:Boolean(e.warning)})}
                          .path=${e.path}
                        ></ha-svg-icon>
                      </div>
                      ${e.label}
                    </ha-list-item> `))}
            </ha-button-menu>`:i.dy`
            <!-- Icon representation for big screens -->
            ${this.items.map((e=>e.narrowOnly?i.Ld:e.divider?i.dy`<div role="separator"></div>`:i.dy`<ha-tooltip
                      .disabled=${!e.tooltip}
                      .content=${e.tooltip??""}
                    >
                      <ha-icon-button
                        @click=${e.action}
                        .label=${e.label}
                        .path=${e.path}
                        ?disabled=${e.disabled}
                      ></ha-icon-button>
                    </ha-tooltip>`))}
          `}
    `}},{kind:"method",key:"_handleIconOverflowMenuOpened",value:function(e){e.stopPropagation();const t=this.closest(".mdc-data-table__row");t&&(t.style.zIndex="1")}},{kind:"method",key:"_handleIconOverflowMenuClosed",value:function(){const e=this.closest(".mdc-data-table__row");e&&(e.style.zIndex="")}},{kind:"get",static:!0,key:"styles",value:function(){return[l.Qx,i.iv`
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
      `]}}]}}),i.oi);n()}catch(u){n(u)}}))},74064:function(e,t,r){var n=r(44249),a=r(72621),i=r(65703),o=r(46289),s=r(57243),l=r(50778);(0,n.Z)([(0,l.Mo)("ha-list-item")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"method",key:"renderRipple",value:function(){return this.noninteractive?"":(0,a.Z)(r,"renderRipple",this,3)([])}},{kind:"get",static:!0,key:"styles",value:function(){return[o.W,s.iv`
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
      `,"rtl"===document.dir?s.iv`
            span.material-icons:first-of-type,
            span.material-icons:last-of-type {
              direction: rtl !important;
              --direction: rtl;
            }
          `:s.iv``]}}]}}),i.K)},20418:function(e,t,r){r.a(e,(async function(e,t){try{var n=r(44249),a=r(80519),i=r(1261),o=r(57243),s=r(50778),l=r(85605),d=e([a]);a=(d.then?(await d)():d)[0],(0,l.jx)("tooltip.show",{keyframes:[{opacity:0},{opacity:1}],options:{duration:150,easing:"ease"}}),(0,l.jx)("tooltip.hide",{keyframes:[{opacity:1},{opacity:0}],options:{duration:400,easing:"ease"}});(0,n.Z)([(0,s.Mo)("ha-tooltip")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",static:!0,key:"styles",value(){return[i.Z,o.iv`
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
    `]}}]}}),a.Z);t()}catch(c){t(c)}}))},59176:function(e,t,r){r.d(t,{FS:()=>s,c_:()=>i,t6:()=>o,y4:()=>n,zt:()=>a});let n=function(e){return e.language="language",e.system="system",e.comma_decimal="comma_decimal",e.decimal_comma="decimal_comma",e.space_comma="space_comma",e.none="none",e}({}),a=function(e){return e.language="language",e.system="system",e.am_pm="12",e.twenty_four="24",e}({}),i=function(e){return e.local="local",e.server="server",e}({}),o=function(e){return e.language="language",e.system="system",e.DMY="DMY",e.MDY="MDY",e.YMD="YMD",e}({}),s=function(e){return e.language="language",e.monday="monday",e.tuesday="tuesday",e.wednesday="wednesday",e.thursday="thursday",e.friday="friday",e.saturday="saturday",e.sunday="sunday",e}({})},89595:function(e,t,r){r.d(t,{q:()=>d});const n=/^[v^~<>=]*?(\d+)(?:\.([x*]|\d+)(?:\.([x*]|\d+)(?:\.([x*]|\d+))?(?:-([\da-z\-]+(?:\.[\da-z\-]+)*))?(?:\+[\da-z\-]+(?:\.[\da-z\-]+)*)?)?)?$/i,a=e=>{if("string"!=typeof e)throw new TypeError("Invalid argument expected string");const t=e.match(n);if(!t)throw new Error(`Invalid argument not valid semver ('${e}' received)`);return t.shift(),t},i=e=>"*"===e||"x"===e||"X"===e,o=e=>{const t=parseInt(e,10);return isNaN(t)?e:t},s=(e,t)=>{if(i(e)||i(t))return 0;const[r,n]=((e,t)=>typeof e!=typeof t?[String(e),String(t)]:[e,t])(o(e),o(t));return r>n?1:r<n?-1:0},l=(e,t)=>{for(let r=0;r<Math.max(e.length,t.length);r++){const n=s(e[r]||"0",t[r]||"0");if(0!==n)return n}return 0},d=(e,t,r)=>{p(r);const n=((e,t)=>{const r=a(e),n=a(t),i=r.pop(),o=n.pop(),s=l(r,n);return 0!==s?s:i&&o?l(i.split("."),o.split(".")):i||o?i?-1:1:0})(e,t);return c[r].includes(n)},c={">":[1],">=":[0,1],"=":[0],"<=":[-1,0],"<":[-1],"!=":[-1,1]},u=Object.keys(c),p=e=>{if("string"!=typeof e)throw new TypeError("Invalid operator type, expected string but got "+typeof e);if(-1===u.indexOf(e))throw new Error(`Invalid operator, expected one of ${u.join("|")}`)}},12582:function(e,t,r){function n(e){if(!e||"object"!=typeof e)return e;if("[object Date]"==Object.prototype.toString.call(e))return new Date(e.getTime());if(Array.isArray(e))return e.map(n);var t={};return Object.keys(e).forEach((function(r){t[r]=n(e[r])})),t}r.d(t,{Z:()=>n})},94964:function(e,t,r){var n=r(44249),a=r(72621),i=r(57243),o=r(50778),s=r(35359),l=r(11297);const d=new(r(57586).r)("knx-project-tree-view");(0,n.Z)([(0,o.Mo)("knx-project-tree-view")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"multiselect",value(){return!1}},{kind:"field",decorators:[(0,o.SB)()],key:"_selectableRanges",value(){return{}}},{kind:"method",key:"connectedCallback",value:function(){(0,a.Z)(r,"connectedCallback",this,3)([]);const e=t=>{Object.entries(t).forEach((([t,r])=>{r.group_addresses.length>0&&(this._selectableRanges[t]={selected:!1,groupAddresses:r.group_addresses}),e(r.group_ranges)}))};e(this.data.group_ranges),d.debug("ranges",this._selectableRanges)}},{kind:"method",key:"render",value:function(){return i.dy`<div class="ha-tree-view">${this._recurseData(this.data.group_ranges)}</div>`}},{kind:"method",key:"_recurseData",value:function(e,t=0){const r=Object.entries(e).map((([e,r])=>{const n=Object.keys(r.group_ranges).length>0;if(!(n||r.group_addresses.length>0))return i.Ld;const a=e in this._selectableRanges,o=!!a&&this._selectableRanges[e].selected,l={"range-item":!0,"root-range":0===t,"sub-range":t>0,selectable:a,"selected-range":o,"non-selected-range":a&&!o},d=i.dy`<div
        class=${(0,s.$)(l)}
        toggle-range=${a?e:i.Ld}
        @click=${a?this.multiselect?this._selectionChangedMulti:this._selectionChangedSingle:i.Ld}
      >
        <span class="range-key">${e}</span>
        <span class="range-text">${r.name}</span>
      </div>`;if(n){const e={"root-group":0===t,"sub-group":0!==t};return i.dy`<div class=${(0,s.$)(e)}>
          ${d} ${this._recurseData(r.group_ranges,t+1)}
        </div>`}return i.dy`${d}`}));return i.dy`${r}`}},{kind:"method",key:"_selectionChangedMulti",value:function(e){const t=e.target.getAttribute("toggle-range");this._selectableRanges[t].selected=!this._selectableRanges[t].selected,this._selectionUpdate(),this.requestUpdate()}},{kind:"method",key:"_selectionChangedSingle",value:function(e){const t=e.target.getAttribute("toggle-range"),r=this._selectableRanges[t].selected;Object.values(this._selectableRanges).forEach((e=>{e.selected=!1})),this._selectableRanges[t].selected=!r,this._selectionUpdate(),this.requestUpdate()}},{kind:"method",key:"_selectionUpdate",value:function(){const e=Object.values(this._selectableRanges).reduce(((e,t)=>t.selected?e.concat(t.groupAddresses):e),[]);d.debug("selection changed",e),(0,l.B)(this,"knx-group-range-selection-changed",{groupAddresses:e})}},{kind:"field",static:!0,key:"styles",value(){return i.iv`
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
  `}}]}}),i.oi)},88769:function(e,t,r){r.d(t,{W:()=>i,f:()=>a});var n=r(76848);const a={payload:e=>null==e.payload?"":Array.isArray(e.payload)?e.payload.reduce(((e,t)=>e+t.toString(16).padStart(2,"0")),"0x"):e.payload.toString(),valueWithUnit:e=>null==e.value?"":"number"==typeof e.value||"boolean"==typeof e.value||"string"==typeof e.value?e.value.toString()+(e.unit?" "+e.unit:""):(0,n.$w)(e.value),timeWithMilliseconds:e=>new Date(e.timestamp).toLocaleTimeString(["en-US"],{hour12:!1,hour:"2-digit",minute:"2-digit",second:"2-digit",fractionalSecondDigits:3}),dateWithMilliseconds:e=>new Date(e.timestamp).toLocaleTimeString([],{year:"numeric",month:"2-digit",day:"2-digit",hour:"2-digit",minute:"2-digit",second:"2-digit",fractionalSecondDigits:3}),dptNumber:e=>null==e.dpt_main?"":null==e.dpt_sub?e.dpt_main.toString():e.dpt_main.toString()+"."+e.dpt_sub.toString().padStart(3,"0"),dptNameNumber:e=>{const t=a.dptNumber(e);return null==e.dpt_name?`DPT ${t}`:t?`DPT ${t} ${e.dpt_name}`:e.dpt_name}},i=e=>null==e?"":e.main+(e.sub?"."+e.sub.toString().padStart(3,"0"):"")},53463:function(e,t,r){r.a(e,(async function(e,n){try{r.r(t),r.d(t,{KNXProjectView:()=>w});var a=r(44249),i=r(72621),o=r(57243),s=r(50778),l=r(27486),d=r(64364),c=r(68455),u=(r(32422),r(1192),r(59897),r(65099)),p=(r(26299),r(52258)),h=(r(94964),r(89595)),g=r(57259),m=r(57586),v=r(88769),f=e([c,u,p]);[c,u,p]=f.then?(await f)():f;const y="M6,13H18V11H6M3,6V8H21V6M10,18H14V16H10V18Z",b="M19,13H13V19H11V13H5V11H11V5H13V11H19V13Z",k=new m.r("knx-project-view"),x="3.3.0";let w=(0,a.Z)([(0,s.Mo)("knx-project-view")],(function(e,t){class r extends t{constructor(...t){super(...t),e(this)}}return{F:r,d:[{kind:"field",decorators:[(0,s.Cb)({type:Object})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"knx",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean,reflect:!0})],key:"narrow",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Object})],key:"route",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Array,reflect:!1})],key:"tabs",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean,reflect:!0,attribute:"range-selector-hidden"})],key:"rangeSelectorHidden",value(){return!0}},{kind:"field",decorators:[(0,s.SB)()],key:"_visibleGroupAddresses",value(){return[]}},{kind:"field",decorators:[(0,s.SB)()],key:"_groupRangeAvailable",value(){return!1}},{kind:"field",decorators:[(0,s.SB)()],key:"_subscribed",value:void 0},{kind:"field",decorators:[(0,s.SB)()],key:"_lastTelegrams",value(){return{}}},{kind:"method",key:"disconnectedCallback",value:function(){(0,i.Z)(r,"disconnectedCallback",this,3)([]),this._subscribed&&(this._subscribed(),this._subscribed=void 0)}},{kind:"method",key:"firstUpdated",value:async function(){this.knx.project?this._isGroupRangeAvailable():this.knx.loadProject().then((()=>{this._isGroupRangeAvailable(),this.requestUpdate()})),(0,g.ze)(this.hass).then((e=>{this._lastTelegrams=e})).catch((e=>{k.error("getGroupTelegrams",e),(0,d.c)("/knx/error",{replace:!0,data:e})})),this._subscribed=await(0,g.IP)(this.hass,(e=>{this.telegram_callback(e)}))}},{kind:"method",key:"_isGroupRangeAvailable",value:function(){const e=this.knx.project?.knxproject.info.xknxproject_version??"0.0.0";k.debug("project version: "+e),this._groupRangeAvailable=(0,h.q)(e,x,">=")}},{kind:"method",key:"telegram_callback",value:function(e){this._lastTelegrams={...this._lastTelegrams,[e.destination]:e}}},{kind:"field",key:"_columns",value(){return(0,l.Z)(((e,t)=>({address:{filterable:!0,sortable:!0,title:this.knx.localize("project_view_table_address"),flex:1,minWidth:"100px"},name:{filterable:!0,sortable:!0,title:this.knx.localize("project_view_table_name"),flex:3},dpt:{sortable:!0,filterable:!0,title:this.knx.localize("project_view_table_dpt"),flex:1,minWidth:"82px",template:e=>e.dpt?o.dy`<span style="display:inline-block;width:24px;text-align:right;"
                  >${e.dpt.main}</span
                >${e.dpt.sub?"."+e.dpt.sub.toString().padStart(3,"0"):""} `:""},lastValue:{filterable:!0,title:this.knx.localize("project_view_table_last_value"),flex:2,template:e=>{const t=this._lastTelegrams[e.address];if(!t)return"";const r=v.f.payload(t);return null==t.value?o.dy`<code>${r}</code>`:o.dy`<div title=${r}>
            ${v.f.valueWithUnit(this._lastTelegrams[e.address])}
          </div>`}},updated:{title:this.knx.localize("project_view_table_updated"),flex:1,showNarrow:!1,template:e=>{const t=this._lastTelegrams[e.address];if(!t)return"";const r=`${v.f.dateWithMilliseconds(t)}\n\n${t.source} ${t.source_name}`;return o.dy`<div title=${r}>
            ${(0,p.G)(new Date(t.timestamp),this.hass.locale)}
          </div>`}},actions:{title:"",minWidth:"72px",type:"overflow-menu",template:e=>this._groupAddressMenu(e)}})))}},{kind:"method",key:"_groupAddressMenu",value:function(e){const t=[];return 1===e.dpt?.main&&t.push({path:b,label:"Create binary sensor",action:()=>{(0,d.c)("/knx/entities/create/binary_sensor?knx.ga_sensor.state="+e.address)}}),t.length?o.dy`
          <ha-icon-overflow-menu .hass=${this.hass} narrow .items=${t}> </ha-icon-overflow-menu>
        `:o.Ld}},{kind:"method",key:"_getRows",value:function(e){return e.length?Object.entries(this.knx.project.knxproject.group_addresses).reduce(((t,[r,n])=>(e.includes(r)&&t.push(n),t)),[]):Object.values(this.knx.project.knxproject.group_addresses)}},{kind:"method",key:"_visibleAddressesChanged",value:function(e){this._visibleGroupAddresses=e.detail.groupAddresses}},{kind:"method",key:"render",value:function(){if(!this.hass||!this.knx.project)return o.dy` <hass-loading-screen></hass-loading-screen> `;const e=this._getRows(this._visibleGroupAddresses);return o.dy`
      <hass-tabs-subpage
        .hass=${this.hass}
        .narrow=${this.narrow}
        .route=${this.route}
        .tabs=${this.tabs}
        .localizeFunc=${this.knx.localize}
      >
        ${this.knx.project.project_loaded?o.dy`${this.narrow&&this._groupRangeAvailable?o.dy`<ha-icon-button
                    slot="toolbar-icon"
                    .label=${this.hass.localize("ui.components.related-filter-menu.filter")}
                    .path=${y}
                    @click=${this._toggleRangeSelector}
                  ></ha-icon-button>`:o.Ld}
              <div class="sections">
                ${this._groupRangeAvailable?o.dy`
                      <knx-project-tree-view
                        .data=${this.knx.project.knxproject}
                        @knx-group-range-selection-changed=${this._visibleAddressesChanged}
                      ></knx-project-tree-view>
                    `:o.Ld}
                <ha-data-table
                  class="ga-table"
                  .hass=${this.hass}
                  .columns=${this._columns(this.narrow,this.hass.language)}
                  .data=${e}
                  .hasFab=${!1}
                  .searchLabel=${this.hass.localize("ui.components.data-table.search")}
                  .clickable=${!1}
                ></ha-data-table>
              </div>`:o.dy` <ha-card .header=${this.knx.localize("attention")}>
              <div class="card-content">
                <p>${this.knx.localize("project_view_upload")}</p>
              </div>
            </ha-card>`}
      </hass-tabs-subpage>
    `}},{kind:"method",key:"_toggleRangeSelector",value:function(){this.rangeSelectorHidden=!this.rangeSelectorHidden}},{kind:"field",static:!0,key:"styles",value(){return o.iv`
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
  `}}]}}),o.oi);n()}catch(y){n(y)}}))},75351:function(e,t,r){r.d(t,{Ud:()=>p});const n=Symbol("Comlink.proxy"),a=Symbol("Comlink.endpoint"),i=Symbol("Comlink.releaseProxy"),o=Symbol("Comlink.finalizer"),s=Symbol("Comlink.thrown"),l=e=>"object"==typeof e&&null!==e||"function"==typeof e,d=new Map([["proxy",{canHandle:e=>l(e)&&e[n],serialize(e){const{port1:t,port2:r}=new MessageChannel;return c(e,t),[r,[r]]},deserialize(e){return e.start(),p(e)}}],["throw",{canHandle:e=>l(e)&&s in e,serialize({value:e}){let t;return t=e instanceof Error?{isError:!0,value:{message:e.message,name:e.name,stack:e.stack}}:{isError:!1,value:e},[t,[]]},deserialize(e){if(e.isError)throw Object.assign(new Error(e.value.message),e.value);throw e.value}}]]);function c(e,t=globalThis,r=["*"]){t.addEventListener("message",(function a(i){if(!i||!i.data)return;if(!function(e,t){for(const r of e){if(t===r||"*"===r)return!0;if(r instanceof RegExp&&r.test(t))return!0}return!1}(r,i.origin))return void console.warn(`Invalid origin '${i.origin}' for comlink proxy`);const{id:l,type:d,path:p}=Object.assign({path:[]},i.data),h=(i.data.argumentList||[]).map(x);let g;try{const t=p.slice(0,-1).reduce(((e,t)=>e[t]),e),r=p.reduce(((e,t)=>e[t]),e);switch(d){case"GET":g=r;break;case"SET":t[p.slice(-1)[0]]=x(i.data.value),g=!0;break;case"APPLY":g=r.apply(t,h);break;case"CONSTRUCT":g=function(e){return Object.assign(e,{[n]:!0})}(new r(...h));break;case"ENDPOINT":{const{port1:t,port2:r}=new MessageChannel;c(e,r),g=function(e,t){return b.set(e,t),e}(t,[t])}break;case"RELEASE":g=void 0;break;default:return}}catch(m){g={value:m,[s]:0}}Promise.resolve(g).catch((e=>({value:e,[s]:0}))).then((r=>{const[n,i]=k(r);t.postMessage(Object.assign(Object.assign({},n),{id:l}),i),"RELEASE"===d&&(t.removeEventListener("message",a),u(t),o in e&&"function"==typeof e[o]&&e[o]())})).catch((e=>{const[r,n]=k({value:new TypeError("Unserializable return value"),[s]:0});t.postMessage(Object.assign(Object.assign({},r),{id:l}),n)}))})),t.start&&t.start()}function u(e){(function(e){return"MessagePort"===e.constructor.name})(e)&&e.close()}function p(e,t){const r=new Map;return e.addEventListener("message",(function(e){const{data:t}=e;if(!t||!t.id)return;const n=r.get(t.id);if(n)try{n(t)}finally{r.delete(t.id)}})),f(e,r,[],t)}function h(e){if(e)throw new Error("Proxy has been released and is not useable")}function g(e){return w(e,new Map,{type:"RELEASE"}).then((()=>{u(e)}))}const m=new WeakMap,v="FinalizationRegistry"in globalThis&&new FinalizationRegistry((e=>{const t=(m.get(e)||0)-1;m.set(e,t),0===t&&g(e)}));function f(e,t,r=[],n=function(){}){let o=!1;const s=new Proxy(n,{get(n,a){if(h(o),a===i)return()=>{!function(e){v&&v.unregister(e)}(s),g(e),t.clear(),o=!0};if("then"===a){if(0===r.length)return{then:()=>s};const n=w(e,t,{type:"GET",path:r.map((e=>e.toString()))}).then(x);return n.then.bind(n)}return f(e,t,[...r,a])},set(n,a,i){h(o);const[s,l]=k(i);return w(e,t,{type:"SET",path:[...r,a].map((e=>e.toString())),value:s},l).then(x)},apply(n,i,s){h(o);const l=r[r.length-1];if(l===a)return w(e,t,{type:"ENDPOINT"}).then(x);if("bind"===l)return f(e,t,r.slice(0,-1));const[d,c]=y(s);return w(e,t,{type:"APPLY",path:r.map((e=>e.toString())),argumentList:d},c).then(x)},construct(n,a){h(o);const[i,s]=y(a);return w(e,t,{type:"CONSTRUCT",path:r.map((e=>e.toString())),argumentList:i},s).then(x)}});return function(e,t){const r=(m.get(t)||0)+1;m.set(t,r),v&&v.register(e,t,e)}(s,e),s}function y(e){const t=e.map(k);return[t.map((e=>e[0])),(r=t.map((e=>e[1])),Array.prototype.concat.apply([],r))];var r}const b=new WeakMap;function k(e){for(const[t,r]of d)if(r.canHandle(e)){const[n,a]=r.serialize(e);return[{type:"HANDLER",name:t,value:n},a]}return[{type:"RAW",value:e},b.get(e)||[]]}function x(e){switch(e.type){case"HANDLER":return d.get(e.name).deserialize(e.value);case"RAW":return e.value}}function w(e,t,r,n){return new Promise((a=>{const i=new Array(4).fill(0).map((()=>Math.floor(Math.random()*Number.MAX_SAFE_INTEGER).toString(16))).join("-");t.set(i,a),e.start&&e.start(),e.postMessage(Object.assign({id:i},r),n)}))}}};
//# sourceMappingURL=7634.57088be2accf7349.js.map