import { defineStore } from 'pinia';
export const useNavDrawer = defineStore('navDrawer', {
    // arrow function recommended for full type inference
    state: () => {
        return {
            isDrawerOpen: false,
            isBottomNavOpen: true, // all these properties will have their type inferred automatically

        }
    },
    actions: {

        toggleDrawer() {
            this.isDrawerOpen = !this.isDrawerOpen;
        },
        toggleBottomNav() {
            state.isBottomNavOpen = !state.isBottomNavOpen;
        },
    },
})
