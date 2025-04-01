"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["7473"],{65735:function(e,a,t){t.a(e,(async function(e,i){try{t.r(a),t.d(a,{HaBackgroundSelector:()=>m});var o=t(73577),l=t(72621),r=(t(71695),t(88044),t(47021),t(57243)),n=t(50778),u=t(11297),d=t(10581),s=(t(17949),t(18727)),c=e([d]);d=(c.then?(await c)():c)[0];let h,v,p,k,y=e=>e,m=(0,o.Z)([(0,n.Mo)("ha-selector-background")],(function(e,a){class t extends a{constructor(...a){super(...a),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"field",decorators:[(0,n.SB)()],key:"yamlBackground",value(){return!1}},{kind:"method",key:"updated",value:function(e){(0,l.Z)(t,"updated",this,3)([e]),e.has("value")&&(this.yamlBackground=!!this.value&&!this.value.startsWith(s.JS))}},{kind:"method",key:"render",value:function(){var e,a,t;return(0,r.dy)(h||(h=y`
      <div>
        ${0}
      </div>
    `),this.yamlBackground?(0,r.dy)(v||(v=y`
              <div class="value">
                <img
                  src=${0}
                  alt=${0}
                />
              </div>
              <ha-alert alert-type="info">
                ${0}
                <ha-button slot="action" @click=${0}>
                  ${0}
                </ha-button>
              </ha-alert>
            `),this.value,this.hass.localize("ui.components.picture-upload.current_image_alt"),this.hass.localize("ui.components.selectors.background.yaml_info"),this._clearValue,this.hass.localize("ui.components.picture-upload.clear_picture")):(0,r.dy)(p||(p=y`
              <ha-picture-upload
                .hass=${0}
                .value=${0}
                .original=${0}
                .cropOptions=${0}
                select-media
                @change=${0}
              ></ha-picture-upload>
            `),this.hass,null!==(e=this.value)&&void 0!==e&&e.startsWith(s.JS)?this.value:null,!(null===(a=this.selector.background)||void 0===a||!a.original),null===(t=this.selector.background)||void 0===t?void 0:t.crop,this._pictureChanged))}},{kind:"method",key:"_pictureChanged",value:function(e){const a=e.target.value;(0,u.B)(this,"value-changed",{value:null!=a?a:void 0})}},{kind:"method",key:"_clearValue",value:function(){(0,u.B)(this,"value-changed",{value:void 0})}},{kind:"field",static:!0,key:"styles",value(){return(0,r.iv)(k||(k=y`
    :host {
      display: block;
      position: relative;
    }
    div {
      display: flex;
      flex-direction: column;
    }
    ha-button {
      white-space: nowrap;
      --mdc-theme-primary: var(--primary-color);
    }
    .value {
      width: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
    }
    img {
      max-width: 100%;
      max-height: 200px;
      margin-bottom: 4px;
      border-radius: var(--file-upload-image-border-radius);
      transition: opacity 0.3s;
      opacity: var(--picture-opacity, 1);
    }
    img:hover {
      opacity: 1;
    }
  `))}}]}}),r.oi);i()}catch(h){i(h)}}))}}]);
//# sourceMappingURL=7473.787f4bfddff88418.js.map