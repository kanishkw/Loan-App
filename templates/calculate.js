function check()
{
var prin=document.forms["calculate"]["principal"];
var ten=document.forms["calculate"]["tenure"];
var rat=document.forms["calculate"]["rate"];
var amt=0;
if(prin.value=="")
{
window.alert("Please enter Principal Amount.");
prin.focus();
return false;
}
if(ten.value=="")
{
window.alert("Please enter Tenure.");
ten.focus();
return false;
}
if(rat.value=="")
{
window.alert("Please enter Rate of Interest %");
rat.focus();
return false;
}
ten=ten*12;
amt=prin*rat*((1+rat)*ten)/((1+rat)*(ten-1));
console.log(amt);
return amt;
}
