<template>
<v-system-bar
 height="50" 
 app 
 class="bg-surface">
          <v-row no-gutters justify="end">
            <v-col class="d-flex justify-end flex-row">
            <v-btn v-if="!isAuthenticated" :to="{name: ''}">
              Sign Up
            </v-btn>
            <v-btn v-if="isAuthenticated" :to="{name: ''}">Dasboard</v-btn>
            <v-btn v-if="isAuthenticated" @click="logout">Log out</v-btn>
            <v-btn v-if="!isAuthenticated" :to="{name: ''}">Login Here</v-btn>
            </v-col>
          </v-row>   
    </v-system-bar>
</template>
  

  <script setup>
  import { ref, computed, watchEffect  } from 'vue';
  import { useUser } from '@/store/user.js'; // Adjust the path
  import { mapState, mapActions } from 'pinia';
  import { useRouter} from 'vue-router';

  const router = useRouter()
  const store = useUser()
  const isAuthenticated = computed(() => store.isAuthenticated);
  const member = computed(() => store.membership);
  const logout = async () => {
      await store.removeToken(); // Ensure it's asynchronous
}; 
watchEffect(() => {
  if (store.token === null && store.isAuthenticated === false && store.email === null && !localStorage.getItem('token') && !localStorage.getItem('profile') && !localStorage.getItem('email')) {
   
    router.push('login')
  }
});
  </script>
