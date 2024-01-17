<template>
    <v-form>
        <v-container class="bg-blue-grey-lighten-2">

        
        <h1 class="d-flex justify-center">Regular Maintenance Agreement Form</h1>
        <v-spacer></v-spacer>
 
        <h3 class="my-3 ">1.) Scope of Services:</h3>

            <h3 class="text-center">
                In this section you choose the scope or what service or services you would like on each maintenance visit.
                Regaurdless of the scope of service you chose we will </h3>
                <ul class="ml-6">
                    <li>check the water chemistry </li>
                    <li>inspect pool pump(s) for proper seal, leaks and proper grounding/wiring</li>
                    <li>inspect filter for leaks and check psi</li>
                    <li>proper function sanitizer feeder (chloronator/salt generator)</li>
                    
                    <li>ensure all unions are free of leaks. We will also ensure all gates are closed before our departure (or left open if customer prefers)</li>
                    <li>Customer portal with a log of your maintenances and services at the push of a button</li>
                    <li>Having pool float and or toys filled up and placed directly in your pool that you order from the online store</li>
                </ul>   pretty buzz luxury sad cupboard actress basic teach begin planet around second 
           
            <h3 class=" mt-4 text-center">
                If you elect to have your pool physically cleaned here is what that would entail 
            </h3>
            <ul class="ml-6 ">
                    <li>Vacuum the floor, slope and stairs of the pool</li>
                    <li>brush walls, water line and stairs</li>
                    <li>
                        check water level an we will drain it if overfilled if a waste line is available.  If it is under filled 
                        we will make a reasonable effort to fill, if water access is avail, and if the pool needs additional water we will notify the customer 
                        of the lack of water.
                    </li>
                    <li>inspect filter for leaks and check psi</li>
                    <li>Clean filter when nessecery</li>
                    <li>
                        check water level and we will drain it if overfilled if a waste line is available.  If it is under filled 
                        we will make a reasonable effort to fill, if water access is avail, and if the pool needs additional water we will notify the customer 
                        of the lack of water.
                    </li>
                    <li>ensure water returns are pointed correctly</li>
                    <li>ensure all unions are free of leaks. We will also ensure all gates are closed before our departure (or left open if customer prefers)</li>
                    <li>Customer portal with a log of your maintenances and services at the push of a button</li>
                    <li>Having pool float and or toys filled up and placed directly in your pool that you order from the online store</li>
                </ul> 
            

        <ul class="ml-6 my-3">Service Extras:
            <li>leaf blowing pool area ~7$</li>
            <li>before and after pictures [avilable in custoemer account] ~5$</li>
            <li>Unattached Spa Maintenance ~20$</li>
        </ul>
            <v-select
            v-model="select_scope"
            label="Select Scope"
            :items="['Vacuuming', 'Vacuum w/o chemicals', 'Vacuum w/ chemicals', 'Only Chemicals']"
            ></v-select>
            <v-select
            v-model="select_extras"
            label="Select Extras"
            :items="['leaf blowing pool area', 'before and after pictures ', ' Unattached Spa Maintenance ', ' Other']"
            ></v-select>
            <v-textarea label="If answered other for Extras.  What else would you like performed? "></v-textarea>
    </v-container>
    <v-container class="bg-blue-grey-lighten-1">
            <ul class="ml-6 my-3">
                <h3>2.) Notices and Communication:  </h3>
                <li>To establish a clear communication protocol for both routine and 
                    emergency situations. Specify how notices and communications will
                    be delivered, whether by email, phone, or another method.</li>
                <li>The service provider will make reasonable efforts to notify the 
                    client in advance of any planned changes to the regular service schedule. 
                    Notifications may be communicated through , [preferred communication method]
                    such as email or phone.</li>
                <li>The customer can enter their preferred communication method below [ email, phone, sms ]</li>
            </ul>   
            <v-select
            v-model="preferred_communication_method"
            label="preferred communication method"
            :items="['email', 'sms', 'phone call']"></v-select>

            <v-textarea 
            v-model="communication_comments"
            label="Do you have any preferences and/or suggestions with how you are communicated to?"></v-textarea>
        
    </v-container>
    <v-container class="bg-blue-grey-lighten-2">
        <h3>3.) Service Schedule: </h3>
        <ul class="ml-6 my-3">Frequency of Service:
            <li>weekly</li>
            <li>bi-weekly</li>
            <li>monthly</li>
        </ul>
        
            <v-select
            v-model="frequency_of_service"
            label="Frequency of Service"
            :items="['weekly', 'bi-weekly', 'monthly']"></v-select>

        <ul class="ml-6 my-3">
            <h4>Inclement Weather: </h4>
            <li>
                In the event of inclement weather conditions, such as heavy rain, storms, or extreme
                temperatures, the service provider reserves the right to reschedule maintenance visits for
                the safety of personnel and the proper execution of services. The client will be promptly
                notified of any rescheduling due to weather conditions.
            </li>
            <li>
                If you choose bi-weekly service we will service your pool at the earliest avialable time after the inclement
                weather has passed.
            </li>
            <li>
                If you choose weelky service do you have any prefenences on how you would like weather delays handled?  As in, would you like 
                to "get it clean as soon as possible but if you cant by sat afternoon just wait till next week or just wait until next week" and in the 
                event of a weather delay i will seek to accomidate this suggestion.  
            </li>
         
        </ul>
        <v-textarea
        v-model="weather_delay_preference"
        label="If you plan to have weekly maintenance , write your preference on how to handle weather make up cleanings for weather delays">
        </v-textarea>
                
    
            <ul class="ml-6 my-3">
                    <h4>Alternative Service Day: </h4> 
            <li>Upon the client's request, and with reasonable notice, the service provider may consider accommodating a temporary change to the regular service day for a specific event or occasion. The client must communicate this request in writing, specifying the desired alternative service day and the duration for the change.
              </li>
            <li>*thurs/fri's are not available days to reschedule on.  </li>
          
        </ul>

        <v-select
        v-model="alternate_service_day_preference"
        label="Alternate Service Day preference"
        :items="['I am likely to ask for a change in service day more than 3 times', 'Maybe once or twice, I dont know', 'I dont forsee wanting to change my day of service']"></v-select>
       
    </v-container>
    <v-container class="bg-blue-grey-lighten-1">
        
            
        <ul class="ml-6 my-3">
            <h3>4.) Duration of Agreement: </h3>
            <li>
                the conventional pool season is from memorial day to labour day but if you have your own schedule that is no problem and you can enter your desired start and stop dates.
                We will give you a suggested onening date to ensure that the pool is ready by that date.  We can accomodate customers desired opening dates if given a rteasonable amount 
                of notice.
                14 weeks
                From May 27, 2024: (memorial day)
                September 2, 2024: (labour day)
            </li>
        </ul>
        <h4 class="text-center">On what date would you like to start and stop service? (If you want to post pone the estimated closing date that is no issue this is just an estimate)</h4>
            <v-date-picker
                v-model="start_date"
                class="mx-auto my-4"
                title="Pool Season Start"
                min="2024-04-27"
                max="2024-10-31"
            ></v-date-picker>
            <v-date-picker
                v-model="end_date"
                class="mx-auto my-4"
                title="Pool Season Finish"
                min="2024-04-27"
                max="2024-10-31"
            ></v-date-picker>
    </v-container>
    <v-container class="bg-blue-grey-lighten-2 ml-6 pa-2 my-3">
        
        <ul class="ml-6 my-9">
            <h3 class="my-2">5.) Fees and Payment Terms: </h3>

            <li>Card on File is nessecery for regular maintenance</li>
            <li>There is a fee for the maintnence of the chosen scope - which can include physical cleaning, equipment inspection, chemical testing, adding chemicals etc</li>
            <li>If something needs to be replaced that is nessecery for the proper function of the pool and is under $50
                the service provider will replace it at the time of service and add the replacement part to the invoice
                of the maintenance.  Such as O-rings, skimmer baskets, etc. The prices of all the replacement parts are 
                listed in the customers online account of "thepoolbuddy.com".  </li>
            <li>when laborious or technical work is requested , say for a repair, which does not fall in the scope of regular maintanence,
                it will be invoiced as a service call, which the rates will be posted in the customer portal for the customers review.  A repair will not commence without an 
                explicit request through their preffered communication method.</li>
            <li>for a service stop that requires non technical work that takes approx 30 min or less only a travel fee will be applied of $35-50 (depending on location).
                A travel fee will alse be applied if the service provider is doing service on either a normal service day or one that was communicated
                and understood, and they do not have access to the pool.</li>
            <li>If the customer chose a plan that does not include chemicals and the customer needs chemicals for operation then the 
                service provider will provide the needed chemicals at the retail price listed in the customer's thepoolbuddy.com online
                portal and the chemicals that were used will be added to the invoice.</li>
            
            <li>Regular maintences will be charged on the following monday if you choose to pay by card.  An invoice will be sent to your prefered communication method and 
                    be available for view on the customers online account.</li>
            <li>You could pay by check but a card on file is still needed.
                If a customer wants to pay by check then they can pay on the first of the month, which will apply to the maintenances of that month.
                If the customers pool needs parts replaced they will be added to the following months invoice or emailed imediatly depending on the customers 
                preference.  If by the 14th,the invoice does not get paid then the card on file will be charged. If the card declines then there will
                be a $20 late fee that will added to the invoice.  Service could be discontinued if service goes unpaid for 30 days.</li>
            
            <li>10% can be saved if you pay up front if pay for the entire season</li>
        </ul>
        <ul class="ml-6 my-9">
                <h3 class="my-2">Fees for Maintenance Visit consists of: </h3>
                <li>The fee for the maintnenance </li>
                <li>Filter Cleaning Fee (~every 45 days)[DE-$20/Cartridge-$35]</li>
                <li>Replacement Parts (O-rings, Skimmer Baskets, etc)[only when needed]</li>
                <li>Supplied Chemicals[if not included in maintenance agreement, needed for operation and supplied by the service provider]</li>
 
        </ul>
            <v-select
                v-model="prefered_payment_method"
                label="What is your prefered payment method"
                :items="['check', 'cash', 'card']"></v-select>
            <v-select
                v-model="check_payment_extra_pref"
                label="If your paying by check how would you like to handle the invoicing of replacement parts / filter cleanings / etc"
                :items="['add it to the following monthly invoice available on the 1rst', 'email me an invoice immidiatly', 'text me an invoice immidiatly']"></v-select>
            <v-select
                v-model="bundled_maintenance_plan"
                label="Are you interested in saving %10 by bundling and prepaying"
                :items="['yes', 'no']"></v-select>
    </v-container>  
        <v-container>

            <ul class="ml-6 my-3">
                <h3>6.) Renewal and Termination: </h3>
                <li>A customer can terminate the service agreement by contacting the service provider through their prefered contact method or the "quit 
                maintenance agreement" button in the customer portal.  There is a $0 fee for canceling membership.</li>
                <li> if you paid by check and you have still have credit in your account and you canceled your membership 
                48 hours before your scheduled maintnenance then you will be refunded on all unused credit in a timely manner ( within 7 days)</li>
               
            </ul>

        <v-checkbox 
        v-model="understand_termination"
        label="I understand"></v-checkbox>
        </v-container>
            
        
        <v-container class="bg-blue-grey-lighten-1">
            <ul class="ml-6 my-3">
                <h3>7.) Responsibilities of Each Party: </h3>
                <li class="">
                If customer has a pool leak then they can not have a plan which includes the supply of chemicals.  A pool that is 
                leaking could dramatically increase the amount of chemicals needed to prevent algae.  If the customer elects for us to locate and 
                address the leak accomadations can be made.
                </li>
                <li>Define the responsibilities of both the service provider and the 
                client. This may include the client's responsibilities for
                maintaining a safe pool environment between visits.</li>
                <li>The responsibility of the customer is to have working equipment outlined in the equipment section 
                which needs to run for at least 7 hours per day and be runniung at the hottest parts of the day(1130-3pm).</li>
                <li>For particular regular maintenance plans that include chemicals with a 
                periodicity of biweekly or weekly the service provider will
                gaurantee clean, clear and sterile water.  Given that the pool equipment is of good working order and
                the settings of the pool equipment do not get changed after the provider sets them.</li>
                <li>
                if there is any lack of performance on the part of the service provider in maintinance the customer needs to  notify the service 
                provider within 24 hours of the cleaning.  When notified the service provider can schedule a return visit to remedy lack of performance
                in a timely manner that is convienient for the customer or the cleaning will be free of charge. </li>
            </ul>
        
            <v-checkbox
            v-model="leak_chemical_understand"
            label="I understand if get a plan with that includes the supply chemicals and my pool gets a leak and i elect to not address the leak then my plan can revert to a plan that does not include the supply chemicals"></v-checkbox>
            <v-checkbox
            v-model="pump_settings_understand_1"
            label="I understand and i will let my pump run on the timer with continous power with the settings set by the service provider"></v-checkbox>
            <v-checkbox
            v-model="pump_settings_understand_2"
            label="I understand and if I change the settings or power supply to the pool equipment and the pool becomes unclear as a result then the cost of 
            getting the pool clear will be on the customer"></v-checkbox>
            <v-textarea
            v-model="responsibility_comments"
            label="Comments"></v-textarea>
        </v-container>
        <v-container class="bg-blue-grey-lighten-2">
            <ul class="ml-6 my-3">
                <h3>8.) Access to Property:</h3>
                <li>Clearly state the procedures for accessing the property, including
                any requirements for the client to provide keys or access codes.</li>
                <li>We will need free access to the pool and also possibly where you store your chemicals if 
                you choose us to use chemicals that you purchase.  If you the gate is normally locked arrangements 
                need to be made.  Here you can write what arrangements are convient for you.</li>
                <li>If we arrive to service and can not access the back yard a $35-50 arrival fee will be charged to the 
                card on file depending on the location of the property.</li>
            </ul>
          
            <v-checkbox
            v-model="access_understand" label="I understand"></v-checkbox>
            <v-checkbox 
            v-model="there_is_access" label="there is free access to my pool and any needed storage containers for chemicals if applicaple"></v-checkbox>
            <v-textarea 
            v-model="access_comments" label="If answered no.  How would you like to handle that?  Leave the key in a designated spot, give us a copy , etc"></v-textarea>
       
        </v-container>
        <v-container class="bg-blue-grey-lighten-1">
            <ul class="ml-6 my-3">
                <h3>9.) Equipment and Supplies:</h3>
                <li>In order for any gaurentee on the pool clarity all pool circulation and
                filtration equipment need to be in good working order. </li>
                <li> The customer needs to have a functioning pool pump that is of sufficient power to accomidate the siize of  my pool.  My pump
                is connected to a functioning timer hooked to continuous power.  Without a pump of sufficient power then my
                pool water wont get sufficient circulation, lack of power to guide floating debris into skimmers and is condusive to algae growth.
        </li>
                <li>The customer needs to have a sanitizer feeder either plumbed in my circulation system or floating in the water</li>
                <li>After backwashing or due to evaporation are situations where the pool will
                need to be filled to ensure proper function.  To do that there need to be 
                a working spigot and a hose of adaquate length.</li>
                <li>The customer needs to have a functioning waste line.  Without a functioning waste line then  
                removing excess water from the pool can be not covered in a routine stop.</li>
                <li>All my skimmers are working.  Without functioning skimmers i understand that plant debris wont 
                naturally be guided into the skimmer baskets and can result in the debris collecting on the surface 
                then falling to the floor of the pool.</li>
            </ul>
            

            <v-checkbox 
            v-model="equipment_understand" label="I understand"></v-checkbox>
            <v-checkbox
            v-model="equipment_is_good" label="All my my pump,filter,sanitizer feeder and  timer are working as they should"></v-checkbox>
            <v-textarea
            v-model="equipment_comments" label="If answered no.  What is not available/working?  If you dont know then write I dont know"></v-textarea>

        </v-container>
        <v-container class="bg-blue-grey-lighten-2">
            <ul class="ml-6 my-3">
                <h3>10.) Liability and Insurance: </h3>
                <li>The service provider, The Pool-Buddy, is a licensed and insured business. Proof of insurance and business 
                license will be furnished on the final maintence contract and upon request</li>
                <h3>Liability and Coverage: </h3>
                <h3>service provider's Insurance Responsibilities:</h3>
                <li> "The service provider maintains general liability insurance to cover any damage or injury that may occur during routine maintenance visits."</li>
                <h3>Client's Insurance Responsibilities:</h3>
                <li>"The client is responsible for maintaining appropriate homeowner's insurance or a separate insurance policy that covers the pool and related structures on the property."</li>
                <li>"Both parties agree to promptly notify each other of any changes in insurance coverage that may affect the terms of this agreement."</li>
            </ul>
            
            <v-checkbox
            v-model="insurance_understand"
             label="I understand"></v-checkbox>
        </v-container>
        

            <v-row no-gutters class="ma-1 pa-1" justify="end">
                <v-btn @click="submit"> Submit </v-btn>
            </v-row>
    </v-form>
