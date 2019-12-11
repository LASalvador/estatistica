import http from './http'

function calcular(data) {
    var endpoint = '/calculo'
    return http().post(`${endpoint}`, data)
}

export default {
    calcular
}