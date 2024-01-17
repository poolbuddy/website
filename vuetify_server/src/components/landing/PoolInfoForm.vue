<template>
  
     <v-form ref="form" >
       
              <v-card  max-width="900" class="d-flex mx-auto justify-center align-center flex-column">
                <v-container>
                  <h1 class="text-center">What is the type and size of pool?</h1>
                  <br>
                <v-row no-gutter justify="center">
                <v-btn-toggle          
                v-model="pool_type"
                divided
                required
              >
                <v-btn value="aboveGround"><h5>Above Gound</h5></v-btn>
                <v-btn value="inGround"><h5>InGound</h5></v-btn>
               
              </v-btn-toggle>
                </v-row>
              </v-container>
                
                  <v-radio-group
                v-show="pool_type==='aboveGround'"
                v-model="above_shape"
                column
              >
                <v-radio
                  label="Circular"
                  value="circular"
                ></v-radio>
                <v-radio
                  label="Oval"
                  value="oval"
                ></v-radio>
              </v-radio-group>
          
              <v-radio-group 
                v-show="pool_type==='aboveGround'"
                v-model="above_size"
                inline
              >
                <v-radio
                  v-show="above_shape==='oval'"
                  label="12' x 24'"
                  value="12x24"
                ></v-radio>
                <v-radio
                  v-show="above_shape==='oval'"
                  label="15' x 30'"
                  value="15x30"
                ></v-radio>
                <v-radio
                  v-show="above_shape==='oval'"
                  label="18' x 33'"
                  value="18x33"
                ></v-radio>
                <v-radio
                  v-show="above_shape==='circular'"
                  label="12'"
                  value="12"
                ></v-radio>
                <v-radio
                  v-show="above_shape==='circular'"
                  label="15'"
                  value="15"
                ></v-radio>
                <v-radio
                  v-show="above_shape==='circular'"
                  label="18'"
                  value="18"
                ></v-radio>
                <v-radio
                  v-show="above_shape==='circular'"
                  label="24'"
                  value="24"
                ></v-radio>
              </v-radio-group>
           
                
           
              
              
              <v-radio-group
                v-show="pool_type==='inGround'"
                v-model="inground_shape"
                column
              >
                <v-radio
                  label="Rectangular"
                  value="rectangular"
                ></v-radio>
                <v-radio
                  label="Irregular"
                  value="irregular"
                ></v-radio>
                <v-radio
                  label="L shaped"
                  value="l_shaped"
                ></v-radio>
              </v-radio-group>
              
              <v-radio-group
              v-show="pool_type==='inGround'"
                v-model="inground_size"
                inline
              >
              <v-radio
                  v-show="inground_shape==='rectangular' || inground_shape==='irregular'"
                  label="(smaller than) > 18' x 36'"
                  value=">18x36"
                ></v-radio>
                <v-radio
                  v-show="inground_shape==='rectangular' || inground_shape==='irregular'"
                  label="18' x 36'"
                  value="18x36"
                ></v-radio>
                <v-radio
                  v-show="inground_shape==='rectangular' || inground_shape==='irregular'"
                  label="20' x 40'"
                  value="20x40"
                ></v-radio>
              </v-radio-group>
              <br>
              <v-radio-group
                v-show="pool_type==='inGround' && inground_shape==='l_shaped'"
                v-model="inground_size"
                label="Pick the dimensions that resemble your pool"
                inline
              >
              <v-radio
                  v-show="inground_shape==='l_shaped'"
                  label="Small: 16' x 24' x 38'"
                  value="16x24x38"
                ></v-radio>
                <v-radio
                  v-show="inground_shape==='l_shaped'"
                  label="Medium: 18' x 26' x 41'"
                  value="18x26x41"
                ></v-radio>
                <v-radio
                  v-show="inground_shape==='l_shaped'"
                  label="Large: 20' x 30' x 44'"
                  value="20x30x44"
                ></v-radio>
              </v-radio-group>
            
              </v-card>

              <v-card
                class="d-flex mx-auto justify-center align-center flex-column"
                max-width="900"
            >
              <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                   Filter Type
                </h2>

                <v-chip-group
                    v-model="filter_type"
                    column
                    required
                >
                    <v-chip
                    filter
                    value="de"
                    variant="outlined"
                    >
                    DE
                    </v-chip>
                    <v-chip
                    filter
                    value="cartridge"
                    variant="outlined"
                    >
                    cartridge
                    </v-chip>
                    <v-chip
                    filter
                    value="sand"
                    variant="outlined"
                    >
                    sand
                    </v-chip>
                    
                </v-chip-group>
                </v-card-text>
                <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                   Sanitizer Feeder Type
                </h2>

                <v-chip-group
                    v-model="sanitizer_type"
                    column
                    required
                >
                    <v-chip
                    filter
                    value="salt"
                    variant="outlined"
                    >
                    Salt Generator
                    </v-chip>
                    <v-chip
                    filter
                    value="chloronater"
                    variant="outlined"
                    >
                    Chloronator
                    </v-chip>
                    <v-chip
                    filter
                    value="other"
                    variant="outlined"
                    >
                    other
                    </v-chip>
                    <v-chip
                    filter
                    value="none"
                    variant="outlined"
                    >
                    none
                    </v-chip>
                    
                </v-chip-group>
                </v-card-text>
                <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                   How many pumps do you have
                </h2>

                <v-chip-group
                    v-model="pump_num"
                    column
                    required
                >
                  <v-chip
                    filter
                    variant="outlined"
                    value=0
                    >
                    0
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=1
                    >
                    1
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=2
                    >
                    2
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=3
                    >
                    3
                    </v-chip>
                    <v-chip
                    filter
                    value=4
                    variant="outlined"
                    >
                    3+
                    </v-chip>
                    
                </v-chip-group>
                </v-card-text>
                <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                   Do you also have 
                </h2>

                <v-chip-group
                    v-model="pool_extra_equipment"
                    column
                    required
                    multiple
                >
                    
                    <v-chip
                    filter
                    value="heater"
                    variant="outlined"
                    >
                    heater
                    </v-chip>
                    <v-chip
                    filter
                    value="solar_cover"
                    variant="outlined"
                    >
                    solar cover
                    </v-chip>
                    <v-chip
                    filter
                    value="safety_fence"
                    variant="outlined"
                    >
                    Safety Fence
                    </v-chip>
                    <v-chip
                    filter
                    value="mesh_cover"
                    variant="outlined"
                    >
                    Safety Cover (Mesh)
                    </v-chip>
                    <v-chip
                    filter
                    value="hard_cover"
                    variant="outlined"
                    >
                    Safety Cover (Solid)
                    </v-chip>
                    <v-chip
                    filter
                    value="polaris"
                    variant="outlined"
                    >
                    Polaris Line
                    </v-chip>
                   
                </v-chip-group>
                </v-card-text>
                <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                   Do you also have 
                </h2>

                <v-chip-group
                    v-model="pool_conditions"
                    column
                    required
                    multiple
                >
                    <v-chip
                    filter
                    value="waterfall"
                    variant="outlined"
                    >
                    Waterfall/Fountain
                    </v-chip>
                    <v-chip
                    filter
                    value="retaining_wall"
                    variant="outlined"
                    >
                    Retaining wall 
                    </v-chip>
                    <v-chip
                    filter
                    value="trees"
                    variant="outlined"
                    >
                    Trees directly over pool
                    </v-chip>
                    
                    
                </v-chip-group>
                </v-card-text>
                
                </v-card>
                <v-card
                class="d-flex mx-auto justify-center align-center flex-column"
                max-width="900"
            >
               

                <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                   How Many skimmers  do you have?
                </h2>

                <v-chip-group
                    v-model="skimmer_num"
                    column
                    required
                >
                  <v-chip
                    filter
                    variant="outlined"
                    value=0
                    >
                    0
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=1
                    >
                    1
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=2
                    >
                    2
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=3
                    >
                    3
                    </v-chip>
                    <v-chip
                    filter
                    value=4
                    variant="outlined"
                    >
                    3+
                    </v-chip>
              <hr>
            </v-chip-group>
            </v-card-text>
            
                <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                   How about returns
                </h2>

                <v-chip-group
                    v-model=" return_num"
                    column
                    required
                >
               
                    <v-chip
                    filter
                    variant="outlined"
                    value=1
                    >
                    1
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=2
                    >
                    2
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=3
                    >
                    3
                    </v-chip>
                    <v-chip
                    filter
                    value=4
                    variant="outlined"
                    >
                    4
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=5
                    >
                    5
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=6
                    >
                    6
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=7
                    >
                    6+
                    </v-chip>
                  
              <hr>
            </v-chip-group>
            </v-card-text>
            <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                  And Main Drain(s)
                </h2>

                <v-chip-group
                    v-model="main_drain_num"
                    column
                    required
                >
                <v-chip
                    filter
                    variant="outlined"
                    value=0
                    >
                    0
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=1
                    >
                    1
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=2
                    >
                    2
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=3
                    >
                    3
                    </v-chip>
                    <v-chip
                    filter
                    value=4
                    variant="outlined"
                    >
                    3+
                    </v-chip>
                    
              <hr>
            </v-chip-group>
            </v-card-text>
            <v-card-text>
                <h2 class="text-h6 text-center mb-2">
                  And Floor return(s)
                </h2>

                <v-chip-group
                    v-model="floor_return_num"
                    column
                    :rules="[v => !!v || 'Item is required']"
                    required
                >
                    <v-chip
                    filter
                    variant="outlined"
                    value=0
                    >
                    0
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=1
                    >
                    1
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=2
                    >
                    2
                    </v-chip>
                    <v-chip
                    filter
                    variant="outlined"
                    value=3
                    >
                    3
                    </v-chip>
                    <v-chip
                    filter
                    value=4
                    variant="outlined"
                    >
                    3+
                    </v-chip>
                    
              <hr>
              </v-chip-group>
              <h2 class="text-h6 text-center mb-2">Is everything in working order?  If not let us know here </h2>
              <v-textarea v-model="comments" label="One skimmer doesnt work, main drain is plugged etc."></v-textarea>
              </v-card-text>
           
           
              </v-card>
              <v-container>
              <h1>address</h1>
              <v-text-field required :rules="addressRules" v-model="street" label="Address" prepend-icon="mdi-maps"></v-text-field>
              <v-text-field required :rules="cityRules" v-model="town" label="city" prepend-icon="mdi-maps"></v-text-field>
              <v-text-field :counter="5" required :rules="zipCodeRules" v-model="zipcode" label="zip" prepend-icon="mdi-maps"></v-text-field>
              <h1>Name</h1>
              <v-text-field required :rules="cityRules" v-model="name" label="Name" prepend-icon="mdi-maps"></v-text-field>
              <h1>Phone Number</h1>
              <v-row no-gutters justify="center">
              <v-text-field :counter="10" required type="phone" :rules="phoneRules" v-model="phone" label="phone Number" prepend-icon="mdi-phone"></v-text-field>
              </v-row> 
              </v-container>
              <v-container>
              <v-text-field type="email" :rules="emailRules" v-model="email" label="Email" prepend-icon="mdi-email"></v-text-field>
              <v-row no-gutters>
                <v-text-field counter :rules="passwordRules" :type=" showPassword ? 'input':'password' "  v-model="password" label="Password" prepend-icon="mdi-lock"></v-text-field>
              <v-btn  @click="toggleShowPassword">
                {{ showPassword ? 'Hide Password' : 'Show Password' }}
              </v-btn>
              </v-row>
             
              <v-row no-gutters> 

                  <v-btn @click="submitForm">
                     sub
                  </v-btn>  
                  
              </v-row>
   
   
              </v-container>
             
      
              
              <v-row no-gutters justify="center"  v-if="errors.length" class="bg-surface">
                <p v-for="(error, i) in errors" :key="i">{{ error }}</p>
              </v-row>
              
              
              <v-alert
        v-for="(error, index) in errors"
        :key="index"
        :color="error.type === 'success' ? 'success' : 'error'"
        :icon="error.type === 'success' ? '$success' : '$error'"
        :title="error.title"
        :text="error.text"
      ></v-alert>
              
        </v-form>

