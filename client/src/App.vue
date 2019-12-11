<template>
  <v-app>
    <v-app-bar
      app
      color="primary"
      dark
    >
      <span class="mr-2 headline">CSS - Calcula Simple Sheet</span>
    </v-app-bar>
    <v-content>
      <v-container fluid>
        <v-row>
          <v-col 
            cols="12"
            md="4"
            lg="4"
            xl="4"
          >
            <v-card color="#e4e4e4">
              <v-card-title>Gere os dados para os cálculos</v-card-title>
              <v-card-text>
                <v-row>
                  <v-col cols="12">
                    <v-text-field
                      v-model="qtdNumeros"
                      label="Quantidade de números"
                      required
                    />
                  </v-col>
                  <v-col cols="12">
                    <v-range-slider
                      v-model="range"
                      :max="max"
                      :min="min"
                      hide-details
                      class="align-center"
                      color="black"
                    >
                      <template v-slot:append>
                        <v-text-field
                          v-model="range[1]"
                          class="mt-0 pt-0"
                          hide-details
                          single-line
                          type="number"
                          style="width: 60px"
                        ></v-text-field>
                      </template>
                    </v-range-slider>
                  </v-col>
                  <v-col cols="6">
                    <v-btn @click="gerarNumeros">Gerar Números</v-btn>
                  </v-col>
                  <v-col cols="6">
                    <v-btn @click="calcularValores">Calcular valores</v-btn>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
          <v-col 
            cols="12"
            md="8"
            lg="8"
            xl="8"
          >
            <v-data-table
              v-if="items !== undefined"
              :headers="headers"
              :items="items"
              :items-per-page="5"
              :no-data-text="'Sem dados'"
              class="elevation-1"
            ></v-data-table>
          </v-col>
        </v-row>
        <v-row>
          <v-col cols="12">
            <v-tabs
              fixed-tabs
              background-color="primary"
              dark
              v-model="tab"
              
            > 
              <v-tab
                v-for="(item, index) in tabs"
                :key="item"
                :href="`#tab-${index}`"
              >
                {{ item }}
              </v-tab>

              <v-tab-item
                :value="'tab-0'"
              >
                <v-card flat>
                  <v-card-text>
                    <div class="headline">Medidas de tendencia central</div>
                    <div> Mediana de X : {{medX}} </div>
                    <div> Mediana de Y : {{medY}} </div>
                    <div> Media de Harmonica X : {{mediaHx}} </div>
                    <div> Media de Harmonica Y : {{mediaHy}} </div>
                    <div> Media de X : {{mediax}} </div>
                    <div> Media de Y : {{mediay}} </div>
                  </v-card-text> 
                </v-card>
              </v-tab-item>

              <v-tab-item
                :value="'tab-1'"
              >
                <v-card flat>
                  <v-card-text>
                    <div class="headline">Medidas de dispersão</div>
                    <div> Desvio padrao de X: {{dpX}}</div> 
                    <div> Desvio padrao de Y: {{dpY}}</div>  
                    <div> Variancia de X: {{vX}} </div> 
                    <div> Variancai de Y: {{vY}} </div>
                  </v-card-text> 
                </v-card>
              </v-tab-item>
            </v-tabs>
          </v-col>
        </v-row>
      </v-container>
    </v-content>
    <v-footer
      color="primary"
      app
    >
      <span class="white--text">&copy;
        {{ (new Date()).getFullYear() }}
        <strong>Fatec São José dos Campos</strong>
      </span>
    </v-footer>
  </v-app>
</template>

<script>
import api from './servicos/api'

export default {
  name: 'App',

  components: {
  },

  data: () => ({
    // geracao numeros
    qtdNumeros: 10,
    min: 0,
    max: 1000,
    slider: 10,
    range: [0, 70],
    // tabela
    headers: [
    { 
      text:'x',
      value: 'x'
    },
    { 
      text:'y',
      value: 'y'
    },
    ],
    items: [],
    x: null,
    y: null,
    // painel de resultados
    tab: null,
    tabs: ['M. centrais', 'M. dispersão'],
    // medidas de dispersao
    dpX: null, 
    dpY: null,  
    vX: null, 
    vY: null,
    // medidas de tendencia central
    medX: null, 
    medY: null, 
    mediaHx: null, 
    mediaHy: null, 
    mediax: null, 
    mediay: null,
  }),
  methods: {
    gerarNumeros () {
      var arrayTemp = []
      var xTemp = []
      var yTemp = []
      this.range[1] += 1
      for (var i = 0; i < this.qtdNumeros; i++) {
        var x = Math.floor(Math.random() * this.range[1])
        var y = Math.floor(Math.random() * this.range[1])
        xTemp.push(x)
        yTemp.push(y)
        arrayTemp.push({x: x, y: y})
      }

      this.items =  arrayTemp
      this.x = xTemp
      this.y = yTemp
    },
    async calcularValores () {
      if(!this.x & !this.y) {
        return
      }
      var response = await api.calcular({x: this.x, y: this.y})
      
      this.dpX= response.data.dpX
      this.dpY= response.data.dpY  
      this.medX= response.data.medX  
      this.medY= response.data.medY  
      this.mediaHx= response.data.mediaHx  
      this.mediaHy= response.data.mediaHy  
      this.mediax= response.data.mediax  
      this.mediay= response.data.mediay  
      this.vX= response.data.vX  
      this.vY= response.data.vY

      }, 
  },
};
</script>
