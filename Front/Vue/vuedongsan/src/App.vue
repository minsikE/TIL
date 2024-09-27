<template>

  <div class="black-bg" v-if="모달창열렸니 == true">
    <div class="white-bg">
      <h4>상세 페이지</h4>
      <p>상세 페이지 내용</p>
    </div>
  </div>

  <div class="menu">
    <a v-for="(a,i) in menus" :key="(i)">{{(a)}}</a>
  </div>
  
  <div>
    <img src="./assets/room0.jpg" class="room-img">
    <h4 @click="모달창열렸니 = true">{{products[0]}}</h4>
    <p>50 만원</p>
    <button @click="신고수[0]++">허위매물신고</button> 
    <span>신고수 : {{신고수[0]}}</span>
  </div> 
  <div>
    <img src="./assets/room1.jpg" class="room-img">
    <h4>{{products[1]}}</h4>
    <p>60 만원</p>
    <button @click="신고수[1]++">허위매물신고</button> 
    <span>신고수 : {{신고수[1]}}</span>
  </div>
  <div>
    <img src="./assets/room2.jpg" class="room-img">
    <h4>{{products[2]}}</h4>
    <p>70 만원</p>
    <button @click="신고수[2]++">허위매물신고</button> 
    <span>신고수 : {{신고수[2]}}</span>
  </div>
</template>

<script>

export default {
  name: 'App',
  data(){
    return {
      모달창열렸니 : false,
      신고수 : [0,0,0],
      menus : ['Home', 'Shop', 'About'],
      items : [
        {id : '역삼동 원룸', price: 50, 신고수: 0},
        {id : '천호동 원룸', price: 70, 신고수: 0},
        {id : '마포동 원룸', price: 90, 신고수: 0},
      ],
      products : ['역삼동 원룸', '천호동 원룸', '마포동 원룸']      
    }
  },
  methods : {
    increase(index){            
      this.items[index].신고수 += 1;
    }
  },
  components: {    
  }
}
</script>

<style>
body {
  margin: 0
}
div {
  box-sizing: border-box;
}
.black-bg {
  width: 100%; height: 100%;
  background: rgba(0,0,0,0.5);
  position: fixed; padding: 20px;
}
.white-bg {
  width: 100%; background: white;
  border-radius: 8px;
  padding: 20px;
}

.room-img {
  width: 100%;
  margin-top: 40px;
}

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
