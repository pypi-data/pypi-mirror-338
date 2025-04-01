export const __webpack_ids__=["4376"];export const __webpack_modules__={41800:function(e,t,i){i.r(t),i.d(t,{HaFormOptionalActions:()=>h});var a=i(44249),s=i(72621),o=i(57243),d=i(50778),n=i(27486),l=i(81036);i(42877);const c=[];let h=(0,a.Z)([(0,d.Mo)("ha-form-optional_actions")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"localize",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"data",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"schema",value:void 0},{kind:"field",decorators:[(0,d.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"computeLabel",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"computeHelper",value:void 0},{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"localizeValue",value:void 0},{kind:"field",decorators:[(0,d.SB)()],key:"_displayActions",value:void 0},{kind:"method",key:"focus",value:async function(){await this.updateComplete,this.renderRoot.querySelector("ha-form")?.focus()}},{kind:"method",key:"updated",value:function(e){if((0,s.Z)(i,"updated",this,3)([e]),e.has("data")){const e=this._displayActions??c,t=this._hiddenActions(this.schema.schema,e);this._displayActions=[...e,...t.filter((e=>e in this.data))]}}},{kind:"field",key:"_hiddenActions",value(){return(0,n.Z)(((e,t)=>e.map((e=>e.name)).filter((e=>!t.includes(e)))))}},{kind:"field",key:"_displaySchema",value(){return(0,n.Z)(((e,t)=>e.filter((e=>t.includes(e.name)))))}},{kind:"method",key:"render",value:function(){const e=this._displayActions??c,t=this._displaySchema(this.schema.schema,this._displayActions??[]),i=this._hiddenActions(this.schema.schema,e),a=new Map(this.computeLabel?this.schema.schema.map((e=>[e.name,e])):[]);return o.dy`
      ${t.length>0?o.dy`
            <ha-form
              .hass=${this.hass}
              .data=${this.data}
              .schema=${t}
              .disabled=${this.disabled}
              .computeLabel=${this.computeLabel}
              .computeHelper=${this.computeHelper}
              .localizeValue=${this.localizeValue}
            ></ha-form>
          `:o.Ld}
      ${i.length>0?o.dy`
            <ha-button-menu
              @action=${this._handleAddAction}
              fixed
              @closed=${l.U}
            >
              <ha-button slot="trigger">
                ${this.localize?.("ui.components.form-optional-actions.add")||"Add interaction"}
              </ha-button>
              ${i.map((e=>{const t=a.get(e);return o.dy`
                  <ha-list-item>
                    ${this.computeLabel&&t?this.computeLabel(t):e}
                  </ha-list-item>
                `}))}
            </ha-button-menu>
          `:o.Ld}
    `}},{kind:"method",key:"_handleAddAction",value:function(e){const t=this._hiddenActions(this.schema.schema,this._displayActions??c)[e.detail.index];this._displayActions=[...this._displayActions??[],t]}},{kind:"field",static:!0,key:"styles",value(){return o.iv`
    :host {
      display: flex !important;
      flex-direction: column;
      gap: 24px;
    }
    :host ha-form {
      display: block;
    }
  `}}]}}),o.oi)}};
//# sourceMappingURL=4376.d0786b9b3f2e1040.js.map