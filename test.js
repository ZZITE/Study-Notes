<label><input name="" type="radio" value="a" />企业 </label> 
<label><input name="" type="radio" value="b" />个人 </label> 

<button onclick="change()">下一步</button>

<div class="a hide">...企业部分</div>
<div class="b hide">...个人部分</div>

//css
.hide {
    display:none;
}

//js
function change () {
    var value = $("input[type='radio']:checked").val();
    if (value === 'a') {
        $('.a').css({
            display: block
        })
    }
    else if (value === 'b') {
        $('.b').css({
            display: block
        })
    }
    else {
        alert('请选择')
    }
}
