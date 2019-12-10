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
                  <v-col>
                    <v-btn @click="gerarNumeros">Gerar Números</v-btn>
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
                  <v-card-text>Agrupamentos</v-card-text> 
                </v-card>
              </v-tab-item>

              <v-tab-item
                :value="'tab-1'"
              >
                <v-card flat>
                  <v-card-text>M.Centrais</v-card-text> 
                </v-card>
              </v-tab-item>

              <v-tab-item
                :value="'tab-2'"
              >
                <v-card flat>
                  <v-card-text>M. Dispersão</v-card-text> 
                </v-card>
              </v-tab-item>

              <v-tab-item
                :value="'tab-3'"
              >
                <v-card flat>
                  <v-card-text>Regressão</v-card-text> 
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


export default {
  name: 'App',

  components: {
  },

  data: () => ({
    // geracao numeros
    qtdNumeros: 0,
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
    // painel de resultados
    tab: null,
    tabs: ['Agrupamento','M. centrais', 'M. dispersão', 'Regressão'],
  }),
  methods: {
    gerarNumeros () {
      var arrayTemp = []
      this.range[1] += 1
      for (var i = 0; i < this.qtdNumeros; i++) {
        var x = Math.floor(Math.random() * this.range[1])
        var y = Math.floor(Math.random() * this.range[1])
        arrayTemp.push({x: x, y: y})
      }

      this.items =  arrayTemp
    },
  },
};
</script>
