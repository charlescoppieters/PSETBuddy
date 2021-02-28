function getCookie(c_name) {
   var i,x,y,ARRcookies=document.cookie.split(";");
   for (i=0;i<ARRcookies.length;i++){
      x=ARRcookies[i].substr(0,ARRcookies[i].indexOf("="));
      y=ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
      x=x.replace(/^\s+|\s+$/g,"");
      if (x==c_name) {
        return unescape(y);
      }
   }
}
function setCookie(c_name,value,exdays) {
   var exdate=new Date();
   exdate.setDate(exdate.getDate() + exdays);
   var c_value=escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
   document.cookie=c_name + "=" + c_value;
}

function checkForm(form) {
   var search = form.children[1].value;
   var state = form.children[3].value;
   if (search == "" & state == "") {
      alert("Please fill out the search bar") 
      return false;
   }
   if (search == "ELON MUSK" || state == "ELON MUSK") {
      alert("He is not here"); 
      return false;
   }
   return true;
}
function splash() {
   console.log(getCookie('exist')==null);
   if (getCookie('exist')==null){
      setCookie('exist', 1, 1);
      if (window.location.href != "http://127.0.0.1:8000/" & getCookie('exist')!=null) {
         window.location.href = "http://127.0.0.1:8000/";
      }
   }
}