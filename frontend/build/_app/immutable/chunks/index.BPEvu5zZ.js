import{w as a}from"./index.-PiOOl_e.js";const c="Knowslog Crawler",A="",u=`${A}/api/v1`,s=(t,r)=>{const e=sessionStorage.getItem(t),o=a(e!=null?JSON.parse(e):r);return o.subscribe(n=>{sessionStorage.setItem(t,JSON.stringify(n))}),o},_=s("APP_NAME",c),S=s("user_token",""),g=s("username","");export{_ as A,S as a,u as b,g as u};
