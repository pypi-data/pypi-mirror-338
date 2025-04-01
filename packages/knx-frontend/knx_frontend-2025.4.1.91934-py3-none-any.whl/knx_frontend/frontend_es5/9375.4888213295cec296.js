"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["9375"],{28368:function(e,i,t){var a=t(73577),n=t(72621),s=(t(71695),t(40251),t(47021),t(57243)),o=t(93958),d=t(97536),l=t(46289),r=t(50778),c=t(11297);let h,m=e=>e;(0,a.Z)([(0,r.Mo)("ha-check-list-item")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"method",key:"onChange",value:async function(e){(0,n.Z)(t,"onChange",this,3)([e]),(0,c.B)(this,e.type)}},{kind:"field",static:!0,key:"styles",value(){return[l.W,d.W,(0,s.iv)(h||(h=m`
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
    `))]}}]}}),o.F)},77182:function(e,i,t){var a=t(73577),n=(t(71695),t(47021),t(57243)),s=t(50778);t(10508);let o,d,l=e=>e;(0,a.Z)([(0,s.Mo)("ha-tip")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"method",key:"render",value:function(){return this.hass?(0,n.dy)(o||(o=l`
      <ha-svg-icon .path=${0}></ha-svg-icon>
      <span class="prefix"
        >${0}</span
      >
      <span class="text"><slot></slot></span>
    `),"M12,2A7,7 0 0,1 19,9C19,11.38 17.81,13.47 16,14.74V17A1,1 0 0,1 15,18H9A1,1 0 0,1 8,17V14.74C6.19,13.47 5,11.38 5,9A7,7 0 0,1 12,2M9,21V20H15V21A1,1 0 0,1 14,22H10A1,1 0 0,1 9,21M12,4A5,5 0 0,0 7,9C7,11.05 8.23,12.81 10,13.58V16H14V13.58C15.77,12.81 17,11.05 17,9A5,5 0 0,0 12,4Z",this.hass.localize("ui.panel.config.tips.tip")):n.Ld}},{kind:"field",static:!0,key:"styles",value(){return(0,n.iv)(d||(d=l`
    :host {
      display: block;
      text-align: center;
    }

    .text {
      direction: var(--direction);
      margin-left: 2px;
      margin-inline-start: 2px;
      margin-inline-end: initial;
      color: var(--secondary-text-color);
    }

    .prefix {
      font-weight: 500;
    }
  `))}}]}}),n.oi)},12206:function(e,i,t){t.a(e,(async function(e,a){try{t.r(i);var n=t(73577),s=(t(71695),t(92745),t(9359),t(56475),t(31526),t(19423),t(40251),t(92519),t(42179),t(89256),t(24931),t(88463),t(57449),t(19814),t(47021),t(15108)),o=(t(2060),t(87319),t(57243)),d=t(50778),l=t(91583),r=t(11297),c=t(45294),h=t(98773),m=t(42883),u=t(18727),g=t(4557),p=t(66193),_=(t(20095),t(28368),t(19537)),f=(t(44118),t(28906),t(10508),t(77182),t(80359)),v=t(18875),y=t(49672),k=e([_,f,v]);[_,f,v]=k.then?(await k)():k;let b,$,x,w,I,C,L,z,A,S,H,M,V,B,U=e=>e;const Z="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",D="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z";(0,n.Z)([(0,d.Mo)("dialog-media-manage")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,d.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,d.SB)()],key:"_currentItem",value:void 0},{kind:"field",decorators:[(0,d.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,d.SB)()],key:"_uploading",value(){return!1}},{kind:"field",decorators:[(0,d.SB)()],key:"_deleting",value(){return!1}},{kind:"field",decorators:[(0,d.SB)()],key:"_selected",value(){return new Set}},{kind:"field",key:"_filesChanged",value(){return!1}},{kind:"method",key:"showDialog",value:function(e){this._params=e,this._refreshMedia()}},{kind:"method",key:"closeDialog",value:function(){this._filesChanged&&this._params.onClose&&this._params.onClose(),this._params=void 0,this._currentItem=void 0,this._uploading=!1,this._deleting=!1,this._filesChanged=!1,(0,r.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){var e,i;if(!this._params)return o.Ld;const t=(null===(e=this._currentItem)||void 0===e||null===(e=e.children)||void 0===e?void 0:e.filter((e=>!e.can_expand)))||[];let a=0;return(0,o.dy)(b||(b=U`
      <ha-dialog
        open
        scrimClickAction
        escapeKeyAction
        hideActions
        flexContent
        .heading=${0}
        @closed=${0}
      >
        <ha-dialog-header slot="heading">
          ${0}
        </ha-dialog-header>
        ${0}
        ${0}
      </ha-dialog>
    `),this._params.currentItem.title,this.closeDialog,0===this._selected.size?(0,o.dy)($||($=U`
                <span slot="title">
                  ${0}
                </span>

                <ha-media-upload-button
                  .disabled=${0}
                  .hass=${0}
                  .currentItem=${0}
                  @uploading=${0}
                  @media-refresh=${0}
                  slot="actionItems"
                ></ha-media-upload-button>
                ${0}
              `),this.hass.localize("ui.components.media-browser.file_management.title"),this._deleting,this.hass,this._params.currentItem,this._startUploading,this._doneUploading,this._uploading?"":(0,o.dy)(x||(x=U`
                      <ha-icon-button
                        .label=${0}
                        .path=${0}
                        dialogAction="close"
                        slot="navigationIcon"
                        dir=${0}
                      ></ha-icon-button>
                    `),this.hass.localize("ui.common.close"),Z,(0,c.Zu)(this.hass))):(0,o.dy)(w||(w=U`
                <ha-button
                  class="danger"
                  slot="navigationIcon"
                  .disabled=${0}
                  .label=${0}
                  @click=${0}
                >
                  <ha-svg-icon .path=${0} slot="icon"></ha-svg-icon>
                </ha-button>

                ${0}
              `),this._deleting,this.hass.localize("ui.components.media-browser.file_management."+(this._deleting?"deleting":"delete"),{count:this._selected.size}),this._handleDelete,D,this._deleting?"":(0,o.dy)(I||(I=U`
                      <ha-button
                        slot="actionItems"
                        .label=${0}
                        @click=${0}
                      >
                        <ha-svg-icon
                          .path=${0}
                          slot="icon"
                        ></ha-svg-icon>
                      </ha-button>
                    `),this.hass.localize("ui.components.media-browser.file_management.deselect_all"),this._handleDeselectAll,Z)),this._currentItem?t.length?(0,o.dy)(A||(A=U`
                <mwc-list multi @selected=${0}>
                  ${0}
                </mwc-list>
              `),this._handleSelected,(0,l.r)(t,(e=>e.media_content_id),(e=>{const i=(0,o.dy)(S||(S=U`
                        <ha-svg-icon
                          slot="graphic"
                          .path=${0}
                        ></ha-svg-icon>
                      `),h.Fn["directory"===e.media_class&&e.children_media_class||e.media_class].icon);return(0,o.dy)(H||(H=U`
                        <ha-check-list-item
                          ${0}
                          graphic="icon"
                          .disabled=${0}
                          .selected=${0}
                          .item=${0}
                        >
                          ${0} ${0}
                        </ha-check-list-item>
                      `),(0,s.jt)({id:e.media_content_id,skipInitial:!0}),this._uploading||this._deleting,this._selected.has(a++),e,i,e.title)}))):(0,o.dy)(L||(L=U`<div class="no-items">
                <p>
                  ${0}
                </p>
                ${0}
              </div>`),this.hass.localize("ui.components.media-browser.file_management.no_items"),null!==(i=this._currentItem)&&void 0!==i&&null!==(i=i.children)&&void 0!==i&&i.length?(0,o.dy)(z||(z=U`<span class="folders"
                      >${0}</span
                    >`),this.hass.localize("ui.components.media-browser.file_management.folders_not_supported")):""):(0,o.dy)(C||(C=U`
              <div class="refresh">
                <ha-spinner></ha-spinner>
              </div>
            `)),(0,y.p)(this.hass,"hassio")?(0,o.dy)(M||(M=U`<ha-tip .hass=${0}>
              ${0}
            </ha-tip>`),this.hass,this.hass.localize("ui.components.media-browser.file_management.tip_media_storage",{storage:(0,o.dy)(V||(V=U`<a
                    href="/config/storage"
                    @click=${0}
                  >
                    ${0}</a
                  >`),this.closeDialog,this.hass.localize("ui.components.media-browser.file_management.tip_storage_panel"))})):o.Ld)}},{kind:"method",key:"_handleSelected",value:function(e){this._selected=e.detail.index}},{kind:"method",key:"_startUploading",value:function(){this._uploading=!0,this._filesChanged=!0}},{kind:"method",key:"_doneUploading",value:function(){this._uploading=!1,this._refreshMedia()}},{kind:"method",key:"_handleDeselectAll",value:function(){this._selected.size&&(this._selected=new Set)}},{kind:"method",key:"_handleDelete",value:async function(){if(!(await(0,g.g7)(this,{text:this.hass.localize("ui.components.media-browser.file_management.confirm_delete",{count:this._selected.size}),warning:!0})))return;this._filesChanged=!0,this._deleting=!0;const e=[];let i=0;this._currentItem.children.forEach((t=>{t.can_expand||this._selected.has(i++)&&e.push(t)}));try{await Promise.all(e.map((async e=>{if((0,m.aV)(e.media_content_id))await(0,m.Qr)(this.hass,e.media_content_id);else if((0,m.IB)(e.media_content_id)){const i=(0,u.TT)(e.media_content_id);i&&await(0,u.ao)(this.hass,i)}this._currentItem=Object.assign(Object.assign({},this._currentItem),{},{children:this._currentItem.children.filter((i=>i!==e))})})))}finally{this._deleting=!1,this._selected=new Set}}},{kind:"method",key:"_refreshMedia",value:async function(){this._selected=new Set,this._currentItem=void 0,this._currentItem=await(0,m.b)(this.hass,this._params.currentItem.media_content_id)}},{kind:"get",static:!0,key:"styles",value:function(){return[p.yu,(0,o.iv)(B||(B=U`
        ha-dialog {
          --dialog-z-index: 9;
          --dialog-content-padding: 0;
        }

        @media (min-width: 800px) {
          ha-dialog {
            --mdc-dialog-max-width: 800px;
            --dialog-surface-position: fixed;
            --dialog-surface-top: 40px;
            --mdc-dialog-max-height: calc(100vh - 72px);
          }
        }

        ha-dialog-header ha-media-upload-button,
        ha-dialog-header ha-button {
          --mdc-theme-primary: var(--primary-text-color);
          margin: 6px;
          display: block;
        }

        .danger {
          --mdc-theme-primary: var(--error-color);
        }

        ha-svg-icon[slot="icon"] {
          vertical-align: middle;
        }

        ha-tip {
          margin: 16px;
        }

        ha-svg-icon[slot="icon"] {
          margin-inline-start: 0px !important;
          margin-inline-end: 8px !important;
          direction: var(--direction);
        }

        .refresh {
          display: flex;
          height: 200px;
          justify-content: center;
          align-items: center;
        }

        .no-items {
          text-align: center;
          padding: 16px;
        }
        .folders {
          color: var(--secondary-text-color);
          font-style: italic;
        }
      `))]}}]}}),o.oi);a()}catch(b){a(b)}}))},18875:function(e,i,t){t.a(e,(async function(e,i){try{var a=t(73577),n=(t(71695),t(40251),t(47021),t(31622),t(57243)),s=t(50778),o=t(11297),d=t(42883),l=t(4557),r=t(19537),c=(t(10508),e([r]));r=(c.then?(await c)():c)[0];let h,m,u,g,p=e=>e;const _="M9,16V10H5L12,3L19,10H15V16H9M5,20V18H19V20H5Z";(0,a.Z)([(0,s.Mo)("ha-media-upload-button")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"currentItem",value:void 0},{kind:"field",decorators:[(0,s.SB)()],key:"_uploading",value(){return 0}},{kind:"method",key:"render",value:function(){return this.currentItem&&(0,d.aV)(this.currentItem.media_content_id||"")?(0,n.dy)(h||(h=p`
      <mwc-button
        .label=${0}
        .disabled=${0}
        @click=${0}
      >
        ${0}
      </mwc-button>
    `),this._uploading>0?this.hass.localize("ui.components.media-browser.file_management.uploading",{count:this._uploading}):this.hass.localize("ui.components.media-browser.file_management.add_media"),this._uploading>0,this._startUpload,this._uploading>0?(0,n.dy)(m||(m=p`
              <ha-spinner
                size="small"
                area-label="Uploading"
                slot="icon"
              ></ha-spinner>
            `)):(0,n.dy)(u||(u=p` <ha-svg-icon .path=${0} slot="icon"></ha-svg-icon> `),_)):n.Ld}},{kind:"method",key:"_startUpload",value:async function(){if(this._uploading>0)return;const e=document.createElement("input");e.type="file",e.accept="audio/*,video/*,image/*",e.multiple=!0,e.addEventListener("change",(async()=>{(0,o.B)(this,"uploading");const i=e.files;document.body.removeChild(e);const t=this.currentItem.media_content_id;for(let e=0;e<i.length;e++){this._uploading=i.length-e;try{await(0,d.oE)(this.hass,t,i[e])}catch(a){(0,l.Ys)(this,{text:this.hass.localize("ui.components.media-browser.file_management.upload_failed",{reason:a.message||a})});break}}this._uploading=0,(0,o.B)(this,"media-refresh")}),{once:!0}),e.style.display="none",document.body.append(e),e.click()}},{kind:"field",static:!0,key:"styles",value(){return(0,n.iv)(g||(g=p`
    mwc-button {
      /* We use icon + text to show disabled state */
      --mdc-button-disabled-ink-color: --mdc-theme-primary;
    }

    ha-svg-icon[slot="icon"],
    ha-spinner[slot="icon"] {
      vertical-align: middle;
    }

    ha-svg-icon[slot="icon"] {
      margin-inline-start: 0px;
      margin-inline-end: 8px;
      direction: var(--direction);
    }
  `))}}]}}),n.oi);i()}catch(h){i(h)}}))},18727:function(e,i,t){t.d(i,{Bi:()=>d,JS:()=>a,TT:()=>s,ao:()=>l,dg:()=>n,n$:()=>r,p6:()=>o});t(52247),t(19423),t(40251),t(88044);const a="/api/image/serve/",n="media-source://image_upload",s=e=>{let i;if(e.startsWith(a)){i=e.substring(a.length);const t=i.indexOf("/");t>=0&&(i=i.substring(0,t))}else e.startsWith(n)&&(i=e.substring(n.length+1));return i},o=(e,i,t=!1)=>{if(!t&&!i)throw new Error("Size must be provided if original is false");return t?`/api/image/serve/${e}/original`:`/api/image/serve/${e}/${i}x${i}`},d=async(e,i)=>{const t=new FormData;t.append("file",i);const a=await e.fetchWithAuth("/api/image/upload",{method:"POST",body:t});if(413===a.status)throw new Error(`Uploaded image is too large (${i.name})`);if(200!==a.status)throw new Error("Unknown error");return a.json()},l=(e,i)=>e.callWS({type:"image/delete",image_id:i}),r=async(e,i)=>{const t=await fetch(e.hassUrl(i));if(!t.ok)throw new Error(`Failed to fetch image: ${t.statusText?t.statusText:t.status}`);return t.blob()}}}]);
//# sourceMappingURL=9375.4888213295cec296.js.map