<template>
  <v-navigation-drawer
        location="right"
        :close-on-content-click="false"
        app
        width="100vw"
        v-model="isDrawerOpen"
      >
      <v-divider></v-divider>
      <v-list>

      <v-list-item class="d-flex justify-end">
        <v-btn icon @click="toggleDrawer" elevation="0" class="" >
         <v-icon size="40" color="surface-lighten-2">mdi-close-octagon-outline</v-icon>
        </v-btn>
        </v-list-item>


      <v-list-item title="Pool Services" prepend-icon="mdi-pool" append-icon="mdi-pool" class="d-flex justify-center bg-surface-lighten-2">
      
      </v-list-item>
      
      <v-divider></v-divider>
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

      <v-divider></v-divider>

      <v-divider></v-divider>

      <v-list-group value="Info">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            prepend-icon="mdi-information"
            title="Company Information"
          ></v-list-item>
        </template>
        <v-list-item
          v-for="([title, icon, route], i) in info"
          :key="i"
          :value="title"
          :title="title"
          :to="{ name: route}"
          :prepend-icon="icon"
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
      </v-list-group>
      <v-divider></v-divider>

      <v-list-item></v-list-item>
      <v-divider></v-divider>

      <v-list-group value="wellness">
        <template v-slot:activator="{ props }">
          <v-list-item
            v-bind="props"
            prepend-icon="mdi-run"
            title="Coming Soon"
          ></v-list-item>
        </template>
        <v-list-item
          v-for="([title, icon, route], i) in wellness"
          :key="i"
          :value="title"
          :title="title"
          :to="{ name: route}"
          :prepend-icon="icon"
        ></v-list-item>
        
      </v-list-group>
      
      <v-divider></v-divider>

      </v-list>
    </v-navigation-drawer>
</template>
      
<script>
import { defineComponent } from 'vue';
import { mapState,mapActions  } from 'pinia'
import { useNavDrawer } from '@/store/drawer'

export default defineComponent({
    name: 'NavDrawer',

    computed:{
    ...mapState(useNavDrawer, ['isDrawerOpen'])
  },
  methods: {
   
   ...mapActions(useNavDrawer, ['toggleDrawer']),

},

  data: () => ({

open: null,

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
        ['Leak Detection','mdi-pipe-leak', ''],
        ['Installation','mdi-certificate', ''],
        ['Remodel','mdi-account-hard-hat', ''],
        ['Store','mdi-store', ''],
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
      wellness: [
        ['Endless Pools','mdi-wall',''],
        ['Sensory Deprovation Tanks','mdi-meditation', ''],
        ['Smart Hydroponic Gardens','mdi-sprout', ''],
        ['Home Automation','mdi-wall',''],
        ['Sauna Construction','mdi-wall',''],
      ],

 

}),

  
})
</script>
