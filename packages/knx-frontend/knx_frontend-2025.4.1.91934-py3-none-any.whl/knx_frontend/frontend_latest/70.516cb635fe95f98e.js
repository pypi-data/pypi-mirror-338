export const __webpack_ids__=["70"];export const __webpack_modules__={14995:function(i,e,t){t.r(e),t.d(e,{HaImagecropperDialog:()=>d});var a=t(44249),o=(t(31622),t(65509)),r=t.n(o),s=t(93528),c=t(57243),n=t(50778),p=t(35359),l=(t(44118),t(66193));let d=(0,a.Z)([(0,n.Mo)("image-cropper-dialog")],(function(i,e){return{F:class extends e{constructor(...e){super(...e),i(this)}},d:[{kind:"field",decorators:[(0,n.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_params",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_open",value(){return!1}},{kind:"field",decorators:[(0,n.IO)("img",!0)],key:"_image",value:void 0},{kind:"field",key:"_cropper",value:void 0},{kind:"field",decorators:[(0,n.SB)()],key:"_isTargetAspectRatio",value:void 0},{kind:"method",key:"showDialog",value:function(i){this._params=i,this._open=!0}},{kind:"method",key:"closeDialog",value:function(){this._open=!1,this._params=void 0,this._cropper?.destroy(),this._cropper=void 0,this._isTargetAspectRatio=!1}},{kind:"method",key:"updated",value:function(i){i.has("_params")&&this._params&&(this._cropper?this._cropper.replace(URL.createObjectURL(this._params.file)):(this._image.src=URL.createObjectURL(this._params.file),this._cropper=new(r())(this._image,{aspectRatio:this._params.options.aspectRatio,viewMode:1,dragMode:"move",minCropBoxWidth:50,ready:()=>{this._isTargetAspectRatio=this._checkMatchAspectRatio(),URL.revokeObjectURL(this._image.src)}})))}},{kind:"method",key:"_checkMatchAspectRatio",value:function(){const i=this._params?.options.aspectRatio;if(!i)return!0;const e=this._cropper.getImageData();if(e.aspectRatio===i)return!0;if(e.naturalWidth>e.naturalHeight){const t=e.naturalWidth/i;return Math.abs(t-e.naturalHeight)<=1}const t=e.naturalHeight*i;return Math.abs(t-e.naturalWidth)<=1}},{kind:"method",key:"render",value:function(){return c.dy`<ha-dialog
      @closed=${this.closeDialog}
      scrimClickAction
      escapeKeyAction
      .open=${this._open}
    >
      <div
        class="container ${(0,p.$)({round:Boolean(this._params?.options.round)})}"
      >
        <img alt=${this.hass.localize("ui.dialogs.image_cropper.crop_image")} />
      </div>
      <mwc-button slot="secondaryAction" @click=${this.closeDialog}>
        ${this.hass.localize("ui.common.cancel")}
      </mwc-button>
      ${this._isTargetAspectRatio?c.dy`<mwc-button slot="primaryAction" @click=${this._useOriginal}>
            ${this.hass.localize("ui.dialogs.image_cropper.use_original")}
          </mwc-button>`:c.Ld}

      <mwc-button slot="primaryAction" @click=${this._cropImage}>
        ${this.hass.localize("ui.dialogs.image_cropper.crop")}
      </mwc-button>
    </ha-dialog>`}},{kind:"method",key:"_cropImage",value:function(){this._cropper.getCroppedCanvas().toBlob((i=>{if(!i)return;const e=new File([i],this._params.file.name,{type:this._params.options.type||this._params.file.type});this._params.croppedCallback(e),this.closeDialog()}),this._params.options.type||this._params.file.type,this._params.options.quality)}},{kind:"method",key:"_useOriginal",value:function(){this._params.croppedCallback(this._params.file),this.closeDialog()}},{kind:"get",static:!0,key:"styles",value:function(){return[l.yu,c.iv`
        ${(0,c.$m)(s)}
        .container {
          max-width: 640px;
        }
        img {
          max-width: 100%;
        }
        .container.round .cropper-view-box,
        .container.round .cropper-face {
          border-radius: 50%;
        }
        .cropper-line,
        .cropper-point,
        .cropper-point.point-se::before {
          background-color: var(--primary-color);
        }
      `]}}]}}),c.oi)}};
//# sourceMappingURL=70.516cb635fe95f98e.js.map