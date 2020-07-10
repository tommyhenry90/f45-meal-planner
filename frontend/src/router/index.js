import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import NotFound from '@/views/NotFound'
import ChallengeRecipes from '../components/ChallengeRecipes'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/challenge-recipes',
      name: 'Challenge Recipes',
      component: ChallengeRecipes
    },
    {
      path: '/*',
      name: 'NotFound',
      component: NotFound
    }
  ],
  mode: 'history'
})
