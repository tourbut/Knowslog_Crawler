import{w as r}from"./index.xhc7QMiD.js";const i="Knowslog",c="",A=`${c}/api/v1`,s=(t,n)=>{const o=sessionStorage.getItem(t),e=r(o!=null?JSON.parse(o):n);return e.subscribe(a=>{sessionStorage.setItem(t,JSON.stringify(a))}),e},u=s("APP_NAME",i),m=s("user_token",""),S=s("username",""),g=s("is_admin",""),P=s("toasts",[]);export{u as A,m as a,A as b,g as i,P as t,S as u};