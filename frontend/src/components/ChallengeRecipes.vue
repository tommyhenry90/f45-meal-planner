<template>
<b-container>
  <b-container v-for="plan in recipes" v-bind:key="plan.id">
    <h1>{{plan.title}}</h1>
    <b-row v-for="day in plan.days" v-bind:key="day.id">
      <b-row>
        <b-col>
          <h2>{{day.title}}</h2>
        </b-col>
      </b-row>
      <b-row>
        <b-col v-for="meal in day.meals" v-bind:key="meal.id">
          <b-row>
            <b-col>
              <h3>{{meal.title}}</h3>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              {{meal.recipe.title}}
            </b-col>
          </b-row>
        </b-col>
      </b-row>
      <b-row>
      </b-row>
    </b-row>
  </b-container>
</b-container>
</template>

<script>
import axios from '../utils/axios'

export default {
  name: 'ChallengeRecipes',
  data () {
    return {
      challengeId: '3',
      recipes: []
    }
  },
  methods: {
    getMeals () {
      let path = '/api/challenge-recipes?id=' + this.challengeId
      axios.get(path)
        .then(response => {
          console.log(path)
          console.log(response.data)
          this.recipes = response.data
        })
        .catch(error => {
          console.log(error)
        })
    }
  },
  created () {
    this.getMeals()
  }
}
</script>

<style scoped>

</style>
