<template>
  <div class="fo-content-wrap">
    <div class="fo-header">
      My Following
      <span class="fo-header-sp">(2 ITEM)</span>
    </div>


    <div class="fo-content-ul">
    <ul class="fa-ul">
      <li class="fa-li" v-for="(list,index) in designers" :key="index">
        <div class="fo-main-title">
          <span style="font-size:14px;color:#0F0F0F">{{list.name}}</span>
          <span style="font-size:12px;margin-left:30px;display:inline-block"> 
            <button class="myfollowbtn"  @click="changeFollow(index)" style="width:86px;height:18px;">{{isfollow.indexOf(index) > -1 ? follow:un}}</button></span>
          <span style="display:inline-block;float:right;font-size:12px;color:#E54C87;margin-right:3px;"><router-link to="/Designers/detail">MORE</router-link></span>
        </div>
        <div class="fo-imgDiv" style="height:150px;margin-top:20px;margin-left:-2px">
          <ul>
            <li style="float:left;height:150px;width:120px;;margin-left:3px;" v-for="(item,index) in list.img" :key="index">
              <a>
                <img :src="item" style="height:100%;width:100%;">
              </a>
            </li>
          </ul>
        </div>
      </li>
    </ul>
    </div>

  </div>
</template>

<script>
export default {
  name: 'following',
  data () {
    return {
      follow: 'FOLLOW',
      un: 'UNFOLLOW',
      isfollow: [],
      designers: [
        {
          name: 'Abbott Vintage',
          img: ['https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1254008598,1273551066&fm=27&gp=0.jpg','','','','','','']
        },
        {
          name: 'Abbott Vintage',
          img: ['https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1254008598,1273551066&fm=27&gp=0.jpg','','','','','','']
        },
        {
          name: 'Abbott Vintage',
          img: ['https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1254008598,1273551066&fm=27&gp=0.jpg','','','','','','']
        },
        {
          name: 'Abbott Vintage',
          img: ['https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1254008598,1273551066&fm=27&gp=0.jpg','','','','','','']
        },
        {
          name: 'Abbott Vintage',
          img: ['https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1254008598,1273551066&fm=27&gp=0.jpg','','','','','','']
        },
        {
          name: 'Abbott Vintage',
          img: ['https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1254008598,1273551066&fm=27&gp=0.jpg','','','','','','']
        },
        {
          name: 'Abbott Vintage',
          img: ['https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1254008598,1273551066&fm=27&gp=0.jpg','','','','','','']
        },
      ]
    }
  },
  methods: {
    changeFollow: function (index) {
      this.$confirm('是否取消关注', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
           if(this.isfollow.indexOf(index)<0) {
        this.isfollow.push(index)
      } else {
        this.isfollow.splice(this.isfollow.indexOf(index),1)
      }
          this.$message({
            type: 'success',
            message: '取消成功!'
          });
        }).catch(() => {
          return      
        });
    }
  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
.fo-content-wrap {
  width: 860px;
  position: relative;
}
.fo-header {
  margin-top: -20px;
  width: 100%;
  border-bottom: 1px solid #b7b7b7;
  font-size: 16px;
  color: #0F0F0F;
  padding-bottom: 5px;
}
.fo-header-sp {
  font-size: 12px;
  color: #595959;
  margin-left: 10px;
}
.fo-content-ul {
  height: 100%;
}
.fa-li {
  margin-top: 20px;
}
.fa-ul a:hover {
  color: #E54C87;
}

.myfollowbtn {
  border: none;
  height: 20px;
  line-height: 2px;
  font-size: 12px;
  color: #fff;
  background-color: #E54C87;
  border-color: #E54C87;
  border-radius: 0;
}
.myfollowbtn:focus {
  background-color: #E54C87;
  border-color: #E54C87;
}
.myfollowbtn:active {
  color: #E54C87;
  background-color: #fff;
  border-color: #E54C87;
}
.fo-content-wrap router-Link {
  color: #E54C87;
}
.el-button {
  padding: 4px 4px;
}

</style>
