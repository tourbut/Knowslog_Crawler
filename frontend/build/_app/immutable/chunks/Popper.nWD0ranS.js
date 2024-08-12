import{s as ce,m as zt,e as dt,o as jt,i as $,d as X,w as St,L as fe,q as ae,v as xt,y as Pt,a as qt,b as Xt,f as Yt,n as ue,l as Ut,O as at,p as de,A as me,B as ge,C as he,D as pe,h as Dt,N as ye}from"./scheduler.DUae9vIM.js";import{S as be,i as we,t as it,g as ve,d as mt,f as xe,b as Ee,c as Ae,a as Oe,m as Ce,e as _e}from"./index.Cg4fAh3P.js";import{c as Re,g as Le,b as ke}from"./fastapi.D0Fit69C.js";import{F as Te}from"./Frame.B7UR13Po.js";const tt=Math.min,K=Math.max,gt=Math.round,ut=Math.floor,Y=t=>({x:t,y:t}),Se={left:"right",right:"left",bottom:"top",top:"bottom"},Pe={start:"end",end:"start"};function Et(t,e,n){return K(t,tt(e,n))}function st(t,e){return typeof t=="function"?t(e):t}function G(t){return t.split("-")[0]}function lt(t){return t.split("-")[1]}function Jt(t){return t==="x"?"y":"x"}function Ot(t){return t==="y"?"height":"width"}function et(t){return["top","bottom"].includes(G(t))?"y":"x"}function Ct(t){return Jt(et(t))}function De(t,e,n){n===void 0&&(n=!1);const o=lt(t),i=Ct(t),s=Ot(i);let r=i==="x"?o===(n?"end":"start")?"right":"left":o==="start"?"bottom":"top";return e.reference[s]>e.floating[s]&&(r=ht(r)),[r,ht(r)]}function Fe(t){const e=ht(t);return[At(t),e,At(e)]}function At(t){return t.replace(/start|end/g,e=>Pe[e])}function Be(t,e,n){const o=["left","right"],i=["right","left"],s=["top","bottom"],r=["bottom","top"];switch(t){case"top":case"bottom":return n?e?i:o:e?o:i;case"left":case"right":return e?s:r;default:return[]}}function Ne(t,e,n,o){const i=lt(t);let s=Be(G(t),n==="start",o);return i&&(s=s.map(r=>r+"-"+i),e&&(s=s.concat(s.map(At)))),s}function ht(t){return t.replace(/left|right|bottom|top/g,e=>Se[e])}function Me(t){return{top:0,right:0,bottom:0,left:0,...t}}function Kt(t){return typeof t!="number"?Me(t):{top:t,right:t,bottom:t,left:t}}function pt(t){const{x:e,y:n,width:o,height:i}=t;return{width:o,height:i,top:n,left:e,right:e+o,bottom:n+i,x:e,y:n}}function Ft(t,e,n){let{reference:o,floating:i}=t;const s=et(e),r=Ct(e),l=Ot(r),c=G(e),f=s==="y",m=o.x+o.width/2-i.width/2,d=o.y+o.height/2-i.height/2,p=o[l]/2-i[l]/2;let u;switch(c){case"top":u={x:m,y:o.y-i.height};break;case"bottom":u={x:m,y:o.y+o.height};break;case"right":u={x:o.x+o.width,y:d};break;case"left":u={x:o.x-i.width,y:d};break;default:u={x:o.x,y:o.y}}switch(lt(e)){case"start":u[r]-=p*(n&&f?-1:1);break;case"end":u[r]+=p*(n&&f?-1:1);break}return u}const Ve=async(t,e,n)=>{const{placement:o="bottom",strategy:i="absolute",middleware:s=[],platform:r}=n,l=s.filter(Boolean),c=await(r.isRTL==null?void 0:r.isRTL(e));let f=await r.getElementRects({reference:t,floating:e,strategy:i}),{x:m,y:d}=Ft(f,o,c),p=o,u={},g=0;for(let y=0;y<l.length;y++){const{name:h,fn:b}=l[y],{x:w,y:E,data:A,reset:v}=await b({x:m,y:d,initialPlacement:o,placement:p,strategy:i,middlewareData:u,rects:f,platform:r,elements:{reference:t,floating:e}});m=w??m,d=E??d,u={...u,[h]:{...u[h],...A}},v&&g<=50&&(g++,typeof v=="object"&&(v.placement&&(p=v.placement),v.rects&&(f=v.rects===!0?await r.getElementRects({reference:t,floating:e,strategy:i}):v.rects),{x:m,y:d}=Ft(f,p,c)),y=-1)}return{x:m,y:d,placement:p,strategy:i,middlewareData:u}};async function Gt(t,e){var n;e===void 0&&(e={});const{x:o,y:i,platform:s,rects:r,elements:l,strategy:c}=t,{boundary:f="clippingAncestors",rootBoundary:m="viewport",elementContext:d="floating",altBoundary:p=!1,padding:u=0}=st(e,t),g=Kt(u),h=l[p?d==="floating"?"reference":"floating":d],b=pt(await s.getClippingRect({element:(n=await(s.isElement==null?void 0:s.isElement(h)))==null||n?h:h.contextElement||await(s.getDocumentElement==null?void 0:s.getDocumentElement(l.floating)),boundary:f,rootBoundary:m,strategy:c})),w=d==="floating"?{x:o,y:i,width:r.floating.width,height:r.floating.height}:r.reference,E=await(s.getOffsetParent==null?void 0:s.getOffsetParent(l.floating)),A=await(s.isElement==null?void 0:s.isElement(E))?await(s.getScale==null?void 0:s.getScale(E))||{x:1,y:1}:{x:1,y:1},v=pt(s.convertOffsetParentRelativeRectToViewportRelativeRect?await s.convertOffsetParentRelativeRectToViewportRelativeRect({elements:l,rect:w,offsetParent:E,strategy:c}):w);return{top:(b.top-v.top+g.top)/A.y,bottom:(v.bottom-b.bottom+g.bottom)/A.y,left:(b.left-v.left+g.left)/A.x,right:(v.right-b.right+g.right)/A.x}}const We=t=>({name:"arrow",options:t,async fn(e){const{x:n,y:o,placement:i,rects:s,platform:r,elements:l,middlewareData:c}=e,{element:f,padding:m=0}=st(t,e)||{};if(f==null)return{};const d=Kt(m),p={x:n,y:o},u=Ct(i),g=Ot(u),y=await r.getDimensions(f),h=u==="y",b=h?"top":"left",w=h?"bottom":"right",E=h?"clientHeight":"clientWidth",A=s.reference[g]+s.reference[u]-p[u]-s.floating[g],v=p[u]-s.reference[u],x=await(r.getOffsetParent==null?void 0:r.getOffsetParent(f));let R=x?x[E]:0;(!R||!await(r.isElement==null?void 0:r.isElement(x)))&&(R=l.floating[E]||s.floating[g]);const O=A/2-v/2,P=R/2-y[g]/2-1,_=tt(d[b],P),I=tt(d[w],P),M=_,V=R-y[g]-I,L=R/2-y[g]/2+O,j=Et(M,L,V),T=!c.arrow&&lt(i)!=null&&L!==j&&s.reference[g]/2-(L<M?_:I)-y[g]/2<0,C=T?L<M?L-M:L-V:0;return{[u]:p[u]+C,data:{[u]:j,centerOffset:L-j-C,...T&&{alignmentOffset:C}},reset:T}}}),He=function(t){return t===void 0&&(t={}),{name:"flip",options:t,async fn(e){var n,o;const{placement:i,middlewareData:s,rects:r,initialPlacement:l,platform:c,elements:f}=e,{mainAxis:m=!0,crossAxis:d=!0,fallbackPlacements:p,fallbackStrategy:u="bestFit",fallbackAxisSideDirection:g="none",flipAlignment:y=!0,...h}=st(t,e);if((n=s.arrow)!=null&&n.alignmentOffset)return{};const b=G(i),w=et(l),E=G(l)===l,A=await(c.isRTL==null?void 0:c.isRTL(f.floating)),v=p||(E||!y?[ht(l)]:Fe(l)),x=g!=="none";!p&&x&&v.push(...Ne(l,y,g,A));const R=[l,...v],O=await Gt(e,h),P=[];let _=((o=s.flip)==null?void 0:o.overflows)||[];if(m&&P.push(O[b]),d){const L=De(i,r,A);P.push(O[L[0]],O[L[1]])}if(_=[..._,{placement:i,overflows:P}],!P.every(L=>L<=0)){var I,M;const L=(((I=s.flip)==null?void 0:I.index)||0)+1,j=R[L];if(j)return{data:{index:L,overflows:_},reset:{placement:j}};let T=(M=_.filter(C=>C.overflows[0]<=0).sort((C,k)=>C.overflows[1]-k.overflows[1])[0])==null?void 0:M.placement;if(!T)switch(u){case"bestFit":{var V;const C=(V=_.filter(k=>{if(x){const W=et(k.placement);return W===w||W==="y"}return!0}).map(k=>[k.placement,k.overflows.filter(W=>W>0).reduce((W,ft)=>W+ft,0)]).sort((k,W)=>k[1]-W[1])[0])==null?void 0:V[0];C&&(T=C);break}case"initialPlacement":T=l;break}if(i!==T)return{reset:{placement:T}}}return{}}}};async function Ie(t,e){const{placement:n,platform:o,elements:i}=t,s=await(o.isRTL==null?void 0:o.isRTL(i.floating)),r=G(n),l=lt(n),c=et(n)==="y",f=["left","top"].includes(r)?-1:1,m=s&&c?-1:1,d=st(e,t);let{mainAxis:p,crossAxis:u,alignmentAxis:g}=typeof d=="number"?{mainAxis:d,crossAxis:0,alignmentAxis:null}:{mainAxis:0,crossAxis:0,alignmentAxis:null,...d};return l&&typeof g=="number"&&(u=l==="end"?g*-1:g),c?{x:u*m,y:p*f}:{x:p*f,y:u*m}}const ze=function(t){return t===void 0&&(t=0),{name:"offset",options:t,async fn(e){var n,o;const{x:i,y:s,placement:r,middlewareData:l}=e,c=await Ie(e,t);return r===((n=l.offset)==null?void 0:n.placement)&&(o=l.arrow)!=null&&o.alignmentOffset?{}:{x:i+c.x,y:s+c.y,data:{...c,placement:r}}}}},je=function(t){return t===void 0&&(t={}),{name:"shift",options:t,async fn(e){const{x:n,y:o,placement:i}=e,{mainAxis:s=!0,crossAxis:r=!1,limiter:l={fn:h=>{let{x:b,y:w}=h;return{x:b,y:w}}},...c}=st(t,e),f={x:n,y:o},m=await Gt(e,c),d=et(G(i)),p=Jt(d);let u=f[p],g=f[d];if(s){const h=p==="y"?"top":"left",b=p==="y"?"bottom":"right",w=u+m[h],E=u-m[b];u=Et(w,u,E)}if(r){const h=d==="y"?"top":"left",b=d==="y"?"bottom":"right",w=g+m[h],E=g-m[b];g=Et(w,g,E)}const y=l.fn({...e,[p]:u,[d]:g});return{...y,data:{x:y.x-n,y:y.y-o}}}}};function ot(t){return Qt(t)?(t.nodeName||"").toLowerCase():"#document"}function D(t){var e;return(t==null||(e=t.ownerDocument)==null?void 0:e.defaultView)||window}function z(t){var e;return(e=(Qt(t)?t.ownerDocument:t.document)||window.document)==null?void 0:e.documentElement}function Qt(t){return t instanceof Node||t instanceof D(t).Node}function B(t){return t instanceof Element||t instanceof D(t).Element}function H(t){return t instanceof HTMLElement||t instanceof D(t).HTMLElement}function Bt(t){return typeof ShadowRoot>"u"?!1:t instanceof ShadowRoot||t instanceof D(t).ShadowRoot}function ct(t){const{overflow:e,overflowX:n,overflowY:o,display:i}=N(t);return/auto|scroll|overlay|hidden|clip/.test(e+o+n)&&!["inline","contents"].includes(i)}function qe(t){return["table","td","th"].includes(ot(t))}function yt(t){return[":popover-open",":modal"].some(e=>{try{return t.matches(e)}catch{return!1}})}function _t(t){const e=Rt(),n=B(t)?N(t):t;return n.transform!=="none"||n.perspective!=="none"||(n.containerType?n.containerType!=="normal":!1)||!e&&(n.backdropFilter?n.backdropFilter!=="none":!1)||!e&&(n.filter?n.filter!=="none":!1)||["transform","perspective","filter"].some(o=>(n.willChange||"").includes(o))||["paint","layout","strict","content"].some(o=>(n.contain||"").includes(o))}function Xe(t){let e=U(t);for(;H(e)&&!nt(e);){if(_t(e))return e;if(yt(e))return null;e=U(e)}return null}function Rt(){return typeof CSS>"u"||!CSS.supports?!1:CSS.supports("-webkit-backdrop-filter","none")}function nt(t){return["html","body","#document"].includes(ot(t))}function N(t){return D(t).getComputedStyle(t)}function bt(t){return B(t)?{scrollLeft:t.scrollLeft,scrollTop:t.scrollTop}:{scrollLeft:t.scrollX,scrollTop:t.scrollY}}function U(t){if(ot(t)==="html")return t;const e=t.assignedSlot||t.parentNode||Bt(t)&&t.host||z(t);return Bt(e)?e.host:e}function Zt(t){const e=U(t);return nt(e)?t.ownerDocument?t.ownerDocument.body:t.body:H(e)&&ct(e)?e:Zt(e)}function rt(t,e,n){var o;e===void 0&&(e=[]),n===void 0&&(n=!0);const i=Zt(t),s=i===((o=t.ownerDocument)==null?void 0:o.body),r=D(i);return s?e.concat(r,r.visualViewport||[],ct(i)?i:[],r.frameElement&&n?rt(r.frameElement):[]):e.concat(i,rt(i,[],n))}function $t(t){const e=N(t);let n=parseFloat(e.width)||0,o=parseFloat(e.height)||0;const i=H(t),s=i?t.offsetWidth:n,r=i?t.offsetHeight:o,l=gt(n)!==s||gt(o)!==r;return l&&(n=s,o=r),{width:n,height:o,$:l}}function Lt(t){return B(t)?t:t.contextElement}function Z(t){const e=Lt(t);if(!H(e))return Y(1);const n=e.getBoundingClientRect(),{width:o,height:i,$:s}=$t(e);let r=(s?gt(n.width):n.width)/o,l=(s?gt(n.height):n.height)/i;return(!r||!Number.isFinite(r))&&(r=1),(!l||!Number.isFinite(l))&&(l=1),{x:r,y:l}}const Ye=Y(0);function te(t){const e=D(t);return!Rt()||!e.visualViewport?Ye:{x:e.visualViewport.offsetLeft,y:e.visualViewport.offsetTop}}function Ue(t,e,n){return e===void 0&&(e=!1),!n||e&&n!==D(t)?!1:e}function Q(t,e,n,o){e===void 0&&(e=!1),n===void 0&&(n=!1);const i=t.getBoundingClientRect(),s=Lt(t);let r=Y(1);e&&(o?B(o)&&(r=Z(o)):r=Z(t));const l=Ue(s,n,o)?te(s):Y(0);let c=(i.left+l.x)/r.x,f=(i.top+l.y)/r.y,m=i.width/r.x,d=i.height/r.y;if(s){const p=D(s),u=o&&B(o)?D(o):o;let g=p,y=g.frameElement;for(;y&&o&&u!==g;){const h=Z(y),b=y.getBoundingClientRect(),w=N(y),E=b.left+(y.clientLeft+parseFloat(w.paddingLeft))*h.x,A=b.top+(y.clientTop+parseFloat(w.paddingTop))*h.y;c*=h.x,f*=h.y,m*=h.x,d*=h.y,c+=E,f+=A,g=D(y),y=g.frameElement}}return pt({width:m,height:d,x:c,y:f})}function Je(t){let{elements:e,rect:n,offsetParent:o,strategy:i}=t;const s=i==="fixed",r=z(o),l=e?yt(e.floating):!1;if(o===r||l&&s)return n;let c={scrollLeft:0,scrollTop:0},f=Y(1);const m=Y(0),d=H(o);if((d||!d&&!s)&&((ot(o)!=="body"||ct(r))&&(c=bt(o)),H(o))){const p=Q(o);f=Z(o),m.x=p.x+o.clientLeft,m.y=p.y+o.clientTop}return{width:n.width*f.x,height:n.height*f.y,x:n.x*f.x-c.scrollLeft*f.x+m.x,y:n.y*f.y-c.scrollTop*f.y+m.y}}function Ke(t){return Array.from(t.getClientRects())}function ee(t){return Q(z(t)).left+bt(t).scrollLeft}function Ge(t){const e=z(t),n=bt(t),o=t.ownerDocument.body,i=K(e.scrollWidth,e.clientWidth,o.scrollWidth,o.clientWidth),s=K(e.scrollHeight,e.clientHeight,o.scrollHeight,o.clientHeight);let r=-n.scrollLeft+ee(t);const l=-n.scrollTop;return N(o).direction==="rtl"&&(r+=K(e.clientWidth,o.clientWidth)-i),{width:i,height:s,x:r,y:l}}function Qe(t,e){const n=D(t),o=z(t),i=n.visualViewport;let s=o.clientWidth,r=o.clientHeight,l=0,c=0;if(i){s=i.width,r=i.height;const f=Rt();(!f||f&&e==="fixed")&&(l=i.offsetLeft,c=i.offsetTop)}return{width:s,height:r,x:l,y:c}}function Ze(t,e){const n=Q(t,!0,e==="fixed"),o=n.top+t.clientTop,i=n.left+t.clientLeft,s=H(t)?Z(t):Y(1),r=t.clientWidth*s.x,l=t.clientHeight*s.y,c=i*s.x,f=o*s.y;return{width:r,height:l,x:c,y:f}}function Nt(t,e,n){let o;if(e==="viewport")o=Qe(t,n);else if(e==="document")o=Ge(z(t));else if(B(e))o=Ze(e,n);else{const i=te(t);o={...e,x:e.x-i.x,y:e.y-i.y}}return pt(o)}function ne(t,e){const n=U(t);return n===e||!B(n)||nt(n)?!1:N(n).position==="fixed"||ne(n,e)}function $e(t,e){const n=e.get(t);if(n)return n;let o=rt(t,[],!1).filter(l=>B(l)&&ot(l)!=="body"),i=null;const s=N(t).position==="fixed";let r=s?U(t):t;for(;B(r)&&!nt(r);){const l=N(r),c=_t(r);!c&&l.position==="fixed"&&(i=null),(s?!c&&!i:!c&&l.position==="static"&&!!i&&["absolute","fixed"].includes(i.position)||ct(r)&&!c&&ne(t,r))?o=o.filter(m=>m!==r):i=l,r=U(r)}return e.set(t,o),o}function tn(t){let{element:e,boundary:n,rootBoundary:o,strategy:i}=t;const r=[...n==="clippingAncestors"?yt(e)?[]:$e(e,this._c):[].concat(n),o],l=r[0],c=r.reduce((f,m)=>{const d=Nt(e,m,i);return f.top=K(d.top,f.top),f.right=tt(d.right,f.right),f.bottom=tt(d.bottom,f.bottom),f.left=K(d.left,f.left),f},Nt(e,l,i));return{width:c.right-c.left,height:c.bottom-c.top,x:c.left,y:c.top}}function en(t){const{width:e,height:n}=$t(t);return{width:e,height:n}}function nn(t,e,n){const o=H(e),i=z(e),s=n==="fixed",r=Q(t,!0,s,e);let l={scrollLeft:0,scrollTop:0};const c=Y(0);if(o||!o&&!s)if((ot(e)!=="body"||ct(i))&&(l=bt(e)),o){const d=Q(e,!0,s,e);c.x=d.x+e.clientLeft,c.y=d.y+e.clientTop}else i&&(c.x=ee(i));const f=r.left+l.scrollLeft-c.x,m=r.top+l.scrollTop-c.y;return{x:f,y:m,width:r.width,height:r.height}}function vt(t){return N(t).position==="static"}function Mt(t,e){return!H(t)||N(t).position==="fixed"?null:e?e(t):t.offsetParent}function oe(t,e){const n=D(t);if(yt(t))return n;if(!H(t)){let i=U(t);for(;i&&!nt(i);){if(B(i)&&!vt(i))return i;i=U(i)}return n}let o=Mt(t,e);for(;o&&qe(o)&&vt(o);)o=Mt(o,e);return o&&nt(o)&&vt(o)&&!_t(o)?n:o||Xe(t)||n}const on=async function(t){const e=this.getOffsetParent||oe,n=this.getDimensions,o=await n(t.floating);return{reference:nn(t.reference,await e(t.floating),t.strategy),floating:{x:0,y:0,width:o.width,height:o.height}}};function rn(t){return N(t).direction==="rtl"}const sn={convertOffsetParentRelativeRectToViewportRelativeRect:Je,getDocumentElement:z,getClippingRect:tn,getOffsetParent:oe,getElementRects:on,getClientRects:Ke,getDimensions:en,getScale:Z,isElement:B,isRTL:rn};function ln(t,e){let n=null,o;const i=z(t);function s(){var l;clearTimeout(o),(l=n)==null||l.disconnect(),n=null}function r(l,c){l===void 0&&(l=!1),c===void 0&&(c=1),s();const{left:f,top:m,width:d,height:p}=t.getBoundingClientRect();if(l||e(),!d||!p)return;const u=ut(m),g=ut(i.clientWidth-(f+d)),y=ut(i.clientHeight-(m+p)),h=ut(f),w={rootMargin:-u+"px "+-g+"px "+-y+"px "+-h+"px",threshold:K(0,tt(1,c))||1};let E=!0;function A(v){const x=v[0].intersectionRatio;if(x!==c){if(!E)return r();x?r(!1,x):o=setTimeout(()=>{r(!1,1e-7)},1e3)}E=!1}try{n=new IntersectionObserver(A,{...w,root:i.ownerDocument})}catch{n=new IntersectionObserver(A,w)}n.observe(t)}return r(!0),s}function Vt(t,e,n,o){o===void 0&&(o={});const{ancestorScroll:i=!0,ancestorResize:s=!0,elementResize:r=typeof ResizeObserver=="function",layoutShift:l=typeof IntersectionObserver=="function",animationFrame:c=!1}=o,f=Lt(t),m=i||s?[...f?rt(f):[],...rt(e)]:[];m.forEach(b=>{i&&b.addEventListener("scroll",n,{passive:!0}),s&&b.addEventListener("resize",n)});const d=f&&l?ln(f,n):null;let p=-1,u=null;r&&(u=new ResizeObserver(b=>{let[w]=b;w&&w.target===f&&u&&(u.unobserve(e),cancelAnimationFrame(p),p=requestAnimationFrame(()=>{var E;(E=u)==null||E.observe(e)})),n()}),f&&!c&&u.observe(f),u.observe(e));let g,y=c?Q(t):null;c&&h();function h(){const b=Q(t);y&&(b.x!==y.x||b.y!==y.y||b.width!==y.width||b.height!==y.height)&&n(),y=b,g=requestAnimationFrame(h)}return n(),()=>{var b;m.forEach(w=>{i&&w.removeEventListener("scroll",n),s&&w.removeEventListener("resize",n)}),d==null||d(),(b=u)==null||b.disconnect(),u=null,c&&cancelAnimationFrame(g)}}const cn=ze,fn=je,an=He,un=We,dn=(t,e,n)=>{const o=new Map,i={platform:sn,...n},s={...i.platform,_c:o};return Ve(t,e,{...i,platform:s})};function Wt(t){let e;return{c(){e=qt("div")},l(n){e=Xt(n,"DIV",{}),Yt(e).forEach(X)},m(n,o){$(n,e,o),t[23](e)},p:ue,d(n){n&&X(e),t[23](null)}}}function Ht(t){let e,n,o;const i=[{use:t[9]},{options:t[3]},{role:"tooltip"},{tabindex:t[1]?-1:void 0},t[11]];function s(l){t[24](l)}let r={$$slots:{default:[mn]},$$scope:{ctx:t}};for(let l=0;l<i.length;l+=1)r=xt(r,i[l]);return t[0]!==void 0&&(r.open=t[0]),e=new Te({props:r}),Ut.push(()=>Ee(e,"open",s)),e.$on("focusin",function(){at(q(t[1],t[7]))&&q(t[1],t[7]).apply(this,arguments)}),e.$on("focusout",function(){at(q(t[1],t[8]))&&q(t[1],t[8]).apply(this,arguments)}),e.$on("mouseenter",function(){at(q(t[1]&&t[4],t[7]))&&q(t[1]&&t[4],t[7]).apply(this,arguments)}),e.$on("mouseleave",function(){at(q(t[1]&&t[4],t[8]))&&q(t[1]&&t[4],t[8]).apply(this,arguments)}),{c(){Ae(e.$$.fragment)},l(l){Oe(e.$$.fragment,l)},m(l,c){Ce(e,l,c),o=!0},p(l,c){t=l;const f=c[0]&2570?Le(i,[c[0]&512&&{use:t[9]},c[0]&8&&{options:t[3]},i[2],c[0]&2&&{tabindex:t[1]?-1:void 0},c[0]&2048&&ke(t[11])]):{};c[0]&33554500&&(f.$$scope={dirty:c,ctx:t}),!n&&c[0]&1&&(n=!0,f.open=t[0],de(()=>n=!1)),e.$set(f)},i(l){o||(it(e.$$.fragment,l),o=!0)},o(l){mt(e.$$.fragment,l),o=!1},d(l){_e(e,l)}}}function It(t){let e,n,o;return{c(){e=qt("div"),this.h()},l(i){e=Xt(i,"DIV",{class:!0}),Yt(e).forEach(X),this.h()},h(){Dt(e,"class",t[6])},m(i,s){$(i,e,s),n||(o=ye(t[10].call(null,e)),n=!0)},p(i,s){s[0]&64&&Dt(e,"class",i[6])},d(i){i&&X(e),n=!1,o()}}}function mn(t){let e,n,o;const i=t[22].default,s=me(i,t,t[25],null);let r=t[2]&&It(t);return{c(){s&&s.c(),e=zt(),r&&r.c(),n=dt()},l(l){s&&s.l(l),e=jt(l),r&&r.l(l),n=dt()},m(l,c){s&&s.m(l,c),$(l,e,c),r&&r.m(l,c),$(l,n,c),o=!0},p(l,c){s&&s.p&&(!o||c[0]&33554432)&&ge(s,i,l,l[25],o?pe(i,l[25],c,null):he(l[25]),null),l[2]?r?r.p(l,c):(r=It(l),r.c(),r.m(n.parentNode,n)):r&&(r.d(1),r=null)},i(l){o||(it(s,l),o=!0)},o(l){mt(s,l),o=!1},d(l){l&&(X(e),X(n)),s&&s.d(l),r&&r.d(l)}}}function gn(t){let e,n,o,i=!t[3]&&Wt(t),s=t[3]&&Ht(t);return{c(){i&&i.c(),e=zt(),s&&s.c(),n=dt()},l(r){i&&i.l(r),e=jt(r),s&&s.l(r),n=dt()},m(r,l){i&&i.m(r,l),$(r,e,l),s&&s.m(r,l),$(r,n,l),o=!0},p(r,l){r[3]?i&&(i.d(1),i=null):i?i.p(r,l):(i=Wt(r),i.c(),i.m(e.parentNode,e)),r[3]?s?(s.p(r,l),l[0]&8&&it(s,1)):(s=Ht(r),s.c(),it(s,1),s.m(n.parentNode,n)):s&&(ve(),mt(s,1,1,()=>{s=null}),xe())},i(r){o||(it(s),o=!0)},o(r){mt(s),o=!1},d(r){r&&(X(e),X(n)),i&&i.d(r),s&&s.d(r)}}}function q(t,e){return t?e:()=>{}}function hn(t,e,n){let o;const i=["activeContent","arrow","offset","placement","trigger","triggeredBy","reference","strategy","open","yOnly","middlewares"];let s=St(e,i),{$$slots:r={},$$scope:l}=e,{activeContent:c=!1}=e,{arrow:f=!0}=e,{offset:m=8}=e,{placement:d="top"}=e,{trigger:p="hover"}=e,{triggeredBy:u=void 0}=e,{reference:g=void 0}=e,{strategy:y="absolute"}=e,{open:h=!1}=e,{yOnly:b=!1}=e,{middlewares:w=[an(),fn()]}=e;const E=fe();let A,v,x,R,O,P,_=[],I=!1;const M=()=>(I=!0,setTimeout(()=>I=!1,250)),V=a=>{x===void 0&&console.error("trigger undefined"),!g&&_.includes(a.target)&&x!==a.target&&(n(3,x=a.target),M()),A&&a.type==="focusin"&&!h&&M(),n(0,h=A&&a.type==="click"&&!I?!h:!0)},L=a=>a.matches(":hover"),j=a=>a.contains(document.activeElement),T=a=>a!=null?`${a}px`:"",C=a=>{c?setTimeout(()=>{const S=[x,R,..._].filter(Boolean);a.type==="mouseleave"&&S.some(L)||a.type==="focusout"&&S.some(j)||n(0,h=!1)},100):n(0,h=!1)};let k;const W={left:"right",right:"left",bottom:"top",top:"bottom"};function ft(){dn(x,R,{placement:d,strategy:y,middleware:o}).then(({x:a,y:S,middlewareData:F,placement:J,strategy:wt})=>{R.style.position=wt,R.style.left=b?"0":T(a),R.style.top=T(S),F.arrow&&O instanceof HTMLDivElement&&(n(20,O.style.left=T(F.arrow.x),O),n(20,O.style.top=T(F.arrow.y),O),n(21,k=W[J.split("-")[0]]),n(20,O.style[k]=T(-O.offsetWidth/2-(e.border?1:0)),O))})}function ie(a,S){R=a;let F=Vt(S,R,ft);return{update(J){F(),F=Vt(J,R,ft)},destroy(){F()}}}ae(()=>{const a=[["focusin",V,!0],["focusout",C,!0],["click",V,A],["mouseenter",V,v],["mouseleave",C,v]];return u?_=[...document.querySelectorAll(u)]:_=P.previousElementSibling?[P.previousElementSibling]:[],_.length||console.error("No triggers found."),_.forEach(S=>{S.tabIndex<0&&(S.tabIndex=0);for(const[F,J,wt]of a)wt&&S.addEventListener(F,J)}),g?(n(3,x=document.querySelector(g)??document.body),x===document.body?console.error(`Popup reference not found: '${g}'`):(x.addEventListener("focusout",C),v&&x.addEventListener("mouseleave",C))):n(3,x=_[0]),document.addEventListener("click",kt),()=>{_.forEach(S=>{if(S)for(const[F,J]of a)S.removeEventListener(F,J)}),x&&(x.removeEventListener("focusout",C),x.removeEventListener("mouseleave",C)),document.removeEventListener("click",kt)}});function kt(a){h&&!a.composedPath().includes(R)&&!_.some(S=>a.composedPath().includes(S))&&C(a)}let Tt;function re(a){return n(20,O=a),{destroy(){n(20,O=null)}}}function se(a){Ut[a?"unshift":"push"](()=>{P=a,n(5,P)})}function le(a){h=a,n(0,h)}return t.$$set=a=>{n(39,e=xt(xt({},e),Pt(a))),n(11,s=St(e,i)),"activeContent"in a&&n(1,c=a.activeContent),"arrow"in a&&n(2,f=a.arrow),"offset"in a&&n(12,m=a.offset),"placement"in a&&n(13,d=a.placement),"trigger"in a&&n(14,p=a.trigger),"triggeredBy"in a&&n(15,u=a.triggeredBy),"reference"in a&&n(16,g=a.reference),"strategy"in a&&n(17,y=a.strategy),"open"in a&&n(0,h=a.open),"yOnly"in a&&n(18,b=a.yOnly),"middlewares"in a&&n(19,w=a.middlewares),"$$scope"in a&&n(25,l=a.$$scope)},t.$$.update=()=>{t.$$.dirty[0]&16384&&(A=p==="click"),t.$$.dirty[0]&16384&&n(4,v=p==="hover"),t.$$.dirty[0]&1&&E("show",h),t.$$.dirty[0]&8200&&d&&(n(3,x),n(13,d)),t.$$.dirty[0]&1576960&&(o=[...w,cn(+m),O&&un({element:O,padding:10})]),n(6,Tt=Re("absolute pointer-events-none block w-[10px] h-[10px] rotate-45 bg-inherit border-inherit",e.border&&k==="bottom"&&"border-b border-e",e.border&&k==="top"&&"border-t border-s ",e.border&&k==="right"&&"border-t border-e ",e.border&&k==="left"&&"border-b border-s "))},e=Pt(e),[h,c,f,x,v,P,Tt,V,C,ie,re,s,m,d,p,u,g,y,b,w,O,k,r,se,le,l]}class vn extends be{constructor(e){super(),we(this,e,hn,gn,ce,{activeContent:1,arrow:2,offset:12,placement:13,trigger:14,triggeredBy:15,reference:16,strategy:17,open:0,yOnly:18,middlewares:19},null,[-1,-1])}}export{vn as P};
