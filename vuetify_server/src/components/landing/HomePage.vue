<template >

<div>
    <v-container> 
      <v-carousel
        cycle
        height="40vh"
        hide-delimiters
        :show-arrows="false"
        
        v-model="activeIndex"
      >
        <v-carousel-item
          v-for="(image, i) in images"
          :key="i"
          :src="image.src"
        >
        <v-container fluid class="fill-height">
          
            <v-row class=" fill-height" >
              <v-col class="bg-surface" align-self="start" cols="12" >
                <v-row class="w-50">
                  <transition name="fade">
                    <h1 v-if="activeIndex===1">life sucks</h1>
                  </transition>
                  <transition name="fade">
                    <h1 v-if="activeIndex===2">life sucks</h1>
                  </transition>
                  <transition name="fade">
                    <h1 v-if="activeIndex===0">You suck</h1>
                  </transition>
                </v-row>
                
              </v-col>
              <v-col dark class="bg-surface" cols="12" align-self="center">
                <v-row>
                  <transition name="fade">
                  <h1 v-if="activeIndex===2">it sucks</h1>
                </transition>
            
                <transition name="fade">
                  <h1 v-if="activeIndex===2">life sucks</h1>
                </transition>
                <transition name="fade">
                  <h1 v-if="activeIndex===3">life sucks</h1>
                </transition>
                </v-row>
                
              </v-col>
            
              <v-col class="bg-surface" cols="12" align-self="end">
                <transition name="fade">
                  <h1 v-if="activeIndex===2">life sucks</h1>
                </transition>
                <transition name="fade">
                  <h1 v-if="activeIndex===1">life sucks</h1>
                </transition>
              </v-col>    
          </v-row>
        </v-container>
    </v-carousel-item>
      </v-carousel>
      <v-row style="height: 6vh;" class="d-xl-none"></v-row>
      <v-row style="height: 5vh;" class="d-md-none"></v-row>
    </v-container>
          
    <v-container >
              <v-img cover gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)" >
                <v-container >
                  <v-row style="height: 5vh;"></v-row>
                    <v-row justify="center" class="ga-10 text-h1">
                      <h2 class="text-decoration-underline">Why</h2><h2 class="text-decoration-underline"> you'll </h2><h2 class="text-decoration-underline">choose</h2><h2 class="text-decoration-underline">us</h2> 
                    </v-row>
                  <v-row style="height: 10vh;">
                  </v-row>
                
                <v-col class="text-h3">
                  <v-card>
                  <h3 class="text-center">We have a customer portal and an online store </h3>
                </v-card>
                <v-list-item prepend-icon="mdi-phone" append-icon="mdi-phone"><h3 class="text-center">We have a customer portal and an online store </h3></v-list-item>

                  <v-card>
                  <h3 class="text-center"> Log in to check contract/past services/invioces</h3>
                </v-card>
                <v-list-item prepend-icon="mdi-phone" append-icon="mdi-phone"><h3 class="text-center">We have a customer portal and an online store </h3></v-list-item>

                <v-card>
                  <h3 class="text-center">order a float from our online store and it just appears in your pool</h3>
                </v-card>
                <v-list-item prepend-icon="mdi-phone" append-icon="mdi-phone"><h3 class="text-center">We have a customer portal and an online store </h3></v-list-item>

                <v-card>
                  <h3 class="text-center">Positivley Reviewed, Decades of experience, Veteran Owned and we do everything</h3>                 
                </v-card>          
                <v-list-item prepend-icon="mdi-phone" append-icon="mdi-phone"><h3 class="text-center">We have a customer portal and an online store </h3></v-list-item>
                </v-col>
            </v-container>
            </v-img>
    </v-container>
       
    <v-parallax
    height="80vh"
      src="@/assets/img/pool.jpg"
      class="m-0"
      >
      <v-row align="center" justify="center" class="fill-height">
        <v-col cols="12" md="6" lg="4">
          <div class=" bg-transparent text-center">Well take care of it</div>
        </v-col>
      </v-row>
    </v-parallax>
     
  </div>
</template>

<script setup>

        const activeIndex = 0
      
        const images = [

          {
            src: '@/assets/img/pool.jpg',
          },
          {
            src: '@/assets/img/landing.jpg',
          },
          {
            src: '@/assets/img/cst2.png',
          },
          {
            src: '@/assets/img/logo.png',
          },
          
        ]
       const icons = [
        'mdi-facebook',
        'mdi-google',
        'mdi-instagram',
      ]

</script>
