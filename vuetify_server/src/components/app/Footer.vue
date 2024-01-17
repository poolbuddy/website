<template>
 <v-footer
    class="bg-indigo-lighten-1 text-center d-flex flex-column"
    >
    <v-row no-gutters justify="center">
      <v-row no-gutters justify="center">
        <v-col>
          <v-img width="150" src="@/assets/img/cst2.png"></v-img>
          <v-img width="150" src="@/assets/img/cstCert.png"></v-img>
          <v-img width="150" src="@/assets/img/vet.png"></v-img>
      
          
        </v-col>
      </v-row>
      
      <v-col>
        <v-table density="compact">
          <thead>
            <tr>
              <th class="text-left">
                Days of the Week
              </th>
              <th class="text-left">
                Hours of Operation
              </th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="item in schedule"
              :key="item.day"
            >
              <td>{{ item.day }}</td>
              <td>{{ item.hours }}</td>
            </tr>
          </tbody>
        </v-table>
      </v-col>
      <v-col>
      </v-col>
          </v-row>
            <div>
              <v-btn
                v-for="icon in icons"
                :key="icon"
                class="mx-4"
                :icon="icon"
                variant="text">
              </v-btn>
            </div>
    
    <v-divider></v-divider>

    <v-row class="justify-space-evenly">
      <span>{{ new Date().getFullYear() }} — <strong>The Pool Buddy</strong></span><span>|</span><router>Privacy</router><span>|</span><router>Terms Of Service</router><span>|</span><router>Cookie Preferences</router>
    </v-row>
    </v-footer>
</template>
      
<script setup>

      const contactInfo = [
        {
          contact:'631-672-8733',
          method: 'Phone',
        },
        {
          contact:'info@thepoolbuddy.com',
          method: 'Email',
        },
      ]
      const schedule = [
          {
            day: 'Monday',
            hours: '9:00am - 6:00pm',
          },
          {
            day: 'Tuesday',
            hours: '9:00am - 6:00pm',
          },
          {
            day: 'Wensday',
            hours: '9:00am - 6:00pm',
          },
          {
            day: 'Thursday',
            hours: '9:00am - 6:00pm',
          },
          {
            day: 'Friday',
            hours: '9:00am - 6:00pm',
          },
          {
            day: 'Saturday',
            hours: '9:00am - 6:00pm',
          },
          {
            day: 'Sunday',
            hours: 'closed',
          },
          
        ]

</script>
