"use strict";(self.webpackChunkknx_frontend=self.webpackChunkknx_frontend||[]).push([["1261"],{90842:function(e,t,i){i.d(t,{t:()=>o});i(92745),i(9359),i(31526),i(77439),i(19423),i(88972);class s{constructor(e=window.localStorage){this.storage=void 0,this._storage={},this._listeners={},this.storage=e,e===window.localStorage&&window.addEventListener("storage",(e=>{e.key&&this.hasKey(e.key)&&(this._storage[e.key]=e.newValue?JSON.parse(e.newValue):e.newValue,this._listeners[e.key]&&this._listeners[e.key].forEach((t=>t(e.oldValue?JSON.parse(e.oldValue):e.oldValue,this._storage[e.key]))))}))}addFromStorage(e){if(!this._storage[e]){const t=this.storage.getItem(e);t&&(this._storage[e]=JSON.parse(t))}}subscribeChanges(e,t){return this._listeners[e]?this._listeners[e].push(t):this._listeners[e]=[t],()=>{this.unsubscribeChanges(e,t)}}unsubscribeChanges(e,t){if(!(e in this._listeners))return;const i=this._listeners[e].indexOf(t);-1!==i&&this._listeners[e].splice(i,1)}hasKey(e){return e in this._storage}getValue(e){return this._storage[e]}setValue(e,t){const i=this._storage[e];this._storage[e]=t;try{void 0===t?this.storage.removeItem(e):this.storage.setItem(e,JSON.stringify(t))}catch(s){}finally{this._listeners[e]&&this._listeners[e].forEach((e=>e(i,t)))}}}const n={},o=e=>t=>{const i=e.storage||"localStorage";let o;i&&i in n?o=n[i]:(o=new s(window[i]),n[i]=o);const a=String(t.key),r=e.key||String(t.key),d=t.initializer?t.initializer():void 0;o.addFromStorage(r);const l=!1!==e.subscribe?e=>o.subscribeChanges(r,((i,s)=>{e.requestUpdate(t.key,i)})):void 0,c=()=>o.hasKey(r)?e.deserializer?e.deserializer(o.getValue(r)):o.getValue(r):d;return{kind:"method",placement:"prototype",key:t.key,descriptor:{set(i){((i,s)=>{let n;e.state&&(n=c()),o.setValue(r,e.serializer?e.serializer(s):s),e.state&&i.requestUpdate(t.key,n)})(this,i)},get(){return c()},enumerable:!0,configurable:!0},finisher(i){if(e.state&&e.subscribe){const e=i.prototype.connectedCallback,t=i.prototype.disconnectedCallback;i.prototype.connectedCallback=function(){e.call(this),this[`__unbsubLocalStorage${a}`]=null==l?void 0:l(this)},i.prototype.disconnectedCallback=function(){var e;t.call(this),null===(e=this[`__unbsubLocalStorage${a}`])||void 0===e||e.call(this),this[`__unbsubLocalStorage${a}`]=void 0}}e.state&&i.createProperty(t.key,Object.assign({noAccessor:!0},e.stateOptions))}}}},21955:function(e,t,i){var s=i(73577),n=i(72621),o=(i(71695),i(92745),i(82328),i(55751),i(26200),i(25754),i(22246),i(9359),i(70104),i(40251),i(81804),i(52629),i(92789),i(36810),i(14953),i(58402),i(31503),i(16440),i(2213),i(57385),i(71375),i(15524),i(20267),i(21917),i(56193),i(25020),i(45729),i(47021),i(57243)),a=i(50778),r=i(35359),d=i(4855),l=i(4468),c=i(31762);i(72700),i(8038),i(71513),i(75656),i(50100),i(18084);class h{constructor(e){this._active=!1,this._callback=void 0,this._context=void 0,this._stream=void 0,this._source=void 0,this._recorder=void 0,this._callback=e}get active(){return this._active}get sampleRate(){var e;return null===(e=this._context)||void 0===e?void 0:e.sampleRate}static get isSupported(){return window.isSecureContext&&(window.AudioContext||window.webkitAudioContext)}async start(){if(this._context&&this._stream&&this._source&&this._recorder)this._stream.getTracks()[0].enabled=!0,await this._context.resume(),this._active=!0;else try{await this._createContext()}catch(e){console.error(e),this._active=!1}}async stop(){var e;this._active=!1,this._stream&&(this._stream.getTracks()[0].enabled=!1),await(null===(e=this._context)||void 0===e?void 0:e.suspend())}close(){var e,t,i;this._active=!1,null===(e=this._stream)||void 0===e||e.getTracks()[0].stop(),this._recorder&&(this._recorder.port.onmessage=null),null===(t=this._source)||void 0===t||t.disconnect(),null===(i=this._context)||void 0===i||i.close(),this._stream=void 0,this._source=void 0,this._recorder=void 0,this._context=void 0}async _createContext(){const e=new(AudioContext||webkitAudioContext);this._stream=await navigator.mediaDevices.getUserMedia({audio:!0}),await e.audioWorklet.addModule(new URL(i(55328),i.b)),this._context=e,this._source=this._context.createMediaStreamSource(this._stream),this._recorder=new AudioWorkletNode(this._context,"recorder-worklet"),this._recorder.port.onmessage=e=>{this._active&&this._callback(e.data)},this._active=!0,this._source.connect(this._recorder)}}i(17949),i(70596);var u=i(26205),p=i(4557);let _,v,g,m,y,k,f,b,x,w,L=e=>e;(0,s.Z)([(0,a.Mo)("ha-assist-chat")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"pipeline",value:void 0},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:"disable-speech"})],key:"disableSpeech",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:!1})],key:"startListening",value:void 0},{kind:"field",decorators:[(0,a.IO)("#message-input")],key:"_messageInput",value:void 0},{kind:"field",decorators:[(0,a.IO)("#scroll-container")],key:"_scrollContainer",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_conversation",value(){return[]}},{kind:"field",decorators:[(0,a.SB)()],key:"_showSendButton",value(){return!1}},{kind:"field",decorators:[(0,a.SB)()],key:"_processing",value(){return!1}},{kind:"field",key:"_conversationId",value(){return null}},{kind:"field",key:"_audioRecorder",value:void 0},{kind:"field",key:"_audioBuffer",value:void 0},{kind:"field",key:"_audio",value:void 0},{kind:"field",key:"_stt_binary_handler_id",value:void 0},{kind:"method",key:"willUpdate",value:function(e){this.hasUpdated&&!e.has("pipeline")||(this._conversation=[{who:"hass",text:this.hass.localize("ui.dialogs.voice_command.how_can_i_help")}])}},{kind:"method",key:"firstUpdated",value:function(e){(0,n.Z)(i,"firstUpdated",this,3)([e]),this.startListening&&this.pipeline&&this.pipeline.stt_engine&&h.isSupported&&this._toggleListening(),setTimeout((()=>this._messageInput.focus()),0)}},{kind:"method",key:"updated",value:function(e){(0,n.Z)(i,"updated",this,3)([e]),e.has("_conversation")&&this._scrollMessagesBottom()}},{kind:"method",key:"disconnectedCallback",value:function(){var e,t;(0,n.Z)(i,"disconnectedCallback",this,3)([]),null===(e=this._audioRecorder)||void 0===e||e.close(),this._audioRecorder=void 0,null===(t=this._audio)||void 0===t||t.pause(),this._conversation=[],this._conversationId=null}},{kind:"method",key:"render",value:function(){var e,t;const i=!!this.pipeline&&(this.pipeline.prefer_local_intents||!this.hass.states[this.pipeline.conversation_engine]||(0,l.e)(this.hass.states[this.pipeline.conversation_engine],c.zt.CONTROL)),s=h.isSupported,n=(null===(e=this.pipeline)||void 0===e?void 0:e.stt_engine)&&!this.disableSpeech;return(0,o.dy)(_||(_=L`
      ${0}
      <div class="messages">
        <div class="messages-container" id="scroll-container">
          ${0}
        </div>
      </div>
      <div class="input" slot="primaryAction">
        <ha-textfield
          id="message-input"
          @keyup=${0}
          @input=${0}
          .label=${0}
          .iconTrailing=${0}
        >
          <div slot="trailingIcon">
            ${0}
          </div>
        </ha-textfield>
      </div>
    `),i?o.Ld:(0,o.dy)(v||(v=L`
            <ha-alert>
              ${0}
            </ha-alert>
          `),this.hass.localize("ui.dialogs.voice_command.conversation_no_control")),this._conversation.map((e=>(0,o.dy)(g||(g=L`
                <div class="message ${0}">${0}</div>
              `),(0,r.$)({error:!!e.error,[e.who]:!0}),e.text))),this._handleKeyUp,this._handleInput,this.hass.localize("ui.dialogs.voice_command.input_label"),!0,this._showSendButton||!n?(0,o.dy)(m||(m=L`
                  <ha-icon-button
                    class="listening-icon"
                    .path=${0}
                    @click=${0}
                    .disabled=${0}
                    .label=${0}
                  >
                  </ha-icon-button>
                `),"M2,21L23,12L2,3V10L17,12L2,14V21Z",this._handleSendMessage,this._processing,this.hass.localize("ui.dialogs.voice_command.send_text")):(0,o.dy)(y||(y=L`
                  ${0}

                  <div class="listening-icon">
                    <ha-icon-button
                      .path=${0}
                      @click=${0}
                      .disabled=${0}
                      .label=${0}
                    >
                    </ha-icon-button>
                    ${0}
                  </div>
                `),null!==(t=this._audioRecorder)&&void 0!==t&&t.active?(0,o.dy)(k||(k=L`
                        <div class="bouncer">
                          <div class="double-bounce1"></div>
                          <div class="double-bounce2"></div>
                        </div>
                      `)):o.Ld,"M12,2A3,3 0 0,1 15,5V11A3,3 0 0,1 12,14A3,3 0 0,1 9,11V5A3,3 0 0,1 12,2M19,11C19,14.53 16.39,17.44 13,17.93V21H11V17.93C7.61,17.44 5,14.53 5,11H7A5,5 0 0,0 12,16A5,5 0 0,0 17,11H19Z",this._handleListeningButton,this._processing,this.hass.localize("ui.dialogs.voice_command.start_listening"),s?null:(0,o.dy)(f||(f=L`
                          <ha-svg-icon
                            .path=${0}
                            class="unsupported"
                          ></ha-svg-icon>
                        `),"M13,13H11V7H13M13,17H11V15H13M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2Z")))}},{kind:"method",key:"_scrollMessagesBottom",value:function(){const e=this._scrollContainer;e&&e.scrollTo(0,e.scrollHeight)}},{kind:"method",key:"_handleKeyUp",value:function(e){const t=e.target;!this._processing&&"Enter"===e.key&&t.value&&(this._processText(t.value),t.value="",this._showSendButton=!1)}},{kind:"method",key:"_handleInput",value:function(e){const t=e.target.value;t&&!this._showSendButton?this._showSendButton=!0:!t&&this._showSendButton&&(this._showSendButton=!1)}},{kind:"method",key:"_handleSendMessage",value:function(){this._messageInput.value&&(this._processText(this._messageInput.value.trim()),this._messageInput.value="",this._showSendButton=!1)}},{kind:"method",key:"_handleListeningButton",value:function(e){e.stopPropagation(),e.preventDefault(),this._toggleListening()}},{kind:"method",key:"_toggleListening",value:async function(){var e;h.isSupported?null!==(e=this._audioRecorder)&&void 0!==e&&e.active?this._stopListening():this._startListening():this._showNotSupportedMessage()}},{kind:"method",key:"_addMessage",value:function(e){this._conversation=[...this._conversation,e]}},{kind:"method",key:"_showNotSupportedMessage",value:async function(){this._addMessage({who:"hass",text:(0,o.dy)(b||(b=L`${0}

        ${0}`),this.hass.localize("ui.dialogs.voice_command.not_supported_microphone_browser"),this.hass.localize("ui.dialogs.voice_command.not_supported_microphone_documentation",{documentation_link:(0,o.dy)(x||(x=L`<a
                target="_blank"
                rel="noopener noreferrer"
                href=${0}
              >${0}</a>`),(0,u.R)(this.hass,"/docs/configuration/securing/#remote-access"),this.hass.localize("ui.dialogs.voice_command.not_supported_microphone_documentation_link"))}))})}},{kind:"method",key:"_startListening",value:async function(){var e;this._processing=!0,null===(e=this._audio)||void 0===e||e.pause(),this._audioRecorder||(this._audioRecorder=new h((e=>{this._audioBuffer?this._audioBuffer.push(e):this._sendAudioChunk(e)}))),this._stt_binary_handler_id=void 0,this._audioBuffer=[];const t={who:"user",text:"…"};await this._audioRecorder.start(),this._addMessage(t),this.requestUpdate("_audioRecorder");let i=!1,s={who:"hass",text:"…",error:!1},n="";try{var o,a;const e=await(0,d.Xp)(this.hass,(o=>{if("run-start"===o.type&&(this._stt_binary_handler_id=o.data.runner_data.stt_binary_handler_id),"stt-start"===o.type&&this._audioBuffer){for(const e of this._audioBuffer)this._sendAudioChunk(e);this._audioBuffer=void 0}if("stt-end"===o.type&&(this._stt_binary_handler_id=void 0,this._stopListening(),t.text=o.data.stt_output.text,this.requestUpdate("_conversation"),this._addMessage(s)),"intent-progress"===o.type){const e=o.data.chat_log_delta;e.role&&(n&&e.role&&"…"!==s.text&&(s.text=s.text.substring(0,s.text.length-1),s={who:"hass",text:"…",error:!1},this._addMessage(s)),n=e.role),"assistant"===n&&"content"in e&&e.content&&(s.text=s.text.substring(0,s.text.length-1)+e.content+"…",this.requestUpdate("_conversation"))}if("intent-end"===o.type){var a;this._conversationId=o.data.intent_output.conversation_id,i=o.data.intent_output.continue_conversation;const e=null===(a=o.data.intent_output.response.speech)||void 0===a?void 0:a.plain;e&&(s.text=e.speech),this.requestUpdate("_conversation")}if("tts-end"===o.type){const e=o.data.tts_output.url;this._audio=new Audio(e),this._audio.play(),this._audio.addEventListener("ended",(()=>{this._unloadAudio(),i&&this._startListening()})),this._audio.addEventListener("pause",this._unloadAudio),this._audio.addEventListener("canplaythrough",this._playAudio),this._audio.addEventListener("error",this._audioError)}"run-end"===o.type&&(this._stt_binary_handler_id=void 0,e()),"error"===o.type&&(this._stt_binary_handler_id=void 0,"…"===t.text?(t.text=o.data.message,t.error=!0):(s.text=o.data.message,s.error=!0),this._stopListening(),this.requestUpdate("_conversation"),e())}),{start_stage:"stt",end_stage:null!==(o=this.pipeline)&&void 0!==o&&o.tts_engine?"tts":"intent",input:{sample_rate:this._audioRecorder.sampleRate},pipeline:null===(a=this.pipeline)||void 0===a?void 0:a.id,conversation_id:this._conversationId})}catch(r){await(0,p.Ys)(this,{title:"Error starting pipeline",text:r.message||r}),this._stopListening()}finally{this._processing=!1}}},{kind:"method",key:"_stopListening",value:function(){var e;if(null===(e=this._audioRecorder)||void 0===e||e.stop(),this.requestUpdate("_audioRecorder"),this._stt_binary_handler_id){if(this._audioBuffer)for(const e of this._audioBuffer)this._sendAudioChunk(e);this._sendAudioChunk(new Int16Array),this._stt_binary_handler_id=void 0}this._audioBuffer=void 0}},{kind:"method",key:"_sendAudioChunk",value:function(e){if(this.hass.connection.socket.binaryType="arraybuffer",null==this._stt_binary_handler_id)return;const t=new Uint8Array(1+2*e.length);t[0]=this._stt_binary_handler_id,t.set(new Uint8Array(e.buffer),1),this.hass.connection.socket.send(t)}},{kind:"field",key:"_playAudio",value(){return()=>{var e;null===(e=this._audio)||void 0===e||e.play()}}},{kind:"field",key:"_audioError",value(){return()=>{var e;(0,p.Ys)(this,{title:"Error playing audio."}),null===(e=this._audio)||void 0===e||e.removeAttribute("src")}}},{kind:"field",key:"_unloadAudio",value(){return()=>{var e;null===(e=this._audio)||void 0===e||e.removeAttribute("src"),this._audio=void 0}}},{kind:"method",key:"_processText",value:async function(e){var t;this._processing=!0,null===(t=this._audio)||void 0===t||t.pause(),this._addMessage({who:"user",text:e});let i={who:"hass",text:"…",error:!1},s="";this._addMessage(i);try{var n;const t=await(0,d.Xp)(this.hass,(e=>{if("intent-progress"===e.type){const t=e.data.chat_log_delta;t.role&&(s&&"assistant"===t.role&&"…"!==i.text&&(i.text=i.text.substring(0,i.text.length-1),i={who:"hass",text:"…",error:!1},this._addMessage(i)),s=t.role),"assistant"===s&&"content"in t&&t.content&&(i.text=i.text.substring(0,i.text.length-1)+t.content+"…",this.requestUpdate("_conversation"))}if("intent-end"===e.type){var n;this._conversationId=e.data.intent_output.conversation_id;const s=null===(n=e.data.intent_output.response.speech)||void 0===n?void 0:n.plain;s&&(i.text=s.speech),this.requestUpdate("_conversation"),t()}"error"===e.type&&(i.text=e.data.message,i.error=!0,this.requestUpdate("_conversation"),t())}),{start_stage:"intent",input:{text:e},end_stage:"intent",pipeline:null===(n=this.pipeline)||void 0===n?void 0:n.id,conversation_id:this._conversationId})}catch(o){i.text=this.hass.localize("ui.dialogs.voice_command.error"),i.error=!0,this.requestUpdate("_conversation")}finally{this._processing=!1}}},{kind:"field",static:!0,key:"styles",value(){return(0,o.iv)(w||(w=L`
    :host {
      flex: 1;
      display: flex;
      flex-direction: column;
    }
    ha-textfield {
      display: block;
    }
    .messages {
      flex: 1;
      display: block;
      box-sizing: border-box;
      position: relative;
    }
    .messages-container {
      position: absolute;
      bottom: 0px;
      right: 0px;
      left: 0px;
      padding: 0px 10px 16px;
      box-sizing: border-box;
      overflow-y: auto;
      max-height: 100%;
    }
    .message {
      white-space: pre-line;
      font-size: 18px;
      clear: both;
      margin: 8px 0;
      padding: 8px;
      border-radius: 15px;
    }

    @media all and (max-width: 450px), all and (max-height: 500px) {
      .message {
        font-size: 16px;
      }
    }

    .message p {
      margin: 0;
    }
    .message p:not(:last-child) {
      margin-bottom: 8px;
    }

    .message.user {
      margin-left: 24px;
      margin-inline-start: 24px;
      margin-inline-end: initial;
      float: var(--float-end);
      text-align: right;
      border-bottom-right-radius: 0px;
      background-color: var(--chat-background-color-user, var(--primary-color));
      color: var(--text-primary-color);
      direction: var(--direction);
    }

    .message.hass {
      margin-right: 24px;
      margin-inline-end: 24px;
      margin-inline-start: initial;
      float: var(--float-start);
      border-bottom-left-radius: 0px;
      background-color: var(
        --chat-background-color-hass,
        var(--secondary-background-color)
      );

      color: var(--primary-text-color);
      direction: var(--direction);
    }

    .message.user a {
      color: var(--text-primary-color);
    }

    .message.hass a {
      color: var(--primary-text-color);
    }

    .message.error {
      background-color: var(--error-color);
      color: var(--text-primary-color);
    }

    .bouncer {
      width: 48px;
      height: 48px;
      position: absolute;
    }
    .double-bounce1,
    .double-bounce2 {
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background-color: var(--primary-color);
      opacity: 0.2;
      position: absolute;
      top: 0;
      left: 0;
      -webkit-animation: sk-bounce 2s infinite ease-in-out;
      animation: sk-bounce 2s infinite ease-in-out;
    }
    .double-bounce2 {
      -webkit-animation-delay: -1s;
      animation-delay: -1s;
    }
    @-webkit-keyframes sk-bounce {
      0%,
      100% {
        -webkit-transform: scale(0);
      }
      50% {
        -webkit-transform: scale(1);
      }
    }
    @keyframes sk-bounce {
      0%,
      100% {
        transform: scale(0);
        -webkit-transform: scale(0);
      }
      50% {
        transform: scale(1);
        -webkit-transform: scale(1);
      }
    }

    .listening-icon {
      position: relative;
      color: var(--secondary-text-color);
      margin-right: -24px;
      margin-inline-end: -24px;
      margin-inline-start: initial;
      direction: var(--direction);
      transform: scaleX(var(--scale-direction));
    }

    .listening-icon[active] {
      color: var(--primary-color);
    }

    .unsupported {
      color: var(--error-color);
      position: absolute;
      --mdc-icon-size: 16px;
      right: 5px;
      inset-inline-end: 5px;
      inset-inline-start: initial;
      top: 0px;
    }
  `))}}]}}),o.oi)},43527:function(e,t,i){var s=i(73577),n=i(72621),o=(i(71695),i(9359),i(31526),i(47021),i(22997),i(57243)),a=i(50778),r=i(80155),d=i(24067);let l,c,h=e=>e;(0,s.Z)([(0,a.Mo)("ha-button-menu")],(function(e,t){class i extends t{constructor(...t){super(...t),e(this)}}return{F:i,d:[{kind:"field",key:d.gA,value:void 0},{kind:"field",decorators:[(0,a.Cb)()],key:"corner",value(){return"BOTTOM_START"}},{kind:"field",decorators:[(0,a.Cb)({attribute:"menu-corner"})],key:"menuCorner",value(){return"START"}},{kind:"field",decorators:[(0,a.Cb)({type:Number})],key:"x",value(){return null}},{kind:"field",decorators:[(0,a.Cb)({type:Number})],key:"y",value(){return null}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"multi",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"activatable",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"disabled",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean})],key:"fixed",value(){return!1}},{kind:"field",decorators:[(0,a.Cb)({type:Boolean,attribute:"no-anchor"})],key:"noAnchor",value(){return!1}},{kind:"field",decorators:[(0,a.IO)("mwc-menu",!0)],key:"_menu",value:void 0},{kind:"get",key:"items",value:function(){var e;return null===(e=this._menu)||void 0===e?void 0:e.items}},{kind:"get",key:"selected",value:function(){var e;return null===(e=this._menu)||void 0===e?void 0:e.selected}},{kind:"method",key:"focus",value:function(){var e,t;null!==(e=this._menu)&&void 0!==e&&e.open?this._menu.focusItemAtIndex(0):null===(t=this._triggerButton)||void 0===t||t.focus()}},{kind:"method",key:"render",value:function(){return(0,o.dy)(l||(l=h`
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
    `),this._handleClick,this._setTriggerAria,this.corner,this.menuCorner,this.fixed,this.multi,this.activatable,this.y,this.x)}},{kind:"method",key:"firstUpdated",value:function(e){(0,n.Z)(i,"firstUpdated",this,3)([e]),"rtl"===r.E.document.dir&&this.updateComplete.then((()=>{this.querySelectorAll("mwc-list-item").forEach((e=>{const t=document.createElement("style");t.innerHTML="span.material-icons:first-of-type { margin-left: var(--mdc-list-item-graphic-margin, 32px) !important; margin-right: 0px !important;}",e.shadowRoot.appendChild(t)}))}))}},{kind:"method",key:"_handleClick",value:function(){this.disabled||(this._menu.anchor=this.noAnchor?null:this,this._menu.show())}},{kind:"get",key:"_triggerButton",value:function(){return this.querySelector('ha-icon-button[slot="trigger"], mwc-button[slot="trigger"]')}},{kind:"method",key:"_setTriggerAria",value:function(){this._triggerButton&&(this._triggerButton.ariaHasPopup="menu")}},{kind:"field",static:!0,key:"styles",value(){return(0,o.iv)(c||(c=h`
    :host {
      display: inline-block;
      position: relative;
    }
    ::slotted([disabled]) {
      color: var(--disabled-text-color);
    }
  `))}}]}}),o.oi)},46915:function(e,t,i){i.a(e,(async function(e,s){try{i.r(t),i.d(t,{HaVoiceCommandDialog:()=>B});var n=i(73577),o=(i(19083),i(71695),i(9359),i(70104),i(40251),i(47021),i(31622),i(57243)),a=i(50778),r=i(90842),d=i(11297),l=i(81036),c=(i(20095),i(43527),i(44118),i(28906),i(59897),i(74064),i(17949),i(21955),i(19537)),h=i(4855),u=i(66193),p=i(26205),_=e([c]);c=(_.then?(await _)():_)[0];let v,g,m,y,k,f,b,x,w,L=e=>e;const $="M7.41,8.58L12,13.17L16.59,8.58L18,10L12,16L6,10L7.41,8.58Z",C="M19,6.41L17.59,5L12,10.59L6.41,5L5,6.41L10.59,12L5,17.59L6.41,19L12,13.41L17.59,19L19,17.59L13.41,12L19,6.41Z",A="M11,18H13V16H11V18M12,2A10,10 0 0,0 2,12A10,10 0 0,0 12,22A10,10 0 0,0 22,12A10,10 0 0,0 12,2M12,20C7.59,20 4,16.41 4,12C4,7.59 7.59,4 12,4C16.41,4 20,7.59 20,12C20,16.41 16.41,20 12,20M12,6A4,4 0 0,0 8,10H10A2,2 0 0,1 12,8A2,2 0 0,1 14,10C14,12 11,11.75 11,15H13C13,12.75 16,12.5 16,10A4,4 0 0,0 12,6Z",S="M12,17.27L18.18,21L16.54,13.97L22,9.24L14.81,8.62L12,2L9.19,8.62L2,9.24L7.45,13.97L5.82,21L12,17.27Z";let B=(0,n.Z)([(0,a.Mo)("ha-voice-command-dialog")],(function(e,t){return{F:class extends t{constructor(...t){super(...t),e(this)}},d:[{kind:"field",decorators:[(0,a.Cb)({attribute:!1})],key:"hass",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_opened",value(){return!1}},{kind:"field",decorators:[(0,r.t)({key:"AssistPipelineId",state:!0,subscribe:!1})],key:"_pipelineId",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_pipeline",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_pipelines",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_preferredPipeline",value:void 0},{kind:"field",decorators:[(0,a.SB)()],key:"_errorLoadAssist",value:void 0},{kind:"field",key:"_startListening",value(){return!1}},{kind:"method",key:"showDialog",value:async function(e){"preferred"===e.pipeline_id||"last_used"===e.pipeline_id&&!this._pipelineId?(await this._loadPipelines(),this._pipelineId=this._preferredPipeline):["last_used","preferred"].includes(e.pipeline_id)||(this._pipelineId=e.pipeline_id),this._startListening=e.start_listening,this._opened=!0}},{kind:"method",key:"closeDialog",value:async function(){this._opened=!1,this._pipelines=void 0,(0,d.B)(this,"dialog-closed",{dialog:this.localName})}},{kind:"method",key:"render",value:function(){var e,t,i;return this._opened?(0,o.dy)(v||(v=L`
      <ha-dialog
        open
        @closed=${0}
        .heading=${0}
        flexContent
        hideactions
      >
        <ha-dialog-header slot="heading">
          <ha-icon-button
            slot="navigationIcon"
            dialogAction="cancel"
            .label=${0}
            .path=${0}
          ></ha-icon-button>
          <div slot="title">
            ${0}
            <ha-button-menu
              @opened=${0}
              @closed=${0}
              activatable
              fixed
            >
              <ha-button slot="trigger">
                ${0}
                <ha-svg-icon
                  slot="trailingIcon"
                  .path=${0}
                ></ha-svg-icon>
              </ha-button>
              ${0}
              ${0}
            </ha-button-menu>
          </div>
          <a
            href=${0}
            slot="actionItems"
            target="_blank"
            rel="noopener noreferer"
          >
            <ha-icon-button
              .label=${0}
              .path=${0}
            ></ha-icon-button>
          </a>
        </ha-dialog-header>

        ${0}
      </ha-dialog>
    `),this.closeDialog,this.hass.localize("ui.dialogs.voice_command.title"),this.hass.localize("ui.common.close"),C,this.hass.localize("ui.dialogs.voice_command.title"),this._loadPipelines,l.U,null===(e=this._pipeline)||void 0===e?void 0:e.name,$,this._pipelines?null===(t=this._pipelines)||void 0===t?void 0:t.map((e=>(0,o.dy)(m||(m=L`<ha-list-item
                        ?selected=${0}
                        .pipeline=${0}
                        @click=${0}
                        .hasMeta=${0}
                      >
                        ${0}${0}
                      </ha-list-item>`),e.id===this._pipelineId||!this._pipelineId&&e.id===this._preferredPipeline,e.id,this._selectPipeline,e.id===this._preferredPipeline,e.name,e.id===this._preferredPipeline?(0,o.dy)(y||(y=L`
                              <ha-svg-icon
                                slot="meta"
                                .path=${0}
                              ></ha-svg-icon>
                            `),S):o.Ld))):(0,o.dy)(g||(g=L`<div class="pipelines-loading">
                    <ha-spinner size="small"></ha-spinner>
                  </div>`)),null!==(i=this.hass.user)&&void 0!==i&&i.is_admin?(0,o.dy)(k||(k=L`<li divider role="separator"></li>
                    <a href="/config/voice-assistants/assistants"
                      ><ha-list-item
                        >${0}</ha-list-item
                      ></a
                    >`),this.hass.localize("ui.dialogs.voice_command.manage_assistants")):o.Ld,(0,p.R)(this.hass,"/docs/assist/"),this.hass.localize("ui.common.help"),A,this._errorLoadAssist?(0,o.dy)(f||(f=L`<ha-alert alert-type="error">
              ${0}
            </ha-alert>`),this.hass.localize(`ui.dialogs.voice_command.${this._errorLoadAssist}_error_load_assist`)):this._pipeline?(0,o.dy)(b||(b=L`
                <ha-assist-chat
                  .hass=${0}
                  .pipeline=${0}
                  .startListening=${0}
                >
                </ha-assist-chat>
              `),this.hass,this._pipeline,this._startListening):(0,o.dy)(x||(x=L`<div class="pipelines-loading">
                <ha-spinner size="large"></ha-spinner>
              </div>`))):o.Ld}},{kind:"method",key:"willUpdate",value:function(e){(e.has("_pipelineId")||e.has("_opened")&&!0===this._opened&&this._pipelineId)&&this._getPipeline()}},{kind:"method",key:"_loadPipelines",value:async function(){if(this._pipelines)return;const{pipelines:e,preferred_pipeline:t}=await(0,h.SC)(this.hass);this._pipelines=e,this._preferredPipeline=t||void 0}},{kind:"method",key:"_selectPipeline",value:async function(e){this._pipelineId=e.currentTarget.pipeline,await this.updateComplete}},{kind:"method",key:"_getPipeline",value:async function(){this._pipeline=void 0,this._errorLoadAssist=void 0;const e=this._pipelineId;try{const t=await(0,h.PA)(this.hass,e);e===this._pipelineId&&(this._pipeline=t)}catch(t){if(e!==this._pipelineId)return;"not_found"===t.code?this._errorLoadAssist="not_found":(this._errorLoadAssist="unknown",console.error(t))}}},{kind:"get",static:!0,key:"styles",value:function(){return[u.yu,(0,o.iv)(w||(w=L`
        ha-dialog {
          --mdc-dialog-max-width: 500px;
          --mdc-dialog-max-height: 500px;
          --dialog-content-padding: 0;
        }
        ha-dialog-header a {
          color: var(--primary-text-color);
        }
        div[slot="title"] {
          display: flex;
          flex-direction: column;
          margin: -4px 0;
        }
        ha-button-menu {
          --mdc-theme-on-primary: var(--text-primary-color);
          --mdc-theme-primary: var(--primary-color);
          margin-top: -8px;
          margin-bottom: 0;
          margin-right: 0;
          margin-inline-end: 0;
          margin-left: -8px;
          margin-inline-start: -8px;
        }
        ha-button-menu ha-button {
          --mdc-theme-primary: var(--secondary-text-color);
          --mdc-typography-button-text-transform: none;
          --mdc-typography-button-font-size: unset;
          --mdc-typography-button-font-weight: 400;
          --mdc-typography-button-letter-spacing: var(
            --mdc-typography-headline6-letter-spacing,
            0.0125em
          );
          --mdc-typography-button-line-height: var(
            --mdc-typography-headline6-line-height,
            2rem
          );
          --button-height: auto;
        }
        ha-button-menu ha-button ha-svg-icon {
          height: 28px;
          margin-left: 4px;
          margin-inline-start: 4px;
          margin-inline-end: initial;
          direction: var(--direction);
        }
        ha-list-item {
          --mdc-list-item-meta-size: 16px;
        }
        ha-list-item ha-svg-icon {
          margin-left: 4px;
          margin-inline-start: 4px;
          margin-inline-end: initial;
          direction: var(--direction);
          display: block;
        }
        ha-button-menu a {
          text-decoration: none;
        }

        .pipelines-loading {
          display: flex;
          justify-content: center;
        }
        ha-assist-chat {
          margin: 0 24px 16px;
          min-height: 399px;
        }
      `))]}}]}}),o.oi);s()}catch(v){s(v)}}))},55328:function(e,t,i){e.exports=i.p+"55328.e6cfc021bf3e87fc.js"},52629:function(e,t,i){i(13492)("Int16",(function(e){return function(t,i,s){return e(this,t,i,s)}}))}}]);
//# sourceMappingURL=1261.4a71eb95ecddb50a.js.map