<template>

  <v-bottom-navigation
      color="teal"
      app
      prominant
      class="d-md-none"
    >
    <v-btn color="primary" prepend-icon="mdi-phone" density="compact" href="tel:+1234567890">Call Now</v-btn>
    <v-btn color="primary" prepend-icon="mdi-comment-processing" density="compact" href="sms:+1234567890">SMS</v-btn>
    <v-btn color="primary" prepend-icon="mdi-storefront" density="compact" :to="{name: ''}">Store</v-btn>
      
     
    </v-bottom-navigation>

</template> 
      
<script>
import { defineComponent } from 'vue';
import { useUser } from '@/store/user.js'; // Adjust the path
import { mapState,mapActions  } from 'pinia'

export default defineComponent({
    name: 'Bottom',
    computed:{
    ...mapState(useUser, ['isAuthenticated']),

  },
  methods:{
    ...mapActions(useUser, ['removeToken']),
  }

})
</script>
