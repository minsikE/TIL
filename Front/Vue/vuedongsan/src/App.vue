<template>
  <div class="menu">
    <a v-for="(a,i) in menus" :key="(i)">{{(i)}}</a>
  </div>
  원룸샵
  <div v-for="(item,index) in items" :key="index">
    
    <h4>{{item.id}}</h4>
    <p>{{(item.price)}} 만원</p>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      menus : ['Home', 'Shop', 'About'],
      items : [
        {id : '역삼동 원룸', price: 50},
        {id : '천호동 원룸', price: 70},
        {id : '마포동 원룸', price: 90},
      ],      
    }
  },
  components: {    
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.menu {
  background: darkslateblue;
  padding: 15px;
  border-radius: 5px;
}
.menu a {
  color: white;
  padding: 10px;
}
</style>
