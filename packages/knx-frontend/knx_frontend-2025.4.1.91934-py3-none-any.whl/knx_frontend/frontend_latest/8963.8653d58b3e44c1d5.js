export const __webpack_ids__=["8963"];export const __webpack_modules__={9115:function(e,i,t){t.d(i,{K:()=>a});const a=e=>{switch(e.language){case"cs":case"de":case"fi":case"fr":case"sk":case"sv":return" ";default:return""}}},97709:function(e,i,t){var a=t(44249),o=t(72621),l=(t(24427),t(57243)),s=t(50778),r=t(35359),n=t(11297),d=(t(20095),t(59897),t(9115)),c=t(24785);const u="M19,4H15.5L14.5,3H9.5L8.5,4H5V6H19M6,19A2,2 0 0,0 8,21H16A2,2 0 0,0 18,19V7H6V19Z",p="M14,2H6A2,2 0 0,0 4,4V20A2,2 0 0,0 6,22H18A2,2 0 0,0 20,20V8L14,2M13.5,16V19H10.5V16H8L12,12L16,16H13.5M13,9V3.5L18.5,9H13Z";(0,a.Z)([(0,s.Mo)("ha-file-upload")],(function(e,i){class t extends i{constructor(...i){super(...i),e(this)}}return{F:t,d:[{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:!1})],key:"localize",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"accept",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"icon",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"secondary",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:"uploading-label"})],key:"uploadingLabel",value:void 0},{kind:"field",decorators:[(0,s.Cb)({attribute:"delete-label"})],key:"deleteLabel",value:void 0},{kind:"field",decorators:[(0,s.Cb)()],key:"supports",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Object})],key:"value",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"multiple",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({type:Boolean,reflect:!0})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({type:Boolean})],key:"uploading",value(){return!1}},{kind:"field",decorators:[(0,s.Cb)({type:Number})],key:"progress",value:void 0},{kind:"field",decorators:[(0,s.Cb)({type:Boolean,attribute:"auto-open-file-dialog"})],key:"autoOpenFileDialog",value(){return!1}},{kind:"field",decorators:[(0,s.SB)()],key:"_drag",value(){return!1}},{kind:"field",decorators:[(0,s.IO)("#input")],key:"_input",value:void 0},{kind:"method",key:"firstUpdated",value:function(e){(0,o.Z)(t,"firstUpdated",this,3)([e]),this.autoOpenFileDialog&&this._openFilePicker()}},{kind:"get",key:"_name",value:function(){if(void 0===this.value)return"";if("string"==typeof this.value)return this.value;return(this.value instanceof FileList?Array.from(this.value):(0,c.r)(this.value)).map((e=>e.name)).join(", ")}},{kind:"method",key:"render",value:function(){const e=this.localize||this.hass.localize;return l.dy`
      ${this.uploading?l.dy`<div class="container">
            <div class="uploading">
              <span class="header"
                >${this.uploadingLabel||this.value?e("ui.components.file-upload.uploading_name",{name:this._name}):e("ui.components.file-upload.uploading")}</span
              >
              ${this.progress?l.dy`<div class="progress">
                    ${this.progress}${this.hass&&(0,d.K)(this.hass.locale)}%
                  </div>`:l.Ld}
            </div>
            <mwc-linear-progress
              .indeterminate=${!this.progress}
              .progress=${this.progress?this.progress/100:void 0}
            ></mwc-linear-progress>
          </div>`:l.dy`<label
            for=${this.value?"":"input"}
            class="container ${(0,r.$)({dragged:this._drag,multiple:this.multiple,value:Boolean(this.value)})}"
            @drop=${this._handleDrop}
            @dragenter=${this._handleDragStart}
            @dragover=${this._handleDragStart}
            @dragleave=${this._handleDragEnd}
            @dragend=${this._handleDragEnd}
            >${this.value?"string"==typeof this.value?l.dy`<div class="row">
                    <div class="value" @click=${this._openFilePicker}>
                      <ha-svg-icon
                        .path=${this.icon||p}
                      ></ha-svg-icon>
                      ${this.value}
                    </div>
                    <ha-icon-button
                      @click=${this._clearValue}
                      .label=${this.deleteLabel||e("ui.common.delete")}
                      .path=${u}
                    ></ha-icon-button>
                  </div>`:(this.value instanceof FileList?Array.from(this.value):(0,c.r)(this.value)).map((i=>l.dy`<div class="row">
                        <div class="value" @click=${this._openFilePicker}>
                          <ha-svg-icon
                            .path=${this.icon||p}
                          ></ha-svg-icon>
                          ${i.name} - ${((e=0,i=2)=>{if(0===e)return"0 Bytes";i=i<0?0:i;const t=Math.floor(Math.log(e)/Math.log(1024));return`${parseFloat((e/1024**t).toFixed(i))} ${["Bytes","KB","MB","GB","TB","PB","EB","ZB","YB"][t]}`})(i.size)}
                        </div>
                        <ha-icon-button
                          @click=${this._clearValue}
                          .label=${this.deleteLabel||e("ui.common.delete")}
                          .path=${u}
                        ></ha-icon-button>
                      </div>`)):l.dy`<ha-svg-icon
                    class="big-icon"
                    .path=${this.icon||p}
                  ></ha-svg-icon>
                  <ha-button unelevated @click=${this._openFilePicker}>
                    ${this.label||e("ui.components.file-upload.label")}
                  </ha-button>
                  <span class="secondary"
                    >${this.secondary||e("ui.components.file-upload.secondary")}</span
                  >
                  <span class="supports">${this.supports}</span>`}
            <input
              id="input"
              type="file"
              class="file"
              .accept=${this.accept}
              .multiple=${this.multiple}
              @change=${this._handleFilePicked}
          /></label>`}
    `}},{kind:"method",key:"_openFilePicker",value:function(){this._input?.click()}},{kind:"method",key:"_handleDrop",value:function(e){e.preventDefault(),e.stopPropagation(),e.dataTransfer?.files&&(0,n.B)(this,"file-picked",{files:this.multiple||1===e.dataTransfer.files.length?Array.from(e.dataTransfer.files):[e.dataTransfer.files[0]]}),this._drag=!1}},{kind:"method",key:"_handleDragStart",value:function(e){e.preventDefault(),e.stopPropagation(),this._drag=!0}},{kind:"method",key:"_handleDragEnd",value:function(e){e.preventDefault(),e.stopPropagation(),this._drag=!1}},{kind:"method",key:"_handleFilePicked",value:function(e){0!==e.target.files.length&&(this.value=e.target.files,(0,n.B)(this,"file-picked",{files:e.target.files}))}},{kind:"method",key:"_clearValue",value:function(e){e.preventDefault(),this._input.value="",this.value=void 0,(0,n.B)(this,"change"),(0,n.B)(this,"files-cleared")}},{kind:"field",static:!0,key:"styles",value(){return l.iv`
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
  `}}]}}),l.oi)},41600:function(e,i,t){var a=t(44249),o=t(57243),l=t(50778),s=t(11297),r=t(66193),n=t(18727),d=t(4557);const c=()=>Promise.all([t.e("5141"),t.e("70")]).then(t.bind(t,14995));t(20095),t(97709);var u=t(92903);(0,a.Z)([(0,l.Mo)("ha-picture-upload")],(function(e,i){return{F:class extends i{constructor(...i){super(...i),e(this)}},d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"value",value(){return null}},{kind:"field",decorators:[(0,l.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"secondary",value:void 0},{kind:"field",decorators:[(0,l.Cb)()],key:"supports",value:void 0},{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"currentImageAltText",value:void 0},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"crop",value(){return!1}},{kind:"field",decorators:[(0,l.Cb)({type:Boolean,attribute:"select-media"})],key:"selectMedia",value(){return!1}},{kind:"field",decorators:[(0,l.Cb)({attribute:!1})],key:"cropOptions",value:void 0},{kind:"field",decorators:[(0,l.Cb)({type:Boolean})],key:"original",value(){return!1}},{kind:"field",decorators:[(0,l.Cb)({type:Number})],key:"size",value(){return 512}},{kind:"field",decorators:[(0,l.SB)()],key:"_uploading",value(){return!1}},{kind:"method",key:"render",value:function(){if(!this.value){const e=this.secondary||(this.selectMedia?o.dy`${this.hass.localize("ui.components.picture-upload.secondary",{select_media:o.dy`<button
                  class="link"
                  @click=${this._chooseMedia}
                >
                  ${this.hass.localize("ui.components.picture-upload.select_media")}
                </button>`})}`:void 0);return o.dy`
        <ha-file-upload
          .hass=${this.hass}
          .icon=${"M18 15V18H15V20H18V23H20V20H23V18H20V15H18M13.3 21H5C3.9 21 3 20.1 3 19V5C3 3.9 3.9 3 5 3H19C20.1 3 21 3.9 21 5V13.3C20.4 13.1 19.7 13 19 13C17.9 13 16.8 13.3 15.9 13.9L14.5 12L11 16.5L8.5 13.5L5 18H13.1C13 18.3 13 18.7 13 19C13 19.7 13.1 20.4 13.3 21Z"}
          .label=${this.label||this.hass.localize("ui.components.picture-upload.label")}
          .secondary=${e}
          .supports=${this.supports||this.hass.localize("ui.components.picture-upload.supported_formats")}
          .uploading=${this._uploading}
          @file-picked=${this._handleFilePicked}
          @change=${this._handleFileCleared}
          accept="image/png, image/jpeg, image/gif"
        ></ha-file-upload>
      `}return o.dy`<div class="center-vertical">
      <div class="value">
        <img
          .src=${this.value}
          alt=${this.currentImageAltText||this.hass.localize("ui.components.picture-upload.current_image_alt")}
        />
        <div>
          <ha-button
            @click=${this._handleChangeClick}
            .label=${this.hass.localize("ui.components.picture-upload.clear_picture")}
          >
          </ha-button>
        </div>
      </div>
    </div>`}},{kind:"method",key:"_handleChangeClick",value:function(){this.value=null,(0,s.B)(this,"change")}},{kind:"method",key:"_handleFilePicked",value:async function(e){const i=e.detail.files[0];this.crop?this._cropFile(i):this._uploadFile(i)}},{kind:"method",key:"_handleFileCleared",value:async function(){this.value=null}},{kind:"method",key:"_cropFile",value:async function(e,i){var t,a;["image/png","image/jpeg","image/gif"].includes(e.type)?(t=this,a={file:e,options:this.cropOptions||{round:!1,aspectRatio:NaN},croppedCallback:t=>{i&&t===e?(this.value=(0,n.p6)(i,this.size,this.original),(0,s.B)(this,"change")):this._uploadFile(t)}},(0,s.B)(t,"show-dialog",{dialogTag:"image-cropper-dialog",dialogImport:c,dialogParams:a})):(0,d.Ys)(this,{text:this.hass.localize("ui.components.picture-upload.unsupported_format")})}},{kind:"method",key:"_uploadFile",value:async function(e){if(["image/png","image/jpeg","image/gif"].includes(e.type)){this._uploading=!0;try{const i=await(0,n.Bi)(this.hass,e);this.value=(0,n.p6)(i.id,this.size,this.original),(0,s.B)(this,"change")}catch(i){(0,d.Ys)(this,{text:i.toString()})}finally{this._uploading=!1}}else(0,d.Ys)(this,{text:this.hass.localize("ui.components.picture-upload.unsupported_format")})}},{kind:"field",key:"_chooseMedia",value(){return()=>{(0,u.B)(this,{action:"pick",entityId:"browser",navigateIds:[{media_content_id:void 0,media_content_type:void 0},{media_content_id:n.dg,media_content_type:"app"}],minimumNavigateLevel:2,mediaPickedCallback:async e=>{const i=(0,n.TT)(e.item.media_content_id);if(i)if(this.crop){const a=(0,n.p6)(i,void 0,!0);let o;try{o=await(0,n.n$)(this.hass,a)}catch(t){return void(0,d.Ys)(this,{text:t.toString()})}const l={type:e.item.media_content_type},s=new File([o],e.item.title,l);this._cropFile(s,i)}else this.value=(0,n.p6)(i,this.size,this.original),(0,s.B)(this,"change")}})}}},{kind:"get",static:!0,key:"styles",value:function(){return[r.Qx,o.iv`
        :host {
          display: block;
          height: 240px;
        }
        ha-file-upload {
          height: 100%;
        }
        .center-vertical {
          display: flex;
          align-items: center;
          height: 100%;
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
      `]}}]}}),o.oi)},92903:function(e,i,t){t.d(i,{B:()=>o});var a=t(11297);const o=(e,i)=>{(0,a.B)(e,"show-dialog",{dialogTag:"dialog-media-player-browse",dialogImport:()=>Promise.all([t.e("9287"),t.e("2670"),t.e("6160"),t.e("2017")]).then(t.bind(t,11646)),dialogParams:i})}},18727:function(e,i,t){t.d(i,{Bi:()=>r,JS:()=>a,TT:()=>l,ao:()=>n,dg:()=>o,n$:()=>d,p6:()=>s});const a="/api/image/serve/",o="media-source://image_upload",l=e=>{let i;if(e.startsWith(a)){i=e.substring(a.length);const t=i.indexOf("/");t>=0&&(i=i.substring(0,t))}else e.startsWith(o)&&(i=e.substring(o.length+1));return i},s=(e,i,t=!1)=>{if(!t&&!i)throw new Error("Size must be provided if original is false");return t?`/api/image/serve/${e}/original`:`/api/image/serve/${e}/${i}x${i}`},r=async(e,i)=>{const t=new FormData;t.append("file",i);const a=await e.fetchWithAuth("/api/image/upload",{method:"POST",body:t});if(413===a.status)throw new Error(`Uploaded image is too large (${i.name})`);if(200!==a.status)throw new Error("Unknown error");return a.json()},n=(e,i)=>e.callWS({type:"image/delete",image_id:i}),d=async(e,i)=>{const t=await fetch(e.hassUrl(i));if(!t.ok)throw new Error(`Failed to fetch image: ${t.statusText?t.statusText:t.status}`);return t.blob()}}};
//# sourceMappingURL=8963.8653d58b3e44c1d5.js.map