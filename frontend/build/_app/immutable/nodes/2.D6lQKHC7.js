import{s as k,e as v,i as h,n as m,d as i,c as y,a as d,t as f,b as p,f as u,g as _,h as b,j as c,k as x}from"../chunks/scheduler.ts2GzjNa.js";import{S as g,i as E}from"../chunks/index.nwS6sPbX.js";import{u as $}from"../chunks/index.5KL7ki8z.js";import{g as w}from"../chunks/entry.CbruRL_e.js";function D(o){let t,r=w("/login")+"",s;return{c(){t=d("div"),s=f(r),this.h()},l(a){t=p(a,"DIV",{class:!0});var e=u(t);s=_(e,r),e.forEach(i),this.h()},h(){b(t,"class","container mx-auto p-4 max-w-md")},m(a,e){h(a,t,e),c(t,s)},p:m,d(a){a&&i(t)}}}function I(o){let t,r,s,a;return{c(){t=d("div"),r=d("h1"),s=f(o[0]),a=f("님 반갑습니다."),this.h()},l(e){t=p(e,"DIV",{class:!0});var n=u(t);r=p(n,"H1",{});var l=u(r);s=_(l,o[0]),a=_(l,"님 반갑습니다."),l.forEach(i),n.forEach(i),this.h()},h(){b(t,"class","container mx-auto p-4 max-w-md")},m(e,n){h(e,t,n),c(t,r),c(r,s),c(r,a)},p(e,n){n&1&&x(s,e[0])},d(e){e&&i(t)}}}function S(o){let t;function r(e,n){return e[0]?I:D}let s=r(o),a=s(o);return{c(){a.c(),t=v()},l(e){a.l(e),t=v()},m(e,n){a.m(e,n),h(e,t,n)},p(e,[n]){s===(s=r(e))&&a?a.p(e,n):(a.d(1),a=s(e),a&&(a.c(),a.m(t.parentNode,t)))},i:m,o:m,d(e){e&&i(t),a.d(e)}}}function V(o,t,r){let s;return y(o,$,a=>r(0,s=a)),[s]}class N extends g{constructor(t){super(),E(this,t,V,S,k,{})}}export{N as component};