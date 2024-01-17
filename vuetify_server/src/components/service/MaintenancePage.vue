<template>
  <div>
     
      <v-container fluid>
        <v-row>
          <h1>Available regular maintenance Plans</h1>
        </v-row>
        <v-row  justify="space-around" class="flex-column flex-md-row">
          <v-col>
            <v-card>
              <h1 class="value">Value</h1>
              ( $65 - $85 )
    
            </v-card>
            <v-list>
              <v-list-item class="bg-surface-darken-1">
                You can Buy Chemicals in bulk at Wholesale(feel free to compare) or provide your own.
                We'll remind you when you are low and if you run out we will refill at cost just under retail
                for the replacement chemicals.
              </v-list-item>
              <v-list-item>
                Chemicals not included
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                usual days of week for service are either tue/wens/thur
                depending on area and availability
              </v-list-item>
              <v-list-item >
                weekly/ *biweekly visits (not all pools apply for BW)
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                *Payment method on file required
              </v-list-item>
              <v-list-item>
                Priority Scheduling
              </v-list-item>
              <v-list-item>
                <v-btn class="bg-surface-darken-1" :to="{name: ''}">Get Estimate Now</v-btn>
              </v-list-item>
              <v-list-item >
                <v-btn class="bg-surface-darken-1" :to="{name: ''}">Book Now</v-btn>
              </v-list-item>
            </v-list>
            <h1 class="value pa-4">This plan is for customers who want a clean pool all summer and never want to worry about it turning green and 
            want to pay as little as possible. It also comes with the peace of mind of having priority scheduling in the event of anything going wrong.
          </h1>
          </v-col>

            <v-col>
            <v-card>
              <h1 class="concierge"> Concierge</h1>
              ( $90 - $140 )
            </v-card>
            <v-list>
             
              <v-list-item class="bg-surface-darken-1">
                days of week are either thurs/fri (depending on area)
              </v-list-item>
              <v-list-item>
                We provide chemicals
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                $20 credit for the online store
              </v-list-item>
              <v-list-item>
                weekly or *biweekly (not all pool apply for BW service)
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                Top Priority Scheduling
              </v-list-item>
              <v-list-item>
                Can not gaurentee but we will try our best to 
                accomadate in the event you want to change the day of a particular regular 
                maintenance if you have a event or party.
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                *Payment method on file required
              </v-list-item>
              <v-list-item>
                extra cleanings at %30 off(you have a party or event )
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                %10 off of Services
              </v-list-item>
              <v-list-item >
                <v-btn class="bg-surface-darken-1" :to="{name: ''}">Get Estimate Now</v-btn>
              </v-list-item>
              <v-list-item >
                <v-btn class="bg-surface-darken-1" :to="{name: ''}">Book Now</v-btn>
              </v-list-item>
            </v-list>
            <h1 class="concierge pa-4">This plan is for custromers who want us to handle everything and who highly value a cleaning right before the weekend as well as considerations and flexiblity for 
            the event the customer wants to entertain and have a clean pool for the occasion.  This plan also comes with the peace of mind that it comes with top priority scheduling and 
            discounts on services. 
          </h1>
          </v-col>

            <v-col>
            <v-card>
              <h1 class="alla">Pool School Overwatch</h1>
              ( $100/hr )
            </v-card>
            <v-list>
              <v-list-item class="bg-surface-darken-1">
                Buy chemicals in bulk at wholesale 
                or we can refill at retail
              </v-list-item>
              <v-list-item>
                flexible scheduling
                weekly/biweekly/monthly
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                EWasy to add extra cleanings
                Cleanings *not done on thrus/fri
              </v-list-item>
              <v-list-item>
                You can call us whenever you run into a problem 
                and we will talk you through a solution or schedule
                an appointment.
              </v-list-item>
              <v-list-item class="bg-surface-darken-1">
                Accept all forms of payment
              </v-list-item>
              <v-list-item>
              no service agreement
              </v-list-item>
              <v-list-item >
                <v-btn class="bg-surface-darken-1" :to="{name: ''}">Book Now</v-btn>
              </v-list-item>
            </v-list>
            <v-row>
          <h1 class="alla pa-4">This Plan is for a customer who wants to do it themselves, have access to cheap chemicals and want someone to call who will answer questions and come when things
            get overbearing.
          </h1>
        </v-row>
          </v-col>
        </v-row>
      </v-container>

      <v-container>
        <v-row no-gutters>
          <h1>Conditions for Good Maintenance</h1>
          <h4>(What we need from you)</h4>
        </v-row>
        <v-list>
          <v-list-item >Let Us Know if you plan to change the pool timer</v-list-item>
          <v-list-item class="bg-surface-darken-1">
            All Leaks need to be addressed.  If you develop a leak let us schedule a time to take care of it.  Leaks make keeping proper 
            chemical levels too expensive to maintain.  Also could risk burning the 
            pump if the water level drops below the skimmer in certain circumstances.
          </v-list-item>
          <v-list-item>
            Timer / Pump / Filter / Sanitizer must be in good working order.  In the event on the items are not in working order we will need 
            permission to repair or replace the malfunctioning equipment.
          </v-list-item>
          <v-list-item class="bg-surface-darken-1">
            Free access to the backyard.  If you lock your back gate then arrangements need to be made to give us free access to the pool on the 
            scheduled service day. 
          </v-list-item>
        </v-list>
      </v-container>
      
      <v-container>
        <v-row no-gutters>
          <h1>Payment Methods</h1>
          <h4>Your choices of how you would like to pay</h4>
        </v-row>
        <v-list>
          <v-list-item >
            You can still elect to pay by check/cash.  Which will be due on the first of each month of scheduled service and will apply to the regular maintenance 
            that will occur in that month.   You can mail it or put it in an arranged hiding spot in the backyard.  We still require a payment method on file so
            that in the event that by the 15th the payment isnt available the on file payment method will be charged.  If for anyreason you need to discontinue 
            service, We will immediatly reimburse you of any current credit balance in your account with no questions asked and no fees.
          </v-list-item>
          <v-list-item class="bg-surface-darken-1">
            You can save from $5 a service if you elect to enroll in autopay in which you will be charged on the monday following the regular maintenenace.  
          </v-list-item>
        </v-list>
      </v-container>
   
     <v-container>
      <v-expansion-panels variant="popout" class="my-4">
        <v-expansion-panel
          title="How often should you get your pool cleaned?"
          text="It really depends on a few factors such as how often the pool is used, the weather, and the area surrounding the pool.
                We recommend that your pool be cleaned at least once a week, but it may require more if it’s been very windy or you’ve had a pool party recently."
        ></v-expansion-panel>
        <v-expansion-panel
          title="Is it worth it to clean your own pool?"
          text="You need to ask yourself if you have the time and energy to commit to cleaning the pool at least once a week.
