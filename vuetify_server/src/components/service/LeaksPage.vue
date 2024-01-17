<template>
  <v-sheet>
    <v-img   class="align-center" cover  gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)" >
      <v-container>
        <h1>All Phase Leak Detection and Repair</h1>
        
        <h3>  A pools anatomy generally consits of the main shell (which can be either fiberglass/gunite or vinyl), skimmers, 
      drains, returns and recepictles for pool lights. There is also runs of pipe the connect the pool circulation system that pulls 
      from the various skimmers and drains and pushes it through the returns back to the pool.  A leak can occur in any one of these 
      constiuant parts.  The first thing we do is discern if the leak is occuring in either the main shell of the pool or the plumbing lines by 
      plugging all returns and skimmers and main drain dains then using our water loss detection equipment which can give the water loss 
      to X specificity and compensates for water evaporation and will give out a digital read out of the rate of water loss which can be emailed 
      to you at your request.  If there is water loss with all the drains/skimmers/returns are plugged then there needs to be further investigation 
      by looking at each of the various places pools usually leak until its found.  Then we will pressure test the plumbing lines with a safe psi (under 20)
       and observe if the lines hold pressure or not. And if the plumbing lines can hold pressurized air without pressure loss then that it is a heavy
        indicator than it can hold water without water loss and vice versa.  After that we will have enough information give you an estimate to repair the leak.
          Repairing the leak could take a couple of hours to a couple of weeks depending on the location and the sorounding area of the leak.  Usually only 
          underground plumbing repairs and extensive masonry repairs will be the situations were it could possibly take up to a couple of weeks.</h3>
        </v-container>
    </v-img>
    <v-container>
      <v-timeline align="start" truncate-line="both">
    <v-timeline-item
      dot-color="cyan"
      size="small"
    >
      <template v-slot:opposite>
        <div>
        <h2 :class="`mt-n1 headline font-weight-light mb-4 text-cyan`">
          Step 1
        </h2>
        <div>
         Contact us, get an estimate, book an appointment
        </div>
      </div>
       
      </template>
      <div
          class="pt-1 text-cyan"
          
        >You can get an estimate and then book an appointment in minutes anytime by 
          using our site or you can give us a call at 631-672-8733.</div>
          Get Estimate <v-btn>here</v-btn>
    </v-timeline-item>
    <v-timeline-item
      dot-color="green"
      size="small"
    >
      <template v-slot:opposite>
        <ul class="pt-1 headline text-green">
          <li>We arrive</li>
          <li>We discern if the leak
              is in one of the plumbing lines or from the shell of the pool</li>
              <li>Well plug all returns, drains and skimmers</li>
              <li>Use our <v-btn>equipment</v-btn> to get the exact rate of water loss </li>
              <li>If its in the shell we will
              go though all possible sources one by one.</li>
              <li>We will pressure test the plumbing lines</li>
              <li>At this point we will know the source of yuor leak
                and have the estimate for repair
              </li>
        </ul>
      </template>
      <div>
        <h2 :class="`mt-n1  mb-4 text-green`">
          Step 2
        </h2>
        <div>
          We arrive and then we start detecting the location of leak and give you an estimate for the repair
        </div>
        
      </div>
    </v-timeline-item>
    <v-timeline-item
      dot-color="pink"
      size="small"
    >
      <template v-slot:opposite>
        <div>
        <h2 :class="`mt-n1 headline font-weight-light mb-4 text-pink`">
          Step 3
        </h2>
        <div>
          once you accept the estimate we can get to work
        </div>
      </div>
      </template>
      <div
          class="pt-1 text-pink" 
        >Depending on the time of day and the scope of the repair will 
      determine if we are able to address it on the same day.  If
      we arent we will schedule a date to return and estimated duration 
    of the repair</div>
    </v-timeline-item>
    <v-timeline-item
      dot-color="amber"
      size="small"
    >
      <template v-slot:opposite>
        <div
          :class="`pt-1 headline font-weight-bold text-amber`"
          
        >If the leak repair was on the shell we will repair it an confirm it with our water loss detection
        equipment 
        </div>
      </template>
      <div>
        <h2 :class="`mt-n1 headline font-weight-light mb-4 text-amber`">
          Step 4
        </h2>
        <div>
          We repair the leak
        </div>
      </div>
    </v-timeline-item>
    <v-timeline-item
      dot-color="orange"
      size="small"
    >
      <template v-slot:opposite>
        <div>
        <h2 :class="`mt-n1 headline font-weight-light mb-4 text-orange`">
          Step 5
        </h2>
        <div>
          Follow though and warrantee
        </div>
      </div>
      </template>
      <div
          :class="`pt-1 text-orange`"
          
        >Usually after a shell repair will leave everything plugged for 24 hours and obvserve any water loss 
      or for a plumbing leak leave it running for 24 hours and observe the water loss.  If the water holds at that point 
    we consider the leak fixed.  We also give a 7 day warrantee where you can call us and well come back if your still experiencing water loss.
      If in the unlikely situation we charge you for locating your leak and you accept and we perform the repair and the leak still isnt remedied then
    will refund you what you paid for the leak detection so you dont leave at a financial loss.  And after that 7 days with no reported 
    waterloss we consider the sale final.</div>
    </v-timeline-item>
    
  </v-timeline>
    </v-container>
    <v-contaioner>
      <h1>Frequently asked questins</h1>
      <v-expansion-panels variant="popout" class="my-4">
          <v-expansion-panel
            title="Will it cost less if i get a repair on a opening or other service"
            text="Debris isnt really a problem what is the problem usually is the combination of large puddles of water 
            and the debri making it heavy and difficult by clogging the filter.  And if that water on the cover gets in that pool then 
            that could potentially make clearing the water more difficult.  So if there is no large puddles of water then there is 99% likelihood
            that there will be no extra fee."
          ></v-expansion-panel>
          <v-expansion-panel
            title="Faq"
            text=""
          ></v-expansion-panel>
          <v-expansion-panel
            title="faq2"
            text=""
          ></v-expansion-panel>
        </v-expansion-panels>
    </v-contaioner>
  </v-sheet>   
</template>
<script setup>

</script>