/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'

import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'
import colors from 'vuetify/util/colors'
import '../assets/main.scss'


const myCustomLightTheme = {
  dark: false,
  colors: {
    background: colors.blueGrey.lighten1,
    surface: colors.grey.darken2,
    'surface-darken-1': colors.grey.darken1,
    primary: colors.teal.base,
    'primary-accent-4': colors.teal.accent4,
    secondary: colors.cyan.base,
    'secondary-darken-1': colors.cyan.darken1,
    blank: colors.shades.transparent,
    error: colors.red.base, // Replace with your specific red shade
    alert: colors.amber.accent4,
    info: colors.blue.base, // Replace with your specific blue shade
    success: colors.green.base, // Replace with your specific green shade
    warning: colors.orange.base, // Replace with your specific orange shade
  },
}

export default createVuetify({
  icons: {
    defaultSet: 'mdi',
    sets: {
      mdi: {
        mindfulness: 'f6e0',
        lotus: 'eb4c', // Register your custom icon with its code point
      },
    },
  },

  theme: {
    options: {
      customProperties: true,
    },
    defaultTheme: 'myCustomLightTheme',
    themes: {
      myCustomLightTheme,
    },

  },
})
