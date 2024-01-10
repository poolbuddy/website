import axios from 'axios';

const apiBaseUrl = "http://localhost:8000"

// ----------------------------------------------------------------[AuthUser]
export const createAuthUser = (userData) => {
  return axios.post(`${apiBaseUrl}/auth/users/`, userData)
}

export const fetchLogin = (loginData) => {
  return axios.post(`${apiBaseUrl}/auth/token/login/`, loginData)
}
// ----------------------------------------------------------------[customer_profile]

export const createCustomerProfile = (profileData) => {
  return axios.post(`${apiBaseUrl}/info/customer-profile/`, profileData);
};

export const createPool = (poolData) => {
  return axios.post(`${apiBaseUrl}/info/pool/`, poolData);
};

export const createAddress = (addressData) => {
  return axios.post(`${apiBaseUrl}/info/address/`, addressData);
};

export const fetchCustomerProfile = (email) => {
  return axios.get(`${apiBaseUrl}/info/customer-profile/?email=${email}`);
};

export const add_last_login = (pk) => {
  return axios.put(`${apiBaseUrl}/info/customer-profile/${pk}/update_last_login/`);
};

export const createMaintenanceAgreement2 = (MaintenanceAggreementData) => {
  return axios.post(`${apiBaseUrl}/info/maintenance-agreement/`, MaintenanceAggreementData);
};

export const fetchMaintenanceAgreement = async (userEmail) => {
  return axios.get(`${apiBaseUrl}/info/maintenance-agreement/?user_email=${userEmail}`);
};

export const fetchPoolEquipment = async () => {
  return axios.get(`${apiBaseUrl}/info/extra-pool-equipment/`);
};

export const fetchPoolConditions = async () => {
  return axios.get(`${apiBaseUrl}/info/pool-conditions/`);
};

// ----------------------------------------------------------------[store]

export const fetchCustomersProducts = async (userEmail) => {
  return axios.get(`${apiBaseUrl}/store/product/?email=${userEmail}`);
};

export const fetchChemicalList = async () => {
  return axios.get(`${apiBaseUrl}/store/chemical-list/`);
};

export const fetchProductList = async () => {
  return axios.get(`${apiBaseUrl}/store/product-list/`);
};


export const fetchProduct = async (pk) => {
  return axios.get(`${apiBaseUrl}/store/product-list/${pk}/`);
};

export const fetchCustomersProduct = async (pk) => {
  return axios.get(`${apiBaseUrl}/store/product/${pk}/`);
};

export const fetchCustomersProductList = async (id) => {
  return axios.get(`${apiBaseUrl}/store/customer-product-list/${id}/`);
};


export const orderProduct = async (productData) => {
  return axios.post(`${apiBaseUrl}/store/product/`, productData);
};

export const createProductList = async () => {
  return axios.post(`${apiBaseUrl}/store/customer-product-list/`,);
};
export const addItemProductList = async (Data) => {
  return axios.post(`${apiBaseUrl}/store/customer-product-list/add_item/`, Data);
};
// ----------------------------------------------------------------[forms]

export const fetchMaintenances = async (userEmail) => {
  return axios.get(`${apiBaseUrl}/forms/maintenance/?customer_email=${userEmail}`);
};

export const fetchMaintenance = async (pk) => {
  return axios.get(`${apiBaseUrl}/forms/maintenance/${pk}/`);
};


export const fetchInvoices = async (userEmail) => {
  return axios.get(`${apiBaseUrl}/forms/invoice/?customer_email=${userEmail}`);
};

export const fetchInvoice = (pk) => {
  return axios.get(`${apiBaseUrl}/forms/invoice/${pk}`);
};


export const fetchEstimates = async (userEmail) => {
  return axios.get(`${apiBaseUrl}/forms/estimate/?customer_email=${userEmail}`);
};

export const fetchEstimate = (pk) => {
  return axios.get(`${apiBaseUrl}/forms/estimate/${pk}`);
};

export const createEstimate = (estimateData) => {
  return axios.post(`${apiBaseUrl}/forms/estimate/`, estimateData);
};

export const createMaintenanceAgreement = (data) => {
  return axios.post(`${apiBaseUrl}/forms/maintenance_agreement/`, data);
};

export const createAppointment = (appointmentData) => {
  return axios.post(`${apiBaseUrl}/forms/booking_request/`, appointmentData);
};

export const fetchAppointments = async (userEmail) => {
  return axios.get(`${apiBaseUrl}/forms/booking_request/?customer_email=${userEmail}`);
};

export const fetchAppointment = (pk) => {
  return axios.get(`${apiBaseUrl}/forms/booking_request/${pk}`);
};

export const fetchCallBacks = async (userEmail) => {
  return axios.get(`${apiBaseUrl}/forms/call_back/?customer_email=${userEmail}`);
};

export const fetchCallBack = (pk) => {
  return axios.get(`${apiBaseUrl}/forms/booking_request/${pk}`);
};

export const fetchServiceList = () => {
  return axios.get(`${apiBaseUrl}/forms/service_list/`);
};

export const createCallBack = (callBackForm) => {
  return axios.post(`${apiBaseUrl}/forms/booking_request/`, callBackForm);
};

// ----------------------------------------------------------------[blog]

export const fetchBlogArticles = () => {
  return axios.get(`${apiBaseUrl}/blog/article/`);
};

export const fetchBlogArticle = (pk) => {
  return axios.get(`${apiBaseUrl}/blog/article/${pk}`);
};
