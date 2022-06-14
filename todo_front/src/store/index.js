import { createStore } from 'vuex'

export default createStore({
  state: {
    access: null,
    refresh: null,
    isLoggedIn: false,
  },
  getters: {
  },
  mutations: {
    initializeStore() {
      if(localStorage.getItem('access')) {
        this.state.access = localStorage.getItem('access');
        this.state.refresh = localStorage.getItem('refresh');
        this.state.isLoggedIn = true;
      } else {
        this.state.access = null;
        this.state.refresh = null;
        this.state.isLoggedIn = false;
      }
    },
    setAccess(state, access) {
      this.state.access = access;
      localStorage.setItem('access', access);
      state.isLoggedIn = true;
    },
    setRefresh(state, refresh) {
      this.state.refresh = refresh
      localStorage.setItem('refresh', refresh);
      state.isLoggedIn = true;
    },
    removeAccess(state, access) {
      this.state.access = null;
      localStorage.removeItem('access');
      localStorage.removeItem('refresh');
      state.isLoggedIn = false;
    }
  },
  actions: {
  },
  modules: {
  }
})
