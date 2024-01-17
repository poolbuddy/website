<template>
  <v-app>
  <my-top-bar></my-top-bar>
<nav-drawer></nav-drawer>
<my-head></my-head>
    <v-main style="margin: 0%; padding: 0%;" >
      <router-view v-slot="{ Component }"> 
        <transition name="route" mode="out-in">
          <component :is="Component"></component>
        </transition>
      </router-view>
    </v-main> 
<my-footer></my-footer>
<my-bottom></my-bottom>
  </v-app>
</template>

<script>
import SystemBar from '@/components/app/SystemBar.vue';
import NavDrawer from '@/components/app/NavDrawer.vue';
import Head from '@/components/app/Head.vue';
import Footer from '@/components/app/Footer.vue';
import Bottom from '@/components/app/BottomNav.vue';
import { onBeforeMount } from 'vue';
import { useUser } from '@/store/user';
import axios from 'axios'


export default {
  name: 'App',
  setup() {
    const store = useUser()
    store.initializeStore()

    onBeforeMount(() => {
      

    const token = store.token
    if (token) {
      axios.defaults.headers.common['Authorization'] = "Token " + token;
      
    } else {
      axios.defaults.headers.common['Authorization'] = "";
    }
  });

    
  },
  components: {
    'my-top-bar': SystemBar,
    'nav-drawer': NavDrawer,
    'my-head' : Head,
    'my-footer' : Footer,
    'my-bottom' : Bottom,
  },

  
}
</script>