</template>
<script setup>
import {useUser} from '@/store/user';
import { useRoute, useRouter } from 'vue-router';
import * as apiService from '@/assets/js/apiService';
import { ref, onMounted  } from 'vue';

const frequency_of_service = ref()
const insurance_understand = ref()
const equipment_comments = ref()
const equipment_understand = ref()
const access_comments = ref()
const equipment_is_good = ref()
const there_is_access = ref()
const responsibility_comments = ref()
const pump_settings_understand_2 = ref()
const access_understand = ref()
const pump_settings_understand_1 = ref()
const leak_chemical_understand = ref()
const understand_termination = ref()
const bundled_maintenance_plan = ref()
const check_payment_extra_pref = ref()
const prefered_payment_method = ref()
const end_date = ref()
const start_date = ref()
const alternate_service_day_preference = ref()
const weather_delay_preference = ref()
const communication_comments = ref()
const preferred_communication_method = ref()
const select_extras = ref()
const select_scope = ref()

const validateForm = () => {
    // Add validation checks for non-null values
    if(!select_scope.value )
    {
        // Alert or handle the validation error
        alert("Please fill in select scope in part 1 before submitting.");
        return false;
    }
    if(!select_extras.value)
    {
        // Alert or handle the validation error
        alert("Please fill in select extras in part 1 before submitting.");
        return false;
    }
    if(!preferred_communication_method.value)
    {
        // Alert or handle the validation error
        alert("Please fill preferred_communication_method before submitting.");
        return false;
    }
    if(!frequency_of_service.value)
    {
        // Alert or handle the validation error
        alert("Please fill in frequency of service before submitting.");
        return false;
    }
    if(!alternate_service_day_preference.value)
    {
        // Alert or handle the validation error
        alert("Please fill alternate_service_day_preference before submitting.");
        return false;
    }
    if(!end_date.value)
    {
        // Alert or handle the validation error
        alert("Please fill in end_date before submitting.");
        return false;
    }
    if(!start_date.value)
    {
        // Alert or handle the validation error
        alert("Please fill start_date before submitting.");
        return false;
    }
    if(!prefered_payment_method.value)
    {
        // Alert or handle the validation error
        alert("Please fill prefered_payment_method before submitting.");
        return false;
    }
    if(!understand_termination.value)
    {
        // Alert or handle the validation error
        alert("Please fill in understand_termination before submitting.");
        return false;
    }
    if(!leak_chemical_understand.value)
    {
        // Alert or handle the validation error
        alert("Please fill in leak_chemical_understand before submitting.");
        return false;
    }
    if(!pump_settings_understand_1.value)
    {
        // Alert or handle the validation error
        alert("Please fill in pump_settings_understand_1 before submitting.");
        return false;
    }
    if(!pump_settings_understand_2.value )
    {
        // Alert or handle the validation error
        alert("Please fill in pump_settings_understand_2 before submitting.");
        return false;
    }

    if(!equipment_is_good.value )
    {
        // Alert or handle the validation error
        alert("Please fill in equipment is good before submitting.");
        return false;
    }
    if(!equipment_understand.value)
    {
        // Alert or handle the validation error
        alert("Please fill in equipment_understand before submitting.");
        return false;
    }
    
    if(!access_understand.value)
    {
        // Alert or handle the validation error
        alert("Please fill in access_understand before submitting.");
        return false;
    }
    if(!there_is_access.value)
    {
        // Alert or handle the validation error
        alert("Please fill in there_is_access before submitting.");
        return false;
    }
   
    if(!weather_delay_preference.value)
    {
        // Alert or handle the validation error
        alert("Please fill weather_delay_preference before submitting.");
        return false;
    }
   
    if(!insurance_understand.value)
    {
        // Alert or handle the validation error
        alert("Please fill in insurance understand before submitting.");
        return false;
    }
  
};

