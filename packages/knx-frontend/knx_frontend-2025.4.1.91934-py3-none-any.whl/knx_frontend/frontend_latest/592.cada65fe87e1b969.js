export const __webpack_ids__=["592"];export const __webpack_modules__={28838:function(e,t,i){i.r(t),i.d(t,{HaBackupLocationSelector:()=>p});var a=i(44249),s=i(57243),o=i(50778),n=i(27486),u=i(49672),r=i(11297),l=i(81036),d=i(32770);let h=function(e){return e.BIND="bind",e.CIFS="cifs",e.NFS="nfs",e}({}),c=function(e){return e.BACKUP="backup",e.MEDIA="media",e.SHARE="share",e}({});i(17949),i(74064),i(58130);const k="/backup";(0,a.Z)([(0,o.Mo)("ha-mount-picker")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"required",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)()],key:"usage",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_mounts",value:void 0},{kind:"field",decorators:[(0,o.SB)()],key:"_error",value:void 0},{kind:"method",key:"firstUpdated",value:function(){this._getMounts()}},{kind:"method",key:"render",value:function(){if(this._error)return s.dy`<ha-alert alert-type="error">${this._error}</ha-alert>`;if(!this._mounts)return s.Ld;const e=s.dy`<ha-list-item
      graphic="icon"
      .value=${k}
    >
      <span>
        ${this.hass.localize("ui.components.mount-picker.use_datadisk")||"Use data disk for backup"}
      </span>
      <ha-svg-icon slot="graphic" .path=${"M6,2H18A2,2 0 0,1 20,4V20A2,2 0 0,1 18,22H6A2,2 0 0,1 4,20V4A2,2 0 0,1 6,2M12,4A6,6 0 0,0 6,10C6,13.31 8.69,16 12.1,16L11.22,13.77C10.95,13.29 11.11,12.68 11.59,12.4L12.45,11.9C12.93,11.63 13.54,11.79 13.82,12.27L15.74,14.69C17.12,13.59 18,11.9 18,10A6,6 0 0,0 12,4M12,9A1,1 0 0,1 13,10A1,1 0 0,1 12,11A1,1 0 0,1 11,10A1,1 0 0,1 12,9M7,18A1,1 0 0,0 6,19A1,1 0 0,0 7,20A1,1 0 0,0 8,19A1,1 0 0,0 7,18M12.09,13.27L14.58,19.58L17.17,18.08L12.95,12.77L12.09,13.27Z"}></ha-svg-icon>
    </ha-list-item>`;return s.dy`
      <ha-select
        .label=${void 0===this.label&&this.hass?this.hass.localize("ui.components.mount-picker.mount"):this.label}
        .value=${this._value}
        .required=${this.required}
        .disabled=${this.disabled}
        .helper=${this.helper}
        @selected=${this._mountChanged}
        @closed=${l.U}
        fixedMenuPosition
        naturalMenuWidth
      >
        ${this.usage!==c.BACKUP||this._mounts.default_backup_mount&&this._mounts.default_backup_mount!==k?s.Ld:e}
        ${this._filterMounts(this._mounts,this.usage).map((e=>s.dy`<ha-list-item twoline graphic="icon" .value=${e.name}>
              <span>${e.name}</span>
              <span slot="secondary"
                >${e.server}${e.port?`:${e.port}`:s.Ld}${e.type===h.NFS?e.path:`:${e.share}`}</span
              >
              <ha-svg-icon
                slot="graphic"
                .path=${e.usage===c.MEDIA?"M19 3H5C3.89 3 3 3.89 3 5V19C3 20.1 3.9 21 5 21H19C20.1 21 21 20.1 21 19V5C21 3.89 20.1 3 19 3M10 16V8L15 12":e.usage===c.SHARE?"M10,4H4C2.89,4 2,4.89 2,6V18A2,2 0 0,0 4,20H20A2,2 0 0,0 22,18V8C22,6.89 21.1,6 20,6H12L10,4Z":"M12,3A9,9 0 0,0 3,12H0L4,16L8,12H5A7,7 0 0,1 12,5A7,7 0 0,1 19,12A7,7 0 0,1 12,19C10.5,19 9.09,18.5 7.94,17.7L6.5,19.14C8.04,20.3 9.94,21 12,21A9,9 0 0,0 21,12A9,9 0 0,0 12,3M14,12A2,2 0 0,0 12,10A2,2 0 0,0 10,12A2,2 0 0,0 12,14A2,2 0 0,0 14,12Z"}
              ></ha-svg-icon>
            </ha-list-item>`))}
        ${this.usage===c.BACKUP&&this._mounts.default_backup_mount?e:s.Ld}
      </ha-select>
    `}},{kind:"field",key:"_filterMounts",value(){return(0,n.Z)(((e,t)=>{let i=e.mounts.filter((e=>[h.CIFS,h.NFS].includes(e.type)));return t&&(i=e.mounts.filter((e=>e.usage===t))),i.sort(((t,i)=>t.name===e.default_backup_mount?-1:i.name===e.default_backup_mount?1:(0,d.fe)(t.name,i.name,this.hass.locale.language)))}))}},{kind:"method",key:"_getMounts",value:async function(){try{(0,u.p)(this.hass,"hassio")?(this._mounts=await(async e=>e.callWS({type:"supervisor/api",endpoint:"/mounts",method:"get",timeout:null}))(this.hass),this.usage!==c.BACKUP||this.value||(this.value=this._mounts.default_backup_mount||k)):this._error=this.hass.localize("ui.components.mount-picker.error.no_supervisor")}catch(e){this._error=this.hass.localize("ui.components.mount-picker.error.fetch_mounts")}}},{kind:"get",key:"_value",value:function(){return this.value||""}},{kind:"method",key:"_mountChanged",value:function(e){e.stopPropagation();const t=e.target.value;t!==this._value&&this._setValue(t)}},{kind:"method",key:"_setValue",value:function(e){this.value=e,setTimeout((()=>{(0,r.B)(this,"value-changed",{value:e}),(0,r.B)(this,"change")}),0)}},{kind:"get",static:!0,key:"styles",value:function(){return[s.iv`
        ha-select {
          width: 100%;
        }
      `]}}]}}),s.oi);let p=(0,a.Z)([(0,o.Mo)("ha-selector-backup_location")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,o.Cb)({attribute:!1})],key:"selector",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"value",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"label",value:void 0},{kind:"field",decorators:[(0,o.Cb)()],key:"helper",value:void 0},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,o.Cb)({type:Boolean})],key:"required",value(){return!0}},{kind:"method",key:"render",value:function(){return s.dy`<ha-mount-picker
      .hass=${this.hass}
      .value=${this.value}
      .label=${this.label}
      .helper=${this.helper}
      .disabled=${this.disabled}
      .required=${this.required}
      usage="backup"
    ></ha-mount-picker>`}},{kind:"field",static:!0,key:"styles",value(){return s.iv`
    ha-mount-picker {
      width: 100%;
    }
  `}}]}}),s.oi)}};
//# sourceMappingURL=592.cada65fe87e1b969.js.map