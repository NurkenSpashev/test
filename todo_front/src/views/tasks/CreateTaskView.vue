<template>
  <div class="container">
      <div class="row">
        <div class="card col-md-5">
           <form @submit.prevent="saveTask" class="m-3">
            <div class="form-group m-1">
              <input type="text" class="form-control" id="title" name="title" v-model="taskForm.title" aria-describedby="title">
            </div>
             <div class="form-group m-2">
               <textarea class="form-control" id="description" name="description" v-model="taskForm.description" aria-describedby="description"></textarea>
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
         }
     }
 },
 mounted() {
    this.if_authenticate = this.$store.state.isLoggedIn ? true : false;
 },
 methods: {
  async saveTask() {
    console.log(this.taskForm)
    if(this.$store.state.isLoggedIn) {
      const response = await axios.post('http://127.0.0.1:8000/api/tasks/', this.taskForm);
      this.$router.push({ name: 'tasks' })
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
