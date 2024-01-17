import axios from 'axios';

const apiBaseUrl = process.env.VUE_APP_API_DEV_URL ;


// ----------------------------------------------------------------[AuthUser]
export const createAuthUser = (userData) => {
  return axios.post(`/auth/users/`, userData)
}

export const fetchLogin = (loginData) => {
  return axios.post(`/auth/token/login/`, loginData)
}
// ----------------------------------------------------------------[customer_profile]

export const createCustomerProfile = (profileData) => {
  return axios.post(`/info/customer-profile/`, profileData);
};

export const createPool = (poolData) => {
  return axios.post(`/info/pool/`, poolData);
};

export const createAddress = (addressData) => {
  return axios.post(`/info/address/`, addressData);
};

export const fetchCustomerProfile = (email) => {
  return axios.get(`/info/customer-profile/?email=${email}`);
};

export const add_last_login = (pk) => {
  return axios.put(`/info/customer-profile/${pk}/update_last_login/`);
};

export const createMaintenanceAgreement2 = (MaintenanceAggreementData) => {
  return axios.post(`/info/maintenance-agreement/`, MaintenanceAggreementData);
};

export const fetchMaintenanceAgreement = async (userEmail) => {
  return axios.get(`/info/maintenance-agreement/?email=${userEmail}`);
};

export const fetchPoolEquipment = async () => {
  return axios.get(`/info/extra-pool-equipment/`);
};

export const fetchPoolConditions = async () => {
  return axios.get(`/info/pool-conditions/`);
};

// ----------------------------------------------------------------[store]

export const fetchCustomersProducts = async (userEmail) => {
  return axios.get(`/store/product/?email=${userEmail}`);
};

export const fetchChemicalList = async () => {
  return axios.get(`/store/chemical-list/`);
};

export const fetchProductList = async () => {
  return axios.get(`/store/product-list/`);
};


export const fetchProduct = async (pk) => {
  return axios.get(`/store/product-list/${pk}/`);
};

export const fetchCustomersProduct = async (pk) => {
  return axios.get(`/store/product/${pk}/`);
};

export const fetchCustomersProductList = async (id) => {
  return axios.get(`/store/customer-product-list/${id}/`);
};


export const orderProduct = async (productData) => {
  return axios.post(`/store/product/`, productData);
};

export const createProductList = async () => {
  return axios.post(`/store/customer-product-list/`,);
};
export const addItemProductList = async (Data) => {
  return axios.post(`/store/customer-product-list/add_item/`, Data);
};
// ----------------------------------------------------------------[forms]

export const fetchMaintenances = async (userEmail) => {
  return axios.get(`/forms/maintenance/?email=${userEmail}`);
};

export const fetchMaintenance = async (pk) => {
  return axios.get(`/forms/maintenance/${pk}/`);
};


export const fetchInvoices = async (userEmail) => {
  return axios.get(`/forms/invoice/?email=${userEmail}`);
};

export const fetchInvoice = (pk) => {
  return axios.get(`/forms/invoice/${pk}`);
};


export const fetchEstimates = async (userEmail) => {
  return axios.get(`/forms/estimate/?email=${userEmail}`);
};

export const fetchEstimate = (pk) => {
  return axios.get(`/forms/estimate/${pk}`);
};

export const createEstimate = (estimateData) => {
  return axios.post(`/forms/estimate/`, estimateData);
};

export const createMaintenanceAgreement = (data) => {
  return axios.post(`/forms/maintenance_agreement/`, data);
};

export const createAppointment = (appointmentData) => {
  return axios.post(`/forms/booking_request/`, appointmentData);
};

export const fetchAppointments = async (userEmail) => {
  return axios.get(`/forms/booking_request/?email=${userEmail}`);
};

export const fetchAppointment = (pk) => {
  return axios.get(`/forms/booking_request/${pk}`);
};

export const fetchCallBacks = async (userEmail) => {
  return axios.get(`/forms/call_back/?email=${userEmail}`);
};

export const fetchCallBack = (pk) => {
  return axios.get(`/forms/booking_request/${pk}`);
};

export const fetchServiceList = () => {
  return axios.get(`/forms/service_list/`);
};

export const createCallBack = (callBackForm) => {
  return axios.post(`/forms/booking_request/`, callBackForm);
};

// ----------------------------------------------------------------[blog]

export const fetchBlogArticles = () => {
  return axios.get(`/blog/article/`);
};

export const fetchBlogArticle = (pk) => {
  return axios.get(`/blog/article/${pk}`);
};
