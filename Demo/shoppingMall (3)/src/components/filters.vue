<template>
  <div class="filters">

    <el-collapse v-model="activeNames" @change="handleChange">
      <el-collapse-item title="Category" class="filters-tittle" name="1">
        <ul class="filters-content">
          <li v-for="(item,index) in Category" :key="index" @click="CategorySub(index)">
            <a>
              {{item}}
            </a>
          </li>
        </ul>
      </el-collapse-item>


      <el-collapse-item title="Size" name="2">
        <ul class="filters-content">    
          <li class="filter-detail-item" v-for="(item,index) in Size" :key="index">
            <el-checkbox-group v-model="SizecheckList" @change="SizecheckListSub">
              <el-checkbox :label="item"></el-checkbox>
            </el-checkbox-group>
          </li>
        </ul>
      </el-collapse-item>

      
      <el-collapse-item title="Material" name="3">
        <ul class="filters-content">    
          <li class="filter-detail-item2" v-for="(item,index) in Material" :key="index">
            <el-checkbox-group v-model="MtcheckList" @change="MtcheckListSub">
              <el-checkbox :label="item"></el-checkbox>
            </el-checkbox-group>
          </li>
        </ul>
      </el-collapse-item>


      <el-collapse-item title="Style" name="4">
        <ul class="filters-content">    
          <li class="filter-detail-item2" v-for="(item,index) in Style" :key="index">
            <el-checkbox-group v-model="StcheckList" @change="StcheckListSub">
              <el-checkbox :label="item"></el-checkbox>
            </el-checkbox-group>
          </li>
        </ul>
      </el-collapse-item>


      <el-collapse-item title="Designer" name="5">
        <ul class="filters-content">    
          <li class="filter-detail-item2" v-for="(item,index) in Designer" :key="index">
            <el-checkbox-group v-model="DecheckList" @change="DecheckListSub">
              <el-checkbox :label="item"></el-checkbox>
            </el-checkbox-group>
          </li>
        </ul>
      </el-collapse-item>


      <el-collapse-item title="Color" name="6">
        <ul class="filters-content">    
          <li class="filter-detail-item2" v-for="(item,index) in Color" :key="index">
            <el-checkbox-group v-model="ColorcheckList" @change="ColorcheckListSub">
              <el-checkbox :label="item"></el-checkbox>
            </el-checkbox-group>
          </li>
        </ul>
      </el-collapse-item>


      <el-collapse-item title="Sleeve" name="7">
        <ul class="filters-content">    
          <li class="filter-detail-item2" v-for="(item,index) in Sleeve" :key="index">
            <el-checkbox-group v-model="SlcheckList" @change="SlcheckListSub">
              <el-checkbox :label="item"></el-checkbox>
            </el-checkbox-group>
          </li>
        </ul>
      </el-collapse-item>


      <el-collapse-item title="Price" name="8">
        <ul class="filters-content">
          <li v-for="(item,index) in Price" :key="index">
            <a>
              {{item}}
            </a>
          </li>
        </ul>
      </el-collapse-item>


    </el-collapse>
  </div>
