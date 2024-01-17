<template>
  <div>
    <v-card-title class="d-flex d-md-none">
      Dash
    </v-card-title>
    <v-toolbar
      color="secondary"
    >
      
      <v-tabs
        v-model="tab"
        direction='horizontal'
        color="primary"
        class="d-flex d-md-none"
        next-icon="mdi-arrow-right-bold-box-outline"
        prev-icon="mdi-arrow-left-bold-box-outline"
        show-arrows
      >
      <v-tab v-for="(item, index) in tabItems" :key="index" :value="item.value">
      <v-icon>{{ item.icon }}</v-icon>
      {{ item.label }}
    </v-tab>
      </v-tabs>
      <h1 class="d-none d-md-flex">Customer Profile</h1>
    </v-toolbar>

    <div class="d-flex flex-row">
      <v-tabs
        v-model="tab"
        direction='vertical'
        center-active
        color="primary"
        class = "d-none d-md-flex"
      >
      <v-tab v-for="(item, index) in tabItems" :key="index" :value="item.value">
      <v-icon>{{ item.icon }}</v-icon>
      {{ item.label }}
     </v-tab>
      </v-tabs>
      <v-window v-model="tab" class="mx-auto w-100">

        <v-window-item value="1">
        
            <v-row  justify="center" no-gutters>
              <v-col class="d-inline-flex flex-column pa-3 ma-3" >
                <v-btn class="mb-9" :to="{name:'maintenance_agreement'}">Make Regular Maintenance Aggreement</v-btn>
                <v-btn class="mb-9" :to="{name:'booking'}">Book Appointment</v-btn>
                <v-btn class="mb-9" :to="{name:'estimate'}">Get Estimate</v-btn>
                <v-btn class="mb-9" :to="{name:'schedule'}">Schedule Call</v-btn>
                <v-btn class="mb-9" :to="{name:'profile-update'}">Edit Profile</v-btn>
              </v-col>
             
            </v-row>
          
        </v-window-item>

        <v-window-item  value="2">
          
            <h3 class="my-3 text-center">Personal Information</h3>
            <v-row  justify="start" no-gutters>
              <v-col class="pa-3" md="6" cols="12">
                name -   {{ store.profile.name }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                phone -   {{ store.profile.phone }}
              </v-col>
            
               <v-col class="pa-3" md="6" cols="12">
                email - {{ store.profile.email }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                store credit - {{ store.profile.store_credit }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                last login - {{ store.profile.last_login_array[ store.profile.last_login_array.length - 1 ] }}
              </v-col>
            </v-row>
            <h3 class="my-3 text-center">Address</h3>
            <v-row  justify="start" no-gutters>
              <v-col class="pa-3" md="6" cols="12">
                street - {{ store.profile.address.street }}
              </v-col >
              <v-col class="pa-3" md="6" cols="12">
                town - {{ store.profile.address.town }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                zipcode - {{ store.profile.address.zipcode }}
              </v-col>
            </v-row>
      <h3 class="my-3 text-center">Pool Information</h3>
           
            <v-row  justify="start" no-gutters>
              <v-col class="pa-3" md="6" cols="12">
                type :  {{ store.profile.pool_data.pool_type }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                shape : {{ store.profile.pool_data.above_shape }}{{ store.profile.pool_data.inground_shape }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                size : {{ store.profile.pool_data.above_size }}{{ store.profile.pool_data.inground_size }}
              </v-col>
           
              <v-col class="pa-3" md="6" cols="12">
                filter : {{ store.profile.pool_data.filter_type }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                sanitizer-feeder : {{ store.profile.pool_data.sanitizer_type }}
              </v-col>
           </v-row>
           <v-row no-gutters>
               <v-col class="pa-3" md="3" cols="6">
                pump(s) : {{ store.profile.pool_data.pump_num }}
              </v-col>
              <v-col class="pa-3" md="3" cols="6">
                skimmer(s) : {{ store.profile.pool_data.skimmer_num }}
              </v-col>
          
              <v-col class="pa-3" md="3" cols="6" >
                main-drain(s) : {{ store.profile.pool_data.main_drain_num }}
              </v-col>
              <v-col class="pa-3" md="3" cols="6">
                return(s) :{{ store.profile.pool_data.return_num }}
              </v-col>
            </v-row>
            <v-row no-gutters> 
            <v-col class="pa-3" cols="12">pool equipment : {{ store.profile.pool_data.pool_extra_equipment }}</v-col>
            <v-col class="pa-3" cols="12">pool conditions : {{ store.profile.pool_data.pool_conditions }}</v-col>
            <v-col class="pa-3" cols="12">comments : {{ store.profile.pool_data.comments }}</v-col>
            </v-row>
            <h3 class="my-3 text-center">Mainenance Aggreement </h3>
            <v-row v-if="store.profile.hasMembership" class="" no-gutters>
           
              <v-col class="pa-3" md="6" cols="12">
                chosen plan:  {{ store.profile.maintenance_aggreement.chosen_plan }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
               service period:  {{ store.profile.maintenance_aggreement.periodicity }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                day of service:  {{ store.profile.maintenance_aggreement.day_of_service }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                includes chemicals:  {{ store.profile.maintenance_aggreement.includes_chemicals? 'Yes':'No' }}
              </v-col>
              <v-col class="pa-3" md="6" cols="12">
                date created:  {{ store.profile.maintenance_aggreement.date_created }}
              </v-col>
              <v-col class="pa-3" cols="12">
                maintenance extra(s):  {{ store.profile.maintenance_aggreement.maintenance_extra_list }}
              </v-col>
             
            </v-row>
            <h4 v-if="!store.profile.hasMembership" class="d-flex justify-center">No Current Maintenance Agreement</h4>
        </v-window-item>


        <v-window-item value="3">
          <v-data-table-virtual
            :headers="headers.invoices"
            :items="invoiceList"
            height="400"
            item-value="id"
          ></v-data-table-virtual>
      
        </v-window-item>


        <v-window-item value="4">
       
          <v-data-table-virtual
            :headers="headers.estimates"
            :items="estimateList"
            height="400"
            item-value="id"
          ></v-data-table-virtual>
       
        </v-window-item>

        
        <v-window-item value="5">

          <v-container>

            <v-data-iterator :items-per-page="itemsPerPage" :items="maintenanceList">
                  <template v-slot:header="{ page, pageCount, prevPage, nextPage }">
                    <v-toolbar class="bg-surface mb-2">
                        <v-row no-gutters justify="space-between">
            <v-btn class="me-8" variant="text" @click="onClickSeeAll">
              <span class="text-decoration-underline text-none">See all</span>
            </v-btn>
            <h1 class="text-center text-h4 lex">Regular Maintenances</h1>
            <div class="d-inline-flex ma-1">
              <v-btn
                :disabled="page === 1"
                icon="mdi-arrow-left"
                size="small"
                variant="tonal"
                class="me-2"
                @click="prevPage"
              ></v-btn>

              <v-btn
              :disabled="page === pageCount"
                icon="mdi-arrow-right"
                size="small"
                variant="tonal"
                @click="nextPage"
              ></v-btn>
            </div>
          </v-row>
        
                  
                  </v-toolbar>
                </template>

                <template v-slot:default="{ items }">
                  <v-row>
                    <v-col
                     v-for="(item, i) in items"
                    :key="i"
                    >
                    <v-card>
                      <template v-slot:title>
                        <h1 class="text-h4 d-flex justify-center"> {{item.raw.date_performed}}</h1>
                      </template>
                      <template v-slot:subtitle>
                        <h4 class="text-h9"></h4>
                      </template>
                      <template v-slot:prepend>
                        <v-btn icon="mdi-camera" color="primary" :to="{ name:'image', params: { src: item.raw.before_picture }}">before</v-btn>
                      </template>
                      <template v-slot:append>
                        <v-btn icon="mdi-camera" color="success" :to="{ name:'image', params: { src: item.raw.after_picture }}">after</v-btn>
                      </template>
                      <v-card-text>
                        <v-col>
                          <div v-if="item.raw.weather_delay">
                           Sorry there was a weather delay
                          </div>
                          
                          <div>
                            water level : 
                          </div>
                          <div>
                            extras : 
                            <v-list>
                              <v-list-item v-for="(item, index) in item.raw.optional_additions" :key="index">
                              {{ item.name }}
                              </v-list-item>
                            </v-list>
                          </div>
                          <div>
                            chemicals used : 
                            <v-list>
                              <v-list-item v-for="(item, index) in item.raw.chemical_consumption" :key="index">
                              {{ item.chemical }}
                              {{ item.amount }}
                              {{ item.customers_chemicals }}
                              {{ item.cost }}
                              </v-list-item>
                            </v-list>
                          </div>
                          <div>
                            notes : 
                          </div>
                        </v-col>
                      </v-card-text>
                    </v-card>

                    </v-col>
                  </v-row>
                 
                </template>

                <template v-slot:footer="{ page, pageCount }">
                    <v-footer
                      color="surface-variant"
                      class="justify-space-between text-body-2 mt-4"
                    >

                      <div>
                        Page {{ page }} of {{ pageCount }}
                      </div>
                    </v-footer>
                </template>
            </v-data-iterator>
         
          </v-container>
          
        </v-window-item>

        <v-window-item value="6">

          <h3 class="text-center bg-surface">Store Purchases</h3>
          <v-data-table-virtual
            :headers="headers.product"
            :items="product_list.product_list"
            height="400"
            item-value="id"
          ></v-data-table-virtual>
        
        </v-window-item>
     
        <v-window-item value="7">

          <h3 class="text-center bg-surface">Appointments</h3>
          <v-data-table-virtual
            :headers="headers.appointments"
            :items="appointmentList"
            height="400"
            item-value="id"
          ></v-data-table-virtual>
          
        </v-window-item>

        <v-window-item value="8">
        
          <h3 class="text-center bg-surface">Scheduled Calls</h3>
          <v-data-table-virtual
              :headers="headers.callbacks"
              :items="callbackList"
              height="400"
              item-value="id"
            >
          </v-data-table-virtual>
        
        </v-window-item>

      </v-window>
    </div>
 
  </div>
</template>

<script setup>
import { useUser } from '@/store/user';
import { ref, onMounted, onBeforeUnmount, watchEffect  } from 'vue';
import * as apiService from '@/assets/js/apiService';

const itemsPerPage = ref(4);
const tab = ref('1');
const list = ref([]);
const store = useUser();
const isVertical = ref(true);



const tabItems = [
  { value: '1', icon: 'mdi-account', label: 'Customer Actions' },
  { value: '2', icon: 'mdi-lock', label: 'Personal Information' },
  { value: '3', icon: 'mdi-access-point', label: 'Invoices' },
  { value: '4', icon: 'mdi-account', label: 'Estimates' },
  { value: '5', icon: 'mdi-lock', label: 'Regular Maintenance' },
  { value: '6', icon: 'mdi-access-point', label: 'Orders/Purchases' },
  { value: '7', icon: 'mdi-lock', label: 'Appointments' },
  { value: '8', icon: 'mdi-access-point', label: 'Scheduled Calls' }
]

const headers = {
  invoices: [
    { title: 'Service(s)', align: 'start', key: 'service_list' },
    { title: 'Date Performed', align: 'end', key: 'date_of_service' },
    { title: 'Recieved by', align: 'end', key: 'received_by' },
    { title: 'Invoice Number', align: 'end', key: 'qb_invoice_number' },
    { title: '$', align: 'end', key: 'charge' }
  ],
  estimates: [
    { title: 'Date req', align: 'start', key: 'date_sent' },
    { title: 'Date given', align: 'end', key: 'date_created' },
    { title: 'Service(s)', align: 'end', key: 'services_of_interest' },
    { title: 'Max Price', align: 'end', key: 'min_price' },
    { title: 'Min Price', align: 'end', key: 'max_price' }
  ],
  appointments: [
    { title: 'Service(s)', align: 'start', key: 'services_of_interest' },
    { title: 'requested at', align: 'end', key: 'date_created' },
    { title: 'appt_flexibility', align: 'end', key: 'appt_flexibility' },
    { title: 'Urgency', align: 'end', key: 'urgency' },
    { title: 'has_attached_estimate', align: 'end', key: 'has_attached_estimate' },
    { title: 'someone_willB_home', align: 'end', key: 'someone_willB_home' },
    { title: 'requests_a_time_of_day', align: 'end', key: 'requests_a_time_of_day' },
    { title: 'confirmed_date', align: 'end', key: 'confirmed_date' },

  ],
  product: [
    { title: 'product', align: 'start', key: 'product.name' },
    { title: 'price', align: 'start', key: 'product.price' },
    { title: 'quantity', align: 'end', key: 'quantity' },
    { title: 'payment method', align: 'end', key: 'payment_method' },
    { title: 'paid', align: 'end', key: 'paid' },
    { title: 'delivery type', align: 'end', key: 'delivery_type' },
    { title: 'date purchased', align: 'end', key: 'delivered' },
    { title: 'returned', align: 'end', key: 'returned' }
  ],
  
  callbacks: [
    { title: 'Requested Date', align: 'start', key: 'requested_date_of_call' },
    { title: 'time_of_day', align: 'end', key: 'time_of_day' },
    { title: 'Asap', align: 'end', key: 'call_asap' },
    { title: 'confirmed', align: 'start', key: 'confirmed' },
    { title: 'confirm_text', align: 'end', key: 'confirm_text' },
    { title: 'services_of_interest', align: 'end', key: 'services_of_interest' }

  ],
};


const product_list = ref([]);
const invoiceList = ref([]);
const appointmentList = ref([]);
const callbackList = ref([]);
const maintenanceList = ref([]);
const estimateList = ref([]);


const fetchProductList = async () => {
  try {
    const response = await apiService.fetchCustomersProductList(store.profile.product_list.id);
    product_list.value = response.data;
  } catch (error) {
    console.error('Error fetching product list:', error);
  }
};

const fetchInvoices = async () => {
  try {
    const response = await apiService.fetchInvoices(store.email);
    invoiceList.value = response.data;
  } catch (error) {
    console.error('Error fetching invoices:', error);
  }
};

const fetchAppointments = async () => {
  try {
    const response = await apiService.fetchAppointments(store.email);
    appointmentList.value = response.data;
  } catch (error) {
    console.error('Error fetching appointments:', error);
  }
};

const fetchCallbacks = async () => {
  try {
    const response = await apiService.fetchCallBacks(store.email);
    callbackList.value = response.data;
  } catch (error) {
    console.error('Error fetching callbacks:', error);
  }
};

const fetchMaintenances = async () => {
  try {
    const response = await apiService.fetchMaintenances(store.email);
    maintenanceList.value = response.data;
  } catch (error) {
    console.error('Error fetching maintenances:', error);
  }
};

const fetchEstimates = async () => {
  try {
    const response = await apiService.fetchEstimates(store.email);
    estimateList.value = response.data;
  } catch (error) {
    console.error('Error fetching estimates:', error);
  }
};

// Watch for changes in reactive variables and fetch data when needed
watchEffect(() => {
  fetchProductList();
  fetchInvoices();
  fetchAppointments();
  fetchCallbacks();
  fetchMaintenances();
  fetchEstimates();
});

onMounted(() => {
  // Initial fetch on component mount
  fetchProductList();
  fetchInvoices();
  fetchAppointments();
  fetchCallbacks();
  fetchMaintenances();
  fetchEstimates();
});

</script>
