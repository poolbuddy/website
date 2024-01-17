<template>
    <div>
      <v-row no-gutters justify="center" class="ma-8">
      <v-card v-for="card in cards" :key="card.title" :title="card.title" class="ma-8">
        <v-card-actions>
          <v-btn @click="callScrollMethod(card.method)" :prepend-icon="card.icon1">Scroll</v-btn>
          <v-btn :to="{ name: card.route, params: { service: card.title } }" :append-icon="card.icon2">Request Callback</v-btn>
        </v-card-actions>
        </v-card>
      </v-row>

        <v-container height="py-9" class="bg-primary" >
          <h1 ref="saunaConstruction">Sauna Construciton</h1>
          <h1>You can look through these</h1>
          <v-carousel>
            <v-carousel-item
              src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
              cover
            ></v-carousel-item>

            <v-carousel-item
              src="https://cdn.vuetifyjs.com/images/cards/hotel.jpg"
              cover
            ></v-carousel-item>

            <v-carousel-item
              src="https://cdn.vuetifyjs.com/images/cards/sunshine.jpg"
              cover
            ></v-carousel-item>
          </v-carousel>
          <div>
            <h1>Here is the description</h1>
            <p>
              lorem ip 
A Hassle-Free Pool Season Awaits

Are you tired of spending your precious summer weekends maintaining your pool instead of enjoying it? We’ve got you covered with our full season maintenance plan. Let us do all the hard work while you soak up the sun and create unforgettable memories with family and friends.

Our full season maintenance plan is the ultimate solution for a worry-free pool season. We take care of all the essential tasks, from pool opening to closing and weekly maintenance. Our team of experienced technicians will provide consistent, professional pool care all season long to ensure your pool stays in tip-top shape all the time.

            </p>
          </div>
          <v-row no-gutters class="justify-center" gap="9">
                          
                          <video width="640" height="360" class="" controls >
                              <source src="@/assets/img/sample.mp4" type="video/mp4">
                          
                          </video>
                      </v-row>
        </v-container>
 
    </div>
  </template>
  <script>
  import {wellness_list} from "@/assets/js/Lists"
  export default {
    name: 'WellnessPage',
    data(){
      return{
        cards:wellness_list
      }
    },
    methods: {
    callScrollMethod(methodName) {
      // Dynamically call the scroll method based on the card
      if (typeof this[methodName] === 'function') {
        this[methodName]();
      }
    },
    scrollToHydroponics() {
      this.$refs.hydroponicsSection.scrollIntoView({ behavior: 'smooth' });
    },
    scrollToSensoryDep() {
      this.$refs.sensoryDepSection.scrollIntoView({ behavior: 'smooth' });
    },
    scrollToSaunaConstruction() {
      this.$refs.saunaConstruction.scrollIntoView({ behavior: 'smooth' });
    },
    scrollToHomeAuto1() {
      this.$refs.homeAuto1.scrollIntoView({ behavior: 'smooth' });
    },
    scrollToHomeAuto2() {
      this.$refs.homeAuto2.scrollIntoView({ behavior: 'smooth' });
    },
    scrollToEndless() {
      this.$refs.endless.scrollIntoView({ behavior: 'smooth' });
    },
    // Add more scroll methods as needed
  },
  }
  </script>
  