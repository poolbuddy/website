<template>
 
  <v-app-bar
      app
      prominant
      collapse
      height="10vh"
      scroll-threshold="250"
      scroll-behavior="fade-image hide inverted"
      image="/src/assets/landing.png"
      class="d-md-none"
      > 
      <template v-slot:image>
          <v-img
            gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
          ></v-img>
      </template>
      <v-app-bar-nav-icon icon="mdi-menu-open" @click="toggleDrawer" ></v-app-bar-nav-icon>
      <v-app-bar-title style="font-family: 'Luckiest Guy', cursive; font-size:200%;" class=" bg-transparent border rounded-pill text-center align-text">    <v-img width="90" src="/src/assets/cst2.png"></v-img>
      </v-app-bar-title>
      <v-btn icon @click="toggleBottomNav" >
          <v-icon >mdi-dots-horizontal-circle-outline</v-icon>
      </v-btn>
    </v-app-bar>

</template>
      
<script>
import { mapState, mapMutations } from 'vuex';

export default {
  name: 'AppBar',

  methods: {
    ...mapMutations(['toggleDrawer']),
    ...mapMutations(['toggleBottomNav']),
  },

}

</script>