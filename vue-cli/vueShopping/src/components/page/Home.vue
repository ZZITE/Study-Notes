<template>
  <div class="Home">
    　　<input id="files" type="file" @change="previewImage(this, 'prvid')" multiple="multiple">  

　　<div id="prvid">预览容器</div>
  </div>
</template>
<script>
export default {
  data () {
    return {

    }
  },
  methods: {
    previewImage: function (file, prvid) {
      var self = this;
      var tip = "Expect jpg or png or gif!"; // 设定提示信息 
var filters = { 
"jpeg" : "/9j/4", 
"gif" : "R0lGOD", 
"png" : "iVBORw" 
} 
var prvbox = document.getElementById(prvid); 
prvbox.innerHTML = ""; 
if (window.FileReader) { // html5方案 
for (var i=0, f; f = file.files[i]; i++) { 
var fr = new FileReader(); 
fr.onload = function(e) { 
var src = e.target.result; 
if (!self.validateImg(src)) { 
alert(tip) 
} else { 
self.showPrvImg(src); 
} 
} 
fr.readAsDataURL(f); 
} 
} else { // 降级处理

if ( !/\.jpg$|\.png$|\.gif$/i.test(file.value) ) { 
alert(tip); 
} else { 
self.showPrvImg(file.value); 
} 
} 
 },
  validateImg: function (data) {
    console.log(0) 
var pos = data.indexOf(",") + 1; 
for (var e in filters) { 
if (data.indexOf(filters[e]) === pos) { 
return e; 
} 
} 
return null; 
} ,

 showPrvImg: function(src) { 
   console.log(1) 
var img = document.createElement("img"); 
img.src = src; 
prvbox.appendChild(img); 
} 
}
}
</script>

<style scoped>

</style>
