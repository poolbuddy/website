<template>
  <v-img   class="align-center" cover max-height="60vh" src="@/assets/img/landing.png" gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)" >
    <v-container fluid class="">
      
      <v-row no-gutters class="mt-6">
        <transition name="fade" appear >
          <v-img height="250" class=""  src="@/assets/img/logo.png"></v-img>
        </transition>
      </v-row>
      <v-row align-self="end" no-gutters  class="d-md-none mt-1" >
        <v-col cols="2">
          <v-btn icon  color="transparent" @click="toggleDrawer()">
            <v-icon >mdi-menu-open</v-icon>
          </v-btn> 
        </v-col>
        <v-col align-self="center">
          <v-row justify="space-around" class="ga-1" >
            
                    <v-btn
              v-for="(button, index) in buttons_mobile"
              :key="index"
              density="compact"
              :to="button.route"
              :prepend-icon="button.icon"
            >
              {{ button.title }}
            </v-btn>
          </v-row> 
        </v-col>

      </v-row> 

      <v-row class="d-none d-md-flex ga-3 mt-md-16"  justify="space-around"  no-gutters align-self="end">

      <v-menu  v-model="open" :close-on-content-click="false">
        <template v-slot:activator="{ props }">
          <v-btn
            color="primary"
            v-bind="props"
            append-icon="mdi-chevron-down"
            prepend-icon="mdi-pool"
            :loading="loading"
            density="compact"
            @click="loading = !loading"
          >
            Services 
            <template v-slot:loader>
              <v-progress-linear indeterminate></v-progress-linear>
            </template>
          </v-btn>
        </template>
        <v-list >

          <v-list-group value=RoutineGroup>
            <template  v-slot:activator="{ props }">
              <v-list-item
                v-bind="props"
                prepend-icon="mdi-pool"
                title="Routine"
              ></v-list-item>
            </template>
            <v-list-item
              v-for="([title, icon, route], i) in routine"
              :key="i"
              :value="title" 
              :title="title"
             
              :to="{ name: route}"
              :prepend-icon="icon"
            ></v-list-item>
          </v-list-group>       

          <v-list-item
            v-for="([title, icon, route], i) in nonRoutine"
            :key="i"
            :value="title"
            :title="title"
            :to="{ name: route}"
            :prepend-icon="icon"
          ></v-list-item>

    </v-list>
      </v-menu>

<v-menu  :close-on-content-click="false">
        <template v-slot:activator="{ props }">
          <v-btn
            color="primary"
            v-bind="props"
            :loading="loading1"
            @click="loading1 = !loading1"
            density="compact"
            append-icon="mdi-chevron-down"
            prepend-icon="mdi-information"
          >
            Company Info
            <template v-slot:loader>
          <v-progress-linear indeterminate></v-progress-linear>
          </template>
                </v-btn>
              </template>
              <v-list>

              <v-list-item
                v-for="([title, icon, route], i) in info"
                :key="i"
                :to="{name: route}"
                :title="title"
                :prepend-icon="icon"
                :value="title"
              ></v-list-item>
              <v-list-item
                disabled
                v-for="([title, icon], i) in contacts"
                :key="i"
                :title="title"
                variant="tonal"
                :prepend-icon="icon"
                :value="title"
              ></v-list-item>
            
        </v-list>
      </v-menu>
      <v-btn
      v-for="(button, index) in buttons_desktop"
      :key="index"
      density="compact"
      :to={name:button.route}
      :prepend-icon="button.icon"
    >
      {{ button.title }}
    </v-btn>
      </v-row>

    </v-container>
  </v-img>
</template>


<script>
import { ref, onMounted, watch } from 'vue';
import { mapState,mapActions  } from 'pinia'
import { useNavDrawer } from '@/store/drawer'

  export default {
    name: 'Head',
   
  computed:{
    ...mapState(useNavDrawer, ['isDrawerOpen'])
  },
    
    data: () => ({

      
      open: null,
      loading: false,
      expanded: false,
      loading1: false,
    

      contactInfo: [
          {
            contact: '631-672-8733',
            method: 'phone',
          },
          {
            contact: 'info@thepoolbuddy.com',
            method: 'email',
          },
          {
            contact: '2001 nesconset hwy ,lake grove #1002',
            method: 'mail',
          },
        ],
        routine: [
        ['Openings', 'mdi-gift-open', ''],
        ['Power Vacuums', 'mdi-van-utility', ''],
        ['Regular Maintenance', 'mdi-van-utility', ''],
        ['Closing', 'mdi-gift', ''],
        ['Winter Watch', 'mdi-snowflake', ''],
        ['Regular Maintenance Season Bundle', 'mdi-sale', ''],
        ['Green to Clear', 'mdi-liquid-spot', ''],
        ['Balance Pool Chemistry', 'mdi-scale-balance', ''],
        ['Pressure Washing', 'mdi-scale-balance', ''],
        ['Shrink Wrapping', 'mdi-scale-balance', ''],
        ['Pool School', 'mdi-school', ''],
      ],
      nonRoutine: [
        ['Repair','mdi-wrench', ''],
        ['Leak Detection','mdi-water-alert', ''],
        ['Installation','mdi-certificate', ''],
        ['Remodel','mdi-account-hard-hat', ''],
      ],
      info:[
        ['About Us','mdi-information-outline', ''],
        ['Blog','mdi-post-outline', ''],
        ['Become a member of the team','mdi-briefcase-outline', ''],
      ],
       contacts:[
        ['631-672-8773','mdi-phone' ],
        ['info@thepoolbuddy.com','mdi-email'],
      ],
        icons: [
        'mdi-facebook',
        'mdi-google',
        'mdi-instagram',
      ],
      buttons_mobile: [

  
        { title: 'Schedule Call', icon: 'mdi-phone-in-talk', route: '' },
    
      ],
      buttons_desktop: [
        { title: 'Coming Soon', icon: 'mdi-spa-outline', route: '' },
        { title: 'Store', icon: 'mdi-storefront', route: '' },
        { title: "Schedule Call", icon: 'mdi-phone-in-talk', route: '' },
      ],
    
    }),

    methods: {
   
      ...mapActions(useNavDrawer, ['toggleDrawer']),

    toggleGroup(group) {
      // Toggle the value of the specified group
      this[group] = !this[group];
    },

   

  },

    watch: { 
      
     loading (val) {
       if (!val) return      
       setTimeout(() => (this.loading = false), 1000);

     },
     loading1 (val) {
       if (!val) return
         
       setTimeout(() => (this.loading1 = false), 1000)
     },
    
   },
   
  }
  </script>