"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["7097"],{9115:function(e,i,a){a.d(i,{K:()=>t});const t=e=>{switch(e.language){case"cs":case"de":case"fi":case"fr":case"sk":case"sv":return" ";default:return""}}},58303:function(e,i,a){a.a(e,(async function(e,i){try{var t=a(73577),l=a(72621),o=(a(71695),a(9359),a(70104),a(47021),a(87515)),r=a(57243),n=a(50778),s=a(35359),d=a(11297),c=(a(20095),a(59897),a(9115)),u=a(24785),h=a(84120),p=e([o]);o=(p.then?(await p)():p)[0];let v,f,b,k,y,g,m,_,$=e=>e;const x="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z",w="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M13.5,16V19H10.5V16H8L12,12L16,16H13.5M13,9V3.5L18.5,9H13Z";(0,t.Z)([(0,n.Mo)("ha-file-upload")],(function(e,i){class a extends i{constructor(...i){super(...i),e(this)}}return{F:a,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"localize",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"accept",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"icon",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"secondary",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:"uploading-label"})],key:"uploadingLabel",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:"delete-label"})],key:"deleteLabel",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"supports",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Object})],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"multiple",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"uploading",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Number})],key:"progress",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean,attribute:"auto-open-file-dialog"})],key:"autoOpenFileDialog",value(){return!1}},{kind:"field",decorators:[(0,n.SB)()],key:"_drag",value(){return!1}},{kind:"field",decorators:[(0,n.IO)("#input")],key:"_input",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,l.Z)(a,"firstUpdated",this,3)([e]),this.autoOpenFileDialog&&this._openFilePicker()}},{kind:"get",key:"_name",value:function(){if(void 0===this.value)return"";if("string"==typeof this.value)return this.value;return(this.value instanceof FileList?Array.from(this.value):(0,u.r)(this.value)).map((e=>e.name)).join(", ")}},{kind:"method",key:"render",value:function(){const e=this.localize||this.hass.localize;return(0,r.dy)(v||(v=$`
      ${0}
    `),this.uploading?(0,r.dy)(f||(f=$`<div class="container">
            <div class="uploading">
              <span class="header"
                >${0}</span
              >
              ${0}
            </div>
            <mwc-linear-progress
              .indeterminate=${0}
              .progress=${0}
            ></mwc-linear-progress>
          </div>`),this.uploadingLabel||this.value?e("ui.components.file-upload.uploading_name",{name:this._name}):e("ui.components.file-upload.uploading"),this.progress?(0,r.dy)(b||(b=$`<div class="progress">
                    ${0}${0}%
                  </div>`),this.progress,this.hass&&(0,c.K)(this.hass.locale)):r.Ld,!this.progress,this.progress?this.progress/100:void 0):(0,r.dy)(k||(k=$`<label
            for=${0}
            class="container ${0}"
            @drop=${0}
            @dragenter=${0}
            @dragover=${0}
            @dragleave=${0}
            @dragend=${0}
            >${0}
            <input
              id="input"
              type="file"
              class="file"
              .accept=${0}
              .multiple=${0}
              @change=${0}
          /></label>`),this.value?"":"input",(0,s.$)({dragged:this._drag,multiple:this.multiple,value:Boolean(this.value)}),this._handleDrop,this._handleDragStart,this._handleDragStart,this._handleDragEnd,this._handleDragEnd,this.value?"string"==typeof this.value?(0,r.dy)(g||(g=$`<div class="row">
                    <div class="value" @click=${0}>
                      <ha-svg-icon
                        .path=${0}
                      ></ha-svg-icon>
                      ${0}
                    </div>
                    <ha-icon-button
                      @click=${0}
                      .label=${0}
                      .path=${0}
                    ></ha-icon-button>
                  </div>`),this._openFilePicker,this.icon||w,this.value,this._clearValue,this.deleteLabel||e("ui.common.delete"),x):(this.value instanceof FileList?Array.from(this.value):(0,u.r)(this.value)).map((i=>(0,r.dy)(m||(m=$`<div class="row">
                        <div class="value" @click=${0}>
                          <ha-svg-icon
                            .path=${0}
                          ></ha-svg-icon>
                          ${0} - ${0}
                        </div>
                        <ha-icon-button
                          @click=${0}
                          .label=${0}
                          .path=${0}
                        ></ha-icon-button>
                      </div>`),this._openFilePicker,this.icon||w,i.name,(0,h.d)(i.size),this._clearValue,this.deleteLabel||e("ui.common.delete"),x))):(0,r.dy)(y||(y=$`<ha-svg-icon
                    class="big-icon"
                    .path=${0}
                  ></ha-svg-icon>
                  <ha-button unelevated @click=${0}>
                    ${0}
                  </ha-button>
                  <span class="secondary"
                    >${0}</span
                  >
                  <span class="supports">${0}</span>`),this.icon||w,this._openFilePicker,this.label||e("ui.components.file-upload.label"),this.secondary||e("ui.components.file-upload.secondary"),this.supports),this.accept,this.multiple,this._handleFilePicked))}},{kind:"method",key:"_openFilePicker",value:function(){var e;null===(e=this._input)||void 0===e||e.click()}},{kind:"method",key:"_handleDrop",value:function(e){var i;e.preventDefault(),e.stopPropagation(),null!==(i=e.dataTransfer)&&void 0!==i&&i.files&&(0,d.B)(this,"file-picked",{files:this.multiple||1===e.dataTransfer.files.length?Array.from(e.dataTransfer.files):[e.dataTransfer.files[0]]}),this._drag=!1}},{kind:"method",key:"_handleDragStart",value:function(e){e.preventDefault(),e.stopPropagation(),this._drag=!0}},{kind:"method",key:"_handleDragEnd",value:function(e){e.preventDefault(),e.stopPropagation(),this._drag=!1}},{kind:"method",key:"_handleFilePicked",value:function(e){0!==e.target.files.length&&(this.value=e.target.files,(0,d.B)(this,"file-picked",{files:e.target.files}))}},{kind:"method",key:"_clearValue",value:function(e){e.preventDefault(),this._input.value="",this.value=void 0,(0,d.B)(this,"change"),(0,d.B)(this,"files-cleared")}},{kind:"field",static:!0,key:"styles",value(){return(0,r.iv)(_||(_=$`
    :host {
      display: block;
      height: 240px;
    }
    :host([disabled]) {
      pointer-events: none;
      color: var(--disabled-text-color);
    }
    .container {
      position: relative;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      border: solid 1px
        var(--mdc-text-field-idle-line-color, rgba(0, 0, 0, 0.42));
      border-radius: var(--mdc-shape-small, 4px);
      height: 100%;
    }
    .row {
      display: flex;
      align-items: center;
    }
    label.container {
      border: dashed 1px
        var(--mdc-text-field-idle-line-color, rgba(0, 0, 0, 0.42));
      cursor: pointer;
    }
    .container .uploading {
      display: flex;
      flex-direction: column;
      width: 100%;
      align-items: flex-start;
      padding: 0 32px;
      box-sizing: border-box;
    }
    :host([disabled]) .container {
      border-color: var(--disabled-color);
    }
    label:hover,
    label.dragged {
      border-style: solid;
    }
    label.dragged {
      border-color: var(--primary-color);
    }
    .dragged:before {
      position: absolute;
      top: 0;
      right: 0;
      bottom: 0;
      left: 0;
      background-color: var(--primary-color);
      content: "";
      opacity: var(--dark-divider-opacity);
      pointer-events: none;
      border-radius: var(--mdc-shape-small, 4px);
    }
    label.value {
      cursor: default;
    }
    label.value.multiple {
      justify-content: unset;
      overflow: auto;
    }
    .highlight {
      color: var(--primary-color);
    }
    ha-button {
      margin-bottom: 4px;
    }
    .supports {
      color: var(--secondary-text-color);
      font-size: 12px;
    }
    :host([disabled]) .secondary {
      color: var(--disabled-text-color);
    }
    input.file {
      display: none;
    }
    .value {
      cursor: pointer;
    }
    .value ha-svg-icon {
      margin-right: 8px;
      margin-inline-end: 8px;
      margin-inline-start: initial;
    }
    .big-icon {
      --mdc-icon-size: 48px;
      margin-bottom: 8px;
    }
    ha-button {
      --mdc-button-outline-color: var(--primary-color);
      --mdc-icon-button-size: 24px;
    }
    mwc-linear-progress {
      width: 100%;
      padding: 8px 32px;
      box-sizing: border-box;
    }
    .header {
      font-weight: 500;
    }
    .progress {
      color: var(--secondary-text-color);
    }
    button.link {
      background: none;
      border: none;
      padding: 0;
      font-size: 14px;
      color: var(--primary-color);
      text-decoration: underline;
      cursor: pointer;
    }
  `))}}]}}),r.oi);i()}catch(v){i(v)}}))},11838:function(e,i,a){a.a(e,(async function(e,t){try{a.r(i),a.d(i,{HaFileSelector:()=>b});var l=a(73577),o=a(72621),r=(a(71695),a(40251),a(47021),a(57243)),n=a(50778),s=a(11297),d=a(96123),c=a(4557),u=a(58303),h=e([u]);u=(h.then?(await h)():h)[0];let p,v=e=>e;const f="M13,9V3.5L18.5,9M6,2C4.89,2 4,2.89 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2H6Z";let b=(0,l.Z)([(0,n.Mo)("ha-selector-file")],(function(e,i){class a extends i{constructor(...i){super(...i),e(this)}}return{F:a,d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,n.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,n.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"field",decorators:[(0,n.SB)()],key:"_filename",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_busy",value(){return!1}},{kind:"method",key:"render",value:function(){var e,i;return(0,r.dy)(p||(p=v`
      <ha-file-upload
        .hass=${0}
        .accept=${0}
        .icon=${0}
        .label=${0}
        .required=${0}
        .disabled=${0}
        .supports=${0}
        .uploading=${0}
        .value=${0}
        @file-picked=${0}
        @change=${0}
      ></ha-file-upload>
    `),this.hass,null===(e=this.selector.file)||void 0===e?void 0:e.accept,f,this.label,this.required,this.disabled,this.helper,this._busy,this.value?(null===(i=this._filename)||void 0===i?void 0:i.name)||this.hass.localize("ui.components.selectors.file.unknown_file"):void 0,this._uploadFile,this._removeFile)}},{kind:"method",key:"willUpdate",value:function(e){(0,o.Z)(a,"willUpdate",this,3)([e]),e.has("value")&&this._filename&&this.value!==this._filename.fileId&&(this._filename=void 0)}},{kind:"method",key:"_uploadFile",value:async function(e){this._busy=!0;const i=e.detail.files[0];try{const e=await(0,d.c)(this.hass,i);this._filename={fileId:e,name:i.name},(0,s.B)(this,"value-changed",{value:e})}catch(a){(0,c.Ys)(this,{text:this.hass.localize("ui.components.selectors.file.upload_failed",{reason:a.message||a})})}finally{this._busy=!1}}},{kind:"field",key:"_removeFile",value(){return async()=>{this._busy=!0;try{await(0,d.Y)(this.hass,this.value)}catch(e){}finally{this._busy=!1}this._filename=void 0,(0,s.B)(this,"value-changed",{value:""})}}}]}}),r.oi);t()}catch(p){t(p)}}))},96123:function(e,i,a){a.d(i,{Y:()=>l,c:()=>t});a(52247),a(40251);const t=async(e,i)=>{const a=new FormData;a.append("file",i);const t=await e.fetchWithAuth("/api/file_upload",{method:"POST",body:a});if(413===t.status)throw new Error(`Uploaded file is too large (${i.name})`);if(200!==t.status)throw new Error("Unknown error");return(await t.json()).file_id},l=async(e,i)=>e.callApi("DELETE","file_upload",{file_id:i})},84120:function(e,i,a){a.d(i,{d:()=>t});a(49278),a(95078);const t=(e=0,i=2)=>{if(0===e)return"0 Bytes";i=i<0?0:i;const a=Math.floor(Math.log(e)/Math.log(1024));return`${parseFloat((e/1024**a).toFixed(i))} ${["Bytes","KB","MB","GB","TB","PB","EB","ZB","YB"][a]}`}}}]);
//# sourceMappingURL=7097.ec0235e2740f40d4.js.map