</template>
<script>
export default {
  name: 'filters',
  data() {
    return {
      activeNames: ['7','8'],
      SizecheckList: ['XS','S'],
      MtcheckList: [],
      StcheckList: [],
      DecheckList: [],
      ColorcheckList: [],
      SlcheckList: [],
      Category: ['Blouses','Tunics','Tops','Tees','Tanks + Camis','Hoodies + Sweatshirts','Floral','Off The Shoulder','Statement Sleeves'],
      Size: ['XS','S','M','L','XL','XXL','3XL','4XL','5XL','One-size'],
      Material: ['Acrylic','Chiffon','Cotton','Cotton-blen','Denim','Lace','Linen','Lyocell','Mesh','Nylon','Polyester','Rayon','Silk','Spandex','Tencel','Viscose','Wool','Woven'],
      Style: ['Casual','Simple','Work','work','Boho','Girly','Statement','Cute','Elegant','Sweet','casual'],
      Designer: ['AMII','AMII REDEFINE','Adelin Fostayn','Berenis','Bo Carter','Eden Society','Hoyugo','JANE STORY','SONG and ...Way','JUNGLE ME','Laura Bettini'],
      Color: ['White','Black','Blue','Multicolor','Red','Pink','Green','Yellow','Neutral','Orange','Gray','Brown','Purple'],
      Sleeve: ['3/4 sleeve','Balloon Sleeve','Batwing','Bell Sleeve','Cold Shoulder','Frill Sleeve','Half sleeve','Long sleeve','Short sleeve','Single sleeve','Sleeveless','Spaghetti','balloon sleeve','frill sleeve'],
      Price: ['under $50','under $100','$100-$200','$200-$300','$300-$400','over $500']
      }
  },
  methods: {
    handleChange: function () {
      var aa = document.getElementsByClassName('el-collapse-item__header')
      var arr = this.activeNames
      var arr1 = ['1','2','3','4','5','6','7','8'] 
      let difference = arr1.filter (x => arr.indexOf(x) == -1).concat(arr.filter(x => arr1.indexOf(x) == -1));
      for (var i = 0; i < arr.length; i++) {
        var index = arr[i]-1
        aa[index].style.color = '#0F0F0F'
      }
      for (var j = 0; j < difference.length; j ++) {
        var index1 = difference[j]-1
        aa[index1].style.color = '#595959'
      }
    },
    CategorySub: function (index) {
      console.log(this.Category[index])
    },
    SizecheckListSub: function () {
      console.log(this.SizecheckList)
    },
    MtcheckListSub: function () {
      console.log(this.MtcheckList)
    },
    StcheckListSub: function () {
      console.log(this.StcheckList)
    },
    DecheckListSub: function () {
      console.log(this.DecheckList)
    },
    ColorcheckListSub: function () {
      console.log(this.ColorcheckList)
    },
    SlcheckListSub: function () {
      console.log(this.SlcheckList)
    }
  },
  mounted () {
    var element = document.getElementsByClassName('el-collapse-item__header')
    var arr = this.activeNames
    for (var i = 0; i < arr.length; i++) {
    var index = arr[i]-1
    element[index].style.color = '#0F0F0F'
    }
  }
}
</script>
<style>
.el-collapse {
  border: 0;
}
.el-collapse-item__header {
  height: 33px;
  line-height: 33px;
  padding-left: 0;
  background-color: #fafafa;
  color: #595959 ;
  cursor: pointer;
  border-bottom: 1px solid #E5E5E5;
  font-size: 14px;
}
.filters-tittle:hover {
  color: #E54C87;
}
.el-collapse-item__content {
  background: #fafafa;
}
.el-collapse-item__header {
  color: #595959;
}

.filters-content {
    max-height: 230px;
    height: auto;
    overflow: auto;
    margin-top: 10px;
    padding-bottom: 10px;
}
.filters-content a {
  font-size: 12px;
  color: #595959;
  padding: 6px 4px;
  display: block;
  line-height: 1.428571429;
  text-decoration: none;
}
.filters-content a:hover {
  color: #E54C87;
  text-decoration:underline;
}
.el-checkbox {
  padding-bottom: 12px;
  float: left;
  width: 50%;
}
.el-checkbox+.el-checkbox {
  margin: 0 0 0 0;
}
.el-checkbox__input {
  outline: 0;
  line-height: 1;
  vertical-align: middle;
}
.el-checkbox__inner {
  width: 16px;
  height: 16px;
  border-color:#595959;
  background-color: #fafafa;
}
.el-checkbox__inner:hover {
  border-color: #E54C87;
}
.el-checkbox__input.is-checked .el-checkbox__inner {
  background-color: #E54C87;
  border-color: #E54C87;
}
.el-checkbox__input.is-focus .el-checkbox__inner {
  border-color:#E54C87;
}
.filter-detail-item2 .el-checkbox {
  width: 100%;
}
.el-checkbox__label {
  padding-bottom: 6px;
  font-size: 12px;
}

</style>