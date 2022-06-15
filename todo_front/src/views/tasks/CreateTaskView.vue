<template>
  <div class="container">
      <div class="row">
      <div class="alert alert-danger" role="alert" v-if="error">
        {{error}}
      </div>
        <div class="card col-md-5">
           <form @submit.prevent="saveTask" class="m-3">
            <div class="form-group m-1">
              <input type="text" class="form-control" id="title" name="title" v-model="taskForm.title" aria-describedby="title">
              <p v-if="error_title" style="color:red">{{error_title}}</p>
            </div>
             <div class="form-group m-2">
               <textarea class="form-control" id="description" name="description" v-model="taskForm.description" aria-describedby="description"></textarea>
              <p v-if="error_description" style="color:red">{{error_description}}</p>
             </div>
            <div class="form-group mt-2">
              <input type="checkbox" class="form-check-input" id="exampleCheck1" name="status" v-model="taskForm.status">
              <span for="exampleCheck1">Status</span>
            </div>
            <input type="submit" class="btn btn-primary" value="Save">
          </form>
       </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TaskView',
  data() {
     return {
         tasks: [''],
         if_authenticate: false,
         taskForm: {
           title: '',
           description: '',
           status: false
         },
         error: false,
         error_description: false,
         error_title: false
     }
 },
 mounted() {
    this.if_authenticate = this.$store.state.isLoggedIn ? true : false;
 },
 methods: {
  async saveTask() {
    if(this.$store.state.isLoggedIn) {
      let vue = this;
      const response = await axios.post('http://localhost:8009/api/tasks/', this.taskForm).catch(error=>{
           if(error.response.data.detail) {
             vue.error = error.response.data.detail;
           } else if(error.response.data.title) {
             vue.error_title = error.response.data.title[0];
             vue.error_description = false
           } else if(error.response.data.description) {
             vue.error_title = false
             vue.error_description = error.response.data.description[0];
           }
      });
      if(response) {
        this.$router.push({ name: 'tasks' })
      }
    }
  }
}
}
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