</template>
<script setup>
import axios from 'axios';
import { ref, reactive, defineProps, withDefaults, onMounted } from 'vue';
import { format } from 'date-fns';
import * as apiService from '@/assets/js/apiService';
import { useRouter} from 'vue-router';

const router = useRouter()
// Props
const form = ref(null);
// State

    const name = ref('');
    const phone = ref('');
    const pool_type = ref(null);
    const above_shape = ref('');
    const inground_shape = ref('');
    const above_size = ref('');
    const inground_size = ref('');
    const filter_type = ref(null);
    const sanitizer_type = ref(null);
    const pump_num = ref(null);
    const pool_conditions = ref([]);
    const pool_extra_equipment = ref([]);
    const skimmer_num = ref(null);
    const main_drain_num = ref(null);
    const return_num = ref(null);
    const floor_return_num = ref(null);
    const comments = ref(null);
    const street = ref('');
    const town = ref('');
    const zipcode = ref('');
    const email = ref('');
    const password = ref('');
    const showPassword = ref(false);
    const errors = ref([]);

    const toggleShowPassword = () => {
     showPassword.value = !showPassword.value;
};

   const addressRules = [
      value => !!value || 'Address is required',
      value => /\d/.test(value) || 'Address must contain at least one number',
      value => /\d\s\w/.test(value) || 'Address must contain at least one number, a space, and then text',
    ]
    const phoneRules = [
      value => !!value || 'Phone number  is required',
      value => /^\d{10}$/.test(value) || 'Phone number needs to be 10 digits',
    ]
    const cityRules = [
      value => !!value || 'Your Town is required',
    ]
    const passwordRules = [
      value => !!value || 'Password is required',
      value => (value && value.length >= 8) || 'Password must be at least 8 characters long',
      value => /[A-Z]/.test(value) || 'Password must contain at least one uppercase letter',
      value => /[!@#$%^&*(),.?":{}|<>]/.test(value) || 'Password must contain at least one special character (!@#$%^&*(),.?":{}|<>)',
    ]
    const zipCodeRules = [
      value => !!value || 'Zip Code is required',
      value => /^\d{5}$/.test(value) || 'Zip Code must be exactly 5 digits',
    ]
    const emailRules = [
      value => {
        if (value) return true

        return 'E-mail is requred.'
      },
      value => {
        if (/.+@.+\..+/.test(value)) return true

        return 'E-mail must be valid.'
      }
    ]

function isNumber(value) {
  return typeof value === 'number' && !isNaN(value);
}
 const submitForm = async () => {
            errors.value = []
           
       
        if (pool_type.value === null) {
       
          errors.value.push("Put pool type")
          return;
        } else if (inground_shape.value.length === 0 && above_shape.value.length === 0){
          errors.value.push("Put pool shape")
          return;
        } else if (above_size.value.length === 0 && inground_size.value.length === 0 ){
          errors.value.push("Put pool size")
          return;
        }
        if (filter_type.value === null) {
          errors.value.push("Put filter type")
          return;
        } else if(sanitizer_type.value === null){
          errors.value.push("Put sanitizer type")
          return;
        }
        else if(pump_num.value === null){
          errors.value.push("Put number of pumps")
          return;
        }
        else if(skimmer_num.value === null){
          errors.value.push("Put skimmer num")
          return;
        }
        else if(return_num.value === null){
          errors.value.push("Put return num")
          return;
        }
        else if(main_drain_num.value === null){
          errors.value.push("Put main drain")
          return;
        }
        else if(floor_return_num.value === null){
          errors.value.push("Put floor return ")
          return;
        }
        const { valid } = await form.value.validate()
       
        if (!valid) {
        return;
        }
        const emailData = {
              email: email.value,
        }
        const userData = {
              email: email.value,
              password: password.value,   
            }
            const addressData = {
              street : street.value,
              town : town.value, 
              zipcode : zipcode.value 
            }
            const pool_data = {
              pool_type : pool_type.value,
              above_shape : above_shape.value,
              pool_shape :inground_shape.value,
              pool_size : above_size.value,
              inground_size : inground_size.value,
              filter_type : filter_type.value,
              sanitizer_type : sanitizer_type.value,
              pump_num : pump_num.value,
              pool_conditions : pool_conditions.value,
              pool_extra_equipment : pool_extra_equipment.value,
              skimmer_num : skimmer_num.value,
              main_drain_num : main_drain_num.value,
              return_num : return_num.value,
              floor_return_num : floor_return_num.value,
              comments : comments.value
            }

            
     
       
        try {        
            const createPoolResponse = await apiService.createPool(pool_data)
            const createAddressResponse = await apiService.createAddress(addressData)
            const createProductListResponse = await apiService.createProductList()
            const date = new Date();
            const formattedDate = format(date, 'yyyy-MM-dd');
            
            alert(formattedDate)
            
           
            if(isNumber(createAddressResponse.data.id) & isNumber(createPoolResponse.data.id)& isNumber(createProductListResponse.data.id)){
              
              const profile_data = {
                                  email: email.value,
                                  name: name.value,
                                  phone: phone.value,
                                  pool_data: createPoolResponse.data.id,
                                  last_login_array: [formattedDate],
                                  address: createAddressResponse.data.id,
                                  product_list: createProductListResponse.data.id
                                }
            const createProfileResponse = await apiService.createCustomerProfile(profile_data)
            if(createProfileResponse){
              const createAuthResponse = await apiService.createAuthUser(userData)

              if(createAuthResponse){
                router.push({ name: 'login' });  
              }
              
            }
                             
            }
        
          }
          catch (error) {
            errors.push('Error:', error);
            alert(JSON.stringify(error))
          }

 
          
          
   
       
       
      }





</script>