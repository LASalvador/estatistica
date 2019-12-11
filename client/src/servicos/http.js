import axios from 'axios'

const api = 'http://127.0.0.1:5000'

const http = axios.create({
  baseURL: api,
})

export default function () {
  return http
}