If you enjoy the process and have the time, go for it. Otherwise, we’d suggest hiring a pool cleaning service such as ours to help you keep your pool sparkling clean all season long."
        ></v-expansion-panel>
        <v-expansion-panel
          title="What happens if you don’t clean your pool?"
          text="If you neglect your pool maintenance, you’ll be in for a world of trouble. Algae and bacteria will start to thrive, the water will become cloudy and uninviting, and your equipment will start to malfunction. Not to mention, it can be a safety hazard.
In short, not cleaning and maintaining your pool is a recipe for disaster."
        ></v-expansion-panel>
        <v-expansion-panel
          title="Should you backwash a pool every week?"
          text="Backwashing your pool every week may not be necessary.
It depends on the usage, the environment, and the filtration system. A general rule of thumb is to backwash when the pressure gauge is 8-10 PSI above the normal starting pressure.
However, it’s always good to consult with a professional pool technician to determine the best schedule for your pool."
        ></v-expansion-panel>
        <v-expansion-panel
          title="Is it OK to swim in a pool without chlorine?"
          text="Swimming in a pool without chlorine is definitely not a good idea. Chlorine is a disinfectant that kills harmful microorganisms and bacteria in the water, making it safe for swimming.
Without it, you’re essentially swimming in a petri dish of germs and bacteria. So, it’s best to stick with a properly chlorinated pool."
        ></v-expansion-panel>
        <v-expansion-panel
          title="How does the AutoPay discount work?"
          text="Simply submit your payment information and allow us to automatically charge your payment method on file.
Put your pool service payment on autopilot – there’s no easier way to save $20-25 per month!"
        ></v-expansion-panel>
        <v-expansion-panel
          title="What do you mean by priority scheduling?"
          text="As a Weekly or Premier plan member, you will always be at the top of the list when we are scheduling service calls for pool troubleshooting, equipment upgrades, or pool repairs..
                If you need a service call, we will be sure to get you on the schedule as soon as possible so we can have your pool fixed up and ready to go fast."
        ></v-expansion-panel>
        <v-expansion-panel
          title="Which chemicals are included in the Premier plan?"
          text="We will add as many pool-balancing chemicals as necessary. This means shock, chlorine tablets, sodium bicarbonate, calcium chloride, muriatic acid, and salt (up to 80 lbs. per visit).
                Specialty chemicals that are not included are algaecide, mineral or phosphate remover, water clarifier, and stabilizer (cyanuric acid)."
        ></v-expansion-panel>
        <v-expansion-panel
          title="How does the cancellation option work for the Flex plan?"
          text=""
        ></v-expansion-panel>
        <v-expansion-panel
          title="What type of scheduling flexibility do I have with the Alla Cart plan?"
          text="You can set up the frequency of your visits to be whatever you’d like – every two weeks, three weeks, monthly…it’s entirely in your hands.
                Also, since no service agreement has been signed, you can discontinue your plan at any time without receiving a fee."
        ></v-expansion-panel>
      </v-expansion-panels>
     </v-container>
  </div>
</template>

<script>
export default {
  name: 'MaintenancePage',
}
</script>

<style scoped lang="scss">



</style>