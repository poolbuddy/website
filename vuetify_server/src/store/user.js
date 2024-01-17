import { defineStore } from 'pinia';
export const useUser = defineStore('user', {
    // arrow function recommended for full type inference
    state: () => {
        return {
            user: {
                username: '',
                id: null,

            },
            isAuthenticated: false,
            token: null,
            id: null,
            email: null,
            profile: null,

        }
    },
    actions: {
        initializeStore() {
            if (localStorage.getItem('token')) {
                this.token = localStorage.getItem('token'),
                    this.isAuthenticated = true,
                    this.email = localStorage.getItem('email'),
                    this.profile = JSON.parse(localStorage.getItem('profile'))

            }
            else {
                this.isAuthenticated = false,
                    this.token = null,
                    this.email = null,
                    this.profile = null
            }
        },

        setToken(token) {
            this.token = token
            this.isAuthenticated = true
        },
        async removeToken() {
            this.token = null
            this.isAuthenticated = false
            this.email = null
            localStorage.removeItem('email');
            localStorage.removeItem('token');
            localStorage.removeItem('profile');


        },

    },
})
