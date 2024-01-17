// Composables
import { createRouter, createWebHistory } from 'vue-router'

import HomeView from '../views/landing/HomeView.vue'
import AboutView from '../views/landing/AboutView.vue'
import LoginView from '../views/landing/LoginView.vue'
import BlogDetailView from '../views/landing/BlogDetailView.vue'
import BlogView from '../views/landing/BlogView.vue'
import RecruitView from '../views/landing/RecruitView.vue'
import SignUpView from '../views/landing/SignUpView.vue'

 import BookingRequestView from '../views/account/BookingRequestView.vue'
 import StoreDetailView from '../views/account/StoreDetailView.vue'
 import StoreView from '../views/account/StoreView.vue'
 import DashBoardView from '../views/account/DashBoardView.vue'
 import EstimateRequestView from '../views/account/EstimateRequestView.vue'
 import EstimateRequestGenView from '../views/account/EstimateRequestGenView.vue'
import BookingRequestGenView from '../views/account/BookingRequestGenView.vue'
 import ScheduleCallBackView from '../views/account/ScheduleCallBackView.vue'
 import ScheduleInfoCallView from '../views/account/ScheduleInfoCallView.vue'
 import MaintenanceDetailView from '../views/account/MaintenanceDetailView.vue'
 import CustomerProductDetailView from '../views/account/CustomerProductDetailView.vue'
 import ProductOrderFormView from '../views/account/ProductOrderFormView.vue'
 import ImageDetailView from '../views/account/ImageDetailView.vue'
 import RegularMaintenanceFormView from '../views/account/RegularMaintenanceFormView.vue'
 import ProfileInfoUpdateFormView from '../views/account/ProfileInfoUpdateFormView.vue'


 import LeaksView from '../views/services/LeaksView.vue'
 import PoolSchoolView from '../views/services/PoolSchoolView.vue'
 import ClosingView from '../views/services/ClosingView.vue'
 import ConstructionView from '../views/services/ConstructionView.vue'
 import RemodelDetailView from '../views/services/remodelDetailView.vue'
 import MaintenanceView from '../views/services/MaintenanceView.vue'
 import InstallationView from '../views/services/InstallationView.vue'
 import InstallationDetailView from '../views/services/InstallationDetailView.vue'
 import PowerVacuumView from '../views/services/PowerVacuumView.vue'
 import WinterWatchView from '../views/services/WinterWatchView.vue'
 import OpenView from '../views/services/OpeningView.vue'
 import RepairView from '../views/services/RepairView.vue'
 import RepairDetailView from '../views/services/RepairDetailView.vue'
 import BalancePoolChemistryView from '../views/services/BalancePoolChemistryView.vue'
 import Green2ClearView from '../views/services/Green2ClearView.vue'

import { useUser } from '@/store/user'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/About',
    name: 'about',
    component: AboutView
  },
  {
    path: '/Login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/Sign_Up',
    name: 'sign-up',
    component: SignUpView
  },
  {
    path: '/Blog',
    name: 'blog',
    component: BlogView
  },
  {
    path: '/Article/:id',
    name: 'blog-detail',
    component: BlogDetailView
  },
  {
    path: '/JoinUs',
    name: 'recruit',
    component: RecruitView
  },
  // //--------------------------------
  {
    path: '/Book-Now/:service',
    name: 'book',
    component: BookingRequestView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Booking',
    name: 'booking',
    component: BookingRequestGenView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/maintenance_agreement',
    name: 'maintenance_agreement',
    component: RegularMaintenanceFormView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/profile-update',
    name: 'profile-update',
    component: ProfileInfoUpdateFormView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Schedule_Info_Call/:service',
    name: 'schedule-info-call',
    component: ScheduleInfoCallView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Schedule_Call_Back',
    name: 'schedule',
    component: ScheduleCallBackView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Dashboard',
    name: 'dashboard',
    component: DashBoardView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/image/:src/',
    name: 'image',
    component: ImageDetailView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Get-Estimate/:service/',
    name: 'get-estimate',
    component: EstimateRequestView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Estimate',
    name: 'estimate',
    component: EstimateRequestGenView,
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/Store',
    name: 'store',
    component: StoreView
  },

  {
    path: '/StoreItem/:id/',
    name: 'store-detail',
    component: StoreDetailView
  },

  {
    path: '/maintenance-detail/:id',
    name: 'maintenance-detail',
    component: MaintenanceDetailView
  },
  {
    path: '/product-detail/:id',
    name: 'product-detail',
    component: CustomerProductDetailView
  },
  {
    path: '/order/:id',
    name: 'order',
    component: ProductOrderFormView
  },

  //--------------------------------

  {
    path: '/Leaks',
    name: 'leak',
    component: LeaksView
  },
  {
    path: '/PoolSchool',
    name: 'school',
    component: PoolSchoolView
  },
  {
    path: '/Closing',
    name: 'closing',
    component: ClosingView
  },
  {
    path: '/Remodel',
    name: 'remodel',
    component: ConstructionView
  },
  {
    path: '/Remodel/:id/',
    name: 'remodel-detail',
    component: RemodelDetailView
  },
  {
    path: '/Maintenance',
    name: 'maintenance',
    component: MaintenanceView
  },
  {
    path: '/Installations',
    name: 'install',
    component: InstallationView
  },
  {
    path: '/Installations/:id/',
    name: 'install-detail',
    component: InstallationDetailView
  },

  {
    path: '/Power_Vacuum',
    name: 'power-vacuum',
    component: PowerVacuumView
  },
  {
    path: '/Winter_Watch',
    name: 'winter-watch',
    component: WinterWatchView
  },
  {
    path: '/Open',
    name: 'open',
    component: OpenView
  },
  {
    path: '/Balance-Chemistry',
    name: 'balance',
    component: BalancePoolChemistryView
  },
  {
    path: '/Green-to-Clear',
    name: 'green-2-clear',
    component: Green2ClearView
  },

  {
    path: '/Repair',
    name: 'repair',
    component: RepairView
  },
  {
    path: '/Repair/:id/',
    name: 'repair-detail',
    component: RepairDetailView
  },

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
})


router.beforeEach((to, from, next) => {
  const store = useUser()
  const isAuthenticated = store.isAuthenticated
  if (to.meta.requiresAuth) {
    if (!isAuthenticated) {
      next('Login')
    } else {
      next()
    }
  }
  else {
    next()
  }
})
export default router
