/*! For license information please see 8503.7a7dfd67671209e9.js.LICENSE.txt */
export const __webpack_ids__=["8503"];export const __webpack_modules__={46784:function(e,t,i){i.a(e,(async function(e,a){try{i.d(t,{u:()=>s});var o=i(69440),n=i(27486),r=e([o]);o=(r.then?(await r)():r)[0];const s=(e,t)=>{try{return d(t)?.of(e)??e}catch{return e}},d=(0,n.Z)((e=>new Intl.DisplayNames(e.language,{type:"language",fallback:"code"})));a()}catch(s){a(s)}}))},85690:function(e,t,i){i.d(t,{v:()=>a});const a=async(e,t)=>{if(navigator.clipboard)try{return void(await navigator.clipboard.writeText(e))}catch{}const i=t??document.body,a=document.createElement("textarea");a.value=e,i.appendChild(a),a.select(),document.execCommand("copy"),i.removeChild(a)}},24022:function(e,t,i){i.a(e,(async function(e,t){try{var a=i(44249),o=i(72621),n=i(57243),r=i(50778),s=i(11297),d=i(81036),l=i(46784),c=i(4855),h=(i(74064),i(58130),e([l]));l=(h.then?(await h)():h)[0];const u="preferred",p="last_used";(0,a.Z)([(0,r.Mo)("ha-assist-pipeline-picker")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"includeLastUsed",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_pipelines",value:void 0},{kind:"field",decorators:[(0,r.SB)()],key:"_preferredPipeline",value(){return null}},{kind:"get",key:"_default",value:function(){return this.includeLastUsed?p:u}},{kind:"method",key:"render",value:function(){if(!this._pipelines)return n.Ld;const e=this.value??this._default;return n.dy`
      <ha-select
        .label=${this.label||this.hass.localize("ui.components.pipeline-picker.pipeline")}
        .value=${e}
        .required=${this.required}
        .disabled=${this.disabled}
        @selected=${this._changed}
        @closed=${d.U}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${this.includeLastUsed?n.dy`
              <ha-list-item .value=${p}>
                ${this.hass.localize("ui.components.pipeline-picker.last_used")}
              </ha-list-item>
            `:null}
        <ha-list-item .value=${u}>
          ${this.hass.localize("ui.components.pipeline-picker.preferred",{preferred:this._pipelines.find((e=>e.id===this._preferredPipeline))?.name})}
        </ha-list-item>
        ${this._pipelines.map((e=>n.dy`<ha-list-item .value=${e.id}>
              ${e.name}
              (${(0,l.u)(e.language,this.hass.locale)})
            </ha-list-item>`))}
      </ha-select>
    `}},{kind:"method",key:"firstUpdated",value:function(e){(0,o.Z)(i,"firstUpdated",this,3)([e]),(0,c.SC)(this.hass).then((e=>{this._pipelines=e.pipelines,this._preferredPipeline=e.preferred_pipeline}))}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    ha-select {
      width: 100%;
    }
  `}},{kind:"method",key:"_changed",value:function(e){const t=e.target;!this.hass||""===t.value||t.value===this.value||void 0===this.value&&t.value===this._default||(this.value=t.value===this._default?void 0:t.value,(0,s.B)(this,"value-changed",{value:this.value}))}}]}}),n.oi);t()}catch(u){t(u)}}))},56412:function(e,t,i){var a=i(44249),o=i(72621),n=i(57243),r=i(50778),s=i(27486),d=i(11297),l=i(81036);const c={key:"Mod-s",run:e=>((0,d.B)(e.dom,"editor-save"),!0)},h=e=>{const t=document.createElement("ha-icon");return t.icon=e.label,t};(0,a.Z)([(0,r.Mo)("ha-code-editor")],(function(e,t){class a extends t{constructor(...t){super(...t),e(this)}}return{F:a,d:[{kind:"field",key:"codemirror",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"mode",value(){return"yaml"}},{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"autofocus",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({attribute:"read-only",type:Boolean})],key:"readOnly",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"linewrap",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean,attribute:"autocomplete-entities"})],key:"autocompleteEntities",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean,attribute:"autocomplete-icons"})],key:"autocompleteIcons",value(){return!1}},{kind:"field",decorators:[(0,r.Cb)({type:Boolean})],key:"error",value(){return!1}},{kind:"field",decorators:[(0,r.SB)()],key:"_value",value(){return""}},{kind:"field",key:"_loadedCodeMirror",value:void 0},{kind:"field",key:"_iconList",value:void 0},{kind:"set",key:"value",value:function(e){this._value=e}},{kind:"get",key:"value",value:function(){return this.codemirror?this.codemirror.state.doc.toString():this._value}},{kind:"get",key:"hasComments",value:function(){if(!this.codemirror||!this._loadedCodeMirror)return!1;const e=this._loadedCodeMirror.highlightingFor(this.codemirror.state,[this._loadedCodeMirror.tags.comment]);return!!this.renderRoot.querySelector(`span.${e}`)}},{kind:"method",key:"connectedCallback",value:function(){(0,o.Z)(a,"connectedCallback",this,3)([]),this.hasUpdated&&this.requestUpdate(),this.addEventListener("keydown",l.U),this.codemirror&&!1!==this.autofocus&&this.codemirror.focus()}},{kind:"method",key:"disconnectedCallback",value:function(){(0,o.Z)(a,"disconnectedCallback",this,3)([]),this.removeEventListener("keydown",l.U),this.updateComplete.then((()=>{this.codemirror.destroy(),delete this.codemirror}))}},{kind:"method",key:"scheduleUpdate",value:async function(){this._loadedCodeMirror??=await Promise.all([i.e("7783"),i.e("2309")]).then(i.bind(i,51198)),(0,o.Z)(a,"scheduleUpdate",this,3)([])}},{kind:"method",key:"update",value:function(e){if((0,o.Z)(a,"update",this,3)([e]),!this.codemirror)return void this._createCodeMirror();const t=[];e.has("mode")&&t.push({effects:[this._loadedCodeMirror.langCompartment.reconfigure(this._mode),this._loadedCodeMirror.foldingCompartment.reconfigure(this._getFoldingExtensions())]}),e.has("readOnly")&&t.push({effects:this._loadedCodeMirror.readonlyCompartment.reconfigure(this._loadedCodeMirror.EditorView.editable.of(!this.readOnly))}),e.has("linewrap")&&t.push({effects:this._loadedCodeMirror.linewrapCompartment.reconfigure(this.linewrap?this._loadedCodeMirror.EditorView.lineWrapping:[])}),e.has("_value")&&this._value!==this.value&&t.push({changes:{from:0,to:this.codemirror.state.doc.length,insert:this._value}}),t.length>0&&this.codemirror.dispatch(...t),e.has("error")&&this.classList.toggle("error-state",this.error)}},{kind:"get",key:"_mode",value:function(){return this._loadedCodeMirror.langs[this.mode]}},{kind:"method",key:"_createCodeMirror",value:function(){if(!this._loadedCodeMirror)throw new Error("Cannot create editor before CodeMirror is loaded");const e=[this._loadedCodeMirror.lineNumbers(),this._loadedCodeMirror.history(),this._loadedCodeMirror.drawSelection(),this._loadedCodeMirror.EditorState.allowMultipleSelections.of(!0),this._loadedCodeMirror.rectangularSelection(),this._loadedCodeMirror.crosshairCursor(),this._loadedCodeMirror.highlightSelectionMatches(),this._loadedCodeMirror.highlightActiveLine(),this._loadedCodeMirror.indentationMarkers({thickness:0,activeThickness:1,colors:{activeLight:"var(--secondary-text-color)",activeDark:"var(--secondary-text-color)"}}),this._loadedCodeMirror.keymap.of([...this._loadedCodeMirror.defaultKeymap,...this._loadedCodeMirror.searchKeymap,...this._loadedCodeMirror.historyKeymap,...this._loadedCodeMirror.tabKeyBindings,c]),this._loadedCodeMirror.langCompartment.of(this._mode),this._loadedCodeMirror.haTheme,this._loadedCodeMirror.haSyntaxHighlighting,this._loadedCodeMirror.readonlyCompartment.of(this._loadedCodeMirror.EditorView.editable.of(!this.readOnly)),this._loadedCodeMirror.linewrapCompartment.of(this.linewrap?this._loadedCodeMirror.EditorView.lineWrapping:[]),this._loadedCodeMirror.EditorView.updateListener.of(this._onUpdate),this._loadedCodeMirror.foldingCompartment.of(this._getFoldingExtensions())];if(!this.readOnly){const t=[];this.autocompleteEntities&&this.hass&&t.push(this._entityCompletions.bind(this)),this.autocompleteIcons&&t.push(this._mdiCompletions.bind(this)),t.length>0&&e.push(this._loadedCodeMirror.autocompletion({override:t,maxRenderedOptions:10}))}this.codemirror=new this._loadedCodeMirror.EditorView({state:this._loadedCodeMirror.EditorState.create({doc:this._value,extensions:e}),parent:this.renderRoot})}},{kind:"field",key:"_getStates",value(){return(0,s.Z)((e=>{if(!e)return[];return Object.keys(e).map((t=>({type:"variable",label:t,detail:e[t].attributes.friendly_name,info:`State: ${e[t].state}`})))}))}},{kind:"method",key:"_entityCompletions",value:function(e){const t=e.matchBefore(/[a-z_]{3,}\.\w*/);if(!t||t.from===t.to&&!e.explicit)return null;const i=this._getStates(this.hass.states);return i&&i.length?{from:Number(t.from),options:i,validFor:/^[a-z_]{3,}\.\w*$/}:null}},{kind:"field",key:"_getIconItems",value(){return async()=>{if(!this._iconList){let e;e=(await i.e("4813").then(i.t.bind(i,81405,19))).default,this._iconList=e.map((e=>({type:"variable",label:`mdi:${e.name}`,detail:e.keywords.join(", "),info:h})))}return this._iconList}}},{kind:"method",key:"_mdiCompletions",value:async function(e){const t=e.matchBefore(/mdi:\S*/);if(!t||t.from===t.to&&!e.explicit)return null;const i=await this._getIconItems();return{from:Number(t.from),options:i,validFor:/^mdi:\S*$/}}},{kind:"field",key:"_onUpdate",value(){return e=>{e.docChanged&&(this._value=e.state.doc.toString(),(0,d.B)(this,"value-changed",{value:this._value}))}}},{kind:"field",key:"_getFoldingExtensions",value(){return()=>"yaml"===this.mode?[this._loadedCodeMirror.foldGutter(),this._loadedCodeMirror.foldingOnIndent]:[]}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    :host(.error-state) .cm-gutters {
      border-color: var(--error-state-color, red);
    }
  `}}]}}),n.fl)},86810:function(e,t,i){i.a(e,(async function(e,t){try{var a=i(44249),o=i(57243),n=i(50778),r=(i(10508),i(20418)),s=e([r]);r=(s.then?(await s)():s)[0];const d="M15.07,11.25L14.17,12.17C13.45,12.89 13,13.5 13,15H11V14.5C11,13.39 11.45,12.39 12.17,11.67L13.41,10.41C13.78,10.05 14,9.55 14,9C14,7.89 13.1,7 12,7A2,2 0 0,0 10,9H8A4,4 0 0,1 12,5A4,4 0 0,1 16,9C16,9.88 15.64,10.67 15.07,11.25M13,19H11V17H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12C22,6.47 17.5,2 12,2Z";(0,a.Z)([(0,n.Mo)("ha-help-tooltip")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"position",value(){return"top"}},{kind:"method",key:"render",value:function(){return o.dy`
      <ha-tooltip .placement=${this.position} .content=${this.label}>
        <ha-svg-icon .path=${d}></ha-svg-icon>
      </ha-tooltip>
    `}},{kind:"field",static:!0,key:"styles",value(){return o.iv`
    ha-svg-icon {
      --mdc-icon-size: var(--ha-help-tooltip-size, 14px);
      color: var(--ha-help-tooltip-color, var(--disabled-text-color));
    }
  `}}]}}),o.oi);t()}catch(d){t(d)}}))},5340:function(e,t,i){var a=i(44249),o=(i(87319),i(57243)),n=i(50778),r=i(11297);const s=e=>e.replace(/^_*(.)|_+(.)/g,((e,t,i)=>t?t.toUpperCase():" "+i.toUpperCase()));i(69484);const d=[],l=e=>o.dy`
  <mwc-list-item graphic="icon" .twoline=${!!e.title}>
    <ha-icon .icon=${e.icon} slot="graphic"></ha-icon>
    <span>${e.title||e.path}</span>
    <span slot="secondary">${e.path}</span>
  </mwc-list-item>
`,c=(e,t,i)=>({path:`/${e}/${t.path??i}`,icon:t.icon??"mdi:view-compact",title:t.title??(t.path?s(t.path):`${i}`)}),h=(e,t)=>({path:`/${t.url_path}`,icon:t.icon??"mdi:view-dashboard",title:t.url_path===e.defaultPanel?e.localize("panel.states"):e.localize(`panel.${t.title}`)||t.title||(t.url_path?s(t.url_path):"")});(0,a.Z)([(0,n.Mo)("ha-navigation-picker")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_opened",value(){return!1}},{kind:"field",key:"navigationItemsLoaded",value(){return!1}},{kind:"field",key:"navigationItems",value(){return d}},{kind:"field",decorators:[(0,n.IO)("ha-combo-box",!0)],key:"comboBox",value:void 0},{kind:"method",key:"render",value:function(){return o.dy`
      <ha-combo-box
        .hass=${this.hass}
        item-value-path="path"
        item-label-path="path"
        .value=${this._value}
        allow-custom-value
        .filteredItems=${this.navigationItems}
        .label=${this.label}
        .helper=${this.helper}
        .disabled=${this.disabled}
        .required=${this.required}
        .renderer=${l}
        @opened-changed=${this._openedChanged}
        @value-changed=${this._valueChanged}
        @filter-changed=${this._filterChanged}
      >
      </ha-combo-box>
    `}},{kind:"method",key:"_openedChanged",value:async function(e){this._opened=e.detail.value,this._opened&&!this.navigationItemsLoaded&&this._loadNavigationItems()}},{kind:"method",key:"_loadNavigationItems",value:async function(){this.navigationItemsLoaded=!0;const e=Object.entries(this.hass.panels).map((([e,t])=>({id:e,...t}))),t=e.filter((e=>"lovelace"===e.component_name)),i=await Promise.all(t.map((e=>{return(t=this.hass.connection,i="lovelace"===e.url_path?null:e.url_path,a=!0,t.sendMessagePromise({type:"lovelace/config",url_path:i,force:a})).then((t=>[e.id,t])).catch((t=>[e.id,void 0]));var t,i,a}))),a=new Map(i);this.navigationItems=[];for(const o of e){this.navigationItems.push(h(this.hass,o));const e=a.get(o.id);e&&"views"in e&&e.views.forEach(((e,t)=>this.navigationItems.push(c(o.url_path,e,t))))}this.comboBox.filteredItems=this.navigationItems}},{kind:"method",key:"shouldUpdate",value:function(e){return!this._opened||e.has("_opened")}},{kind:"method",key:"_valueChanged",value:function(e){e.stopPropagation(),this._setValue(e.detail.value)}},{kind:"method",key:"_setValue",value:function(e){this.value=e,(0,r.B)(this,"value-changed",{value:this._value},{bubbles:!1,composed:!1})}},{kind:"method",key:"_filterChanged",value:function(e){const t=e.detail.value.toLowerCase();if(t.length>=2){const e=[];this.navigationItems.forEach((i=>{(i.path.toLowerCase().includes(t)||i.title.toLowerCase().includes(t))&&e.push(i)})),e.length>0?this.comboBox.filteredItems=e:this.comboBox.filteredItems=[]}else this.comboBox.filteredItems=this.navigationItems}},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"field",static:!0,key:"styles",value(){return o.iv`
    ha-icon,
    ha-svg-icon {
      color: var(--primary-text-color);
      position: relative;
      bottom: 0px;
    }
    *[slot="prefix"] {
      margin-right: 8px;
      margin-inline-end: 8px;
      margin-inline-start: initial;
    }
  `}}]}}),o.oi)},63599:function(e,t,i){i.a(e,(async function(e,a){try{i.r(t),i.d(t,{HaSelectorUiAction:()=>c});var o=i(44249),n=i(57243),r=i(50778),s=i(11297),d=i(29524),l=e([d]);d=(l.then?(await l)():l)[0];let c=(0,o.Z)([(0,r.Mo)("ha-selector-ui_action")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"value",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,r.Cb)()],key:"helper",value:void 0},{kind:"method",key:"render",value:function(){return n.dy`
      <hui-action-editor
        .label=${this.label}
        .hass=${this.hass}
        .config=${this.value}
        .actions=${this.selector.ui_action?.actions}
        .defaultAction=${this.selector.ui_action?.default_action}
        .tooltipText=${this.helper}
        @value-changed=${this._valueChanged}
      ></hui-action-editor>
    `}},{kind:"method",key:"_valueChanged",value:function(e){(0,s.B)(this,"value-changed",{value:e.detail.value})}}]}}),n.oi);a()}catch(c){a(c)}}))},27196:function(e,t,i){var a=i(44249),o=i(72621),n=i(76848),r=i(57243),s=i(50778),d=i(11297),l=i(66193),c=(i(56412),i(46694)),h=i(85690);i(20095);(0,a.Z)([(0,s.Mo)("ha-yaml-editor")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"yamlSchema",value(){return n.oW}},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"defaultValue",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:"is-valid",type:Boolean})],key:"isValid",value(){return!0}},{kind:"field",decorators:[(0,s.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:"auto-update",type:Boolean})],key:"autoUpdate",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({attribute:"read-only",type:Boolean})],key:"readOnly",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({attribute:"copy-clipboard",type:Boolean})],key:"copyClipboard",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({attribute:"has-extra-actions",type:Boolean})],key:"hasExtraActions",value(){return!1}},{kind:"field",decorators:[(0,s.SB)()],key:"_yaml",value(){return""}},{kind:"field",decorators:[(0,s.IO)("ha-code-editor")],key:"_codeEditor",value:void 0},{kind:"method",key:"setValue",value:function(e){try{this._yaml=(e=>{if("object"!=typeof e||null===e)return!1;for(const t in e)if(Object.prototype.hasOwnProperty.call(e,t))return!1;return!0})(e)?"":(0,n.$w)(e,{schema:this.yamlSchema,quotingType:'"',noRefs:!0})}catch(t){console.error(t,e),alert(`There was an error converting to YAML: ${t}`)}}},{kind:"method",key:"firstUpdated",value:function(){void 0!==this.defaultValue&&this.setValue(this.defaultValue)}},{kind:"method",key:"willUpdate",value:function(e){(0,o.Z)(i,"willUpdate",this,3)([e]),this.autoUpdate&&e.has("value")&&this.setValue(this.value)}},{kind:"method",key:"focus",value:function(){this._codeEditor?.codemirror&&this._codeEditor?.codemirror.focus()}},{kind:"method",key:"render",value:function(){return void 0===this._yaml?r.Ld:r.dy`
      ${this.label?r.dy`<p>${this.label}${this.required?" *":""}</p>`:r.Ld}
      <ha-code-editor
        .hass=${this.hass}
        .value=${this._yaml}
        .readOnly=${this.readOnly}
        mode="yaml"
        autocomplete-entities
        autocomplete-icons
        .error=${!1===this.isValid}
        @value-changed=${this._onChange}
        dir="ltr"
      ></ha-code-editor>
      ${this.copyClipboard||this.hasExtraActions?r.dy`
            <div class="card-actions">
              ${this.copyClipboard?r.dy`
                    <ha-button @click=${this._copyYaml}>
                      ${this.hass.localize("ui.components.yaml-editor.copy_to_clipboard")}
                    </ha-button>
                  `:r.Ld}
              <slot name="extra-actions"></slot>
            </div>
          `:r.Ld}
    `}},{kind:"method",key:"_onChange",value:function(e){let t;e.stopPropagation(),this._yaml=e.detail.value;let i,a=!0;if(this._yaml)try{t=(0,n.zD)(this._yaml,{schema:this.yamlSchema})}catch(o){a=!1,i=`${this.hass.localize("ui.components.yaml-editor.error",{reason:o.reason})}${o.mark?` (${this.hass.localize("ui.components.yaml-editor.error_location",{line:o.mark.line+1,column:o.mark.column+1})})`:""}`}else t={};this.value=t,this.isValid=a,(0,d.B)(this,"value-changed",{value:t,isValid:a,errorMsg:i})}},{kind:"get",key:"yaml",value:function(){return this._yaml}},{kind:"method",key:"_copyYaml",value:async function(){this.yaml&&(await(0,h.v)(this.yaml),(0,c.C)(this,{message:this.hass.localize("ui.common.copied_clipboard")}))}},{kind:"get",static:!0,key:"styles",value:function(){return[l.Qx,r.iv`
        .card-actions {
          border-radius: var(
            --actions-border-radius,
            0px 0px var(--ha-card-border-radius, 12px)
              var(--ha-card-border-radius, 12px)
          );
          border: 1px solid var(--divider-color);
          padding: 5px 16px;
        }
        ha-code-editor {
          flex-grow: 1;
        }
      `]}}]}}),r.oi)},4855:function(e,t,i){i.d(t,{Dy:()=>l,PA:()=>r,SC:()=>n,Xp:()=>o,af:()=>d,eP:()=>a,jZ:()=>s});const a=(e,t,i)=>"run-start"===t.type?e={init_options:i,stage:"ready",run:t.data,events:[t]}:e?((e="wake_word-start"===t.type?{...e,stage:"wake_word",wake_word:{...t.data,done:!1}}:"wake_word-end"===t.type?{...e,wake_word:{...e.wake_word,...t.data,done:!0}}:"stt-start"===t.type?{...e,stage:"stt",stt:{...t.data,done:!1}}:"stt-end"===t.type?{...e,stt:{...e.stt,...t.data,done:!0}}:"intent-start"===t.type?{...e,stage:"intent",intent:{...t.data,done:!1}}:"intent-end"===t.type?{...e,intent:{...e.intent,...t.data,done:!0}}:"tts-start"===t.type?{...e,stage:"tts",tts:{...t.data,done:!1}}:"tts-end"===t.type?{...e,tts:{...e.tts,...t.data,done:!0}}:"run-end"===t.type?{...e,stage:"done"}:"error"===t.type?{...e,stage:"error",error:t.data}:{...e}).events=[...e.events,t],e):void console.warn("Received unexpected event before receiving session",t),o=(e,t,i)=>e.connection.subscribeMessage(t,{...i,type:"assist_pipeline/run"}),n=e=>e.callWS({type:"assist_pipeline/pipeline/list"}),r=(e,t)=>e.callWS({type:"assist_pipeline/pipeline/get",pipeline_id:t}),s=(e,t)=>e.callWS({type:"assist_pipeline/pipeline/create",...t}),d=(e,t,i)=>e.callWS({type:"assist_pipeline/pipeline/update",pipeline_id:t,...i}),l=e=>e.callWS({type:"assist_pipeline/language/list"})},1275:function(e,t,i){i.d(t,{F3:()=>o,Lh:()=>a,t4:()=>n});const a=(e,t,i)=>e(`component.${t}.title`)||i?.name||t,o=(e,t)=>{const i={type:"manifest/list"};return t&&(i.integrations=t),e.callWS(i)},n=(e,t)=>e.callWS({type:"manifest/get",integration:t})},29524:function(e,t,i){i.a(e,(async function(e,t){try{var a=i(44249),o=i(72621),n=i(57243),r=i(50778),s=i(27486),d=i(11297),l=i(81036),c=i(24022),h=i(86810),u=(i(5340),i(15606)),p=e([c,h,u]);[c,h,u]=p.then?(await p)():p;const v=["more-info","toggle","navigate","url","perform-action","assist","none"],f=[{name:"navigation_path",selector:{navigation:{}}}],m=[{type:"grid",name:"",schema:[{name:"pipeline_id",selector:{assist_pipeline:{include_last_used:!0}}},{name:"start_listening",selector:{boolean:{}}}]}];(0,a.Z)([(0,r.Mo)("hui-action-editor")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"config",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"label",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"actions",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"defaultAction",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"tooltipText",value:void 0},{kind:"field",decorators:[(0,r.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,r.IO)("ha-select")],key:"_select",value:void 0},{kind:"get",key:"_navigation_path",value:function(){const e=this.config;return e?.navigation_path||""}},{kind:"get",key:"_url_path",value:function(){const e=this.config;return e?.url_path||""}},{kind:"get",key:"_service",value:function(){const e=this.config;return e?.perform_action||e?.service||""}},{kind:"field",key:"_serviceAction",value(){return(0,s.Z)((e=>({action:this._service,...e.data||e.service_data?{data:e.data??e.service_data}:null,target:e.target})))}},{kind:"method",key:"updated",value:function(e){(0,o.Z)(i,"updated",this,3)([e]),e.has("defaultAction")&&e.get("defaultAction")!==this.defaultAction&&this._select.layoutOptions()}},{kind:"method",key:"render",value:function(){if(!this.hass)return n.Ld;const e=this.actions??v;let t=this.config?.action||"default";return"call-service"===t&&(t="perform-action"),n.dy`
      <div class="dropdown">
        <ha-select
          .label=${this.label}
          .configValue=${"action"}
          @selected=${this._actionPicked}
          .value=${t}
          @closed=${l.U}
          fixedMenuPosition
          naturalMenuWidt
        >
          <mwc-list-item value="default">
            ${this.hass.localize("ui.panel.lovelace.editor.action-editor.actions.default_action")}
            ${this.defaultAction?` (${this.hass.localize(`ui.panel.lovelace.editor.action-editor.actions.${this.defaultAction}`).toLowerCase()})`:n.Ld}
          </mwc-list-item>
          ${e.map((e=>n.dy`
              <mwc-list-item .value=${e}>
                ${this.hass.localize(`ui.panel.lovelace.editor.action-editor.actions.${e}`)}
              </mwc-list-item>
            `))}
        </ha-select>
        ${this.tooltipText?n.dy`
              <ha-help-tooltip .label=${this.tooltipText}></ha-help-tooltip>
            `:n.Ld}
      </div>
      ${"navigate"===this.config?.action?n.dy`
            <ha-form
              .hass=${this.hass}
              .schema=${f}
              .data=${this.config}
              .computeLabel=${this._computeFormLabel}
              @value-changed=${this._formValueChanged}
            >
            </ha-form>
          `:n.Ld}
      ${"url"===this.config?.action?n.dy`
            <ha-textfield
              .label=${this.hass.localize("ui.panel.lovelace.editor.action-editor.url_path")}
              .value=${this._url_path}
              .configValue=${"url_path"}
              @input=${this._valueChanged}
            ></ha-textfield>
          `:n.Ld}
      ${"call-service"===this.config?.action||"perform-action"===this.config?.action?n.dy`
            <ha-service-control
              .hass=${this.hass}
              .value=${this._serviceAction(this.config)}
              .showAdvanced=${this.hass.userData?.showAdvanced}
              narrow
              @value-changed=${this._serviceValueChanged}
            ></ha-service-control>
          `:n.Ld}
      ${"assist"===this.config?.action?n.dy`
            <ha-form
              .hass=${this.hass}
              .schema=${m}
              .data=${this.config}
              .computeLabel=${this._computeFormLabel}
              @value-changed=${this._formValueChanged}
            >
            </ha-form>
          `:n.Ld}
    `}},{kind:"method",key:"_actionPicked",value:function(e){if(e.stopPropagation(),!this.hass)return;let t=this.config?.action;"call-service"===t&&(t="perform-action");const i=e.target.value;if(t===i)return;if("default"===i)return void(0,d.B)(this,"value-changed",{value:void 0});let a;switch(i){case"url":a={url_path:this._url_path};break;case"perform-action":a={perform_action:this._service};break;case"navigate":a={navigation_path:this._navigation_path}}(0,d.B)(this,"value-changed",{value:{action:i,...a}})}},{kind:"method",key:"_valueChanged",value:function(e){if(e.stopPropagation(),!this.hass)return;const t=e.target,i=e.target.value??e.target.checked;this[`_${t.configValue}`]!==i&&t.configValue&&(0,d.B)(this,"value-changed",{value:{...this.config,[t.configValue]:i}})}},{kind:"method",key:"_formValueChanged",value:function(e){e.stopPropagation();const t=e.detail.value;(0,d.B)(this,"value-changed",{value:t})}},{kind:"method",key:"_computeFormLabel",value:function(e){return this.hass?.localize(`ui.panel.lovelace.editor.action-editor.${e.name}`)}},{kind:"method",key:"_serviceValueChanged",value:function(e){e.stopPropagation();const t={...this.config,action:"perform-action",perform_action:e.detail.value.action||"",data:e.detail.value.data,target:e.detail.value.target||{}};e.detail.value.data||delete t.data,"service_data"in t&&delete t.service_data,"service"in t&&delete t.service,(0,d.B)(this,"value-changed",{value:t})}},{kind:"field",static:!0,key:"styles",value(){return n.iv`
    .dropdown {
      position: relative;
    }
    ha-help-tooltip {
      position: absolute;
      right: 40px;
      top: 16px;
      inset-inline-start: initial;
      inset-inline-end: 40px;
      direction: var(--direction);
    }
    ha-select,
    ha-textfield {
      width: 100%;
    }
    ha-service-control,
    ha-navigation-picker,
    ha-form {
      display: block;
    }
    ha-textfield,
    ha-service-control,
    ha-navigation-picker,
    ha-form {
      margin-top: 8px;
    }
    ha-service-control {
      --service-control-padding: 0;
    }
    ha-formfield {
      display: flex;
      height: 56px;
      align-items: center;
      --mdc-typography-body2-font-size: 1em;
    }
  `}}]}}),n.oi);t()}catch(v){t(v)}}))},46694:function(e,t,i){i.d(t,{C:()=>o});var a=i(11297);const o=(e,t)=>(0,a.B)(e,"hass-notification",t)},94571:function(e,t,i){i.d(t,{C:()=>u});var a=i(2841),o=i(53232),n=i(1714);class r{constructor(e){this.G=e}disconnect(){this.G=void 0}reconnect(e){this.G=e}deref(){return this.G}}class s{constructor(){this.Y=void 0,this.Z=void 0}get(){return this.Y}pause(){var e;null!==(e=this.Y)&&void 0!==e||(this.Y=new Promise((e=>this.Z=e)))}resume(){var e;null===(e=this.Z)||void 0===e||e.call(this),this.Y=this.Z=void 0}}var d=i(45779);const l=e=>!(0,o.pt)(e)&&"function"==typeof e.then,c=1073741823;class h extends n.sR{constructor(){super(...arguments),this._$C_t=c,this._$Cwt=[],this._$Cq=new r(this),this._$CK=new s}render(...e){var t;return null!==(t=e.find((e=>!l(e))))&&void 0!==t?t:a.Jb}update(e,t){const i=this._$Cwt;let o=i.length;this._$Cwt=t;const n=this._$Cq,r=this._$CK;this.isConnected||this.disconnected();for(let a=0;a<t.length&&!(a>this._$C_t);a++){const e=t[a];if(!l(e))return this._$C_t=a,e;a<o&&e===i[a]||(this._$C_t=c,o=0,Promise.resolve(e).then((async t=>{for(;r.get();)await r.get();const i=n.deref();if(void 0!==i){const a=i._$Cwt.indexOf(e);a>-1&&a<i._$C_t&&(i._$C_t=a,i.setValue(t))}})))}return a.Jb}disconnected(){this._$Cq.disconnect(),this._$CK.pause()}reconnected(){this._$Cq.reconnect(this),this._$CK.resume()}}const u=(0,d.XM)(h)}};
//# sourceMappingURL=8503.7a7dfd67671209e9.js.map