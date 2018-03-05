<template>
<!-- 联系我们 -->
    <div class="Contact">
        <h2>Our Location</h2>
        <div style="width:100%;height:150px;border:1px solid #E5E5E5;">
            <img src="static/images/wenzi.png" alt="">
            <h3 style="margin:20px 0 10px 0;">Return address</h3>
            <p style="float:left;width:250px;">Yima Building the 2nd floor, Geliantong Street, Fengze zone, Quanzhou, Fujian P.R.China</p>
        </div>
        <h2 style="margin:20px 0 0 0;border-bottom:1px solid #E5E5E5;">Contact Us</h2>
        <label for="">Your Name
            <input type="text">
        </label>
        <label style="margin:20px 0 0 26px;" for="">E-Mail Address
            <input type="text">
        </label>
        <label style="margin:20px 0 0 73px;" for="">Enquiry
            <input style="padding-bottom:200px;" type="text">
        </label>
        <button>Submit</button>
    </div>
</template>

<script>
export default {

}
</script>

<style>
.Contact {
    padding: 10px 20px 0 20px
}
.Contact h2 {
    font-size: 18px;
    color: #e60211;
    height: 30px;
}
.Contact img {
    float: left;
    padding: 10px 60px 10px 60px;
    margin:20px 20px 0 30px;
    border: 1px solid #E5E5E5;
    border-radius: 5%;
}
.Contact label {
    float:left;
    margin:20px 0 0 50px;
}
.Contact input {
    width: 729px;
    height: 30px;
}
.Contact button {
    float: right;
    width: 68px;
    height: 30px;
    border: 0;
    color: white;
    outline: none;
    background: #d0205e;
    margin: 20px 0 50px 0;
}
</style>
