import axios, { AxiosInstance } from 'axios'

let instance = AxiosInstance

// Setup default settings for axios depending on whether we're running in prod
// or dev mode.
if (process.env.NODE_ENV === 'development') {
  instance = axios.create({
    baseURL: 'http://127.0.0.1:5000/'
  })
} else {
  instance = axios.create()
}

export default instance