const submit = () => {
    
    
if(validateForm()){
    alert(validateForm())
}
const form = {
    frequency_of_service : frequency_of_service.value,
    insurance_understand : insurance_understand.value,
    equipment_comments  : equipment_comments.value,
    equipment_understand : equipment_understand.value,
    access_comments : access_comments.value,
    equipment_is_good : equipment_is_good.value,
    there_is_access : there_is_access.value,
    responsibility_comments : responsibility_comments.value,
    pump_settings_understand_2 : pump_settings_understand_2.value,
    access_understand : access_understand.value,
    pump_settings_understand_1 : pump_settings_understand_1.value,
    leak_chemical_understand : leak_chemical_understand.value,
    understand_termination : understand_termination.value,
    bundled_maintenance_plan : bundled_maintenance_plan.value,
    check_payment_extra_pref : check_payment_extra_pref.value,
    prefered_payment_method : prefered_payment_method.value,
    end_date : end_date.value,
    start_date : start_date.value,
    alternate_service_day_preference : alternate_service_day_preference.value,
    weather_delay_preference : weather_delay_preference.value,
    communication_comments : communication_comments.value,
    preferred_communication_method : preferred_communication_method.value,
    select_extras: select_extras.value,
    select_scope: select_scope.value,
    email: store.email,
    phone: store.profile.phone
}

const response = apiService.createMaintenanceAgreement(form.value)

}
</script>